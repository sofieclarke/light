---
title: "Martin Common Conventions"
manufacturer: "Martin"
model: null
aliases: ["martin menu", "martin error", "martin firmware", "martin companion", "martin uploader", "martin service menu", "mac error message", "fback err", "fan error martin", "martin display"]
type: "reference"
verification: "web-search"
last_updated: "2026-10-03"
---

# Martin Common Conventions

> **2AM CARD**
> - **Error on the display?** Errors **flash, 1 s on and 1 s off**. If there are several, each flashes **three times** before the next one shows, and the cycle repeats. Errors show even on a blanked display, and the LED indicator **flashes or stays red** (HARMAN help center).
> - **PAN FBACK ERR / TILT FBACK ERR**, or the short forms **FBEP / FBET**, mean pan/tilt feedback (sensor) trouble. The fixture fails reset or keeps moving until it times out. Check the sensor and belt (MAC Aura XB service manual).
> - **Fan error / TMP CUT OFF / TMP SEN ERR** mean the LEDs won't turn on. Check fans and airflow first (MAC Aura XB service manual).
> - **Firmware:** most current MACs take a **.BANK file on a USB stick** (root folder, SERVICE → USB). Or **Martin Companion** + **Companion Cable P/N 91616091** over DMX (or RDM over Art-Net). Older: **Martin Uploader** + **USB Duo**. Console off, never power off mid-update. Bricked Quantum/Encore? Hold the **bootloader switch** (inside the base) while powering on.
> - **Fixture went dark from the desk?** Most MAC control channels have **display ON/OFF**, **reset**, and on discharge fixtures **lamp ON/OFF** values. See each fixture page.

## Control panel & menu navigation
- MAC fixtures use an **onboard control panel with a backlit graphic display** to set the DMX address, change fixture settings, read data, and run service utilities (MAC Aura / Aura XB manual).
- The DMX address shows on the display after power-up and reset. **Default address is 1.** The address range is limited so the fixture's footprint always fits in 512 (MAC Aura manual).
- Typical top-level menus (MAC Aura XB): **DMX ADDRESS, CONTROL MODE** (DMX mode), **COLOR MODE, PERSONALITY, FACTORY SETTING, SERVICE**. SERVICE holds **CALIBRATION** (for example PAN OFFSET).
- Exact button names, and whether there are 4 buttons or an encoder: Not found — fill in from the fixture. ⚠️ unverified

## Battery-powered display (newer fixtures)
- Not confirmed by any source this session. Some newer Martin fixtures are said to let you address them with no mains power, via a battery-backed display. ⚠️ unverified. Check on the fixture and note which models do it.

## Service / hidden menus & display lock
- SERVICE → CALIBRATION is in the normal user menu on the Aura XB (manual). No source found a **hidden menu or passcode** for any Martin MAC covered here.
- Display lock / unlock: Not found. On many MACs the display can be turned **on and off from DMX** through the control channel:
  - Viper Performance: **155–159 ON, 160–164 OFF**.
  - Encore Performance and Atomic 3000 LED: **52 ON, 53 OFF**.
  (All from Open Fixture Library / QLC+ transcriptions of the manuals.)

## Common control-channel patterns (community transcriptions of the manuals)
| Function | Viper family | Encore Performance | Original MAC Aura | Atomic 3000 LED |
|---|---|---|---|---|
| Reset entire fixture | 10–14 (hold 5 s) | 10–14 (5 s) | 10–14 | 10–14 (5 s) |
| Lamp ON / OFF | 40–44 / 45–49 (5 s) | n/a (LED) | n/a | n/a |
| Display ON / OFF | 155–159 / 160–164 | 52 / 53 | — | 52 / 53 |
| Fan modes | — | 54–58 (54 regulated … 58 ultra-low) | 60–64 FULL, 70–74 REGULATED | 54–58 |
| Hibernation ON / OFF | — | 61 / 62 (5 s) | — | — |
| Factory calibration reset | 245–249 (5 s) | 199 (5 s) | — | — |

Always confirm with the specific fixture's page. These ranges differ between models.

## Firmware updates
Download firmware from **martin.com/en-US/firmware**, or let **Martin Companion** download it from the cloud automatically (Martin firmware page; HARMAN help "Where to find Martin firmware updates").

### Tools
| What | Details |
|---|---|
| **Martin Companion (Companion Desktop)** | Free Windows app: fixture setup, addressing, RDM toolkit, firmware upload. Latest found: **Companion Desktop – Windows v2.1.4** (martin.com, checked 2026-10-03). Talks to fixtures through the Companion Cable, or **RDM over Art-Net** from the PC's normal network port. Can export firmware for USB-stick or P3 System Controller updates. |
| **Martin Companion Cable, P/N 91616091** | USB-to-DMX/RDM cable for Companion. Retailers list it for MAC, ERA, ELP, RUSH and Exterior series. XLR pin count (3 vs 5) not confirmed — carry a 5→3 adapter (⚠️ unverified). Update Companion before first use (cable user guide). |
| **Martin Uploader** (legacy) | Older Windows app (also inside the Martin DMX Tools suite) used with **Martin Universal USB Duo**, **DABS1** or **M-DMX** USB-DMX interfaces. Used by MAC Viper, MAC Quantum, MAC Encore (older docs), original MAC Aura, MAC 250/500/700 era. |
| **USB stick** | MAC Viper, Quantum, Encore and Aura PXL take a **.BANK** file in the **root directory** of a stick (user guides). MAC Ultra, ERA 400 and Atomic 3000 LED also update from USB (file type not captured). Stick format not stated — FAT32 is the safe guess (⚠️ unverified). |
| **P3 System Controller** | Updates P3-capable fixtures (MAC Aura PXL, MAC Ultra) over Ethernet. Aura PXL needs P3 System Controller software 5.1.0+. Martin also publishes a "P3 Personality and Firmware Update Package" (6.3.2, 2025-12-24). |

### Check the installed version
- **INFORMATION** menu on the fixture: shown as **SW VERSION** (ERA 400) or **SW VERSION / FW VERSION** (MAC Ultra). The MAC Quantum Wash guide says the new version shows in INFORMATION after an update.

### USB stick procedure (MAC Quantum Wash user guide; Viper/Encore guides are the same pattern)
1. Download the **.BANK** file (martin.com product support page, or export from Companion). Read the release notes for warnings.
2. Copy it to the **root directory** of a USB stick.
3. **Disconnect the data link** (console) from the fixture.
4. Insert the stick. If the fixture doesn't react, go to **SERVICE → USB**. (MAC Ultra: **USB → FIRMWARE**.) Viper shows **UPDATING FILES** while it reads the stick.
5. **AVAILABLE FIRMWARE**: scroll to the version, Enter, confirm with Enter (Menu = exit without installing).
6. Let it install and reboot. **Don't switch off and don't pull the stick** while updating.
7. Remove the stick, check INFORMATION, reconnect the data link.

### Martin Companion procedure (DMX or network)
1. Install/update Martin Companion on a Windows PC.
2. Connect: Companion Cable USB → PC, XLR → fixture DMX in, **console unplugged** — or use RDM over Art-Net on the PC's network port.
3. Discover the fixtures, pick the firmware (Companion downloads it), update. Exact screens: ⚠️ unverified.
- **Update the Companion Cable itself** (HARMAN help): close Companion, unplug the cable, open Companion → **Tools → Update Companion Cable**, pick the version, **hold the reset pinhole button** in the middle of the cable while plugging it back into the PC, release, click Update.

### Batch limits
- Companion can push settings to many selected fixtures at once (Settings Templates). Maximum fixtures per firmware update: Not found.
- USB stick: one fixture at a time (you move the stick).
- P3 System Controller: whole P3 rig over Ethernet; limit not found.

### Recovery / bootloader
- **MAC Quantum and MAC Encore series:** a **bootloader switch** inside the base on the main display PCB. **Hold it while powering on** to force bootloader mode, then reinstall firmware by USB or DMX (HARMAN help center). Exact position on the board: ⚠️ unverified.
- **Older MACs (MAC 250/500/700 era) with Martin Uploader:** a **boot-mode upload** is only for software that is totally corrupted (control panel doesn't respond at power-up) or when the release notes call for a **boot sector update**. Move the **boot sector jumper** (next to the control-panel data cable plug) to **Init**, check the **Flash Write** jumper is on **Enable**, power up and run a boot-mode upload from the Uploader. Put the jumper back afterwards (⚠️ unverified). A **checksum error** or fixture that won't reset means the data was interrupted — re-run the upload (MAC 250/500/700 manuals via search).
- Newer models (Ultra, ERA, Aura XB, Aura PXL): recovery procedure Not found.

### Gotchas
- Disconnect the console / data link before updating (Martin user guides).
- **Never power off mid-update** — "firmware will be corrupted" (Martin user guides).
- Don't mix models on the update line (⚠️ unverified, general practice).
- Firmware can add or renumber DMX modes (e.g. MAC Ultra 2.0.0 added an Extended Gamut color mode; Viper 2.0.0 was a major release with its own upload instructions) — re-check the console patch/profile afterwards.
- MAC Aura XB **1.3.0** is needed for units built with a replacement Beam-LED-board component — don't downgrade newer-built XBs (⚠️ inference from the release note).
- Latest versions found 2026-10-03 (martin.com via search summary): MAC Ultra Performance 2.3.0 · ERA 400 Performance 2.0.0 · MAC Aura XB 1.3.0 · MAC Aura PXL 1.6.0 · MAC Encore Performance 1.6.1 · MAC Quantum Wash 2.2.0 · MAC Viper Profile 2.3.0B · Atomic 3000 LED 1.4.0.

## Error message conventions
| Message | Meaning | Source |
|---|---|---|
| `xxx TMP SEN ERR` (MAIN / BEAM / AURA) | A temperature sensor circuit has failed. The matching LEDs won't turn on. | MAC Aura XB manual and service manual |
| `xxx TMP CUT OFF` | Over-temperature. LED power is cut. | Aura XB |
| `PAN FBACK ERR` / `TILT FBACK ERR` | The optical pan/tilt feedback circuit has failed | Aura XB |
| `FBEP` / `FBET` | Fails reset because pan / tilt keeps moving until it times out | Aura XB service manual |
| Fan error | A fan has stopped, so the LEDs are disabled | Aura XB service manual |
| Voltage error | Reset is fine but an error shows. The Beam LEDs won't light. | Aura XB service manual |
| `MEMORY ERROR` | The EEPROM can't be read | Aura XB |
| Beam Calib Err | Beam color doesn't match other units | Aura XB service manual |
| `MMER` (MAC Quantum) | HARMAN has an article on it. Meaning not captured. | HARMAN help center |
| "CLOSED LOOP" codes | Not found in any source | — |

Some errors disable the whole fixture. Others disable only the affected part (HARMAN help center).

## Sources
- [HARMAN help: Martin MAC fixture display error messages explained](https://help.harmanpro.com/en_US/general-mac-inquiries/martin-mac-fixture-display-error-messages-explained): how errors flash and the LED indicator behaves.
- [MAC Aura XB user manual (manualslib, menus p.30, messages p.32)](https://www.manualslib.com/manual/889904/Martin-Mac-Aura-Xb.html?page=30) and [service manual p.6](https://www.manualslib.com/manual/1404416/Martin-Mac-Aura-Xb.html?page=6): menu names, error list.
- [MAC Aura user manual (martin.com)](https://www.martin.com/en/site_elements/mac-aura-user-manual): control panel description, default address 1, Uploader + USB Duo.
- [Martin firmware page](https://www.martin.com/en-US/firmware): Martin Companion and cable P/N 91616091.
- [HARMAN help: MMER Code on MAC Quantum](https://help.harmanpro.com/discontinued-products-martin/mmer-code-on-mac-quantum): MMER exists.
- [Open Fixture Library, Martin fixtures](https://github.com/OpenLightingProject/open-fixture-library/tree/master/fixtures/martin) and [QLC+ Martin fixtures](https://github.com/mcallegari/qlcplus/tree/master/resources/fixtures/Martin): control-channel values (community).
- [Martin Companion Cable user guide](https://www.martin.com/en-US/site_elements/martin-manuals-martin-companion-cable-user-manual): cable use, update Companion first.
- [HARMAN help: How to update the Companion Cable](https://help.harmanpro.com/service-tools/how-to-update-the-companion-cable): reset-pinhole procedure.
- [Companion Desktop – Windows v2.1.4](https://www.martin.com/en-US/softwares/companion-desktop-windows-v2-1-4-windows) and [Companion Desktop page](https://www.martin.com/en-US/products/companion-desktop): latest Companion found, RDM over Art-Net, Settings Templates.
- [HARMAN help: Where to find Martin firmware updates](https://help.harmanpro.com/general-martin-inquiries/where-to-find-martin-firmware-updates).
- [MAC Quantum Wash user guide, firmware installation (manualslib p.16)](https://www.manualslib.com/manual/1053770/Martin-Mac-Quantum-Wash.html?page=16): USB .BANK procedure.
- [HARMAN help: Bootloader button on MAC Quantum and MAC Encore series](https://help.harmanpro.com/en_US/general-mac-encore-inquiries/bootloader-button-on-mac-quantum-and-mac-encore-series): bootloader switch.
- [MAC 700 Wash user manual](https://adn.harmanpro.com/site_elements/executables/5949_1526695117/UM_MAC700Wash_EN_D_original.pdf) and [MAC 500 service manual p.20 (manualslib)](https://www.manualslib.com/manual/993688/Martin-Mac-500.html?page=20): boot-mode upload, boot sector / Flash Write jumpers, checksum errors (via search summary).
- [MAC Ultra Performance Safety and Installation Manual rev B](https://www.christielites.com/file_uploads/SFTY_MACUltraPerformance_EN_B.pdf): USB / Companion / P3 System Controller methods.
