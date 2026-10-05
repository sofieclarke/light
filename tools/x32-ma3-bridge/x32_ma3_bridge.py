#!/usr/bin/env python3
"""Use the faders and buttons on a Behringer X32 / Midas M32 to drive grandMA3.

The X32 speaks OSC on UDP port 10023. A client that sends /xremote gets every
change made on the desk (fader moves, mute presses) pushed back to it for the
next 10 seconds, so this script renews /xremote every few seconds, listens, and
re-sends each mapped change to grandMA3's OSC input as an executor fader move,
an executor key press, or a command line.

Standard library only (Python 3.8+), so it runs on a stock Windows install.

Usage:
  python x32_ma3_bridge.py --find                      find X32s on the network
  python x32_ma3_bridge.py --config config.json --monitor
                                                       print what the desk sends, forward nothing
  python x32_ma3_bridge.py --config config.json        run the bridge
  python x32_ma3_bridge.py --config config.json --dry-run
                                                       run, but print MA3 messages instead of sending
"""
import argparse
import json
import socket
import struct
import sys
import time
from pathlib import Path

X32_PORT = 10023
XREMOTE_EVERY = 8.0  # seconds; the desk drops a client after 10 s without /xremote


# --- OSC encoding -----------------------------------------------------------

def _pad(b):
    return b + b"\0" * (4 - len(b) % 4)


def osc_message(address, *args):
    """Encode an OSC message. Arguments may be int, float or str."""
    tags = ","
    data = b""
    for a in args:
        if isinstance(a, bool):
            raise TypeError("send booleans as 0/1")
        if isinstance(a, int):
            tags += "i"
            data += struct.pack(">i", a)
        elif isinstance(a, float):
            tags += "f"
            data += struct.pack(">f", a)
        elif isinstance(a, str):
            tags += "s"
            data += _pad(a.encode())
        else:
            raise TypeError(f"unsupported OSC argument {a!r}")
    return _pad(address.encode()) + _pad(tags.encode()) + data


def _read_str(buf, i):
    end = buf.index(b"\0", i)
    s = buf[i:end].decode(errors="replace")
    return s, (end // 4 + 1) * 4


def osc_parse(buf):
    """Decode a packet into a list of (address, [args]). Bundles are flattened."""
    if buf.startswith(b"#bundle\0"):
        out = []
        i = 16  # "#bundle\0" + 8-byte timetag
        while i + 4 <= len(buf):
            (size,) = struct.unpack(">i", buf[i:i + 4])
            out += osc_parse(buf[i + 4:i + 4 + size])
            i += 4 + size
        return out
    address, i = _read_str(buf, 0)
    if i >= len(buf):
        return [(address, [])]
    tags, i = _read_str(buf, i)
    args = []
    for t in tags[1:]:
        if t == "i":
            args.append(struct.unpack(">i", buf[i:i + 4])[0])
            i += 4
        elif t == "f":
            args.append(struct.unpack(">f", buf[i:i + 4])[0])
            i += 4
        elif t == "s":
            s, i = _read_str(buf, i)
            args.append(s)
        elif t == "b":
            (size,) = struct.unpack(">i", buf[i:i + 4])
            args.append(buf[i + 4:i + 4 + size])
            i += 4 + (size + 3) // 4 * 4
        else:
            break  # a type we don't need; stop rather than misread the rest
    return [(address, args)]


# --- Mapping ----------------------------------------------------------------

class Mapper:
    """Turns X32 messages into grandMA3 OSC messages according to the config."""

    def __init__(self, cfg):
        ma3 = cfg.get("ma3", {})
        prefix = ma3.get("prefix", "").strip("/")
        self.prefix = f"/{prefix}" if prefix else ""
        self.page_word = ma3.get("page_word", "Page")
        self.fader_word = ma3.get("fader_word", "Fader")
        self.key_word = ma3.get("key_word", "Key")
        self.fader_range = float(ma3.get("fader_range", 100))
        self.value_type = ma3.get("value_type", "float")
        self.faders = {m["x32"]: m for m in cfg.get("faders", [])}
        self.buttons = {m["x32"]: m for m in cfg.get("buttons", [])}
        self._last = {}
        for m in list(self.faders.values()) + list(self.buttons.values()):
            if "ma3_exec" not in m and "ma3_cmd" not in m:
                raise ValueError(f"mapping for {m['x32']} needs ma3_exec or ma3_cmd")

    def _exec_address(self, m, word):
        page = int(m.get("ma3_page", 1))
        # Page 0 leaves the page out, which MA3 reads as the currently selected page.
        page_part = f"/{self.page_word}{page}" if page else ""
        return f"{self.prefix}{page_part}/{word}{int(m['ma3_exec'])}"

    def _cmd(self, text):
        return (f"{self.prefix}/cmd", [text])

    def fader_addresses(self):
        return list(self.faders)

    def translate(self, address, args):
        """Return the list of (address, [args]) to send to MA3 for one X32 message."""
        if not args:
            return []
        if address in self.faders:
            return self._fader(self.faders[address], args[0])
        if address in self.buttons:
            return self._button(self.buttons[address], args[0])
        return []

    def _fader(self, m, x32_value):
        level = max(0.0, min(1.0, float(x32_value)))
        lo, hi = m.get("range", [0, self.fader_range])
        value = lo + (hi - lo) * level
        value = round(value) if self.value_type == "int" else round(value, 2)
        if self._last.get(m["x32"]) == value:
            return []
        self._last[m["x32"]] = value
        if "ma3_cmd" in m:
            # e.g. "Master 3.1 At {value}"
            return [self._cmd(m["ma3_cmd"].format(value=value))]
        return [(self._exec_address(m, self.fader_word), [value])]

    def _button(self, m, x32_value):
        # X32 mute/on buttons latch, and /xremote only reports changes, so every
        # message is one press whichever way the button went.
        if "ma3_cmd" in m:
            return [self._cmd(m["ma3_cmd"])]
        addr = self._exec_address(m, self.key_word)
        return [(addr, [1]), (addr, [0])]


# --- Network ----------------------------------------------------------------

def label_address(fader_address):
    """/ch/01/mix/fader -> /ch/01/config/name, /dca/1/fader -> /dca/1/config/name."""
    base = fader_address.rsplit("/", 1)[0]
    if base.endswith("/mix"):
        base = base[:-len("/mix")]
    return base + "/config/name"


def find_x32(target="255.255.255.255", timeout=2.0):
    """Broadcast /xinfo and list every desk that answers."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.settimeout(0.3)
    s.sendto(osc_message("/xinfo"), (target, X32_PORT))
    found = {}
    end = time.time() + timeout
    while time.time() < end:
        try:
            data, (ip, _) = s.recvfrom(4096)
        except socket.timeout:
            continue
        for address, args in osc_parse(data):
            if address == "/xinfo":
                found[ip] = args
    for ip, args in found.items():
        print(f"{ip}  {'  '.join(str(a) for a in args[1:])}")
    if not found:
        print("No X32 answered. Check the desk's network cable and Setup > Network, "
              "or set its IP in the config by hand.")
    return found


def run(cfg, monitor=False, dry_run=False, verbose=False):
    x32 = (socket.gethostbyname(cfg["x32"]["ip"]), int(cfg["x32"].get("port", X32_PORT)))
    ma3_cfg = cfg.get("ma3", {})
    ma3 = (ma3_cfg.get("ip", "127.0.0.1"), int(ma3_cfg.get("port", 8000)))
    mapper = Mapper(cfg)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", int(cfg.get("local_port", 0))))
    sock.settimeout(0.5)
    out = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def to_ma3(address, args):
        if dry_run or verbose:
            print(f"  -> MA3 {address} {' '.join(map(str, args))}")
        if not dry_run:
            out.sendto(osc_message(address, *args), ma3)

    print(f"X32 {x32[0]}:{x32[1]}   MA3 {ma3[0]}:{ma3[1]}   "
          f"{len(mapper.faders)} faders, {len(mapper.buttons)} buttons mapped"
          + ("   [monitor only]" if monitor else "") + ("   [dry run]" if dry_run else ""))
    print("Ctrl+C to stop.")

    sock.sendto(osc_message("/xremote"), x32)
    if cfg.get("sync_on_start") and not monitor:
        # Ask the desk where every mapped control sits now; replies flow through the loop below.
        for address in mapper.fader_addresses():
            sock.sendto(osc_message(address), x32)
    for m in mapper.faders.values():
        if m.get("x32_label") and not monitor:
            sock.sendto(osc_message(label_address(m["x32"]), str(m["x32_label"])[:12]), x32)

    last_renew = time.time()
    heard = False
    try:
        while True:
            now = time.time()
            if now - last_renew >= XREMOTE_EVERY:
                sock.sendto(osc_message("/xremote"), x32)
                last_renew = now
            try:
                data, src = sock.recvfrom(65535)
            except socket.timeout:
                continue
            except ConnectionResetError:
                continue  # Windows reports an ICMP "port unreachable" this way; ignore
            if src[0] != x32[0]:
                continue
            if not heard:
                print("Hearing from the X32.")
                heard = True
            for address, args in osc_parse(data):
                if monitor:
                    print(f"X32 {address} {' '.join(map(str, args))}")
                    continue
                msgs = mapper.translate(address, args)
                if msgs and verbose:
                    print(f"X32 {address} {' '.join(map(str, args))}")
                for a, v in msgs:
                    to_ma3(a, v)
    except KeyboardInterrupt:
        print("\nStopped.")


def load_config(path):
    cfg = json.loads(Path(path).read_text(encoding="utf-8"))
    if "x32" not in cfg or "ip" not in cfg["x32"]:
        sys.exit("config needs x32.ip - run with --find to look for the desk")
    return cfg


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--config", default=str(Path(__file__).with_name("config.json")))
    p.add_argument("--find", nargs="?", const="255.255.255.255", metavar="ADDRESS",
                   help="look for X32 desks (broadcast, or ask one address) and exit")
    p.add_argument("--monitor", action="store_true", help="print everything the X32 sends, forward nothing")
    p.add_argument("--dry-run", action="store_true", help="print MA3 messages instead of sending them")
    p.add_argument("-v", "--verbose", action="store_true", help="print every forwarded message")
    a = p.parse_args()
    if a.find:
        find_x32(a.find)
        return
    run(load_config(a.config), monitor=a.monitor, dry_run=a.dry_run, verbose=a.verbose)


if __name__ == "__main__":
    main()
