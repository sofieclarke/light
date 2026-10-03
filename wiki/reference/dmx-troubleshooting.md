---
title: "DMX & Network Troubleshooting"
aliases: ["dmx", "flicker", "flickering", "no dmx", "termination", "terminator", "art-net", "sacn", "rdm", "network", "universe", "address"]
type: reference
last_updated: "2026-10-03"
---

# DMX & Network Troubleshooting

> **2AM CARD**
> - **Fixture flickering / twitching / random moves?** Terminate the end of the line → swap the cable feeding the first bad fixture → check for address overlap → check mode.
> - **Everything after fixture X is dead?** The problem is the cable going **into** the first dead fixture, or fixture X's thru (some fixtures lose thru when unpowered; a few have relay bypass, many don't).
> - **Art-Net universe 0 = sACN universe 1.** Off-by-one universe is the #1 network mistake.
> - **Fixture responds but wrong things move?** Wrong DMX mode on the fixture vs the console patch.

## 1. Flowchart: a fixture isn't doing what the console says

```
Does the fixture show DMX present? (display icon / LED / "DMX OK" / signal indicator)
│
├─ NO → Is the fixture before it working?
│        ├─ YES → swap the cable between them; check the previous fixture's DMX thru
│        └─ NO  → walk upstream to the first dead fixture; check splitter output / node / console universe output
│
└─ YES → Is the address right? (display vs paperwork vs console patch)
         ├─ NO  → fix the address
         └─ YES → Is the DMX MODE right? (fixture mode must match the patched profile/footprint)
                  ├─ NO  → fix the mode (or re-patch the console)
                  └─ YES → Is anything else on the same addresses? (overlap — check console patch & other fixtures)
                           └─ Still weird? → check the fixture's own issues: shutter/dimmer channel at 0,
                                              control/reset channel being sent, pan/tilt inverted or disabled
                                              in the fixture menu, transport locks.
```

## 2. Symptom → cause

| Symptom | Most likely | Also check |
|---|---|---|
| Flicker / jitter / random movement, worse at end of line | No terminator | Bad cable, too many fixtures on one run (>32), mic cable used as DMX |
| All fixtures after one point dead | Cable into first dead unit, or previous unit's thru failed | Unpowered fixture in the chain without thru bypass |
| One fixture wrong, neighbours fine | Address / mode | Fixture faulty → swap address with a known-good unit to prove it |
| Fixture resets / homes mid-show | **Reset command being sent** on its control channel (a preset or effect with control values) | Power dropping (loose TRUE1), overheating |
| Lamp douses mid-show | Lamp-off command on control channel | Thermal protection |
| Fixture runs its own show / ignores console | Standalone / auto / master-slave mode active, or "DMX fail → hold/blackout" setting | No DMX present, so it fell back |
| Works on console A, not on console B | Different profile / mode | 3-pin vs 5-pin adaptor with wrong pinout |
| Intermittent with radio / wireless DMX | Interference, link lost | Re-pair, change channel, line of sight, receiver antenna |
| Network fixtures: some universes dead | Universe offset (Art-Net vs sACN), node config, IP subnet | Switch / VLAN, multicast flooding (sACN) |

## 3. DMX rules that matter

| Rule | Detail |
|---|---|
| Daisy-chain only | No Y-cables. Use an **opto-isolated splitter** to branch. |
| Terminate the last fixture | 120 Ω resistor across **pins 2 and 3** (Data– / Data+). Some fixtures have an internal termination switch/menu. |
| 32 devices per run | One "unit load" each (RS-485). More than that → splitter. Some newer devices are ¼-load, but plan on 32. |
| Length | Up to ~300 m / 1000 ft on proper DMX cable. Long runs + many fixtures = splitter. |
| Use DMX cable (110–120 Ω) | Mic cable often works on short runs, then fails mysteriously on long ones. |
| 512 channels per universe | Start address + footprint – 1 must be ≤ 512. |
| RDM through splitters | Needs **RDM-capable** splitters/nodes; standard opto-splitters block RDM. |
| Shield | Pin 1 is shield/common — don't tie it to the fixture chassis ground at both ends unless the system is designed that way. Ground loops cause noise. |

## 4. Pinouts

| Pin | 5-pin XLR | 3-pin XLR |
|---|---|---|
| 1 | Shield / common | Shield / common |
| 2 | Data – | Data – |
| 3 | Data + | Data + |
| 4 | Data 2 – (unused) | — |
| 5 | Data 2 + (unused) | — |

3↔5-pin adaptors are wired 1-1, 2-2, 3-3. **Some old (pre-standard) fixtures used 3-pin with pins 2/3 reversed** — if a 3-pin fixture behaves randomly with everything else fine, try a phase-reverse adaptor.

## 5. Network: Art-Net, sACN, RDMnet

| | Art-Net | sACN (E1.31) |
|---|---|---|
| Universe numbering | **Starts at 0** (Net:Subnet:Universe, e.g. 0:0:0) | **Starts at 1** |
| Typical IP | 2.x.x.x or 10.x.x.x, mask 255.0.0.0 | Any; multicast to 239.255.*.* |
| Transport | Broadcast (old) or unicast | Multicast (default) or unicast |
| Gotcha | Universe 0 on Art-Net = universe 1 on sACN | Multicast floods unmanaged switches when using many universes; use IGMP snooping |

- **Priority (sACN):** Two sources sending the same universe → the higher priority wins; equal priority → merge/flicker depending on receiver. Common cause of "fighting" between console and backup.
- **IP conflicts:** Two devices with the same IP = intermittent everything. Static IP scheme on paper.
- **etherCON:** RJ45 T568B; fixtures with etherCON in/out usually have an internal switch — check whether the thru stays alive when the fixture is unpowered (many don't).
- **Fiber/network distro:** If a whole node's worth of universes dies, check node power, link LEDs, and whether someone changed the node's universe patch.

## 6. Wireless DMX (CRMX / W-DMX)
- Receiver must be **linked/paired** to the transmitter (unlink → link). Lumen Radio CRMX: link from the transmitter, receivers set to "unlinked" accept the next link.
- Wireless adds a little latency and can drop out near LED walls and big RF; keep antennas clear of truss steel.
- Many fixtures (Astera, Chauvet Pro "W" units, GLP, Robe with CRMX option) have it built in — the fixture page says how to (un)link.

## 7. Tools worth carrying
- DMX tester / sniffer (e.g. Swisson XMT-350, DMXcat, Netron handheld) — tells you instantly whether data is present and what values are on each channel.
- Terminators (5-pin and 3-pin), 3↔5-pin adaptors, female-female / male-male barrels.
- Cable tester.
- Laptop/phone with sACN/Art-Net viewer for network shows.

## Sources
- General DMX512-A / RS-485 / E1.31 / Art-Net practice — general knowledge. Specific fixture behaviour (thru when unpowered, termination menus) is on each fixture page.
