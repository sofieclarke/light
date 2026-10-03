---
title: "Chauvet Professional — common menus, passcodes, errors, firmware"
manufacturer: "Chauvet Professional"
model: null
aliases: ["chauvet pro password", "chauvet passcode", "rogue password", "chauvet firmware", "upload 08", "chauvet error"]
type: "reference"
verification: "web-search"
last_updated: "2026-10-03"
---

# Chauvet Professional — shared conventions (Rogue / Outcast / Maverick)

> **2AM CARD**
> - **Offset / Zero Adjust passcode: 2323.** From the main screen, **press and hold MENU** until "Password" shows. **UP** raises the digit, **DOWN** goes to the next digit → **ENTER**. Confirmed in search summaries of the manuals for the Rogue Outcast 2X Wash, Outcast 1 BeamWash, Outcast 3 Spot and R2X Wash, and cited for the R3X Wash, R3 Beam, R2 Wash, R2 Spot, R2X Beam, R1 and Outcast 1L Beam.
> - **Control-panel lock default code: UP, DOWN, UP, DOWN, ENTER.** Documented on the R3 Beam, R2X Beam, Outcast 1L Beam and Outcast 2 Beam manuals. It also appears on the Ovation C-640FC.
> - **Firmware:** Rogue Outcast, COLORado PXL and Maverick Force S take a **USB stick** (FAT32, ≤32 GB, .CHL in the root, USB-C port). Rogue R-series and Maverick MK3 use the **UPLOAD 08** (USB-to-DMX box + Windows app, up to 10 same-model fixtures). STRIKE fixtures update each other over DMX from a stick. Files: **github.com/Chauvet-Pro/<MODELNAME>**. See "Firmware updates" below.
> - **Don't pull power** during a USB update while the USB LED blinks. A failed update needs an UPLOAD 08 (Force Upload) to recover. **Firmware updates can add or rename DMX modes**, so re-check the console patch.

## Menu navigation (four-button panel)
- **MENU**: exit the current menu or function. Hold it from the main level to get the passcode screen.
- **ENTER**: open the displayed menu, or save the value.
- **UP / DOWN**: move through the list, or change the value. In passcode entry, **UP raises the digit and DOWN moves to the next digit**.
- Typical top-level items: **Address** (001–512), **Personality** (e.g. 15CH, 33MS…), **Setup**, **Sys Info**.
- Setup usually holds:
  - Pan Reverse and Tilt Reverse (OFF/ON).
  - Screen Rev (display invert) and Display (OFF = screen sleeps / ON).
  - Fan Mode (Auto / Full / ECO-quiet on Outcast).
  - Dimmer Curve, White Mode, Running Mode (DMX / Auto / Sound / Slave …).
  - Reset Function (Pan/Tilt, Zoom, All, Factory Settings).
  - USB Update.
  - Source: Outcast 2X Wash manual summaries plus firmware strings.
- **Factory reset:** Setup → Factory Reset (or Reset Function → Factory Settings) → YES.
- **"MS" personalities** (33MS, 54MS) are the multi-segment / pixel modes on the wash fixtures (general knowledge).

## Passcodes (sourced only)
| Code | What it opens | Where it's documented |
|---|---|---|
| **2323** | Offset / Zero Adjust: home-position trim for Pan, Tilt, Zoom and other motors, 000–255 | Outcast 2X Wash UM Rev 4/6/7, Outcast 1 BeamWash UM, Outcast 3 Spot UM Rev 3, R2X Wash UM (manualslib). Also cited for R3X Wash, R3 Beam, R2 Wash, R2 Spot, R2X Beam, R1, Outcast 1L Beam |
| **UP, DOWN, UP, DOWN, ENTER** | Unlocks the control-panel lock (Menu Access Lock) | R3 Beam UM Rev 5, R2X Beam UM Rev 1, Outcast 1L Beam UM, Outcast 2 Beam UM Rev 4 |

- One search result noted that the "press and hold" button renders as a blank glyph in some PDFs. The manualslib text of the R2X Wash manual and the Outcast 2X Wash summary both name **MENU**.
- Every Rogue and Outcast firmware file checked (O1BW, O2X, O3S, R2XW, R2XS, R3S, R3XW) contains both "Password" and "Zero Adjust" screens.
- No other service or factory passcodes were found. Don't trust forum "master codes" without a manual source.

## Common messages (from firmware strings)
These strings were pulled from Chauvet's own firmware files on GitHub. The **meanings are inferred** ⚠️. The manual error tables were not reachable during research.

| Message | Probable meaning | First fix |
|---|---|---|
| Thermistor Open | Temperature sensor open circuit or unplugged | Check head wiring and connectors, then service |
| Thermistor Short | Temperature sensor shorted | Service |
| Thermistor Hot / Lamp Hot / Hot | Over-temperature (LED engine) | Check fans and filters, set Fan Mode to Full, give it shade or airflow |
| Light Block (Outcast 3 Spot only) | Unknown | Not found — fill in from the fixture |
| USB Update / USB Update Wait | Update in progress | Wait. Don't pull power |
| USB Error / File Not Found / USB Disconnected | Bad stick, wrong format, or .chl not in the root folder | FAT32, 32 GB max, file in root, one model's file |

## Firmware updates
Checked 2026-10-03. "Chauvet Pro Upload / CHAUVET Pro Firmware Uploader" was **not found** as a product name. Chauvet uses four update routes. Which one a fixture takes depends on its ports.

### Which route for which fixture
| Route | Hardware | Software | Cable / media | File | Fixtures in this wiki |
|---|---|---|---|---|---|
| **A. USB stick, "USB Update" menu** | FAT32 stick, **≤32 GB**, USB-C plug or adapter | none | stick in the fixture's USB-C port | `.CHL` in the stick's **root** | Rogue Outcast 1 BeamWash / 2X Wash / 3 Spot, COLORado PXL Bar 8 / Bar 16 / Curve 12, Maverick Force S Spot |
| **B. USB stick, "Upgrade Firmware" menu (STRIKE family)** | FAT32 stick; a 5-pin DMX cable for other units | none | stick in USB-C; DMX to slave units | `.chl` (root per GitHub; the Color STRIKE M manual says a `STRIKE` folder) | Color STRIKE M, STRIKE Array 4 |
| **C. UPLOAD 08 over DMX** | **UPLOAD 08** (SKU UPLOAD08): USB-powered USB-to-DMX box with **3-pin and 5-pin XLR** | UPLOAD 08 Setup **v4.5.2+** (Windows XP or later) + MS .NET + Silicon Labs **CP210x** driver | USB cable to the PC; DMX cable to the fixtures | `.CHL` or older `.CL` | Rogue R2X Spot / R2X Wash / R3 Spot / R3X Wash, Maverick MK3 Spot / MK3 Wash, and **recovery for route A** |
| **D. Web server (Ethernet)** | laptop + network cable | web browser, login **admin / admin** | Art-Net, static IP | `.CHL` via the **Upgrade** page | COLORado PXL Bar 16 and Curve 12 (manuals), Maverick MK3 Spot (manual), MK3 Wash (repo README says "Uploader 08, Webserver"). Firmware strings suggest PXL Bar 8 and Force S Spot too ⚠️ |

- **CHAUVET Firmware USB** (SKU CHAUVETFIRMWAREUSB): an 8 GB stick with both USB-A and USB-C plugs. It arrives pre-formatted and works with any Chauvet Pro fixture that has a USB-A or USB-C port. It's the easy way past the USB-C problem.
- **Where the files are:** `https://github.com/Chauvet-Pro/<MODELNAME>`, all caps with no spaces. Examples: ROGUEOUTCAST2XWASH, COLORADOPXLBAR16, MAVERICKFORCESSPOT, STRIKEARRAY4.
  - The Color STRIKE M lives at **COLORSTRIKEMV2**; COLORSTRIKEM points to it.
  - Variants have their own repos: ROGUEOUTCAST2XWASHM, ROGUER2XWASHVW, STRIKEARRAY4C. **Never load a variant's file into the base model.**
  - The README version list is the authority. Git tags are sometimes missing or duplicated.
  - Some zips contain a `__MACOSX` folder. Copy only the `.CHL`.
- **Check the installed version:**
  - Rogue (Outcast and R-series): **MENU → Sys Info → Ver**.
  - Maverick and STRIKE: **Fixture Information**. On the Color STRIKE M, "Display Ver" is the main version.
  - COLORado PXL: the firmware has "Sys Info" / "Firmware Version" screens, but the README says "Fixture Information". Check both names.

### Route A: USB stick ("USB Update")
From Chauvet's GitHub READMEs:
1. Unzip the download. Put the `.CHL` file in the **root** of a **FAT32** stick of **32 GB or less**. Several versions can sit on one stick.
2. Power on the fixture. On COLORado PXL, check Setup → **USB Update = YES** first. Plug in the stick.
3. **"USB Update"** appears → **YES**.
4. Pick the version with **UP / DOWN** → **ENTER**.
5. **"USB Update"** appears again → **YES**.
6. **"USB Update Wait"** shows. It can take several minutes. **Don't cut power or pull the stick while the USB LED blinks.** Some PXL units then show "DO NOT UNPLUG, UPDATING".
7. On Rogue Outcast: when the LED stops, the motors power down and the display blanks. **Still don't cut power.** It reboots by itself.
8. Check the version (Sys Info / Fixture Information), then restart the fixture.

- **Batch:** Maverick Force S Spot only: "It is possible to update multiple units with the USB if they are daisy chained via DMX" (README and manual). The Outcast and PXL READMEs don't say this ⚠️. For those, update one at a time, or use route C.

### Route B: STRIKE family ("Upgrade Firmware")
From the STRIKE Array 4 README and the Color STRIKE M manual:
1. Power on and plug in the stick.
2. **"Upgrade Firmware"** appears → **ENTER**. If something else shows: main menu → Update Firmware → **Only This Fixture** / **Multiple Fixture** / **Other Fixture Type**.
3. Select the file. **"Are you sure?"** → **ENTER**. A wrong file just fails and returns to the main screen.
4. Don't power off. It reboots by itself.

- **Multiple Fixture** updates DMX-linked units of the same product line.
- **Other Fixture Type** updates a different Chauvet product from this one. Example: a Maverick Silens 2 Profile updating a Color STRIKE M.
- Set the main unit's protocol to **DMX512**.

### Route C: UPLOAD 08 over DMX
From the UPLOAD 08 Instructions Rev 4:
1. Uninstall any older UPLOAD 08 software.
2. Install Microsoft .NET Framework, the Silicon Labs **CP210x** USB-UART driver, then **UPLOAD 08 Setup v4.5.2 or later**.
3. Plug the UPLOAD 08 into the PC with its USB cable. In Device Manager → Ports (COM & LPT), find "Silicon Labs CP210x USB to UART Bridge (COM#)". Go to Port Settings → Advanced and set it to **COM129**.
4. Run the app. Earlier wiki research noted it asks you to unplug and replug the uploader.
5. Click **Open** and select the `.CL` / `.CHL` file.
6. Unplug the console from the line (general knowledge). Daisy-chain **up to 10 fixtures of the same product** from the UPLOAD 08's 3-pin or 5-pin output. Power them on.
7. Follow the on-screen directions.
8. Products that won't take it → **Force Upload** (below).

- **Batch limit:** 10 per pass per the Rev 4 instructions. The product page says 12. Plan on 10.

### Route D: Web server
From the PXL Bar 16 / MK3 Spot manuals and the web page built into the firmware:
1. Set the fixture to Control Protocol **Art-Net** and IP mode **Static**.
2. Cable it to a computer. Give the computer an IP with the same first 3 numbers.
3. Browse to the fixture's IP. Log in as **admin / admin**.
4. Open the **Upgrade** page → choose the file → **Upload File**.
5. The page shows "Fixture updating, please wait and do not power off the fixture", then "FILE UPLOAD SUCCESS, PLEASE WAIT FOR FIXTURE TO FINISH THE UPGRADE".

### Recovery (failed or interrupted update)
- **Route A fixtures (Outcast, PXL, Force S):** Chauvet says a power cut or stick pull while the LED blinks causes "partial or total firmware failure". Fixing it **needs the UPLOAD 08**.
- **UPLOAD 08 Force Upload** (Instructions Rev 4):
  1. Power the product **off**, but leave it connected to the UPLOAD 08.
  2. Make sure the UPLOAD 08 LED is flashing.
  3. Make sure the right `.CL`/`.CHL` is selected.
  4. Click **Force Upload** and follow the prompts.
- **STRIKE family Force Upload** (no UPLOAD 08 needed):
  1. Run a 5-pin DMX cable from a working "main" fixture to the dead "target", with the target **off**.
  2. Main fixture: protocol DMX512. Stick in → Upgrade Firmware → Multiple Fixture (or Other Fixture Type).
  3. Select the file → "Are you sure?" → ENTER. **Turn the target on within 1–2 s.** Its display stays off while the main shows 0–100 %.
  4. The target shows "< UPDATE >" and then reboots.
  - **One target at a time.**
- If none of that works, contact Chauvet service. The Force S Spot manual says "Please contact Chauvet regarding this device" about the UPLOAD 08.

### Gotchas
- **Disconnect the console** (and any splitter or wireless transmitter feeding the line) before a DMX-based update, so the uploader is the only DMX source (general knowledge).
- **Don't mix models on one update line.** UPLOAD 08: "of the same product". STRIKE "Multiple Fixture" = same product line. Base and variant (M, VW, 4C) files are different.
- **Never power-cycle mid-update.** On Outcast, the display goes blank *before* the reboot. That is normal, so wait.
- **The stick must be FAT32 and ≤32 GB.** Most new sticks are bigger and exFAT. Reformat, or use the Chauvet Firmware USB. Outcast and PXL ports are **USB-C**.
- **Firmware changes DMX modes and can break the console patch.** Examples from release notes:
  - Outcast 2X Wash V1.230504 added 23CH and 55CH.
  - R3X Wash V1.250331 added 27CH.
  - Color STRIKE M V4.0.0 added 68CH, and V4.0.7 added 96CH and changed pixel-priority behavior.
  - STRIKE Array 4 V1.230817 added an amber mode.
  - Outcast 1 BeamWash V1.251216 removed custom white mode and reserved control-channel values 232–239.
  - R2X Wash V1.250715 renamed mislabeled personalities.
  - PXL Bar 8 V1.250911 changed how the Art-Net universe is entered.
  - Update the **whole rig to one version**, then check the patch and profile.
- **Network fixes worth taking before an Art-Net or sACN show:** IGMP fixes (PXL Bar 8/16 V1.240219, Curve 12 V1.240806, Color STRIKE M V4.0.3). sACN universes above 256 (Curve 12 V1.250410+, Color STRIKE M V4.0.6). **MA3 Art-Net + RDM random movement** fixed in PXL Bar 16 V1.251014 and Curve 12 V1.251029.
- Repos with **no release notes**: ROGUER3SPOT, MAVERICKMK3SPOT, MAVERICKMK3WASH. Test one unit before updating a rig.
- The MAVERICKMK3SPOT V2.210608 zip contains a `.rar`, which needs a second extraction.

### Latest versions found (2026-10-03)
| Fixture | Latest found | Route |
|---|---|---|
| Rogue Outcast 2X Wash | V1.260610 | A |
| Rogue Outcast 1 BeamWash | V1.251216 | A |
| Rogue Outcast 3 Spot | V1.241025 | A |
| Rogue R2X Spot | V4.231211 | C |
| Rogue R2X Wash | V1.250715 | C |
| Rogue R3 Spot | V3.230807 | C |
| Rogue R3X Wash | V1.250331 | C |
| COLORado PXL Bar 16 | V1.260709 ("update all units ASAP") | A / D |
| COLORado PXL Bar 8 | V1.250911 | A |
| COLORado PXL Curve 12 | V1.251029 | A / D |
| Maverick Force S Spot | V1.240826 (internal); last public fix V1.211005 | A |
| Maverick MK3 Spot | V2.210608 | C / D |
| Maverick MK3 Wash | V9.211118 | C / D |
| Color STRIKE M | V4.0.7 | B |
| STRIKE Array 4 | V1.3.0 | B |

## Rogue Outcast lineup (as found)
- Outcast 1 Beam, **Outcast 1 BeamWash** (and BeamWash M), Outcast 1L Beam, Outcast 1M Beam.
- Outcast 2 Beam, Outcast 2 Hybrid, **Outcast 2X Wash** (and 2X Wash M).
- **Outcast 3 Spot** (and the Spot-2 SKU), Outcast 3X Wash.
- All IP65 except the 2X Wash M, which a retailer lists as IP66.
- Power and data are **Seetronic Powerkon IP65 and IP65 5-pin XLR**, NOT standard powerCON TRUE1. Bring Powerkon jumpers.
- Wiki pages exist for the bolded models. Which models are most common in rental stock could not be determined from sources.

## Rogue R-series hardware notes (from Chauvet BOMs)
- Power: Neutrik powerCON NAC3MPA (blue in) and NAC3MPB (grey out). Supplied cord: powerCON to Edison, 1.5 m.
- DMX: one shared "4-in-1" DMX board with **3-pin and 5-pin XLR in/out**.
- Omega: 140 mm quick-lock (CD-D01; the R3X Wash has bracket revisions V2, V3 and V4).
- Fuses (5×20 mm, 250 V): **7 A on the R2 Wash/R2X Wash BOM, R2X Spot and R3 Spot. 12 A on the R3X Wash.** Outcast models use an F8A (8 A) in an IP fuse holder.
- Locks: the R2 Spot, R2X Spot, R3 Spot, R3X Wash and Outcast 3 Spot have pan and tilt locks. The R2X Wash, Outcast 2X Wash and Outcast 1 BeamWash BOMs show none.

## Sources
- [UPLOAD 08 Instructions Rev 4](https://www.chauvetprofessional.com/wp-content/uploads/2015/12/UPLOAD_08_Instructions_Rev4.pdf) — software setup, CP210x driver, .NET, up to 10 fixtures, Force Upload
- [UPLOAD 08 product page](https://chauvetprofessional.com/product/upload-08/) — up to 12 fixtures, USB-powered, 3/5-pin
- [Firmware USB product page](https://chauvetprofessional.com/product/firmware-usb/) — USB-A/C 8 GB stick
- [Chauvet GitHub portal announcement](https://chauvetprofessional.com/welcome-to-our-github-portal/), [Updating Maverick software with a USB drive](https://chauvetprofessional.com/updating-maverick-fixture-software-with-a-usb-drive/)
- [github.com/Chauvet-Pro](https://github.com/Chauvet-Pro) repos ROGUEOUTCAST2XWASH, ROGUEOUTCAST1BEAMWASH, ROGUEOUTCAST3SPOT, ROGUER2XWASH, ROGUER2XSPOT, ROGUER2SPOT, ROGUER3SPOT, ROGUER3XWASH — USB procedure, changelogs, BOMs, firmware strings
- [Rogue Outcast 2X Wash UM Rev 4](https://www.chauvetprofessional.com/wp-content/uploads/2022/08/Rogue_Outcast_2X_Wash_UM_Rev4.pdf) — buttons, passcode, setup menu
- [R2X Wash manual (manualslib)](https://www.manualslib.com/manual/1824482/Chauvet-Professional-Rogue-R2x-Wash.html) — hold MENU + 2323
- [R3 Beam UM Rev 5](https://www.chauvetprofessional.com/wp-content/uploads/2021/04/Rogue_R3_Beam_UM_Rev5.pdf), [R2X Beam UM Rev 1](https://www.chauvetprofessional.com/wp-content/uploads/2018/09/Rogue_R2X_Beam_UM_Rev1.pdf), [Outcast 1L Beam UM Rev 3](https://www.chauvetprofessional.com/wp-content/uploads/2022/08/Rogue-Outcast-1L-Beam_UM_Rev3.pdf), [Outcast 2 Beam UM Rev 4](https://saleswl.com/wp-content/uploads/2023/05/Chauvet-Professional-Rogue-Outcast-2-Beam-User-Guide.pdf) — panel lock code, 2323
- [Rogue Outcast family page](https://www.chauvetprofessional.com/rogueoutcast/) — lineup
- [UPLOAD 08 Instructions Rev 4](https://www.chauvetprofessional.com/wp-content/uploads/2015/12/UPLOAD_08_Instructions_Rev4.pdf) — also: COM129 port setting, Force Upload steps (re-checked via search 2026-10-03)
- [Firmware USB on B&H](https://www.bhphotovideo.com/c/product/1809871-REG/chauvet_professional_chauvetfirmwareusb_chauvet_firmware_usb.html) — CHAUVETFIRMWAREUSB, 8 GB, USB-A/C, pre-formatted
- GitHub READMEs checked 2026-10-03: [COLORADOPXLBAR16](https://github.com/Chauvet-Pro/COLORADOPXLBAR16), [COLORADOPXLBAR8](https://github.com/Chauvet-Pro/COLORADOPXLBAR8), [COLORADOPXLCURVE12](https://github.com/Chauvet-Pro/COLORADOPXLCURVE12), [MAVERICKFORCESSPOT](https://github.com/Chauvet-Pro/MAVERICKFORCESSPOT), [MAVERICKMK3SPOT](https://github.com/Chauvet-Pro/MAVERICKMK3SPOT), [MAVERICKMK3WASH](https://github.com/Chauvet-Pro/MAVERICKMK3WASH), [COLORSTRIKEMV2](https://github.com/Chauvet-Pro/COLORSTRIKEMV2), [STRIKEARRAY4](https://github.com/Chauvet-Pro/STRIKEARRAY4) (USB, Multiple Fixture and Force Upload procedures), plus the Rogue repos above — versions, release notes, file names; web-server upgrade page text from the firmware files
- [Color STRIKE M User Manual Rev 12](https://www.chauvetprofessional.com/wp-content/uploads/2021/09/Color_STRIKE_M_UM_Rev12.pdf) — Upgrade Firmware menu, STRIKE folder, Fixture Information (via search summary)
- [COLORado PXL Bar 16 UM Rev 10](https://www.chauvetprofessional.com/wp-content/uploads/2021/11/COLORado_PXL_16_UM_Rev10.pdf), [Maverick MK3 Spot UM Rev 6](https://www.chauvetprofessional.com/wp-content/uploads/2019/02/Maverick_MK3_Spot_UM_Rev6.pdf) — web server Upgrade page, admin/admin (via search summary)
- [Maverick Force S Spot UM Rev 7](https://www.chauvetprofessional.com/wp-content/uploads/2021/03/Maverick-Force-S-Spot_UM_Rev7.pdf) — multi-unit USB update over DMX, UPLOAD 08 recovery (via search summary)
