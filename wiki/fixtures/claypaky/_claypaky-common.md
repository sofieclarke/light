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

## Firmware upload
- Started from **Advanced → Upload Firmware** on the fixture (Sharpy manual).
- Tooling: Claypaky's "Uploader" software with a DMX/USB interface for older products, and USB on newer ones, is general knowledge ⚠️ unverified. The tool name, interface and connector weren't confirmed from a source. Claypaky documentation sits on its restricted Customer Care site.

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
