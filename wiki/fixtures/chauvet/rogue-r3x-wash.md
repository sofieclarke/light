---
title: "Chauvet Professional Rogue R3X Wash"
manufacturer: "Chauvet Professional"
model: "Rogue R3X Wash"
aliases: ["r3x wash", "r3x", "rogue r3x", "rogue r3x wash", "roguer3xwash"]
type: "wash"
light_source: null
ip_rating: null
weight_lb: null
weight_kg: null
dimensions: null
power:
  input: null
  connector_in: "Neutrik powerCON NAC3MPA-1 (blue), per BOM"
  connector_out: "Neutrik powerCON NAC3MPB-1 (grey), per BOM"
  watts_max: null
  amps_120v: null
  amps_208v: null
  amps_230v: null
  link_max_120v: null
  link_max_208v: null
  link_max_230v: null
  per_20a_120v: null
  per_20a_208v: null
  fuse: "12 A, 250 V (BOM: 'fuse 12A 520 250V', likely 5x20 mm)"
dmx:
  connectors: "3-pin and 5-pin XLR in/out (BOM)"
  protocols: ["DMX", "RDM"]
  modes:
    - { name: "15CH", channels: 15 }
    - { name: "21CH", channels: 21 }
    - { name: "27CH", channels: 27 }
    - { name: "33MS", channels: 33 }
    - { name: "54MS", channels: 54 }
    - { name: "62CH", channels: 62 }
    - { name: "71CH", channels: 71 }
    - { name: "107CH", channels: 107 }
menu_password: "2323"
tools: []
verification: "web-search"
last_updated: "2026-10-03"
---

# Chauvet Professional Rogue R3X Wash

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** **2323**. From the main screen, press and hold the menu button (MENU, per the sibling R2X manual) until the passcode screen appears → 2323 → ENTER → Zero Adjust (offset). The R3X Wash manual Rev 4 was the top result for this procedure.
> - **Power:** amps **Not found — fill in from the fixture label**. Link limit not found.
> - **DMX:** firmware modes 15 / 21 / 27 / 33MS / 54MS / 62 / 71 / 107. 27CH was added in V1.250331. 3-pin and 5-pin XLR.
> - **Won't move?** **Pan lock and tilt lock** (BOM). Release both.
> - **Tools:** TBD – check on next show.

## Identity
- What crews call it: "R3X", "R3X Wash".
- Not the same as the **R3 Wash** (older) or the **Outcast 3X Wash** (IP65).

## Passwords, menu locks & hidden menus
- **2323**: from the main level, press and hold the menu button until the passcode screen appears. UP raises the value, DOWN moves to the next digit. ENTER → offset / Zero Adjust.
- Firmware strings: "Password", "Zero Adjust".

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found | Not found | Not found |
| Power (W) | Not found | Not found | Not found |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | Can't compute | Can't compute | Can't compute |

- Connectors (BOM): powerCON NAC3MPA-1 in and NAC3MPB-1 out.
- Fuse (BOM): "fuse 12A 520 250V" in an FH1-B-MW holder. The R2X and R3 Spot use 7 A, so this fuse is NOT interchangeable with them. Carry the right spare.
- PSU (BOM): H08-UP450S30.

## Data & addressing
- DMX: 3-pin and 5-pin (DMX012A Amphenol board, BOM).
- Modes (firmware strings): 15CH, 21CH, 27CH, 33MS, 54MS, 62CH, 71CH, 107CH ⚠️ (check against the menu and console library; strings can include unused modes).
- Address: MENU → Address → 001–512 → ENTER.

## Rigging & hardware
- Omega bracket (BOM): several revisions exist, and they are not identical:
  - V2: CD-D13 140 mm, shorter, with 6 mm washer.
  - V3: CD-D13, taller.
  - V4: CD-D23-140, the current one.
  - There is also a "Quick Lock Hanging Bracket – 140V".
  - If a clamp/omega combo won't seat, it may be a mixed bracket revision.
- **Locks (BOM):** tilt lock (wheel, pick, axis, plus a complete Tilt Lock Assembly part) and pan lock (post, pick).
- Weight / dimensions: Not found.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | Not found | TBD – check on next show |
| Gobo / effects module access | n/a | n/a |
| Lens / front glass | Not found | TBD – check on next show |
| Omega bracket | Quarter-turn quick lock | TBD – check on next show |

The BOM lists M8×30 and M8×90 screws, location not stated.

## Optics & consumables
- LED count and wattage: Not found. BOM: LED PCBs ALJB061A / ALJB062A, a lens cluster, and a frost filter assembly (Ø13 mm 10° frost filters).

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Thermistor Open / Thermistor Short | Firmware strings. Probably a temperature sensor fault ⚠️ | Service |
| Lamp Hot / Hot | Firmware string. Probably over-temperature ⚠️ | Check fans |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Grinding at power-up | Locks engaged | Release pan and tilt locks |
| Full output differs between dimmer modes | Old firmware | V1.191202+ |
| No 27CH mode | Old firmware | V1.250331 |

## Maintenance
- Firmware: github.com/Chauvet-Pro/ROGUER3XWASH (latest found: V1.250331), .CHL files. No USB instructions in the repo, so expect UPLOAD 08 over DMX ⚠️.

## Road notes (community)
- No specific notes found.

## Sources
- [Rogue R3X Wash User Manual Rev 4](https://www.chauvetprofessional.com/wp-content/uploads/2019/10/Rogue_R3X_Wash_UM_Rev4.pdf) — passcode procedure (top search result for "press and hold … 2323")
- [github.com/Chauvet-Pro/ROGUER3XWASH](https://github.com/Chauvet-Pro/ROGUER3XWASH) — firmware history, BOM (12 A fuse, powerCON, DMX board, Omega revisions, locks), firmware strings (modes, messages)
