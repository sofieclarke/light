---
title: "Chauvet Professional Rogue R2X Wash"
manufacturer: "Chauvet Professional"
model: "Rogue R2X Wash"
aliases: ["r2x wash", "r2x", "rogue r2x", "rogue r2x wash", "roguer2xwash"]
type: "wash"
light_source: null
ip_rating: null
weight_lb: null
weight_kg: null
dimensions: null
power:
  input: null
  connector_in: "Neutrik powerCON (NAC3MPA, blue), per R2 Wash BOM in the R2X repo"
  connector_out: "Neutrik powerCON out (grey), per same BOM"
  watts_max: null
  amps_120v: null
  amps_208v: null
  amps_230v: null
  link_max_120v: null
  link_max_208v: null
  link_max_230v: null
  per_20a_120v: null
  per_20a_208v: null
  fuse: "7 A, 5x20 mm, 250 V (BOM labelled ROGUER2WASH — verify on the R2X)"
dmx:
  connectors: "3-pin and 5-pin XLR in/out (4-in-1 DMX board, per BOM)"
  protocols: ["DMX", "RDM"]
  modes:
    - { name: "15CH", channels: 15 }
    - { name: "17CH", channels: 17 }
    - { name: "22CH", channels: 22 }
    - { name: "23CH", channels: 23 }
    - { name: "33CH", channels: 33 }
    - { name: "33MS", channels: 33 }
    - { name: "54CH", channels: 54 }
    - { name: "54MS", channels: 54 }
    - { name: "55CH", channels: 55 }
    - { name: "56CH", channels: 56 }
menu_password: "2323"
tools: []
verification: "web-search"
last_updated: "2026-10-03"
---

# Chauvet Professional Rogue R2X Wash

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** **2323**. From the main screen, **press and hold MENU** until the passcode screen appears. Enter 2323 (UP raises the value, DOWN goes to the next digit) → **ENTER**. This opens Offset mode (Pan / Tilt / Zoom zero trim). Source: R2X Wash manual on manualslib.
> - **Power:** amps at 120 V and 208 V: **Not found — fill in from the fixture** (read the label on the base). The power-linking limit was not found either. Don't guess; check the label before daisy-chaining.
> - **DMX:** modes in firmware: 15 / 17 / 22 / 23 / 33 / 33MS / 54 / 54MS / 55 / 56. 3-pin and 5-pin XLR. Address: MENU → Address.
> - **Won't move?** No pan/tilt lock parts in the BOM ⚠️. Check it isn't homing in Manual/Auto run mode, then Reset Function.
> - **Tools:** TBD – check on next show.

## Identity
- What crews call it: "R2X", "R2X Wash".
- Variants:
  - **Rogue R2 Wash**: the older model, with powerCON and a similar mode list.
  - **Rogue R2X Wash VW**: a variant with its own manual (ROGUER2XWASHVW) and firmware repo.
  - **Rogue Outcast 2X Wash**: the IP65 version. Its BOM lists an "R2X WASH" light guide.
- Note: the BOM PDF in Chauvet's R2X Wash GitHub repo is titled "ROGUER2WASH". It may be shared with, or copied from, the R2 Wash, so treat BOM details as ⚠️ until checked on an R2X.

## Passwords, menu locks & hidden menus
- **2323** (Offset mode): main level → press and hold **MENU** until the passcode screen appears → enter 2323 → **ENTER** → choose PAN, TILT or ZOOM → adjust the zero position 000–255.
- The firmware contains the strings "Password" and "Zero Adjust".
- Panel lock: not confirmed. See `_chauvet-common.md`.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found | Not found | Not found |
| Power (W) | Not found | Not found | Not found |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | Can't compute (amps unknown) | Can't compute | Can't compute |

- Connectors (BOM): powerCON NAC3MPA (blue) in and powerCON out. Supplied cord: Neutrik powerCON to Edison, 1.5 m.
- Fuse (BOM): 7 A, 5×20 mm, 250 V, in a panel-mount holder.
- Internal PSU (BOM): 30 V 12 A plus 12 V 2 A.
- Electrical table: Not found — fill in from the fixture label or manual.

## Data & addressing
- Connectors: 3-pin and 5-pin XLR in and out ("dmx board 4-IN-1 (3-PIN & 5-PIN IN/OUT)" in the BOM).
- Modes (from firmware strings): 15CH, 17CH, 22CH, 23CH, 33CH, 33MS, 54CH, 54MS, 55CH, 56CH. Firmware V1.250715 "fixed the issue with the personalities names being mislabeled". If the menu names look wrong, update.
- Address: MENU → Address → 001–512 → ENTER.
- Factory reset: Not found for this model specifically. The Rogue convention is Setup → Reset Function / Factory Reset.

## Rigging & hardware
- Bracket (BOM): 140 mm quick-lock Omega bracket (CD-D01) with quarter-turn "fast lock" fasteners.
- Transport locks: none in the BOM ⚠️.
- Weight / dimensions: Not found.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | Not found | TBD – check on next show |
| Gobo / effects module access | n/a | n/a |
| Lens / front glass | Not found | TBD – check on next show |
| Omega bracket | Quarter-turn fast lock | TBD – check on next show |

The handle uses M6×16 screws (BOM).

## Optics & consumables
- LED count and wattage: Not found ⚠️. Firmware notes mention a "center LED and the other 2 rings" (V1.201119).
- Zoom: Not found.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Thermistor Open / Thermistor Short | Firmware strings. Probably a temperature sensor fault ⚠️ | Service |
| Lamp Hot / Hot | Firmware string. Probably over-temperature ⚠️ | Check fans |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Fixture homes 90° off (perpendicular to the LCD) after DMX is re-plugged | Reported on ControlBooth; no resolution captured | Check the console profile and pan invert, run Offset (2323), and do a full reset ⚠️ |
| Center and rings don't match in color | Old firmware | V1.201119+ |
| Output changes between dimmer modes | Old firmware | V1.191202+ |
| RDM problems | Old firmware | V1.230614 / V1.230627 |

## Maintenance
- Firmware: GitHub repo files are .CHL. The BOM shows no USB connector and the repo has no USB instructions, so expect the **UPLOAD 08** over DMX ⚠️ (see `_chauvet-common.md`). Latest found: V1.250715.

## Road notes (community)
- ControlBooth thread "Chauvet Pro Rogue R2x Wash Home Position": a venue added 8 R2X units and found the home position 90° off, perpendicular to the LCD instead of parallel. It happened after DMX was plugged back in.
- ControlBooth thread "Chauvet Rogue R2 wash color snap": a user with 24 R2 Washes reported a slight delay when bumping between colors (applies to the R2 Wash; may apply to the R2X).

## Sources
- [R2X Wash manual (manualslib)](https://www.manualslib.com/manual/1824482/Chauvet-Professional-Rogue-R2x-Wash.html) — passcode 2323, hold MENU, offset Pan/Tilt/Zoom
- [R2X Wash VW manual](https://cdn01.usedlighting.com/products/files/f61f493ac93d46.pdf) — VW variant
- [github.com/Chauvet-Pro/ROGUER2XWASH](https://github.com/Chauvet-Pro/ROGUER2XWASH) — firmware history, BOM (labelled ROGUER2WASH: powerCON, 7 A fuse, DMX 3/5-pin, Omega, PSU), firmware strings (modes, messages)
- [ControlBooth: R2x Wash Home Position](https://www.controlbooth.com/threads/chauvet-pro-rogue-r2x-wash-home-position.48256/), [ControlBooth: R2 wash color snap](https://www.controlbooth.com/threads/chauvet-rogue-r2-wash-color-snap.39741/) — road notes
