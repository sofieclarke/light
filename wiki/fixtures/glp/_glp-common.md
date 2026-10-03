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
> - **Firmware:** GLP's tool is the **D3Prog** (USB to PC, 5- and 3-pin XLR out, battery powered). Console off the line. X5 family also has **Firmware Push** fixture-to-fixture. See [Firmware updates](#firmware-updates).
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

## Firmware updates
Checked 2026-10-03. GLP's update tool is the **D3Prog** programmer. Names like "GLP Uploader" or "GLP Fixture Updater" weren't found in any GLP source. Firmware is on each product page on **glp.de → Downloads**, on **germanlightproducts.com/downloads**, and (newer fixtures) on the **GLP iQ.Service Portal**.

### Tools
| Tool | What it is | Connects with | Notes |
|---|---|---|---|
| **GLP D3Prog** | Handheld firmware programmer, 2.24" LCD, 5 buttons, 43 x 120 x 78 mm | PC → D3Prog over **USB Type B** or **Sub-D 9-pin**. D3Prog → fixture over **XLR 5-pin female or XLR 3-pin female** (DMX link, RS-485), or **AVR/ISP** (service) | Several firmware versions in separate **memory slots**. Runs on **2x 1.2 V Mignon (AA)** cells, no mains needed. Updates **several fixtures on one DMX line at once**. The D3Prog's own firmware gets updated too (download dated 2022-06-22). All from glp.de |
| D-Prog (part **9506**) | Older/sibling GLP uploader sold in the US | — | Retail listings only ⚠️. Whether 9506 is the D3Prog's part number too: unverified |
| **GLP iQ.Service** | Onboard iQ.Service module + **GLP iQ.Service App** (phone/tablet), and the iQ.Service Portal for files | Wireless (iQ.Mesh) | Listed for impression X5 family and S350. "Wireless firmware updates, information readout, fixture configuration" (glp.de) |
| **Internal web interface** | Fixture's own web page | Ethernet | Listed as an upload method for the impression X5 (manual). Steps: Not found |
| **Firmware Push (Fixture2Fixture)** | Menu item on the fixture | DMX link | impression X5 family: pushes its firmware to every fixture of the same type on the line (manual) |
| GLP iQ.Tool | — | DMX link | Named only in the JDC Burst 1 manual (not covered here) |

- **File types:** when importing to the D3Prog choose **Intel hex** or **BIN** to match the file; it depends on the firmware version (GLP tech note, via search summary ⚠️). JDC-1 updates are **BIN, 3 driver files, all updated in sequence** (via search summary ⚠️).
- **USB port on newer impression fixtures:** Not found. **Art-Net / sACN firmware update:** Not found. The Ethernet route found is the X5's internal web interface.

### D3Prog procedure
1. Download the firmware from glp.de (read the update note on that page; some products have their own update manual, e.g. "impression X4 Software Update Manual", "impression X4S Software Update Instructions").
2. Connect the D3Prog to the PC (USB or Sub-D 9) and load the file into a memory slot, choosing **hex** or **BIN** as the file type.
3. **Unplug the console and anything else on the line you aren't updating.** GLP: no other DMX receivers or consoles may be active on the line (tech note, via search summary).
4. D3Prog XLR (5- or 3-pin) → DMX in of the first fixture, daisy-chain the rest. Fixtures powered.
5. Select the slot and start. The D3Prog's own button sequence: Not found.
6. Don't power-cycle until it's done ⚠️ (general practice). Check the version on every fixture.

### Version per fixture (latest found, 2026-10-03)
| Fixture | Latest found | Where |
|---|---|---|
| JDC1 | 1.95 | germanlightproducts.com download page title |
| impression X5 | 1.1.3 (X5 IP variant: 2.0.1) | manual covers; iQ.Service Portal may be newer |
| impression S350 | V53 (Rev20200203) | glp.de product page |
| impression FR10 Bar | V64 (Rev20230526-1) | glp.de product page |
| JDC Line 1000 | 1.0.0 | DMX Channel Index Rev 20240618-01 |
| impression X4 Bar 20 | Not found (file dated 2023-05-02) | glp.de product page |
| impression X4 / X4 S / X4 L | Not found (X4 file dated 2014-08-20) | glp.de product pages |

### Batch limits
- D3Prog: "multiple fixtures in a DMX line simultaneously" (glp.de). A maximum per line: Not found.
- Firmware Push (X5): every compatible fixture on the link. **An X5 push also updates X5 Compact, X5 Bar 1000 and X5 IP Bar 1000** on the same line (manual).

### Recovery / bootloader
- A GLP firmware page says: **if the fixture is on V1.78 or below, update the Bootloader first**, then the main application (via search summary; it appeared alongside the JDC-1 firmware pages, ⚠️ not pinned to a product).
- The D3Prog can also program over **AVR/ISP**, which is the service route for a fixture that won't take a DMX update (glp.de). Procedure: Not found; the JDC1 technical service manual (rev 2.0) probably covers it (not read).
- Otherwise: support@glp.de.

### Gotchas
- **Console off the line.** GLP says so explicitly.
- **One model per line**, except where GLP says otherwise (X5 push deliberately covers the X5 family). Watch look-alikes: X4 Bar 10 vs 20, X4 vs X4 S vs X4 L, JDC Line 500 vs 1000, S350 vs S350 Wash, JDC1 vs JDC Burst 1 ⚠️.
- **Don't power-cycle mid-update** ⚠️ (general practice).
- **Updates add modes.** JDC1 SW 1.78 added Mode 6 Easy (11 ch); older units (1.35 / 1.70) have only 5 modes. A mixed-version rig can't all run the same mode, and a console profile built for one version may not match the other. Update the whole rig to one version and re-check the patch.
- Some fixtures have more than one firmware part: the X4 Bar 20 has a separate **Tilt firmware** (menu Reset needs Tilt V.20+), the JDC1 shows main and distributed versions, and the X4 manual lists "1.18/18/12/10/n".
- Check the version before you trust a console profile: JDC1 **Information → software versions**.

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
- [GLP D3Prog product page (glp.de)](https://glp.de/en/products/service-firmware/service-tools/d3prog-en) — D3Prog connectors, memory slots, batteries, size, DMX link / AVR-ISP, multiple fixtures at once (via search summary)
- [D3-Prog/D-Prog/pa firmware update download](https://www.germanlightproducts.com/download/d3-prog-dp-rog-pa-firmware-update-this-version-supersedes-all-previous-versions/) — programmer firmware
- GLP Tech News [2019/10/30](https://www.glp.de/en/service/tech-info-archive/archive/80-glp-tech-news-2019-10-30?tmpl=component) and [2019/01/14](https://www.glp.de/en/service/tech-info-archive/archive/73-glp-tech-news-2019-01-14) — hex vs BIN, no other DMX receivers/consoles on the line, bootloader-first note (via search summary; not pinned)
- [GoKnight: GLP 9506 D-Prog Uploader](https://goknight.com/german-light-products-9506-d-prog-uploader/), [Solotech: GLP 9506 D-Prog](https://shop.solotech.com/products/glp-9506-d-prog-firmware-uploader) — part number (retail)
- [impression X5 User Manual Rev 20240207-01 (SW 1.1.3)](https://www.germanlightproducts.com/wp-content/uploads/2022/01/GLP-impression-X5-User-Manual-Rev-20240207.pdf), [X5 IP User Manual Rev 20250129-01](https://glp.de/files/products/impression-x5-ip-product-data/GLP_impression_X5_IP_User_Manual_EN_Rev20250129-01.pdf) — D3Prog / iQ.Service / web interface, Firmware Push (via search summary)
- GLP download pages: [JDC-1 Firmware 1.95](https://www.germanlightproducts.com/download/jdc-1-firmware-1-95/), [impression X4 Software Update Manual](https://www.germanlightproducts.com/download/impression-x4-software-update-manual/), [impression X4S Software Update Instructions](https://www.germanlightproducts.com/download/impression-x4s-software-update-instructions/) — titles only
- Product pages (via search summary): [S350](https://www.glp.de/en/products/entertainment-lighting/moving-lights-led/impression-s350), [FR10 Bar](https://glp.de/en/products/entertainment-lighting/moving-lights/impression-fr10-bar-en), [JDC Line 1000](https://glp.de/en/products/entertainment-lighting/strobes/jdc-line-1000-en), [X4 Bar 20](https://glp.de/en/products/entertainment-lighting/moving-lights/impression-x4-bar-20-en), [X4](https://glp.de/en/products/entertainment-lighting/moving-lights/impression-x4-en), [X5](https://www.glp.de/en/products/moving-lights-led/impression-x5) — firmware versions/dates, update methods, iQ.Service Portal
- [JDC Burst 1 User Manual Rev 20250606-02](https://www.germanlightproducts.com/wp-content/uploads/2025/06/GLP-JDC-Burst1-User-Manual-EN-Rev20250606-02.pdf) — D-Prog / iQ.Mesh / iQ.Tool update routes (via search summary)
