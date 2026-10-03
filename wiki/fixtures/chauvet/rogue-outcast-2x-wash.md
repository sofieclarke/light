---
title: "Chauvet Professional Rogue Outcast 2X Wash"
manufacturer: "Chauvet Professional"
model: "Rogue Outcast 2X Wash"
aliases: ["outcast 2x", "outcast 2x wash", "rogue outcast 2x", "o2x wash", "rogueoutcast2xwash"]
type: "wash"
light_source: "LED 19x 25W RGBW quad-color, 5 pixel zones"
ip_rating: IP65
weight_lb: 23.4
weight_kg: 10.6
dimensions: "11.92 x 8.58 x 14.1 in (303 x 218 x 361 mm)"
power:
  input: "100–240 VAC, 50/60 Hz, auto-ranging"
  connector_in: "Seetronic Powerkon IP65 (SAC3MPX)"
  connector_out: "Seetronic Powerkon IP65 (SAC3FPX)"
  watts_max: 291
  amps_120v: 2.47
  amps_208v: 1.41
  amps_230v: 1.28
  link_max_120v: 5
  link_max_208v: 9
  link_max_230v: null
  per_20a_120v: 5
  per_20a_208v: 9
  fuse: "F8A (8 A) in panel fuse holder FH15-22A, per Chauvet BOM; size/blow type not stated"
dmx:
  connectors: "5-pin XLR IP65 in/out"
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

# Chauvet Professional Rogue Outcast 2X Wash

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** **2323**. From the main screen, **press and hold MENU** until the passcode screen appears. **UP** raises the digit, **DOWN** moves to the next digit, then **ENTER**. This opens Offset / Zero Adjust (fine home-position trim for Pan, Tilt, Zoom). Source: manual Rev 4/Rev 7 search summaries.
> - **Power:** 2.47 A @120 V / 1.41 A @208 V → **5 per circuit @120 V, 9 @208 V** (Chauvet link limit, counted as the total on one feed; 12 A max per circuit).
> - **DMX:** 15/17/22/33/54/56/33MS/54MS in the manual. Firmware V1.230504+ adds 23CH and 55CH. Address: MENU → Address → 001–512 → ENTER.
> - **Won't move?** No pan/tilt lock parts show up in Chauvet's parts list (BOM), so it probably has no transport locks ⚠️ unverified. Run Setup → Reset Function → Pan/Tilt.
> - **Tools:** head back cover uses M3×8 stainless hex socket cap screws and the front cover uses M4×12 countersunk hex screws (BOM). Bit size: see the Tools table.

## Identity
- What crews call it: "Outcast 2X", "O2X wash", "the IP R2X".
- Fixture library / profile names: Chauvet lists the model ID as ROGUEOUTCAST2XWASH. Profile names for MA3, GDTF, Hog and Eos were not checked. Not found — fill in from the fixture.
- Variants and how to tell them apart:
  - **Rogue Outcast 2X Wash M** (ROGUEOUTCAST2XWASHM) is a newer variant. A retailer lists it as IP66, and it has a USB-C update port. It has its own manual: Rogue_Outcast_2X_Wash_M_UM_Rev1. Check the rear label.
  - **Rogue R2X Wash** is the indoor sibling. The Outcast 2X Wash BOM lists a "light guide assembly R2X WASH" and a "frost filter PRO-1915" (an R2 Wash part family), so the optics look shared with the R2X/R2 Wash. This is inferred from part names ⚠️.

## Passwords, menu locks & hidden menus
- **Default passcode: 2323** (Offset Mode / Zero Adjust).
  1. Go to the main level screen.
  2. Press and hold **MENU** until "Password" appears.
  3. **UP** raises the current digit and **DOWN** moves to the next digit. Enter 2-3-2-3.
  4. Press **ENTER**.
  5. Choose **PAN, TILT, ZOOM, RDM4, RDM5 or RDM6**. That list comes from the search summary; the "RDM4–6" items look odd ⚠️. Adjust the zero point 000–255.
- The firmware for this model contains the strings "Password" and "Zero Adjust", which matches this procedure.
- Control-panel lock: some other Rogue and Outcast models have a panel lock with code UP, DOWN, UP, DOWN, ENTER (see `_chauvet-common.md`). No "lock" menu string was found in this fixture's firmware, so it may not have one ⚠️ unverified.
- Service / factory menu: Not found — fill in from the fixture.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | 2.47 | 1.41 | 1.28 |
| Power (W) | 291 | 284 | 282 |
| Max power-link (manufacturer) | 5 (12 A max) | 9 (12 A max) | Not found |
| **Max per 20 A circuit** (16 A continuous) | link limit **5** total (5 × 2.47 = 12.4 A, Chauvet's 12 A cap) → **5** | link limit **9** total (9 × 1.41 = 12.7 A) → **9** | floor(12/1.28)=9 (no link limit found, using Chauvet's 12 A cap) → **9** ⚠️ |

Chauvet link limits are read as the **total** on one feed. Every Chauvet limit works out to about 12 A total, which matches the manual's 12 A cap; see [power math](../../reference/power-math.md).

- Input range: 100–240 VAC, 50/60 Hz, auto-ranging.
- Connectors: Seetronic Powerkon IP65 in and out (BOM parts SAC3MPX male in, SAC3FPX female out). A manual summary describes the supplied input cable as Powerkon A to bare wire. US retail listings for the sister Outcast models show Edison to Powerkon. Powerkon is NOT a standard Neutrik powerCON cable, so carry the right jumpers.
- **Link-limit wording:** the manual says "power link up to 5 products at 120 V or 9 at 208 V… maximum of 12 A on a single circuit." It does not clearly say whether the first fixture counts. 5 × 2.47 A = 12.35 A and 9 × 1.41 A = 12.7 A, both right at the 12 A cap, so this wiki reads the limit as **5 total @120 V, 9 total @208 V**.
- Fuse: F8A (8 A) in an FH15-22A holder with an IP fuse cap (Chauvet BOM). Fuse body size and slow/fast type were not stated ⚠️.
- Inrush notes: Not found.

## Data & addressing
- Connectors: 5-pin XLR IP65 in and out (BOM: J5F2C male / K5F2C female).
- Protocols: DMX, RDM.
- DMX modes: the manual lists 56CH, 54CH, 33CH, 22CH, 17CH, 15CH, 54MS and 33MS. GitHub firmware notes say V1.230504 "Added 55CH and 23CH personalities". Firmware strings confirm all 10 modes.
- Set the address: MENU → **Address** → UP/DOWN to 001–512 → ENTER.
- Set the personality: MENU → Personality (or DMX Personality) → choose → ENTER.
- Factory reset: Setup → **Factory Reset** (or Reset Function → Factory Settings) → YES. Reset Function also has Pan/Tilt, Zoom and All. Sys Info shows the firmware version.
- Other settings: Pan Reverse, Tilt Reverse, Screen Rev (display invert), Display On/Off, and Fan Mode (Auto / Full / ECO = quiet). Firmware also has Dimmer Curve (Linear/Square/I-Square/S-Curve), White Mode, Color calibration and a Running Mode (DMX / Auto / Sound / Slave / IR / Manual).
- Wireless / Ethernet: none.

## Rigging & hardware
- Bracket: 2 Omega brackets are included (BOM part "Omega Bracket CD-D11"). Clamps are sold separately. Clamp spacing: Not found.
- The search summary gives an Omega holder torque of "12.2 kgf·cm / 10.6 lbf·in". It is unclear what that applies to ⚠️.
- Safety cable: use one when flown. Attachment point: Not found — fill in from the fixture.
- Orientations: Not found. Outdoor IP65 units normally have orientation limits for water ingress, so check the manual ⚠️.
- Transport locks: no pan/tilt lock parts in the BOM. Probably none ⚠️ unverified.
- Weight / dimensions: 23.4 lb (10.6 kg); 11.92 × 8.58 × 14.1 in (303 × 218 × 361 mm).
- There is a pressure-equalising vent valve in the base (BOM: VV-P465). Don't block or pressure-wash it.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | Head back cover: M3×8 stainless hex socket cap screw. Head front cover: M4×12 stainless countersunk hex (Chauvet BOM) | 2.5 mm hex for both, from ISO screw standards, not from Chauvet ⚠️. TBD – check on next show |
| Gobo / effects module access | No gobos (wash) | n/a |
| Lens / front glass | Glass Ø193×3 mm behind a front cover (BOM) | TBD – check on next show |
| Omega bracket | Quarter-turn | TBD – check on next show |

## Optics & consumables
- Source: 19 × 25 W RGBW LEDs in 5 pixel-mappable zones. Rated 50,000 h. 16-bit dimming.
- Color: RGBW, CTO/CTC 2800–10000 K. Firmware V1.260610 added a CTC preset to the color macro channel.
- Zoom: 8°–66.1°. Output 6,258 lm (spec sheet).
- Frost filter: listed in the BOM.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Thermistor Open / Thermistor Short | Found as firmware strings only. Probably a failed or disconnected temperature sensor ⚠️ | Not found in the manual. Check head wiring, then call Chauvet service |
| Lamp Hot | Found as a firmware string. Probably LED over-temperature ⚠️ | Check fans and airflow, set Fan Mode to Full |
| USB Error / File Not Found / USB Disconnected | Firmware strings from the USB update routine | Use a FAT32 drive of 32 GB or less with the .chl file in the root folder |

The manual's error-code table did not come through in search. Not found — fill in from the fixture.

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Home position slightly off | Offset drifted or was changed | Passcode 2323 → Zero Adjust → trim Pan/Tilt |
| White shifts as it settles after a color change | Known firmware bug | Fixed in V1.240318. Update firmware |
| Ring flicker at low dimming | Known firmware bug | Fixed in V1.230928 |
| Console has no 23CH or 55CH mode | Old firmware | Update to V1.230504 or later |

## Maintenance
- Recalibrate: Setup → Reset Function → Pan/Tilt / Zoom / All.
- Fans: Fan Mode Auto / Full / ECO. Cleaning interval: Not found.
- **Firmware:** USB flash drive in the fixture's USB-C port (BOM lists a USB-C connector). Use FAT32, 32 GB max, with the .chl file in the root folder.
  1. Power on and insert the drive. "USB Update" appears → YES.
  2. Pick the version → ENTER → YES.
  3. "USB Update Wait" shows. **Do not cut power while the USB LED blinks.**
  4. The fixture reboots. Check Sys Info.
- If a USB update fails part-way, Chauvet says you need the **UPLOAD 08** to recover. Latest firmware as of this writing: V1.260610 on github.com/Chauvet-Pro/ROGUEOUTCAST2XWASH. See `_chauvet-common.md`.

## Road notes (community)
- No Outcast 2X–specific forum threads turned up. ControlBooth threads on its sibling the R2X Wash (home position 90° off after DMX re-plug; color-change delay on R2 Wash) are on the R2X Wash page.

## Sources
- [Rogue Outcast 2X Wash User Manual Rev 4](https://www.chauvetprofessional.com/wp-content/uploads/2022/08/Rogue_Outcast_2X_Wash_UM_Rev4.pdf) — passcode 2323 and how to enter it, offset functions, current/watts, link limits, personalities, menu buttons, factory reset, fan/display/invert settings
- [Rogue Outcast 2X Wash User Manual Rev 6](https://www.chauvetprofessional.com/wp-content/uploads/2022/08/Rogue_Outcast_2X_Wash_UM_Rev6.pdf) and [Rev 7 (Innovation Lighting mirror)](https://www.innovationlighting.net/wp-content/uploads/2024/11/Rogue_Outcast_2X_Wash_UM_Rev7.pdf) — same data, settings menu
- [Rogue Outcast 2X Wash User Manual Rev 1 (riggit mirror)](https://riggit.com/wp-content/uploads/2023/01/Rogue_Outcast_2X_Wash_UM_Rev1.pdf) — Omega brackets, safety cable
- [Rogue Outcast 2X Wash M User Manual Rev 1](https://www.chauvetprofessional.com/wp-content/uploads/2025/03/Rogue_Outcast_2X_Wash_M_UM_Rev1.pdf) — M variant, USB-C update
- [Outcast 2X Wash datasheet (Full Compass)](https://www.fullcompass.com/common/files/84770-RogueOutcast2XWashDatasheet.pdf), [B&H product page](https://www.bhphotovideo.com/c/product/1714499-REG/chauvet_professional_rogueoutcast2xwash_rogue_outcast_2x_washincludes.html), [Full Compass product](https://www.fullcompass.com/prod/612879-chauvet-pro-rogue-outcast-2x-wash-moving-head-wash-fixture) — weight, dimensions, LEDs, zoom, lumens, Powerkon
- [github.com/Chauvet-Pro/ROGUEOUTCAST2XWASH](https://github.com/Chauvet-Pro/ROGUEOUTCAST2XWASH) — firmware history, USB update procedure, BOM PDF (fuse F8A, connectors, screws, Omega CD-D11, vent valve, USB-C), firmware strings (error messages, modes)
- [manuals.plus copy](https://manuals.plus/chauvet-professional/1512-rogue-outcast-2x-wash-manual) — passcode procedure, cross-check
