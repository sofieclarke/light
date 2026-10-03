---
title: "Chauvet Professional COLORado PXL Curve 12"
manufacturer: "Chauvet Professional"
model: "COLORado PXL Curve 12"
aliases: ["pxl curve", "pxl curve 12", "curve 12", "colorado pxl curve", "coloradopxlcurve12"]
type: "pixel-bar"
light_source: "LED 12x 45W RGBW (12 individually tilting heads)"
ip_rating: IP65
weight_lb: 76
weight_kg: 34.5
dimensions: "39.49 x 12.76 x 6.65 in (1003 x 324 x 169 mm)"
power:
  input: "100–240 VAC, 50/60 Hz, auto-ranging (⚠️ assumed from family)"
  connector_in: "Seetronic Powerkon IP65 (power input cord with Edison plug, US)"
  connector_out: null
  watts_max: null
  amps_120v: 6.70
  amps_208v: 3.80
  amps_230v: null
  link_max_120v: 1
  link_max_208v: 3
  link_max_230v: 3
  per_20a_120v: 1
  per_20a_208v: 3
  fuse: null
dmx:
  connectors: null
  protocols: ["DMX", "Art-Net", "sACN"]
  modes:
    - { name: "Single", channels: 20 }
    - { name: "Single", channels: 53 }
    - { name: "Single", channels: 101 }
    - { name: "Single", channels: 155 }
    - { name: "Single", channels: 179 }
    - { name: "Dual Movement", channels: 8 }
    - { name: "Dual Movement", channels: 41 }
    - { name: "Dual Movement", channels: 53 }
    - { name: "Dual Movement", channels: 59 }
    - { name: "Dual Pixels", channels: 36 }
    - { name: "Dual Pixels", channels: 48 }
    - { name: "Dual Pixels", channels: 96 }
menu_password: "2323"
firmware:
  latest_known: "V1.251029"
  checked: "2026-10-03"
  check_on_fixture: "MENU → Sys Info → Firmware Version (README says 'Fixture Information')"
  methods: ["USB stick (USB-C)", "Web server (Ethernet)", "DMX cable + UPLOAD 08 (recovery)"]
  interface: null
  software: "Web browser (fixture web server)"
  file_type: ".chl"
  download: "https://github.com/Chauvet-Pro/COLORADOPXLCURVE12"
tools: []
verification: "web-search"
last_updated: "2026-10-03"
---

# Chauvet Professional COLORado PXL Curve 12

> **2AM CARD** — the stuff you need first
> - **Power:** 6.70 A @120 V / 3.80 A @208 V → **1 per circuit @120 V, 3 @208 V** (Chauvet link limits 1 @120 / 3 @208 / 3 @230 V, "no single circuit exceeding 12 A")
> - **Password:** from the Main Level, press and hold **MENU** → passcode **2323** (Zero Adjust)
> - **DMX:** Single 20/53/101/155/179 · Dual Movement 8/41/53/59 · Dual Pixels 36/48/96
> - **Power in is a Seetronic Powerkon IP65**, not TRUE1. Bring the right whip.
> - **Tools:** TBD – check on next show.

## Identity
- What crews call it: "PXL Curve", "Curve 12".
- Fixture library / profile names: Chauvet Professional "COLORado PXL Curve 12". Chauvet's GitHub repo: github.com/Chauvet-Pro/COLORADOPXLCURVE12 (⚠️ unverified what it contains).
- Variants and how to tell them apart: 12 heads that tilt **individually** (tilt 200° / 180° per spec). The PXL Bar 8/16 tilt as one piece.

## Passwords, menu locks & hidden menus
- **Zero Adjust: passcode 2323.** From the Main Level, press and hold MENU until the passcode screen appears.
- **Web Server:** exists, and firmware can be updated through it. Login: Not found (the PXL Bar 16 uses admin/admin, ⚠️ unverified here).
- Service menu: Not found.
- Display lock: Not found.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | 6.70 | 3.80 | Not found |
| Power (W) | Not found | Not found | Not found |
| Max power-link (manufacturer) | 1 | 3 | 3 |
| **Max per 20 A circuit** (16 A continuous) | floor(16/6.70)=2, 12 A rule floor(12/6.70)=1 = link 1 → **1** | floor(16/3.80)=4, floor(12/3.80)=3 = link 3 → **3** | 230 V amps not found → link limit **3** |

- **How to read the link limit.** The manual's table shows current per voltage "with no single circuit exceeding 12 A" and lists "1 unit @ 120 V; 3 units @ 208 V; 3 units @ 230 V". At 120 V, 1 unit = 6.7 A and 2 = 13.4 A, so the number counts **total fixtures on the circuit**.
- Input range: likely 100–240 VAC auto-ranging like the rest of the family (⚠️ unverified).
- Connectors in / out: power input cord with a **Seetronic Powerkon IP65** connector and an Edison plug (US). Power-linking cables are sold separately. Output connector type: Not found.
- Fuse: Not found.
- Inrush: none found.

## Data & addressing
- Connectors: Not found — fill in from the fixture.
- Protocols: DMX, Art-Net, sACN (⚠️ from the family, unverified).
- DMX modes / footprints: Single Mode 20 / 53 / 101 / 155 / 179. Dual Mode Movement 8 / 41 / 53 / 59. Dual Mode Pixels 36 / 48 / 96. Mode names weren't in the excerpts.
- Set the address: Not found.
- Battery / unpowered addressing: Not found.
- Factory reset: Not found.
- Wireless / Ethernet setup: there is a Web Server (supports firmware update).

## Rigging & hardware
- Bracket / omega: Not found.
- Fasteners: Not found.
- Safety cable point: Not found.
- Orientations: Not found.
- Transport / tilt locks: Not found.
- Weight / dimensions: 76 lb (34.5 kg). 39.49 x 12.76 x 6.65 in (100.3 x 32.41 x 16.89 cm). Much heavier than a PXL Bar 16 (45.6 lb), so allow for it in truss loading.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD – check on next show |
| Gobo / effects module access | n/a | n/a |
| Lens / front glass | TBD – check on next show | TBD – check on next show |
| Omega bracket | TBD – check on next show | TBD – check on next show |

## Optics & consumables
- Source: 12 × 45 W RGBW LEDs (retailer title).
- Color system: RGBW.
- Zoom: 5.7°–36.3°.
- Tilt: 200° / 180° (per spec; which figure applies where isn't stated).

## Error codes
The manual has an error table. The search excerpts gave only the names below, without exact codes:

| Code / message | Meaning | Fix |
|---|---|---|
| Base Fan (exact code not found) | Base fan error | Not found — likely check/replace fan as on the PXL Bar 8 |
| CPU error (exact code not found) | CPU error | Not found |
| LED overheating (exact code not found) | LED over-temperature | Not found |
| Thermistor error (exact code not found) | Thermistor fault | Not found |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| 120 V breaker trips with 2 chained | 2 × 6.7 A = 13.4 A, over the 12 A rule (limit 1 @120 V) | 1 per 120 V circuit, or 3 per circuit on 208 V |
| Can't plug in the power whip | Input is Seetronic Powerkon IP65, not TRUE1 | Use the supplied cord or a matching Powerkon cable |
| USB update ignored | Drive not FAT32, too large, or file not in the root | FAT32, ≤32 GB, .chl file in the root, Setup → USB Update |

## Maintenance
- Recalibrate: Zero Adjust (2323).
- Fan / filter cleaning: Not found.

## Firmware
- Installed version — where to see it on the fixture: the firmware has **Sys Info** screens. The GitHub README says "Fixture Information" ⚠️.
- Latest known version: **V1.251029** (latest found 2026-10-03). Download from [github.com/Chauvet-Pro/COLORADOPXLCURVE12](https://github.com/Chauvet-Pro/COLORADOPXLCURVE12) as `firmware/V1.251029.zip`, which holds `A40833-COLORado PXL Curve 12-V1.251029-251029-1.CHL`.
- What you need: a FAT32 USB stick (≤32 GB) with USB-C or an adapter, or a laptop on Ethernet for the web server. Keep an UPLOAD 08 for recovery.
- Update steps (USB stick, from Chauvet's GitHub README; the manual's menu has Setup → USB Update):
  1. Unzip the download. Copy only the **.CHL** file to the **root** of a **FAT32** stick, **32 GB or smaller**. The GitHub zip also has a `__MACOSX` folder. Don't copy it.
  2. Power on and plug the stick into the IP65 **USB-C** port. You need a USB-C stick or an adapter.
  3. **"USB UPDATE"** appears → **YES**.
  4. Pick the version with **UP / DOWN** → **ENTER**.
  5. **"USB UPDATE"** appears again → **YES**.
  6. **"USB Update Wait"** shows. **Don't cut power or pull the stick while the USB LED blinks.** Some units then show **"DO NOT UNPLUG, UPDATING"**.
  7. The bar reboots by itself.
  8. Confirm the version, then restart.
- Web server route (the manual says firmware can be updated through the Web Server; login unconfirmed for this model, admin/admin on the PXL Bar 16 ⚠️):
  1. Set the Control Protocol to **Art-Net** and the IP mode to **Static**.
  2. Cable the fixture to a computer. Give the computer an IP address with the same first 3 numbers as the fixture's.
  3. Browse to the fixture's IP address. Log in as **admin / admin**.
  4. Open the **Upgrade** page → choose the file → **Upload File**.
  5. The page warns "Fixture updating, please wait and do not power off the fixture", then "FILE UPLOAD SUCCESS, PLEASE WAIT FOR FIXTURE TO FINISH THE UPGRADE".
  - The button and message text come from the web page built into the firmware.
- Updating a whole rig: one fixture at a time. No batch method found ⚠️.
- If it fails or bricks mid-update: partial or total firmware failure needs the **UPLOAD 08** (GitHub README). See `_chauvet-common.md`.
- Release notes worth knowing (GitHub README):
  - **V1.251029**: strobe refreshes on every value change. **Fixed random movement in MA3 Art-Net mode with RDM on.** Art-Net universes now go up to 32767. The web server works in any control mode. Also listed: "if fixture is set to tilt invert, heads will randomly get stuck during reset". Chauvet doesn't say whether that is fixed or a known issue ⚠️.
  - V1.250624 / V1.250410: sACN universe limit raised from 256 to 32000.
  - V1.250508: tilt improvement.
  - **V1.250120**: fixed the LED color changing when DMX is lost.
  - **V1.240806**: fixed sACN timing and IGMP subscription bugs.
  - V1.240509: better calibration and LED color uniformity.
  - **V1.240411**: fixed color snap. The web server mode names were corrected to Basic, Basic2, Standard, Advanced, Advanced2, Tour and Full PXL; it used to show 3/5/9/12/17/19/37.
  - V1.240222: fixed IGMP.
  - **V1.240131: added a new zoom mode.** Check the profile.
  - V1.231222: improved dimming and added tilt adjustment.

## Road notes (community)
- No forum threads turned up in search. Add notes here.

## Sources
- [COLORado PXL Curve 12 User Manual Rev 3 (Chauvet)](https://www.chauvetprofessional.com/wp-content/uploads/2023/04/COLORado-PXL-Curve-12_UM_Rev3.pdf): current draw, link limits, 12 A statement, Seetronic Powerkon input
- [User Manual Rev 6 (Chauvet)](https://www.chauvetprofessional.com/wp-content/uploads/2023/04/COLORado-PXL-Curve-12_UM_Rev6.pdf): passcode 2323, error message names
- [manualslib, USB update page 13](https://www.manualslib.com/manual/3395060/Chauvet-Colorado-Pxl-Curve-12.html?page=13): USB update, .chl, FAT32, 32 GB, Web Server update
- [User Manual Rev 1 (Hibino)](https://www.hibinolighting.co.jp/hibino_wp/wp-content/uploads/2023/08/COLORado-PXL-Curve-12_UM_Rev1.pdf): electrical
- [AV-iQ data sheet](https://cdn-docs.av-iq.com/dataSheet/COLORADOPXLCURVE12.pdf), [B&H](https://www.bhphotovideo.com/c/product/1784524-REG/chauvet_professional_coloradopxlcurve12_colorado_pxl_curve_12.html), [Farralane](https://www.farralane.com/chauvet-professional-colorado-pxl-curve-12-12-x-45w-rgbw-led-ip65-rated-batten-with-12-controllable-tilting-heads-and-5-7-to-36-3-degree-zoom.html): DMX modes, weight, dimensions, zoom, tilt
- [github.com/Chauvet-Pro/COLORADOPXLCURVE12](https://github.com/Chauvet-Pro/COLORADOPXLCURVE12) — firmware versions, release notes, USB update procedure, .CHL file name; web upgrade page text from the firmware file (checked 2026-10-03)
- [UPLOAD 08 Instructions Rev 4](https://www.chauvetprofessional.com/wp-content/uploads/2015/12/UPLOAD_08_Instructions_Rev4.pdf) — UPLOAD 08 PC setup, COM129, up to 10 same-product fixtures, Force Upload
