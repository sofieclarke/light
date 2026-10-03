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
> - **Firmware:** newer Outcast models take a **USB stick** (FAT32, 32 GB max, .chl file in the root folder). Older Rogue R-series and Maverick fixtures use the **UPLOAD 08** (USB-to-DMX box + Windows app). Firmware lives at **github.com/Chauvet-Pro/<MODELNAME>**.
> - **Don't pull power** during a USB update while the USB LED blinks. A failed update needs an UPLOAD 08 to recover.

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

## Firmware updating
The name the coordinator gave, "Chauvet Pro Upload / CHAUVET Pro Firmware Uploader", was **not found** as a product name. What exists:

1. **UPLOAD 08** (SKU UPLOAD08). This is the "USB-DMX adapter" route.
   - A USB-powered hardware box plus the PC app *Upload08.exe*, for updating Maverick and most Rogue fixtures **through the DMX port**.
   - It has 3-pin and 5-pin XLR.
   - Windows XP or later, with UPLOAD 08 Setup v4.5.2 or later.
   - Install Microsoft .NET Framework and the Silicon Labs **CP210x** USB-UART driver. Uninstall any older version first.
   - Steps:
     1. Plug in the UPLOAD 08 and run Upload08.exe. It asks you to unplug and replug the uploader.
     2. Click **Open** and choose the **.CL or .CHL** file.
     3. Daisy-chain fixtures of the **same model** and power them on.
     4. Follow the on-screen steps.
     5. If products don't take the update, use **Force Upload** mode.
   - Fixture count per pass: the Rev 4 instructions say "up to 10 of the same product". The product page says "up to 12 DMX-linked fixtures". Use 10 to be safe.
   - This is also **the recovery tool** if a USB update is interrupted.
2. **USB flash drive**, on fixtures with a USB port. That includes the Outcast 2X Wash, Outcast 1 BeamWash and Outcast 3 Spot (USB-C in their BOMs) and the Maverick line.
   - Use FAT32, **32 GB max**, with the .chl file in the **root folder**.
   - Steps:
     1. Power on and insert the drive. "USB Update" appears → **YES**.
     2. Pick the version with UP/DOWN → **ENTER**.
     3. "USB Update" appears again → **YES**.
     4. "USB Update Wait" shows. Several minutes. **Don't cut power while the USB LED blinks.**
     5. The motors power down, the screen blanks, and the fixture reboots itself.
     6. Check **Sys Info**, then restart.
   - Source: Chauvet GitHub READMEs.
3. **CHAUVET Firmware USB** (SKU CHAUVETFIRMWAREUSB). An 8 GB stick with both USB-A and USB-C plugs, pre-formatted, for any Chauvet Pro fixture with a USB-A or USB-C port. No laptop needed.
4. **Where the files are:** `https://github.com/Chauvet-Pro/<FULLMODELNAME-NO-SPACES>`, e.g. ROGUEOUTCAST2XWASH, ROGUER2XWASH, ROGUER3XWASH. Each repo has a README with the changelog, firmware zips (.CHL or .CL) and usually a **BOM PDF** with part numbers. BOM parts link to chauvetvip.com. Older R-series repos have no USB instructions; those fixtures have no USB port in their BOMs, so use UPLOAD 08 ⚠️.

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
