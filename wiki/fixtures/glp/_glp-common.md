---
title: "GLP common conventions"
manufacturer: "GLP (German Light Products)"
verification: "web-search"
last_updated: "2026-10-03"
---

# GLP: menus, locks, firmware, errors (shared notes)

> **2AM CARD**
> - **4 buttons on every GLP fixture covered here: Mode / Enter / Up / Down.** Mode = into the menu or back out to the top. Enter = select / confirm / go down a level. Up/Down = scroll. (X4 Bar 20 and JDC1 manuals.)
> - **Keys dead on an X4 Bar?** Press **Mode + Enter + Up** together to lock/unlock (X4 Bar 20 manual). Not confirmed for other models.
> - **No published user passcode** was found for any GLP fixture. The JDC1 **Service** menu takes a **Key Code (0–255)** and is meant for GLP Service; the code isn't published.
> - **JDC1 (and probably newer JDC models ⚠️) has a battery-backed display**, so you can address it with no power.
> - **JDC1 errors are sticky.** The message flashes alternately with the DMX address until a power cycle or reset. Check Information → System Errors List.
> - **JDC1 has no AC thru: one per 20 A circuit at 120 V.**
> - Support e-mail printed on every manual: **support@glp.de**

## Menu conventions
- **Buttons:** Mode, Enter, Up, Down. Confirmed in the X4 Bar 20 and JDC1 manuals.
- **X4 Bar series (older impression firmware style):**
  - The DMX Address is at menu Level 1 (default 001).
  - "Set DMX Mode" and "Special" are at Level 2.
  - Special holds: dimmer curve (ESOFT / LIN / SOFT), Tilt reset, Tilt current, Tilt slow, Reverse tilt, Reverse pixel, Display flip, Reset.
  - Mode names are short lowercase codes: norm, comp, hires, dpix, dpixh, spix.
- **JDC-series (newer GLP style):**
  - Big DMX address on the home screen, with network IP addresses shown below it.
  - An **Information** menu shows the error list, SW/HW versions (main and distributed), temperature sensors, operating hours, boot count, and AC vs battery power.
  - A password-protected **Service** menu (Key Code 0–255).
- **"Fixture Settings":** no source confirms a menu literally named "Fixture Settings" on GLP fixtures. Not found. The X4 Bar uses "Special".
- **Ethernet addressing (JDC Burst 1 manual, ⚠️ may not apply to older JDC1 firmware):**
  - Addressing Mode: Auto 2.x.x.x / Auto 10.x.x.x / Custom IP
  - separate Art-Net Port and sACN Universe settings
  - choose the active protocol under **Protocol Setup → Data In**
  - 1-scene standalone mode

## Battery / unpowered addressing
- **JDC1:** yes. The graphic LCD has a self-charging battery and settings can be changed with power off (JDC1 manual).
- **X4 Bar 10/20:** no source mentions it, so assume no ⚠️.
- Other models: Not found.

## Unlocking / passwords
- X4 Bar: **Mode + Enter + Up** toggles the key lock.
- JDC1 Service menu: Key Code 0–255, GLP Service only, code not published.
- Others: Not found — fill in from the fixture.

## Reset / service
- X4 Bar: the menu **Reset** recalibrates all functions (needs Tilt firmware V.20 or later). No factory-defaults procedure was found.
- JDC1: errors clear on a power cycle or reset. Factory reset procedure: Not found.
- A **JDC1 technical service manual** (rev 2.0, 30 Aug 2023) exists: <https://germanlightproducts.com/wp-content/uploads/2025/03/Service-manual-of-JDC-1-rev2.0-Aug.30th-2023.pdf> (not read).

## Firmware update
- **Not found in any source retrieved.** The user-manual excerpts don't describe the update procedure.
- From general knowledge ⚠️ unverified: GLP distributes firmware with a PC tool called **GLP Uploader**. It sends updates over the DMX line through a GLP USB-to-DMX interface, and newer fixtures may update over Ethernet. Don't rely on this. Get the current procedure and files from glp.de / support@glp.de.
- Version check before you trust a console profile: on the JDC1 use **Information → software versions**. The JDC1 Easy mode (11 ch) needs SW 1.78 (manual "178-69-19") or later. Older manuals (SW 1.35 / 1.70) list only 5 modes.

## Common error messages
| Fixture | Message | Meaning | Fix |
|---|---|---|---|
| JDC1 | Any error text flashing with the address | Self-diagnosis found a fault; it stays until power cycle/reset | Information → System Errors List; power-cycle; if it returns, it's real |
| All others | Not found | | Fill in from the manuals |

## Power-linking gotchas
- **X4 Bar 20:** powerCON in/thru. The manual says never more than **20 A total** through the chain (connector limit). A rental spec gives 4.6 A @120 V, which means **3 per 20 A circuit**.
- **JDC1:** a single powerCON TRUE1 in with **no thru**. It's 5.8 A @208 V (rental spec) / 5.3 A @230 V (GLP spec). At 120 V figure ≈10 A, so **one per circuit**.

## Sources
- [impression X4 Bar 20 User Manual v1.8](https://glp.de/files/products/impression-x4-bar-20-product-data/impression_X4_Bar_20_User_Manual_v1.8_EN.pdf) — key lock combo, menu levels, Special menu, Reset, 20 A connector note
- [ManualsLib X4 Bar 20, menu pages](https://www.manualslib.com/manual/1568587/Glp-Impression-X4-Bar-20.html?page=9) — menu field
- [JDC1 User Manual Rev 20240830-01](https://glp.de/files/products/jdc1-product-data/GLP_JDC1_User_Manual_EN_Rev20240830-01.pdf) — buttons, Service Key Code, battery LCD, Information menu, sticky errors
- [JDC1 DMX Channel Index V4.0](https://glp.de/files/products/jdc1-product-data/JDC1_DMX_Channel_Index_EN_V.4.0_Rev.20191023.pdf) — Easy mode / SW 1.78
- [JDC Burst 1 User Manual](https://saleswl.com/wp-content/uploads/2025/04/GLP-JDC-Burst-1-User-Guide.pdf) — Ethernet addressing menu, Protocol Setup → Data In
- [JDC1 technical service manual rev 2.0](https://germanlightproducts.com/wp-content/uploads/2025/03/Service-manual-of-JDC-1-rev2.0-Aug.30th-2023.pdf) — exists, not read
