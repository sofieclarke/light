# X32 → grandMA3 fader bridge

This lets the faders and buttons on a Behringer X32 (or Midas M32) control grandMA3 executors.

```
X32 desk ──Ethernet, OSC :10023──▶ x32_ma3_bridge.py ──OSC :8000──▶ grandMA3 onPC
 DCA 1–8 faders                     (on the desktop)                  Page 1, executors 201–208
 DCA 1–8 mute buttons                                                 keys 201–208
```

The X32 sends OSC (Open Sound Control) over the network. A program that sends the desk `/xremote` gets every change made on the surface pushed to it for 10 seconds. The bridge renews that every 8 seconds and passes each change you've mapped on to grandMA3's OSC input:

- **fader** → executor fader (`/Page1/Fader201`, 0–100)
- **mute button** → executor key tap (`/Page1/Key201` press, then release)
- or either one → a command line (`/cmd "Master 2.1 At 50"`)

It's one Python file with no extra packages.

## Before you start: read these three things

1. **The USB cable doesn't carry this.** X32 USB is for audio, plus MIDI for DAW control. OSC needs a **network cable** from the X32's **REMOTE** Ethernet port to the desktop, or to the router or switch the desktop is on.
2. **Use controls that don't touch the audio.** By default the bridge listens to the **8 DCA faders**. A DCA with no channels assigned does nothing to the sound, so the faders are free for lighting. If a DCA has channels assigned, moving it changes the mix *and* the lights. Use empty DCAs, or map controls you don't use (spare channels, buses, matrices). Run `--monitor` to see the address of any fader.
3. **It's one-way.** The X32 controls MA3. MA3 doesn't move the X32's motor faders back. If you change a fader in MA3, it jumps to the X32 fader's position the next time you touch that fader.

## Setup

### 1. X32
- Plug the Ethernet cable into the **REMOTE** port.
- Press **SETUP**, open the **network** tab, and write down the desk's **IP address**. It needs to be on the same subnet as the desktop. A DHCP router handles that for you. Otherwise give both machines fixed addresses, e.g. `192.168.1.64` and `192.168.1.10`.
- Make sure **DCAs 1–8 have nothing assigned** if you're using the default mapping.

### 2. grandMA3
**Menu → In & Out → OSC**:

1. Tap **Enable Input** (top right). It lights yellow when it's on.
2. **Insert new OSCData** to add a line, then set:

| Column | Value |
|---|---|
| Name | `X32` |
| Mode | `UDP` |
| Port | `8000` (must match `ma3.port` in the config) |
| Prefix | blank (or match `ma3.prefix`) |
| Page / Fader / Key | leave as `Page` / `Fader` / `Key` |
| FaderRange | `100` |
| Receive | **Yes** |
| ReceiveCmd | **Yes** only if a mapping uses `ma3_cmd` |
| Send / SendCmd | No |

3. **Interface** (top of the screen) is the network adapter MA3 listens on. If the bridge runs on the same PC, try `127.0.0.1` in the config first. If MA3 doesn't respond, set `ma3.ip` to the address shown in the Interface field.
4. If you have **two MA3 instances** open, only one can listen on port 8000. Close the one you aren't using.

### 3. The bridge (Windows)
1. Install Python 3 from python.org. Tick **Add Python to PATH**.
2. Copy this folder to the desktop PC. Make a copy of `config.example.json` called `config.json`.
3. Open a terminal in the folder and find the desk:
   ```
   python x32_ma3_bridge.py --find
   ```
   Put the IP it prints into `config.json` → `x32.ip`.
4. **When Windows Firewall asks, allow Python on private networks.** The X32's replies come in over UDP, and a blocked firewall looks exactly like a dead cable.
5. Check that you're receiving from the desk. Move a DCA fader and you should see lines like `X32 /dca/1/fader 0.5`:
   ```
   python x32_ma3_bridge.py --monitor
   ```
6. Preview what will be sent to MA3, without sending anything:
   ```
   python x32_ma3_bridge.py --dry-run
   ```
7. Run it for real:
   ```
   python x32_ma3_bridge.py -v
   ```
   Assign something to executor 201 (`Assign Sequence 1 At Page 1.201`) and move DCA 1.

## Config reference (`config.json`)

| Key | Meaning |
|---|---|
| `x32.ip`, `x32.port` | Desk address. The port is always `10023` on an X32 or M32 |
| `ma3.ip`, `ma3.port` | Where MA3's OSC input listens |
| `ma3.prefix` | Same as the Prefix column in MA3. Blank means none |
| `ma3.fader_range` | Same as the FaderRange column (default 100) |
| `ma3.value_type` | `float` (default, smoother) or `int` |
| `sync_on_start` | `true` reads every mapped X32 fader at startup and sends its position to MA3. **Off by default** because MA3 levels jump the moment the bridge starts |
| `local_port` | UDP port the bridge listens on. Default 0 picks any free port |

Each entry in **`faders`**:

| Key | Meaning |
|---|---|
| `x32` | X32 address, e.g. `/dca/1/fader`, `/ch/17/mix/fader`, `/bus/01/mix/fader`, `/mtx/01/mix/fader`, `/auxin/01/mix/fader`, `/main/st/mix/fader` |
| `ma3_page`, `ma3_exec` | Target executor. `ma3_page: 0` sends `/Fader201` with no page, which MA3 should read as the current page ⚠️ unverified |
| `ma3_cmd` | Send a command instead of moving an executor. `{value}` is replaced with the level, e.g. `"Master 3.1 At {value}"` for a speed master |
| `range` | `[low, high]` output range, default `[0, 100]` |
| `x32_label` | Optional. Writes this name (max 12 characters) to the X32 scribble strip at startup. **This changes the desk's DCA or channel name** |

Each entry in **`buttons`**: `x32` (e.g. `/dca/1/on`, `/ch/17/mix/on`) plus either `ma3_page` + `ma3_exec` (taps that executor's key) or `ma3_cmd`.

X32 mute buttons latch, so **every press counts as one tap**, whether the mute lit up or went dark. Mutes changed by a scene recall or by X32-Edit count as taps too.

The X32 fader position (0–1) maps straight onto 0–100, so the 0 dB mark (about 75 % of travel) sends 75.

## How this was checked

| Part | Status |
|---|---|
| X32 side: `/xremote` renewal, fader and mute messages, `/xinfo` discovery, scribble-strip names | Tested against Patrick-Gilles Maillot's [X32 emulator](https://github.com/pmaillot/X32-Behringer), including a fader moved after the 10-second `/xremote` window. **Not yet tested on a real desk** |
| MA3 address format `/Page1/Fader201`, 0–100, `/cmd` | From MA's OSC manual page and two independent implementations ([sstaub/gma3](https://github.com/sstaub/gma3), [grandMA3-Chataigne-Module](https://github.com/yastefan/grandMA3-Chataigne-Module)). **Not yet tested on 2.4.2.2** |
| `ma3_page: 0` → current page | Used by the Chataigne module. ⚠️ unverified |
| What an OSC fader does on an **X** or **Temp** executor | ⚠️ unverified. Test on a Master executor first |

Unit tests: `python test_x32_ma3_bridge.py`.

## The other route: MIDI (no script) ⚠️ unverified

The X32 can also send faders as MIDI (SETUP → remote, over USB or the MIDI DIN ports), and MA3 has **Menu → In & Out → MIDI Remotes**. MA's documentation says onPC needs MA hardware or a supported USB MIDI device before it accepts MIDI. Reports also say the X32's built-in DAW-remote modes limit which faders are free. The OSC bridge avoids both problems, which is why it's the recommended route here.
