---
title: "Chauvet Professional Rogue R3 Spot"
manufacturer: "Chauvet Professional"
model: "Rogue R3 Spot"
aliases: ["r3 spot", "rogue r3 spot", "roguer3spot"]
type: "spot"
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
  fuse: "7 A, 5x20 mm, 250 V (BOM)"
dmx:
  connectors: "3-pin and 5-pin XLR in/out"
  protocols: ["DMX", "RDM"]
  modes:
    - { name: "19CH", channels: 19 }
    - { name: "25CH", channels: 25 }
menu_password: "2323"
tools: []
verification: "web-search"
last_updated: "2026-10-03"
---

# Chauvet Professional Rogue R3 Spot

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** **2323** (Rogue family offset passcode). **Hold MENU** on the main screen → passcode screen → 2323 → ENTER → Zero Adjust. The firmware has "Password" and "Zero Adjust" screens, but the R3 Spot manual wording wasn't seen ⚠️.
> - **Power:** amps **Not found — fill in from the fixture label**. Link limit not found.
> - **DMX:** 19CH or 25CH (firmware strings). 3-pin and 5-pin XLR.
> - **Won't move?** **Pan lock and tilt lock** (BOM). Release both.
> - **Tools:** TBD – check on next show.

## Identity
- What crews call it: "R3 Spot".
- Variants: **R3E Spot** (newer, separate manual and repo) and **R3 Beam**. Different profiles.
- Firmware files: V3 (2017–2023), .CHL.

## Passwords, menu locks & hidden menus
- **2323**: hold MENU from the main level until the passcode screen appears. UP raises the value, DOWN moves to the next digit. ENTER → Zero Adjust. This is the documented procedure on the R3X Wash, R3 Beam and R2X Wash; on the R3 Spot it is ⚠️ inferred.
- The R3 Beam (same generation) has a control-panel lock with default code UP, DOWN, UP, DOWN, ENTER. On the R3 Spot it is ⚠️ unverified.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found | Not found | Not found |
| Power (W) | Not found | Not found | Not found |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | Can't compute | Can't compute | Can't compute |

- Connectors (BOM): powerCON NAC3MPA-1 in and NAC3MPB-1 out. Supplied cord: powerCON to Edison, 1.5 m. Retail listings say it ships with a powerCON cord and 2 Omega brackets.
- Fuse (BOM): 7 A 5×20 mm 250 V in an FH1-B-MW holder.
- PSUs (BOM): H18-UP350S (LED) plus K18N-UP200S30 (main).

## Data & addressing
- DMX: 3-pin and 5-pin (DMX012A board, BOM; retailer listing "Control: 3-pin DMX, 5-pin DMX").
- Modes: 19CH and 25CH (firmware strings) ⚠️ (check against the console library).
- Address: MENU → Address → 001–512 → ENTER.

## Rigging & hardware
- Bracket (BOM): 140 mm quick-lock Omega (CD-D01) with 1/4-turn quick-lock screws.
- **Locks (BOM):** pan lock (wheel, pick, pothook, bracket) and tilt lock (block, pick, support board).
- Weight / dimensions: Not found.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | Not found | TBD – check on next show |
| Gobo / effects module access | Gobos held by circlip Ø32×1.0 (BOM) | TBD – check on next show |
| Lens / front glass | Not found | TBD – check on next show |
| Omega bracket | 1/4-turn quick-lock | TBD – check on next show |

## Optics & consumables
- Source (BOM): LED module LCOB-4400FC2-W. That is the same part number as in the R2X Spot BOM, which may be a BOM copy error ⚠️. Wattage not confirmed.
- Two color wheels, fixed and rotating gobo wheels, prism ("prism 31 set"), frost (BOM).
- Gobos (BOM part names): aluminum "Φ29-…-25" and "Φ27-…-22.5", the same set as the R2X Spot ⚠️ (check with calipers).

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Thermistor Open / Thermistor Short / Thermistor Hot | Firmware strings. Probably a temperature sensor fault or over-temperature ⚠️ | Check fans, then service |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Grinding at power-up | Locks engaged | Release pan and tilt locks |

## Maintenance
- Firmware: github.com/Chauvet-Pro/ROGUER3SPOT (latest found: V3 08-07-2023, file "R3 SPOT-V3.230807.CHL"). That repo has no release notes or USB instructions, so expect UPLOAD 08 over DMX ⚠️.

## Road notes (community)
- No specific notes found.

## Sources
- [R3 Spot User Manual Rev 7](https://www.chauvetprofessional.com/wp-content/uploads/2018/10/Rogue_R3_Spot_UM_Rev7.pdf) — listed in search results; electrical data not captured
- [R3 Spot QRG (AV-iQ)](https://cdn-docs.av-iq.com/dataSheet/Rogue%20R3%20Spot.pdf) — listed in search results only
- [R3 Beam UM Rev 5](https://www.chauvetprofessional.com/wp-content/uploads/2021/04/Rogue_R3_Beam_UM_Rev5.pdf) — panel lock code, passcode procedure (sibling model)
- [gearclubdirect R3 Spot listing](https://www.gearclubdirect.com/chauvet-professional-roguer3spot-rogue-r3-spot-includes-powercon-power-cord-2pcs-omega-brackets-control-3-pin-dmx-5-pin-dmx/) — included accessories, 3-pin/5-pin DMX
- [github.com/Chauvet-Pro/ROGUER3SPOT](https://github.com/Chauvet-Pro/ROGUER3SPOT) — firmware files, BOM (locks, fuse, connectors, gobos), firmware strings (modes, messages)
