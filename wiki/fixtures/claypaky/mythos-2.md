---
title: "Claypaky Mythos 2"
manufacturer: "Claypaky"
model: "Mythos 2"
aliases: ["mythos 2", "mythos2", "c61396", "clay paky mythos 2", "claypaky mythos 2", "mythos"]
type: "hybrid"
light_source: "Osram Sirius HRI 440W X"
ip_rating: null
weight_lb: 70.54
weight_kg: 32
dimensions: "L 420 mm (16.53 in) x W 396 mm (15.59 in) x H 628 mm (24.72 in)"
power:
  input: "115/230 V 50/60 Hz with automatic power supply switching (manual); rental specs list 100-240 V"
  connector_in: ""
  connector_out: ""
  watts_max: 700
  amps_120v: null
  amps_208v: null
  amps_230v: null
  link_max_120v: null
  link_max_208v: null
  link_max_230v: null
  per_20a_120v: null
  per_20a_208v: null
  fuse: ""
dmx:
  connectors: "5-pin XLR in/out"
  protocols: ["DMX"]
  modes:
    - { name: "Standard", channels: 30 }
    - { name: "Vector", channels: 34 }
menu_password: "1234"
firmware:
  latest_known: null
  checked: "2026-10-03"
  check_on_fixture: "Information menu → system version ⚠️ (Sharpy-family menu name)"
  methods: ["Fixture-to-fixture over DMX (Advanced → Upload Firmware, code 1234)", "PC + Claypaky Firmware Uploader USB/DMX interface ⚠️", "CloudIO Box + USB stick ⚠️ compatibility unverified"]
  interface: "None for fixture-to-fixture; Claypaky Firmware Uploader USB/DMX interface (C61206) for PC updates ⚠️"
  software: "Claypaky FUL Uploader ⚠️ (name from a Claypaky video title)"
  file_type: ".img (CloudIO USB-stick update); other methods: Not found"
  download: "Claypaky Customer Care site (service.claypaky.it, restricted login) — ask your Claypaky distributor / rental house"
tools: []
verification: "web-search"
last_updated: "2026-10-03"
---

# Claypaky Mythos 2

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** Advanced menu code **1234**. Menu Locking is a user-set 4-digit password (Mythos manual).
> - **Power:** 700 VA @230 V (manufacturer). Amps at 120 V and 208 V not published. Derived: 700/120 ≈ 5.8 A → **2 per 20 A circuit @120 V**, 700/208 ≈ 3.4 A → **4 @208 V** ⚠️ derived from VA, not manufacturer amps. Power factor isn't confirmed, so real current could be higher. Link limit not found.
> - **DMX:** Standard **30 ch** / Vector **34 ch**. Lamp Control 101-255 ON, 26-100 OFF.
> - **Won't move?** Pan locks every 90°, tilt locks every 45° (manual).
> - **Rigging:** quarter-turn (fast-lock) omega clamps on the base.
> - **Tools:** TBD – check on next show

## Identity
- What crews call it: "Mythos", "Mythos 2". Codes: C61391 = Mythos (first version), C61396 = Mythos 2 (the shared manual is titled "C61391 C61396").
- Fixture library / profile names: Standard 30 ch, Vector 34 ch. The DMX charts are the same for Mythos and Mythos 2 (QLC+ uses one "Mythos" profile with 30/34 ch).
- Variants: Mythos (original) used a 470 W lamp per vendor listings ⚠️ unverified. Mythos 2 uses the Osram Sirius HRI 440W X.

## Passwords, menu locks & hidden menus
- Advanced Menu: "enter the code (1234)" (Mythos / Mythos 2 manuals).
- Menu Locking: assigns a 4-digit password to the user menu. Default unlock not stated for Mythos in what I found. The Sharpy family default is 1234 ⚠️ unverified for Mythos 2.
- Service / factory menu: Advanced menu. See [_claypaky-common.md](_claypaky-common.md).

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not published. ≈5.8 A derived ⚠️ | Not published. ≈3.4 A derived ⚠️ | Not published as amps |
| Power (W) | — | — | 700 VA input @230 V 50 Hz (manual) |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | floor(16/5.8)=2 → **2** ⚠️ derived | floor(16/3.4)=4 → **4** ⚠️ derived | — |

- Input range / auto-ranging: manual says "115/230V 50/60 Hz, automatic power supply switching". Rental listings say 100-240 V.
- Connectors in / out: Not found — fill in from the fixture.
- Fuse: Not found — fill in from the fixture.
- Inrush / power-up notes: discharge lamp. Don't hot-restrike repeatedly.

## Data & addressing
- Connectors: 5-pin XLR (QLC+ community). Full list: Not found.
- Protocols: DMX (others not confirmed).
- DMX modes: **Standard 30**, **Vector 34** (Mythos DMX chart 12.2016). Standard order (QLC+): Cyan, Magenta, Yellow, Colour 1, 2, 3, Shutter/Strobe, Dimmer, Dimmer fine, Static Gobo, Disk insert, Disk rotation, Rotating Gobo, Gobo Rot, Gobo Rot fine, Prism insert, Prism rot, Frost, Zoom, Focus, Focus fine, Beam Mode, Pan, Pan fine, Tilt, Tilt fine, Function, Reset, Lamp Control, Macros.
- Control values (QLC+ community): Reset 26-76 zoom reset, 77-127 pan/tilt reset, 128-255 complete. Lamp 26-100 OFF, 101-255 ON. Function 38-50 conventional dimmer curve, 88-101 CMY shortcut ON, 102-114 CMY shortcut OFF.
- Set the address: via the display menu. Battery/unpowered addressing is likely the same as the rest of the line ⚠️ unverified for this model.
- Factory reset: Advanced menu → Factory Default ⚠️ assumed from family structure.

## Rigging & hardware
- Bracket / omega type: fast-lock omega clamps (1/4 turn) on the base (manual). Spacing: Not found.
- Safety cable point: Not found — fill in from the fixture.
- Transport / pan-tilt locks: PAN lock/release every 90°, TILT every 45° (manual). Two side handles.
- Weight / dimensions: 32 kg (70.54 lb). L 420 x W 396 x H 628 mm.
- Automatic repositioning of PAN and TILT after uncommanded movement (manual).

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD – check on next show |
| Gobo / effects module access | TBD – check on next show | TBD – check on next show |
| Lens / front glass | TBD – check on next show | TBD – check on next show |
| Omega bracket | 1/4-turn fast-lock | TBD – check on next show |

## Optics & consumables
- Source / lamp: Osram Sirius HRI 440W X, 7000 K, 1500 h (vendor/datasheet).
- Color system: CMY plus 14 colour filters on three wheels.
- Gobo wheels: 6 HQ dichroic, indexable, interchangeable rotating gobos, **Ø 25.9 mm**. Interchangeable wheel with 18+1 fixed metal gobos (including 6 beam reducers). Thickness: Not found.
- Prism / frost / zoom: zoom 4-50° (1:12). Fixed beam down to 2.5° with a 160 mm front lens. Prism and frost included.
- Gobo change procedure: Not found.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| System Errors list (Information menu) | Errors since power-on | Press OK, answer YES to "Are you sure you want to clear error list?" (manual) |
| Stopper/strobe closes after a bump | "Shutter on error" option (closes on pan/tilt position error) | Normal, let it re-home (manual) |
| Specific error code strings | Not found — fill in from the fixture | |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Head won't pan/tilt | Transport locks engaged | Release (pan 90° / tilt 45° steps) |
| Lamp won't strike from desk | Lamp control channel not sent or profile lacks it | Send Lamp Control 101-255. Check the Lamp DMX option if present ⚠️ |
| No light, electronics OK | Lamp exhausted | Replace lamp (family troubleshooting table) |

## Maintenance
- Recalibrate / reset: Advanced → Calibration ⚠️ family structure. DMX complete reset 128-255.
- Fan / filter cleaning: Not found.

## Firmware
- Installed version — where to see it on the fixture: Information menu → system version ⚠️ (Sharpy-family name; not confirmed in the Mythos manual).
- Latest known version (date checked) and where to download it: **Not found** (checked 2026-10-03). Claypaky doesn't publish version numbers openly. Files live on the restricted **Claypaky Customer Care** site (service.claypaky.it). Ask your distributor or the rental house's service department, and write the version you find here.
- Update features Claypaky lists for this model: "firmware upgrade with no power" and "firmware upload from another fixture" (Claypaky product guide / dealer page, via search summary). The original Mythos and Mythos 2 share one manual (C61391/C61396), but don't push Mythos firmware onto a Mythos 2 or the other way round ⚠️.
- What you need:
  - **Fixture-to-fixture (no PC):** one Mythos 2 already on the version you want, plus a DMX cable to the others. DMX connector type: see Data & addressing.
  - **From a PC:** Claypaky's **Firmware Uploader USB/DMX interface** (retail listings: "Firmware Uploader Kit USB/DMX", part **C61206** listed for the Alpha 1500). ⚠️ unverified which kit and which PC software suit this model. Claypaky's own Tech Corner video calls the PC tool **"FUL Uploader"** (video title only).
  - **CloudIO / CloudIO Box (CA8001):** copy the `.img` firmware file to the **root** of a USB stick, plug it into the CloudIO, open **Fixture Firmware Uploader**, press **CONTINUE**. Every compatible Claypaky fixture on its DMX OUT updates (CloudIO manual). ⚠️ unverified whether this model is on CloudIO's compatible list. USB stick format: Not found.
- Update steps (fixture-to-fixture, Advanced menu; menu path from Claypaky manuals):
  1. Unplug the console from the DMX line ⚠️ (general practice). Leave only fixtures of **the same model** on the line.
  2. Run DMX from the Mythos 2 that has the wanted firmware into the first fixture to update, and daisy-chain the rest.
  3. On the source fixture: menu → **Advanced** → enter access code **1234** → **Upload Firmware** → confirm.
  4. Don't touch or power-cycle anything until it finishes ⚠️ (general practice). Then check the version on every target (see above).
- Updating a whole rig: **same model only**, and Claypaky recommends **5–6 units at a time maximum** for fixture-to-fixture (manual, via search summary). CloudIO handles up to 31 lights on one DMX line (CloudIO page). Art-Net / sACN firmware update: Not found.
- If it fails or bricks mid-update (recovery mode): **Not found.** No bootloader or recovery procedure was found. Retry from a known-good fixture of the same model, then call Claypaky service. See [_claypaky-common.md](_claypaky-common.md#firmware-updates).
- Release notes worth knowing: Not found. A firmware change can add or renumber DMX modes, so check your console profile against the fixture's mode list after any update.

## Road notes (community)
- No sourced forum notes found. Add your own.

## Sources
- [Mythos / Mythos 2 manual C61391 C61396 (carlosmendoza.com.mx mirror)](http://www.carlosmendoza.com.mx/Descargas/Clay_Paky_Mythos_manual.pdf) — locks, omega, features
- [Mythos 2 manual (prolight.com.pl)](https://prolight.com.pl/images/content/Image/instrukcje/claypaky_mythos_2_instrukcja_eng.pdf), [ManualsLib Mythos2](https://www.manualslib.com/manual/2365196/Clay-Paky-Mythos2.html), [Mythos C61391 manual (huss-licht-ton)](https://www.huss-licht-ton.de/images/products_download/User_Manual_17456_1.pdf) — Advanced code 1234, Menu Locking, system errors, power supply 115/230 V, 700 VA
- [Mythos DMX Channels 12.2016 (lightmoves.com.au)](https://www.lightmoves.com.au/downloads/Documentation/Clay%20Paky/Mythos_DMX-Channels_12.2016_EN.pdf), [VLS mirror](https://rent.vls.com/wp-content/uploads/2022/02/Mythos-DMX-Channels_12.2016_EN.pdf) — 30/34 ch
- [Mythos2 datasheet 07.2019 (visiontwo.de)](https://www.visiontwo.de/fileadmin/user_upload/Claypaky_Mythos2_Datenblatt_07.2019.pdf), [Resolution X](https://resolutionx.com.au/products/automated-fixtures/clay-paky-mythos-2/), [Showtech](https://www.showtech.com.au/product/mythos-2/) — lamp, weight, dims, gobo sizes
- QLC+ Clay-Paky-Mythos.qxf (github.com/mcallegari/qlcplus, commit 1ccdab8) — channel order and control values (community)
- [Claypaky Product Guide 2019 (sgssistemas.lv mirror)](https://www.sgssistemas.lv/uploads/resources/166/lv/claypaky-productguide2019-en.pdf), [Showtech Mythos 2 page](https://www.showtech.com.au/product/mythos-2/) — Mythos 2: firmware upgrade with no power, firmware upload from another fixture (via search summary; which of the two pages said it wasn't pinned)
- Claypaky instruction manuals (Sharpy [manuals.plus copy](https://manuals.plus/m/0dc75ba9bd5c288c40aa1eb565a0d3d88973ac670f2f407b78f1e04c1552d923), [A.leda B-EYE K10/K20 user guide (cpl.tech)](https://www.cpl.tech/wp-content/uploads/2018/10/Clay-Paky-A-leda-B-EYE-K10-User-Guide.pdf), [Sharpy Plus (ManualsLib)](https://www.manualslib.com/manual/1637972/Claypaky-Sharpy-Plus.html)) — Upload Firmware copies firmware from one fixture to the others on the line, same model only, 5/6 units at a time max (via search summary; the exact manual page wasn't pinned)
- [B&H: Claypaky C61206 Firmware Uploader USB/DMX interface](https://www.bhphotovideo.com/c/product/1827391-REG/claypaky_c61206_firmware_uploader_usb_dmx_interfacefor.html), [Lightspares: Claypaky Firmware Uploader Kit USB/DMX](https://lightspares.com/claypaky-firmware-uploader-kit-usbdmx-010-074) — the interface exists (retail listings; listed for Alpha-series fixtures)
- [Claypaky CloudIO Instruction Manual 01.2020 (visiontwo.de)](https://www.visiontwo.de/fileadmin/user_upload/Claypaky_CloudIO_Manual_01.2020.pdf), [06.2022 (ltb.no)](https://ltb.no/media/multicase/documents/claypaky/manual_claypaky_cloudio_06.2022.pdf), [CloudIO product page](https://www.claypaky.it/products/cloudio/) — Fixture Firmware Uploader app, `.img` on USB-key root, up to 31 lights on its DMX line, offline use (via search summary)
- Claypaky Tech Corner videos (titles only, not watched): [Firmware Update with FUL Uploader](https://www.youtube.com/watch?v=hyeRWUqLlTk), [Firmware Update with Web Server](https://www.youtube.com/watch?v=Jp4SJ3HJ9N4), [Firmware Update from Fixture to Fixture](https://www.youtube.com/watch?v=xGVPVCwnRPg)
