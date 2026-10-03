---
title: "Chauvet Professional Rogue Outcast 1 BeamWash"
manufacturer: "Chauvet Professional"
model: "Rogue Outcast 1 BeamWash"
aliases: ["outcast 1", "outcast 1 beamwash", "outcast 1 beam wash", "rogue outcast 1", "o1 beamwash", "rogueoutcast1beamwash"]
type: "beam-wash"
light_source: "LED 7x 45W RGBW + ring of 97x 0.2W RGB (12 zones)"
ip_rating: IP65
weight_lb: 20
weight_kg: 9.16
dimensions: "11.92 x 7.58 x 15.75 in (303 x 192 x 391 mm)"
power:
  input: "100–240 VAC, 50/60 Hz, auto-ranging"
  connector_in: "Seetronic Powerkon IP65 (SAC3MPX)"
  connector_out: "Seetronic Powerkon IP65 (SAC3FPX)"
  watts_max: null
  amps_120v: 3.25
  amps_208v: 1.92
  amps_230v: 1.69
  link_max_120v: 3
  link_max_208v: 6
  link_max_230v: 7
  per_20a_120v: 4
  per_20a_208v: 7
  fuse: "F8A (8 A) in FH15-22A holder, per Chauvet BOM"
dmx:
  connectors: "5-pin XLR IP65 in/out"
  protocols: ["DMX", "RDM"]
  modes:
    - { name: "15CH", channels: 15 }
    - { name: "24CH", channels: 24 }
    - { name: "30CH", channels: 30 }
    - { name: "37CH", channels: 37 }
    - { name: "54CH", channels: 54 }
    - { name: "64CH", channels: 64 }
    - { name: "111CH", channels: 111 }
    - { name: "135CH", channels: 135 }
menu_password: "2323"
tools: []
verification: "web-search"
last_updated: "2026-10-03"
---

# Chauvet Professional Rogue Outcast 1 BeamWash

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** **2323**. **Hold MENU** on the main screen → passcode screen. **UP** raises the digit, **DOWN** goes to the next digit → **ENTER**. This opens Offset / Zero Adjust.
> - **Power:** 3.25 A @120 V / 1.92 A @208 V → **4 per 20 A circuit @120 V, 7 @208 V**. Manual's link limit is 3 @120 V, 6 @208 V and 7 @230 V, with a 12 A max.
> - **DMX:** 15 / 24 / 30 / 64 / 111 / 135 ch in the manual. Firmware also has 37CH and 54CH. Address: MENU → Address → 001–512.
> - **Won't move?** No transport-lock parts in the BOM ⚠️. Try a Reset Function → Pan/Tilt. LEDs stay dark for about 3 s after a full reset on purpose (firmware V1.221103+).
> - **Tools:** TBD – check on next show.

## Identity
- What crews call it: "Outcast 1", "Outcast BeamWash", "O1".
- Fixture library names: model ID ROGUEOUTCAST1BEAMWASH. Not found — fill in from the fixture.
- Variants:
  - **Rogue Outcast 1 BeamWash M** (newer, has its own manual).
  - **Outcast 1 Beam**, **Outcast 1L Beam** and **Outcast 1M Beam** are different fixtures. They are narrow beams with no LED ring. Don't load the wrong profile.

## Passwords, menu locks & hidden menus
- **Passcode 2323** for Offset Mode / Zero Adjust: from the main level, press and hold MENU until the passcode screen appears, enter 2323 with UP/DOWN, then ENTER. Pick PAN, TILT, ZOOM, RDM4, RDM5 or RDM6 and trim 000–255.
- The firmware contains the strings "Password" and "Zero Adjust".
- Panel lock: not confirmed on this model. See `_chauvet-common.md`.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | 3.25 | 1.92 | 1.69 |
| Power (W) | Not found | Not found | Not found |
| Max power-link (manufacturer) | 3 (12 A max) | 6 (12 A max) | 7 (12 A max; also 7 @240 V) |
| **Max per 20 A circuit** (16 A continuous) | floor(16/3.25)=4 (link limit 3+1=4) → **4** | floor(16/1.92)=8 (link limit 6+1=7) → **7** | floor(16/1.69)=9 (link limit 7+1=8) → **8** |

- The manual gives the link limit as "up to 3 at 100 V or 120 V". Each limit equals floor(12 A ÷ current), so it may mean the **total** on one 12 A chain. If you read it that way, the conservative counts are **3 @120 V, 6 @208 V**.
- Input: 100–240 VAC auto-ranging. Connectors: Seetronic Powerkon IP65 in and out. The US kit ships an Edison to Powerkon cable.
- Fuse: F8A in an FH15-22A holder with an IP fuse safety cap (BOM).

## Data & addressing
- Connectors: 5-pin XLR IP65 in and out (J5F2C / K5F2C).
- Modes: the manual and retailers list 15, 24, 30, 64, 111 and 135. The firmware strings also include **37CH and 54CH** ⚠️. These probably came with firmware V1.220822 "Added new personalities". Check the menu on the fixture.
- Address: MENU → Address → 001–512 → ENTER.
- Pan Reverse and Tilt Reverse: OFF/ON.
- Factory reset: Setup → Factory Reset → YES.
- Firmware V1.251216 **removed the "custom white mode" menu option**, and control-channel values 232–239 are now reserved. Old show files that use those values will act differently.

## Rigging & hardware
- Bracket: 120 mm Omega bracket (BOM). Clamps not included.
- Transport locks: none in the BOM ⚠️.
- Weight: 20 lb (9.16 kg). Dimensions: 11.92 × 7.58 × 15.75 in (303 × 192 × 391 mm).
- Pan/tilt: 540° / 260°, with selectable ranges 180/360/540 pan and 90/180/260 tilt.
- Pressure valve VV-POVM12022 in the base. It has a defrost fan; firmware V1.220311 fixed a bug that kept the defrost fan always on.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | Not found | TBD – check on next show |
| Gobo / effects module access | n/a | n/a |
| Lens / front glass | Front glass Ø190/198 × 3 mm with gasket (BOM) | TBD – check on next show |
| Omega bracket | Quarter-turn | TBD – check on next show |

## Optics & consumables
- Source: 7 × 45 W RGBW LEDs plus a 12-zone ring of 97 × 0.2 W RGB LEDs. Rated 50,000 h.
- Zoom: 3.9°–55.3°.
- Firmware has Red Shift (V1.220112+) and separate ring/center power adjustment (V1.240718+).

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Thermistor Open / Short | Firmware string. Probably a temperature sensor fault ⚠️ | Service |
| Lamp Hot / Hot | Firmware string. Probably over-temperature ⚠️ | Check fans and airflow |
| USB Error / File Not Found / USB Disconnected | USB update messages | FAT32 drive, .chl file in root |

The manual's error table was not found.

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| LEDs dark for a few seconds after reset | Intentional 3 s delay (V1.221103) | Wait |
| USB stick not detected for update | Old firmware bug | Fixed in V1.220217. On older units use UPLOAD 08 |
| Color shift when RGBW all go 0→255 together | Firmware bug | Fixed in V1.251216 |

## Maintenance
- Firmware: USB-C port (BOM). Same USB procedure as the other Outcast models (see `_chauvet-common.md`). Latest found: V1.251216 on github.com/Chauvet-Pro/ROGUEOUTCAST1BEAMWASH.

## Road notes (community)
- No specific forum notes found.

## Sources
- [Rogue Outcast 1 Beam Wash UM Rev 7](https://www.chauvetprofessional.com/wp-content/uploads/2021/06/Rogue_Outcast_1_Beam_Wash_UM_Rev7.pdf), [Rev 4 (B&H)](https://www.bhphotovideo.com/lit_files/938773.pdf), [Rev 5 (enlx mirror)](https://enlx.co.uk/wptemp/wp-content/uploads/2024/05/Rogue_Outcast_1_Beam_Wash_UserManual.pdf) — current draw, link limits, passcode/offset, pan/tilt reverse
- [Outcast 1 BeamWash datasheet](https://saleswl.com/wp-content/uploads/2021/07/Chauvet-Professional-Rogue-Outcast-1-BeamWash-Data-Sheet.pdf), [B&H page](https://www.bhphotovideo.com/c/product/1658235-REG/chauvet_professional_rogueoutcast1beamwash_rogue_outcast_1_beam.html), [Stage Lighting Store](https://www.stagelightingstore.com/Rogue-Outcast-1-BeamWash) — LEDs, weight, zoom, modes, dimensions, pan/tilt, Edison→Powerkon
- [Outcast 1 BeamWash M manual](https://www.chauvetprofessional.com/wp-content/uploads/2025/03/Rogue_Outcast_1_BeamWash_M_UM_Rev1.pdf) — M variant
- [github.com/Chauvet-Pro/ROGUEOUTCAST1BEAMWASH](https://github.com/Chauvet-Pro/ROGUEOUTCAST1BEAMWASH) — firmware history, BOM (fuse, connectors, Omega, glass, valve), firmware strings (modes, messages)
