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
> - **Firmware:** newer fixtures use **Martin Companion** over DMX with the **Martin Companion Cable, P/N 91616091**. Older ones use **Martin Uploader** with a **USB Duo** DMX box. Download from martin.com/firmware.
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

## Firmware update
- **Martin Companion** (free Windows software) plus the **Martin Companion Cable, P/N 91616091**, updates firmware **over DMX**. This is how the MAC Aura XB is updated (Martin firmware page).
- **Martin Uploader** (Windows) plus a **Martin USB Duo DMX interface** is the older method. The original MAC Aura uses it (Martin docs, via search).
- **USB stick** updates are mentioned for newer models such as the MAC Aura XIP (search summary). Which models take USB: Not found. ⚠️ unverified
- **P3** is Martin's video/pixel protocol (used by the MAC Aura PXL for pixel content). P3 firmware updating: Not found.

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
