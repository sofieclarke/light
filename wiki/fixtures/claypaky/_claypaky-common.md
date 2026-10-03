---
title: "Claypaky common conventions"
manufacturer: "Claypaky"
model: "_common"
aliases: ["claypaky menu", "clay paky password", "claypaky advanced menu", "claypaky 1234"]
verification: "web-search"
last_updated: "2026-10-03"
---

# Claypaky: display & menu conventions (whole line)

> **2AM CARD**
> - **Advanced menu code: 1234.** Confirmed in the Sharpy, Sharpy Plus / Plus Aqua and Mythos / Mythos 2 manuals. Likely, but not confirmed, on other models.
> - **Menu Locking** (a 4-digit user-menu password someone may have set): default unlock **1234** (Sharpy and Sharpy Plus Aqua manuals). If a rental house changed it, ask them.
> - **Display works with no mains:** press **F** (enter) to wake it on the buffer battery, then set the address. It sleeps again after about 30 s without confirmation (Sharpy manual).
> - **Address flashing = no DMX signal.** Not a fault.
> - **DMX control channels, common pattern** (seen on Sharpy, Sharpy Plus, Mythos, Xtylos, X Frame, Unico, B-EYE profiles): **Reset 128-255 = complete reset, 77-127 = pan/tilt reset, 26-76 = effects (or zoom) reset. Lamp Control 26-100 = OFF, 101-255 = ON, hold about 5 s.**
> - **Firmware:** fixture-to-fixture via **Advanced (1234) → Upload Firmware**, same model only, 5–6 at a time. Newer fixtures also update via Web Server or CloudIO (`.img` on a USB stick). See [Firmware updates](#firmware-updates).
> - **Lamp won't strike from the desk:** check that the fixture menu option **Lamp DMX** is On (Sharpy family) and that your profile includes the lamp channel.

## Buttons
- Sharpy-era fixtures (manual): keys referred to as **F** (enter/confirm, also wakes the display), **UP (B)**, **DOWN (C)**, **RIGHT (E)** and **LEFT**. LEFT escapes and keeps the current setting.
- Typical flow: press F → DMX address shows → UP/DOWN/RIGHT to set → F to confirm (Sharpy manual).

## Menu structure (as found in manuals)
- **DMX Address**: the first thing shown when you press F.
- **Setup / Options**: personality (Standard/Vector), lamp options such as **Lamp DMX** (default On on Sharpy), **Shutter on error** (closes the stopper/strobe on a pan/tilt position error), and display settings. Exact submenu names vary by model.
- **Information** (Sharpy manual list): System Errors, Fixture Hours (total + partial), Lamp Hours (total + partial), Lamp Strikes, System Version, Board Diagnostic, DMX Monitor, Fans Monitor, Sensor Status, Network Parameters.
- **Manual Control**: drive individual effects without a console.
- **Test**: Pan-Tilt, Colour, Beam, Gobo tests.
- **Advanced** (code 1234): Access code, Upload Firmware, Setup Model, Calibration, Factory Default, Menu Locking (Sharpy manual).
- Xtylos-generation fixtures also have operating modes **Standard / Smart / Service**. Smart Mode needs a password supplied **by Claypaky** (Xtylos user menu).

## Errors & messages across the line
| Message | Meaning | Fix | Source |
|---|---|---|---|
| Address field flashing | No DMX input | Check data chain / console output | Sharpy manual |
| System Errors (Information menu) | Log of warnings since power-on | Read it, fix, then clear. Mythos asks "Are you sure you want to clear error list?" → YES | Sharpy, Mythos manuals |
| Shutter closes by itself after a knock | Shutter on error + automatic pan/tilt repositioning | Normal. Let it re-home or send a pan/tilt reset | Sharpy, Mythos manuals |
| Specific numbered error codes | **Not found.** Claypaky manuals list errors as text messages in the System Errors list. Record the exact strings you see here | — | — |

Generic troubleshooting table, the same in every Claypaky manual found (Sharpy, Sharpy Plus, Sharpy Wash 330):
- Won't switch on → no mains → check supply voltage.
- Electronics fine, no light → lamp exhausted or defective → replace lamp.
- Erratic / no response → bad data cable → replace.
- Low output → wrong address, dirty or broken optics → check address / clean / call a technician.
- Fast lamp ON-OFF cycles reduce lamp life.

## Firmware updates
Checked 2026-10-03. Claypaky keeps firmware files, release notes and technical notes on its **restricted Customer Care site (service.claypaky.it)**, so no version numbers were found for any fixture in this wiki. Ask your distributor or the rental house service department for the file, and record the version on the fixture page.

### The four ways Claypaky fixtures get updated
| Method | Hardware | Software | File | Which fixtures (as listed by Claypaky) |
|---|---|---|---|---|
| **Fixture-to-fixture** (Advanced → Upload Firmware) | DMX cable from a fixture already on the wanted firmware | none | — | Sharpy, Mythos 2, B-EYE K20, Scenius Unico, Xtylos (product pages: "firmware upload from another fixture"). Sharpy Plus has Upload Firmware in its Advanced menu (manual) |
| **PC over DMX** | Claypaky **Firmware Uploader USB/DMX interface** (retail: "Firmware Uploader Kit USB/DMX"; B&H lists part **C61206** for the Alpha 1500) | Claypaky PC uploader, shown as **"FUL Uploader"** in a Claypaky Tech Corner video (title only) ⚠️ | Not found | Older DMX-only fixtures ⚠️ unverified which models |
| **Web Server** (Ethernet) | Laptop on the fixture's RJ45 | Web browser (fixture's built-in web server) | Not found | Sharpy Plus, Sharpy X Frame, Xtylos (product pages: "firmware upgrade via Web Server") |
| **CloudIO / CloudIO Box (CA8001)** | CloudIO unit (7" touchscreen, two DMX in/out pass-through ports, up to 31 lights on its DMX line) + USB stick | CloudIO's **Fixture Firmware Uploader** app | **`.img`** in the **root** of the USB stick | "Any Claypaky fixture" per the CloudIO manual; ⚠️ check CloudIO's compatibility list for older models |

- "**Firmware upgrade with no power**" is listed for the Sharpy, Mythos 2 and B-EYE K20 (product pages / product guide). These fixtures have a self-charging buffer battery for the display, which probably powers the board for this ⚠️ unverified. The exact procedure wasn't found.
- **Upbox / Upbox 2 / Upbox Pro are Prolights (Music & Lights) uploaders, not Claypaky.** Retail listings describe them as USB in, 5-pin XLR DMX out. Don't assume they work on Claypaky fixtures.
- **Art-Net / sACN firmware update:** Not found for any Claypaky fixture in this wiki.
- **USB port on the fixture itself:** Not found for these models. The USB-stick route found is via CloudIO.

### Fixture-to-fixture step by step (Advanced menu)
1. **Disconnect the console** from the DMX line ⚠️ (general practice). Only fixtures of the **same model** on the line.
2. DMX from the fixture with the wanted firmware into the first target, daisy-chain the rest. **5–6 targets at a time max** (Claypaky manuals, via search summary).
3. On the source: wake the display (F on Sharpy-era fixtures), menu → **Advanced** → access code **1234** (UP / DOWN / RIGHT, then F) → **Upload Firmware** → confirm.
4. Don't power-cycle or pull cables until it's finished ⚠️ (general practice). Check **Information → System Version** (Sharpy menu name) on every target afterwards.

### CloudIO step by step (CloudIO manual)
1. Copy the `.img` firmware file to the **root folder** of a USB key. Stick format (FAT32 etc.): Not found.
2. CloudIO DMX OUT → the fixtures to update. Insert the USB key and open the **Fixture Firmware Uploader** app.
3. Select the firmware and press **CONTINUE**. Claypaky fixtures on DMX OUT update "if compatible with the firmware version selected" (manual, via search summary). What happens to the others isn't stated, so keep the line to one model ⚠️.
4. CloudIO Box also works **offline** with firmware pre-loaded on a USB stick (Claypaky).

### Batch limits
- Fixture-to-fixture: same model only, 5–6 units per run (manual).
- CloudIO: up to 31 lights on its DMX line (Claypaky CloudIO page).
- PC uploader / Web Server: Not found.

### Recovery / bootloader
- **Not found.** No bootloader, safe-mode or recovery procedure was found in anything public. If a fixture is left half-updated: retry fixture-to-fixture from a known-good unit of the same model, then call Claypaky service (they have the Customer Care documents).

### Gotchas
- **Disconnect the console** and anything else that transmits DMX before updating ⚠️ (general practice).
- **Don't mix models on the update line.** Claypaky manuals limit fixture-to-fixture to the same model. Watch sibling pairs that look alike: Mythos vs Mythos 2, B-EYE K10 vs K20, Sharpy X Frame vs Sharpy X Spot, Xtylos vs Mini Xtylos, Scenius Unico vs Scenius Spot/Profile.
- **Don't power-cycle mid-update** ⚠️ (general practice).
- **A firmware update can add or renumber DMX modes and break your console patch.** Check the fixture's mode list against your profile after updating a rig, and update the whole rig to one version so every unit behaves the same.
- Videos (titles only, not watched): Claypaky Tech Corner "Firmware Update with FUL Uploader", "Firmware Update with Web Server", "Firmware Update from Fixture to Fixture"; third-party "Updating Firmware on Clay Paky Sharpy", "Updating Firmware via Network on Clay Paky Fixtures". Watch them before the gig if you can: they show the real screens.

## Lamp handling (discharge models)
- Don't touch the lamp envelope bare-handed. If you do, clean it with alcohol and dry it with a clean cloth (Sharpy Plus manual).

## Pan/tilt transport locks
- Sharpy Plus and Mythos 2: pan lock positions every 90°, tilt every 45° (manuals).

## US laser rules (Xtylos family)
- Xtylos and Mini Xtylos HPE need an FDA CDRH variance in the US. The Mini Xtylos CJ3003 adjusted-output version doesn't. Claypaky runs a Laser Variance Program (claypaky.it).

## Sources
- [Sharpy C61375 manual (4wall mirror)](https://cdn01.4wall.com/cms/rentals/files/f60ef02cea55e4.pdf), [Christie Lites mirror](https://www.christielites.com/file_uploads/manual_643_Sharpy_Manual.pdf), [ManualsLib p.20](https://www.manualslib.com/manual/963250/Clay-Paky-Sharpy.html?page=20) — code 1234, Advanced contents, buttons, battery display, Information/Test menus
- [Sharpy Plus Aqua User Menu 03.2023](https://ltb.no/media/multicase/documents/claypaky/brukermeny_claypaky_sharpyplusaqua_03.2023.pdf), [Sharpy Plus manual 11.2020](https://www.visiontwo.de/fileadmin/user_upload/Claypaky_Sharpy_Plus_Manual_11.2020.pdf) — 1234, Menu Locking default, lamp handling, locks
- [Mythos C61391 manual](https://www.huss-licht-ton.de/images/products_download/User_Manual_17456_1.pdf), [Mythos 2 manual (prolight.com.pl)](https://prolight.com.pl/images/content/Image/instrukcje/claypaky_mythos_2_instrukcja_eng.pdf) — 1234, clearing the error list
- [Xtylos User Menu 01/2021 (Christie Lites)](https://www.christielites.com/file_uploads/Xtylos_UserMenu_01_2021.pdf) — Standard/Smart/Service modes
- [Sharpy Wash 330 manual (hirewl)](https://hirewl.com/wp-content/uploads/2019/08/HR_SharpyWash330_and_PC_Manual_11.2014_EN.pdf) — same troubleshooting table
- QLC+ Claypaky fixture definitions (github.com/mcallegari/qlcplus, commit 1ccdab8) — reset/lamp DMX value pattern (community)
- Claypaky Sharpy manual ([manuals.plus copy](https://manuals.plus/m/0dc75ba9bd5c288c40aa1eb565a0d3d88973ac670f2f407b78f1e04c1552d923)), [A.leda B-EYE K10/K20 user guide (cpl.tech)](https://www.cpl.tech/wp-content/uploads/2018/10/Clay-Paky-A-leda-B-EYE-K10-User-Guide.pdf), [Sharpy Plus manual (ManualsLib)](https://www.manualslib.com/manual/1637972/Claypaky-Sharpy-Plus.html) — Upload Firmware is fixture-to-fixture, same model only, 5/6 units max (via search summary)
- [CloudIO Instruction Manual 01.2020 (visiontwo.de)](https://www.visiontwo.de/fileadmin/user_upload/Claypaky_CloudIO_Manual_01.2020.pdf), [06.2022 (ltb.no)](https://ltb.no/media/multicase/documents/claypaky/manual_claypaky_cloudio_06.2022.pdf), [CloudIO product page](https://www.claypaky.it/products/cloudio/), [GoKnight CA8001 CloudIO Box](https://goknight.com/claypaky-ca8001-cloudio-box-iot-device/) — Fixture Firmware Uploader, `.img` on USB root, CONTINUE, 31 lights, offline use (via search summary)
- [B&H: Claypaky C61206 Firmware Uploader USB/DMX interface](https://www.bhphotovideo.com/c/product/1827391-REG/claypaky_c61206_firmware_uploader_usb_dmx_interfacefor.html), [Lightspares: Claypaky Firmware Uploader Kit USB/DMX](https://lightspares.com/claypaky-firmware-uploader-kit-usbdmx-010-074) — the PC interface exists (retail)
- Product pages (via search summary): [Sharpy](https://www.claypaky.it/products/sharpy-legacy/), [Sharpy Plus](https://www.claypaky.it/products/sharpy-plus/), [Sharpy X Frame](https://www.claypaky.it/products/sharpy-xframe/), [Xtylos](https://www.claypaky.it/products/xtylos/), [B-EYE K20](https://www.claypaky.it/en/products/b-eye-k20), [Scenius Unico datasheet (proscene.ch)](https://www.proscene.ch/data/web/proscene.ch/uploads/database/L10010/scenius_unico_.pdf), [Product Guide 2019 (sgssistemas.lv)](https://www.sgssistemas.lv/uploads/resources/166/lv/claypaky-productguide2019-en.pdf) — which update methods each model lists; Customer Care site
- [Prolights UpBox Pro](https://www.prolights.it/en/product/UPBOXPRO), [Maccam: PIUPBOX2](https://www.maccam.tv/product/a-c-lighting-piupbox2-firmware-uploader-kit-usb-in-5-pin-xlr-dmx-out/) — Upbox is a Prolights product
- Videos (titles only): [Tech Corner: FUL Uploader](https://www.youtube.com/watch?v=hyeRWUqLlTk), [Tech Corner: Web Server](https://www.youtube.com/watch?v=Jp4SJ3HJ9N4), [Tech Corner: Fixture to Fixture](https://www.youtube.com/watch?v=xGVPVCwnRPg), [Updating Firmware on Clay Paky Sharpy](https://www.youtube.com/watch?v=ODyM8kxGaLU), [Updating Firmware via Network on Clay Paky Fixtures](https://www.youtube.com/watch?v=v6mLxOmnia4)
