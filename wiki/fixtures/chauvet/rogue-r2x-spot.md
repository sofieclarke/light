---
title: "Chauvet Professional Rogue R2X Spot"
manufacturer: "Chauvet Professional"
model: "Rogue R2X Spot"
aliases: ["r2x spot", "rogue r2x spot", "r2 spot", "rogue r2 spot", "roguer2xspot", "roguer2spot"]
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
  connectors: "3-pin and 5-pin XLR in/out (BOM)"
  protocols: ["DMX", "RDM"]
  modes:
    - { name: "18CH", channels: 18 }
    - { name: "21CH", channels: 21 }
menu_password: "2323"
tools: []
verification: "web-search"
last_updated: "2026-10-03"
---

# Chauvet Professional Rogue R2X Spot (also covers R2 Spot)

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** **2323** is the Rogue offset (Zero Adjust) passcode: **hold MENU** on the main screen → passcode screen → 2323 → ENTER. The R2 Spot and R2X Spot manuals came up in searches for this procedure, and the firmware has "Password" and "Zero Adjust" screens. Exact R2X Spot wording not seen ⚠️.
> - **Power:** amps **Not found — fill in from the fixture label**. Link limit not found.
> - **DMX:** 18CH or 21CH (firmware strings; the QLC+ community R2 Spot profile agrees). 3-pin and 5-pin XLR.
> - **Won't move?** It has **pan lock and tilt lock** (BOM). Release both.
> - **Tools:** TBD – check on next show.

## Identity
- What crews call it: "R2 Spot", "R2X Spot".
- Variants:
  - **R2 Spot**: the original. Firmware V4 / V4.1 (2015–2016), as a .CL file for UPLOAD 08.
  - **R2X Spot**: the successor. Firmware V4.2017+ as a .CHL file.
  - **R2E Spot**: a separate, newer model with its own repo.
  - The two BOMs share pan/tilt lock and gobo part numbers, so the mechanics are similar.
- R2X Spot firmware V4.211118 was "updated to be compatible with fixtures with new and old ICs", and V4.191024 matched "the new MCU on the MPCB". So hardware revisions exist. Use current firmware.

## Passwords, menu locks & hidden menus
- **2323**: press and hold MENU from the main level until the passcode screen appears. UP raises the value, DOWN moves to the next digit. Then ENTER → Zero Adjust (offset). Search summaries cite this as common to the R2 Spot, R2 Wash, R2X Beam, R1 and others ⚠️.
- Firmware strings: "Password", "Zero Adjust".
- Panel lock (UP, DOWN, UP, DOWN, ENTER) is documented on the R2X Beam and R3 Beam. On this model it's ⚠️ unverified.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found | Not found | Not found |
| Power (W) | Not found | Not found | Not found |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | Can't compute | Can't compute | Can't compute |

- Connectors (BOM): powerCON NAC3MPA-1 in and NAC3MPB-1 out. Supplied cord: powerCON to Edison, 1.5 m.
- Fuse (BOM): 7 A 5×20 mm 250 V. The R2 Spot BOM lists a panel-mount fuse holder with no rating shown.
- PSUs (BOM): H18-UP350S (LED) plus 30 V 5 A (main).

## Data & addressing
- DMX: 3-pin and 5-pin XLR in and out (BOM: DMX012A board. The R2 Spot BOM lists separate 3-pin and 5-pin sockets).
- Modes: 18CH and 21CH.
- Address: MENU → Address → 001–512 → ENTER.
- Firmware V4.200225 "fixed ETC identifying issue" and corrected the product UID. Update if RDM or Eos discovery misbehaves.

## Rigging & hardware
- Bracket (BOM): 140 mm quick-lock Omega bracket (CD-D01) with 1/4-turn quick-lock screws.
- **Locks (BOM):** pan lock (wheel, hook, pick) and tilt lock (block, pick, support board). Location: TBD – check on next show.
- Weight / dimensions: Not found.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | Not found | TBD – check on next show |
| Gobo / effects module access | Gobos held by circlip Ø32×1.0 (BOM) | TBD – check on next show |
| Lens / front glass | Not found | TBD – check on next show |
| Omega bracket | 1/4-turn quick-lock | TBD – check on next show |

The BOM also lists M8×35 and M8×90 screws with M8 lock nuts, location not stated. The R2 Spot pan orientation post uses M4×8.

## Optics & consumables
- Source (BOM): LED module LCOB-4400FC2-W. Wattage not confirmed ⚠️. The same module part number also appears in the R3 Spot BOM.
- Color: two color wheels (SPP-18-A / SPP-18-B).
- Gobos: a fixed wheel and a rotating wheel. The BOM lists aluminum gobos named "Φ29-…-25" and "Φ27-…-22.5". That reads as OD 29 mm or 27 mm, with the second number possibly image size ⚠️ (inferred from part names; check with calipers). The R2 Spot BOM also has one "STEEL GOBO 27".
- Iris, prism wheel, frost (BOM).

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Thermistor Open / Thermistor Short / …Hot | Firmware strings. Probably a temperature sensor fault or over-temperature ⚠️ | Check fans, then service |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Grinding at power-up / won't home | Pan or tilt lock engaged | Release locks |
| Eos/ETC doesn't identify it properly | Old firmware | V4.200225+ |
| Manual test mode broken | Old firmware | V4.231211 |

## Maintenance
- Firmware: .CHL (R2X) or .CL (R2) files on github.com/Chauvet-Pro/ROGUER2XSPOT and /ROGUER2SPOT. No USB update instructions in these repos, so expect UPLOAD 08 over DMX ⚠️. Latest R2X Spot: V4.231211.

## Road notes (community)
- No specific notes found.

## Sources
- [R2X Spot UM Rev 3 (Innovation Lighting mirror)](https://www.innovationlighting.net/wp-content/uploads/2024/01/ROGUE_R2X_Spot_UM_Rev3_WO.pdf) — appeared in search results for the 2323 passcode procedure (content not quoted directly)
- [R2 Spot UM Rev 7 (bplsv mirror)](https://bplsv.com/manfacturers/lighting/manuals/chauvet/ROGUE_R2_Spot_UM_Rev7_WO.pdf), [R2 Spot UM Rev 9](https://www.chauvetprofessional.com/wp-content/uploads/2015/06/ROGUE_R2_Spot_UM_Rev9_WO.pdf) — cited in the summary of Rogue models sharing passcode 2323
- [github.com/Chauvet-Pro/ROGUER2XSPOT](https://github.com/Chauvet-Pro/ROGUER2XSPOT), [github.com/Chauvet-Pro/ROGUER2SPOT](https://github.com/Chauvet-Pro/ROGUER2SPOT) — firmware history, BOMs (locks, fuse, connectors, gobos, LED module, Omega), firmware strings (modes, messages)
- [QLC+ fixture Chauvet-Rogue-R2-Spot.qxf](https://github.com/mcallegari/qlcplus/tree/master/resources/fixtures/Chauvet) — community profile with 18/21 ch modes
