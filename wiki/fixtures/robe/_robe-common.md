---
title: "Robe Common Menu & Service Conventions"
manufacturer: "Robe"
scope: "Shared across the Robe Robin line (touchscreen-era fixtures: Pointe, MegaPointe, Spiider, BMFL, Esprite, Forte, LEDBeam 150, iFORTE and others)"
verification: "web-search"
last_updated: 2026-10-03
---

# Robe common menu & service conventions

> **2AM CARD** — applies to most current Robe Robin fixtures; check the model page for exceptions
> - **Service menu password:** **7623** — fixed, "cannot be changed" (quoted in Robin Forte, T2 Profile, MegaPointe, Pointe manual search summaries)
> - **REAP (web portal) default login:** user **robe** / password **2479** (Service → "Reset Web Password" restores it)
> - **Buttons locked?** Go to the ROBE logo screen, touch [ESCAPE] and slide your finger clockwise 360°: [ESCAPE] → [NEXT] → [ENTER/Display On] → [PREV] → [ESCAPE]. Same gesture locks and unlocks ("Buttons are locked" appears when locked).
> - **Screen went dark/locked by itself?** "Touchscreen Lock" auto-locks after the last touch — press [ENTER/Display On] to unlock.
> - **Address with no power:** press [ENTER/Display On] — the touchscreen runs off its backup battery. Green battery icon = charged, red = flat.
> - **See the error:** touch the warning icon or press [ESCAPE]. History: Service → Fixture Errors.
> - **Firmware:** DSU package from robe.cz + Robe Universal Interface (DMX) or ROBE Uploader (Ethernet/RDM, several units at once). Version: Information → Software Versions. Update mode: Service → Update Software (older: Special → SW Upd → On). Console off the line, do not interrupt. Stuck in update mode? ROBE Uploader → DSU Mode / Fix broken device with RUNIT.

## Control panel & menu navigation
- Buttons (Robin manuals: Forte, Esprite, 600E Spot, Pointe, MegaPointe, Spiider TW, others):
  - **[ESCAPE]** — leave the menu without saving.
  - **[NEXT] / [PREV]** — move between menu items and adjust values.
  - **[ENTER/Display On]** — enter the selected menu / confirm a value; it also wakes the display when the fixture is unplugged.
- Touchscreen: Robe calls it a "QVGA Robe touch screen with battery backup". On-screen icons: back arrow (previous screen), up/down arrows (page up/down), confirm (save, leave, or run the action).
- Touch the screen or press [ENTER/Display On] and the **Address** screen with the current DMX start address comes up first. The DMX Address menu sets the start address.
- Main tabs seen in Robin manuals: Address, Information, Personality, Manual Control, Stand-Alone, Service (from the manual page titles for Pointe: "Tab Manual Control", "Tab Stand-Alone", "Tab Service").
- Personality menu: the manuals tell you to set Date & Time there before the fixture's first use.

## Battery / unpowered addressing
- With the fixture unplugged, [ENTER/Display On] turns the touchscreen on from its backup battery, so you can set the address and other settings on the truck or the deck.
- Battery icon (top right): green = charged, red = exhausted. Mains power recharges it.
- **"Robe Navigator"**: no source found under that name. Robe manuals describe the battery-backed display shown above. Not found — fill in if a fixture or doc uses that name.

## Passwords, locks & hidden menus
| What | Default | Notes |
|---|---|---|
| Service menu password | **7623** | "set to 7623 and cannot be changed". Search summaries quote it for Robin Forte, T2 Profile, MegaPointe and Pointe. The Forte summary attaches the same wording to "Password Protection". |
| REAP (Robe Ethernet Access Portal) | user `robe` / pass `2479` | From the REAP manual and the MegaPointe manual. Service → Reset Web Password restores the default. |
| Robin Forte LightMaster (followspot controller) | 5242 | Applies only to the LightMaster, not to the fixture. |
| Button lock | gesture | ROBE logo screen → circular slide [ESCAPE]→[NEXT]→[ENTER]→[PREV]→[ESCAPE] |
| Touchscreen Lock | auto | Locks after the last touch. Unlock with [ENTER/Display On]. |

- Service menu contents (Robin manuals): **Fixture Errors** (log of errors seen during operation), **Adjust DMX Values** (move effects into place before fine calibration), **Calibrations** (fine-calibrate effects and reload the default calibration values), software update items.
- Entering the password: the touchscreen shows a numeric keypad (⚠️ unverified, general knowledge).

## Error message conventions
Robe numbers a sensor error "1" or "2" for the two failed sensor states and puts a short word on the display. In current manuals, touch the warning icon or press [ESCAPE] to read the messages.

| Message | Meaning (from Robe manuals) | First things to try |
|---|---|---|
| Pan Error 1 / Pan Error 2 | Yoke not in its default position after reset. MegaPointe manual: magnetic-indexing circuit fault (sensor failed or magnet missing) or a defective stepping motor. MegaPointe defines Error 1 = sensor not in state "connected", Error 2 = sensor not in state "unconnected". | Remove the pan transport lock. Check for obstructions. Reset. If it repeats, call service. |
| Pan Error 3 (MegaPointe) | Pan feedback error | Reset. Note how often it happens. Service. |
| Tilt Error (1/2) | Head magnetic-indexing circuit fault (sensor failed or magnet missing), or a defective stepping motor or its driver IC on the PCB | Remove the tilt lock, check that the head moves freely, reset |
| Zoom Error 1/2, Gobo Carousel Error, Gobo Rotation Error, etc. | Effect not in its default position after the module resets | Reset. Check the module seating and that the gobos are in correctly. |
| Lamp Error (discharge models) | Ignition failed repeatedly (3 tries in the MegaPointe manual, 4 in older manuals): lamp damaged or missing, or igniter/ballast/lamp driver failure | Let it cool, re-strike, check the lamp |
| FtEr (older Robe) | Fixture overheated (ambient 40 °C or more) and the relay switched the lamp off | Cool down. Clean the fans and filters. |
| Temper. Sensor Error (older Robe) | Head temperature sensor lost contact with the main processor, so the lamp was switched off | Service |
| Fan message (older Robe) | Fixture overheated and switched off, with fan mode "LOOF" selected | Change the fan mode, clean the fans and filters |
| Air filter icon (newer LED Robin, e.g. Spiider) | The air-filter cleaning interval has run out | Clean the filters, then reset the counter |

The older-model rows come from Wash 575XT, Scan 1200 XT, Robin 300E Wash and 250 XT manuals on manualslib. Wording on current fixtures may differ. ⚠️ Check the model page.

## Firmware updates
Robe calls firmware "software". Files come as a **DSU package** (.zip) per fixture model from robe.cz. Inside is an uploader program, e.g. `DSU_RobinSpikie_xxxxxxxx.exe` (Spikie manual). No USB-stick update method was found for Robe fixtures.

### Tools
| What | Details |
|---|---|
| **Robe Universal Interface** ("RUNIT", RUI) | USB-to-DMX/RDM box. Replaces the old "RS232 to DMX Flashing Cable" (RUI manual). Used for DMX updates and for recovery of broken units. |
| **RUNIT WTX** | Wireless version: adds CRMX wireless DMX/RDM. 2 DMX ports, 1 USB 2.0 port, locking 5-pin XLR, wired fixture software updates (robe.cz RUNIT WTX page). |
| Part numbers | Not confirmed. Retailer listings show model numbers 1008 0160 and 1008 0245 for Universal Interface variants — which is which not confirmed ⚠️ unverified. |
| **ROBE Uploader** | Robe's desktop app for automated updates (TB54). Uses the fixture's Ethernet port and/or RDM. Updates several units in parallel over Ethernet with no RUNIT needed. Switches fixtures to update mode by itself. Some fixtures (e.g. Robin ProMotion) update only this way. |
| **DSU uploader** | The per-model program inside the DSU package, used with the RUI over DMX. |
| **Robe Toolkit** | Separate Robe PC utility (manual: software 1.2.0, manual v2.1). Firmware role not confirmed. |
| PC | Robe lists Windows (XP–W10, 32/64-bit tested); Linux and macOS PCs are also listed as supported. |
| Cable | DMX cable from RUI DMX out to the fixture DMX in. Robe touchscreen fixtures generally have 5-pin XLR; some (e.g. Spiider) also have 3-pin — use a 3→5 adapter if needed (general knowledge, ⚠️ unverified). |

### Check the installed version
- Touchscreen Robins: **Information → Software Versions**. Each processor module is listed: Display System (display board in the base), Module M (pan/tilt), plus model-specific modules such as Module G (MegaPointe gobo/effects) or Module DR (Spiider LED driver). Source: Spiider and MegaPointe manuals.

### Method A — Robe Universal Interface over DMX (one line)
1. Download the DSU package for the exact model from robe.cz and unzip it. Close other programs.
2. **Disconnect the console** from the line.
3. RUI to the PC by USB; DMX cable from RUI DMX out to the fixture's DMX in.
4. Put the fixture in update mode: touchscreen Robins **Service → Update Software** (Spiider manual); older displays **Special Functions → Updating Software** (RUI manual), shown as **Special → SW Upd → On** on e.g. the Spikie.
5. Run the uploader, select **Robe Universal Interface** in the port list, Connect, start the update.
6. Don't interrupt it. Check Information → Software Versions afterwards.

### Method B — ROBE Uploader (Ethernet / RDM, many units)
1. Ethernet: set the PC to **2.x.x.x**, e.g. 2.0.0.1, netmask **255.0.0.0** (TB54, ProMotion manual).
2. Discover devices: **RDM automatic or manual discovery**, or build the setup on screen by hand.
3. Select the devices and start the update. The Uploader switches them to update mode.
4. Fixtures without Ethernet are reached over RDM through a RUNIT (TB54: "Ethernet-based update with no RUNIT required" implies the RDM route needs one).

### Batch limits
- ROBE Uploader: several units in parallel over Ethernet. Maximum number: Not found.
- RUI over DMX: how many fixtures per line: Not found. Keep one model per line (general practice, ⚠️ unverified).

### Recovery (failed / interrupted update) — TB54
- A unit left in update mode **cannot be re-discovered automatically**. Update it by hand with **DSU Mode / "Fix broken device with RUNIT"** in ROBE Uploader: a one-to-one update through the RUNIT.
- If a fixture restarts mid-update (e.g. power cut), fixtures with **Display System 3.0** wait in the **bootloader** for a software update on an IP address in the **10.x.x.x** range.

### Gotchas
- Disconnect the console before updating (RUI/Spikie manuals).
- Don't power-cycle or pull cables mid-update.
- Don't mix models on one update line (⚠️ unverified, general practice); each DSU package is model-specific.
- Software updates can add or change DMX modes — check the release notes and your console patch/profile afterwards.
- Update all units of a model on a rig to the same version so they behave the same (⚠️ unverified, general practice).

## Sources
- [Robin Forte manual v3.8](https://www.robe.cz/res/downloads/user_manuals/User_manual_Robin_Forte.pdf) — 7623 password wording, button names, Address screen
- [Robin T2 Profile manual](https://www.robe.cz/res/downloads/user_manuals/User_manual_Robin_T2_Profile.pdf) — 7623 service password, screen lock
- [Robin MegaPointe manual](https://www.robe.cz/res/downloads/user_manuals/User_manual_Robin_MegaPointe.pdf) — Pan Error 1/2/3 definitions, 7623, REAP 2479, battery icon
- [Robin Pointe manual v2.5](https://www.robe.cz/res/downloads/user_manuals/User_manual_Robin_Pointe.pdf) and [manualslib Pointe Service tab](https://www.manualslib.com/manual/829894/Robe-Robin-Pointe.html?page=28) — Service menu, Fixture Errors, Calibrations
- [REAP manual v1.2](https://www.robe.cz/res/downloads/user_manuals/User_manual_REAP.pdf) — REAP default robe/2479
- [Robin Forte LightMaster manual](https://www.robe.cz/res/downloads/user_manuals/User_manual_Robin_Forte_LightMaster.pdf) — LightMaster password 5242
- [Robin iBeam 350 RGBA manual](https://www.robe.cz/res/downloads/user_manuals/User_manual_Robin_iBeam_350_RGBA.pdf), [DLX Spot](https://www.robe.cz/res/downloads/user_manuals/User_manual_Robin_DLX_Spot.pdf), [Linee](https://www.robe.cz/res/downloads/user_manuals/User_manual_Robin_Linee.pdf) — button-lock gesture, Touchscreen Lock
- [Robin Esprite manual](https://www.robe.cz/res/downloads/user_manuals/User_manual_Robin_Esprite.pdf), [600E Spot](https://www.robe.cz/res/downloads/user_manuals/User_manual_Robin_600E_Spot.pdf) — [ESCAPE]/[NEXT]/[PREV]/[ENTER/Display On], QVGA touchscreen with battery backup
- [Robin Spiider manual v3.3](https://www.robe.cz/res/downloads/user_manuals/User_manual_Robin_Spiider.pdf) — warning icon / [ESCAPE] shows errors, air filter icon, Fixture Errors
- Older error list: [Wash 575XT p27](https://www.manualslib.com/manual/1151132/Robe-Wash-575xt.html?page=27), [Scan 1200 XT p27](https://www.manualslib.com/manual/1141551/Robe-Scan-1200-Xt.html?page=27), [Robin 300E Wash p26](https://www.manualslib.com/manual/1140890/Robe-Robin-300e-Wash.html?page=26) — Tilt Error, Lamp Error, FtEr, Temper. Sensor Error, Fan
- [Robin Spikie manual v1.9](https://www.robe.cz/res/downloads/user_manuals/User_manual_Robin_Spikie.pdf) and [Robe Universal Interface manual v1.7](https://www.robe.cz/res/downloads/user_manuals/User_manual_Robe_Universal_Interface.pdf) — RUI update steps, Special → SW Upd
- [TB54 ROBE Uploader manual v1.0.9](https://www.robelighting.de/res/downloads/tech_bulletins/TB54_ROBE_Uploader_manual_EN.pdf), [Robe Uploader page](https://www.robe.cz/robe-uploader) — Ethernet/RDM parallel update
- [Robin ProMotion ADM manual p32](https://www.manualslib.com/manual/2067829/Robe-Robin-Promotion-Adm.html?page=32) — Ethernet-only update, 2.x.x.x LAN address
- [Robe Toolkit manual](https://www.robe.cz/res/downloads/user_manuals/User_manual_Robe_Toolkit.pdf)
- [RUNIT WTX page](https://www.robe.cz/runit-wtx) and [RUI WTX manual v1.1](https://www.robe.cz/res/downloads/user_manuals/User_manual_Robe_Universal_Interface_WTX.pdf) — wireless RUI, ports
- [Robin Spiider manual v3.3](https://www.robelighting.com/res/downloads/user_manuals/User_manual_Robin_Spiider.pdf) — Information → Software Versions modules, Service → Update software
- [Robe news: Software improvements for Robin MegaPointe](https://www.robe.cz/news/software-improvements-for-robin-megapointe-documentation-updates) — update mode via Service tab
