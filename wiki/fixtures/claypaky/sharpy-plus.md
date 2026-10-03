---
title: "Claypaky Sharpy Plus"
manufacturer: "Claypaky"
model: "Sharpy Plus"
aliases: ["sharpy plus", "sharpy+", "cd3000", "clay paky sharpy plus", "claypaky sharpy plus"]
type: "hybrid"
light_source: "Osram Sirius HRI 330W X8"
ip_rating: "IP20"
weight_lb: 50.7
weight_kg: 23
dimensions: "Base 307 x 375 mm, height 635 mm with head vertical (datasheet)"
power:
  input: "100-240 V, 50/60 Hz, electronic auto-range with active PFC"
  connector_in: "Neutrik powerCON TRUE1"
  connector_out: null
  watts_max: 540
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
  connectors: "Locking 5-pin XLR in/out, RJ45 Ethernet"
  protocols: ["DMX", "RDM", "Art-Net", "sACN"]
  modes:
    - { name: "Standard", channels: 31 }
menu_password: "1234"
firmware:
  latest_known: null
  checked: "2026-10-03"
  check_on_fixture: "Information menu → system version ⚠️ (Sharpy-family menu name, not confirmed on the Plus)"
  methods: ["Fixture-to-fixture over DMX (Advanced → Upload Firmware, code 1234)", "Web Server over Ethernet (RJ45)", "PC + Claypaky Firmware Uploader USB/DMX interface ⚠️", "CloudIO Box + USB stick ⚠️ compatibility unverified"]
  interface: "None for fixture-to-fixture or Web Server; Claypaky Firmware Uploader USB/DMX interface (C61206) for PC-over-DMX ⚠️"
  software: "Web browser (built-in web server); Claypaky FUL Uploader ⚠️"
  file_type: ".img (CloudIO USB-stick update); other methods: Not found"
  download: "Claypaky Customer Care site (service.claypaky.it, restricted login) — ask your Claypaky distributor / rental house"
tools: []
verification: "web-search"
last_updated: "2026-10-03"
---

# Claypaky Sharpy Plus

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** Advanced menu code **1234**. Menu Locking default unlock code is **1234** (Sharpy Plus / Plus Aqua manuals).
> - **Power:** 540 VA max @230 V (manufacturer). Amps at 120 V and 208 V not published. Derived estimate (active PFC, so VA ≈ W): ≈4.5 A @120 V → **3 per 20 A circuit @120 V**, ≈2.6 A @208 V → **6 @208 V** ⚠️ derived, not manufacturer amps. Power link limit not found.
> - **DMX:** one mode, **31 ch**. DMX/RDM/Art-Net/sACN. Address via the display (F to wake). The display works unpowered on its buffer battery.
> - **Lamp control:** Lamp Control channel 26-100 OFF, 101-255 ON (community profile; hold a few seconds).
> - **Won't move?** Pan locks every 90°, tilt locks every 45° (manual). Release both.
> - **Tools:** TBD – check on next show

## Identity
- What crews call it: "Sharpy Plus", "Sharpy+". Product code CD3000. The IP66 outdoor version is **Sharpy Plus Aqua** (also CD3000 family).
- Fixture library / profile names: a single 31-channel profile, "Sharpy Plus Standard". (Some search summaries mixed in the original Sharpy's 16/20-ch Standard/Vector modes. Those are wrong for the Plus.)
- Variants: Sharpy Plus (indoor) vs Sharpy Plus Aqua (IP66, heavier). The original Sharpy has no CMY and no zoom.

## Passwords, menu locks & hidden menus
- Advanced menu: enter code **1234** (Sharpy Plus manual; Sharpy Plus Aqua user menu).
- Menu Locking: 4-digit user-menu password, default unlock **1234** (manual).
- Service / factory menu: Advanced menu holds Factory Default, Calibration, Upload Firmware (same structure as the Sharpy line; see [_claypaky-common.md](_claypaky-common.md)).

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not published. ≈4.5 A derived (540/120) ⚠️ | Not published. ≈2.6 A derived (540/208) ⚠️ | Not published as amps. 540 VA (manufacturer) |
| Power (W) | — | — | 540 VA max @230 V 50 Hz |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | floor(16/4.5)=3 → **3** ⚠️ derived | floor(16/2.6)=6 → **6** ⚠️ derived | — |

- Input range / auto-ranging: 100-240 V 50/60 Hz, electronic auto-range, active PFC (datasheet).
- Connectors in / out: Neutrik powerCON TRUE1 (IP65) in. Power thru: Not found — fill in from the fixture.
- Fuse: Not found — fill in from the fixture.
- Inrush / power-up notes: discharge lamp. Fast ON-OFF cycles reduce lamp life (manual).

## Data & addressing
- Connectors: locking 5-pin XLR IN/OUT, RJ45 Ethernet IN (datasheet). PLSN's road test mentions Ethernet in and thru on the faceplate. Confirm on the unit.
- Protocols: DMX, Art-Net, RDM, sACN.
- DMX modes: one profile, 31 ch (datasheet, PLSN). Order per QLC+ community profile: Cyan, Magenta, Yellow, Colour Wheel 1, 2, 3, Strobe, Dimmer, Dimmer fine, Fixed Gobo, Animation insert, Animation rotation, Rotating Gobo, Gobo Rot, Gobo Rot fine, 4-facet prism in, 4-facet rot, 8-facet prism in, 8-facet rot, Frost, Zoom, Focus, Focus fine, Beam Mode, Pan, Pan fine, Tilt, Tilt fine, Function, Reset, Lamp Control.
- Control values (QLC+ community): Reset 26-76 effects, 77-127 pan/tilt, 128-255 complete. Function 151-160 display OFF, 161-170 display ON. Lamp 26-100 OFF, 101-255 ON.
- Set the address: press F to wake the display. Use UP / DOWN / RIGHT, then F to confirm (same key scheme as the Sharpy manual) ⚠️ key labels unverified for this model.
- Battery / unpowered addressing: yes. The display uses a buffer battery (Sharpy Plus manual, per search summary).
- Factory reset: Advanced menu → Factory Default.
- Wireless / Ethernet setup notes: Not found.

## Rigging & hardware
- Bracket / omega type: Not found — fill in from the fixture.
- Safety cable point: Not found.
- Transport / pan-tilt locks: PAN lock/release every 90°, TILT lock/release every 45° (manual, "Unpacking and preparation", Figs 2-3). Location of the levers: TBD – check on next show.
- Weight / dimensions: 23 kg (50.7 lb). Base 307 x 375 mm, H 635 mm.
- Pan 540° / tilt 270° (QLC+ community).

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD – check on next show |
| Gobo / effects module access | TBD – check on next show | TBD – check on next show |
| Lens / front glass | TBD – check on next show | TBD – check on next show |
| Omega bracket | TBD – check on next show | TBD – check on next show |

## Optics & consumables
- Source / lamp: Osram Sirius HRI 330W X8, rated life 1500 h. 12,000 lm output (datasheet).
- Don't touch the lamp envelope bare-handed. If you do, clean it with alcohol and dry it with a clean cloth (manual).
- Color system: CMY plus 15 colours on 3 wheels, including 2 CTO filters.
- Gobo wheels: rotating wheel with **8 interchangeable glass gobos, OD 15.9 mm, image 12 mm, thickness 1.1 mm**. Static wheel with 18 gobos. Animation wheel.
- Prism / frost / zoom: rotating 4-facet and 8-facet prisms, linear soft-edge frost, zoom 3-36°.
- Gobo change procedure: Not found.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| System Errors list (Information menu) | Warnings and messages since power-on | Reset from the same menu after fixing (manual) |
| Specific error code strings | Not found — fill in from the fixture | |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| No power | No mains | Check supply (manual) |
| No light | Lamp exhausted or defective | Replace lamp (manual) |
| Not responding / bad projection | Faulty data cable | Replace cable (manual) |
| Reduced light | Wrong address, dirty or broken optics | Check address, clean optics (manual) |
| Head locked | Transport locks engaged | Release pan (90° steps) and tilt (45° steps) locks |

## Maintenance
- Recalibrate / reset: Advanced → Calibration. DMX reset 128-255.
- Fan / filter cleaning: Not found.

## Firmware
- Installed version — where to see it on the fixture: Information menu → system version ⚠️ (that's the Sharpy manual's name, "System Version"; not confirmed on the Plus).
- Latest known version (date checked) and where to download it: **Not found** (checked 2026-10-03). Claypaky doesn't publish version numbers openly. Files live on the restricted **Claypaky Customer Care** site (service.claypaky.it). Ask your distributor or the rental house's service department, and write the version you find here.
- Update features Claypaky lists for this model: firmware upgrade via **Web Server** (Claypaky product page). The Advanced menu has **Upload Firmware** (manual).
- What you need:
  - **Fixture-to-fixture (no PC):** one Sharpy Plus already on the version you want, plus a DMX cable to the others. DMX is locking 5-pin XLR only (datasheet): bring a 3-to-5-pin adapter if your interface is 3-pin.
  - **From a PC:** Claypaky's **Firmware Uploader USB/DMX interface** (retail listings: "Firmware Uploader Kit USB/DMX", part **C61206** listed for the Alpha 1500). ⚠️ unverified which kit and which PC software suit this model. Claypaky's own Tech Corner video calls the PC tool **"FUL Uploader"** (video title only).
  - **Web Server (Ethernet):** the Sharpy Plus has a built-in web server and Claypaky lists "firmware upgrade via Web Server" (product page). Laptop on the fixture's RJ45, browser to the fixture. The exact steps and IP aren't sourced: see the Tech Corner "Firmware Update with Web Server" video.
  - **CloudIO / CloudIO Box (CA8001):** copy the `.img` firmware file to the **root** of a USB stick, plug it into the CloudIO, open **Fixture Firmware Uploader**, press **CONTINUE**. Every compatible Claypaky fixture on its DMX OUT updates (CloudIO manual). ⚠️ unverified whether this model is on CloudIO's compatible list. USB stick format: Not found.
- Update steps (fixture-to-fixture, Advanced menu; menu path from Claypaky manuals):
  1. Unplug the console from the DMX line ⚠️ (general practice). Leave only fixtures of **the same model** on the line.
  2. Run DMX from the Sharpy Plus that has the wanted firmware into the first fixture to update, and daisy-chain the rest.
  3. On the source fixture: menu → **Advanced** → enter access code **1234** → **Upload Firmware** → confirm.
  4. Don't touch or power-cycle anything until it finishes ⚠️ (general practice). Then check the version on every target (see above).
- Updating a whole rig: **same model only**, and Claypaky recommends **5–6 units at a time maximum** for fixture-to-fixture (manual, via search summary). CloudIO handles up to 31 lights on one DMX line (CloudIO page). Art-Net / sACN firmware update: Not found.
- If it fails or bricks mid-update (recovery mode): **Not found.** No bootloader or recovery procedure was found. Retry from a known-good fixture of the same model, then call Claypaky service. See [_claypaky-common.md](_claypaky-common.md#firmware-updates).
- Release notes worth knowing: Not found. A firmware change can add or renumber DMX modes, so check your console profile against the fixture's mode list after any update.

## Road notes (community)
- ControlBooth "Sharply Plus for theatre": it's a hybrid that zooms to 36° and has frost. Unlike the original Sharpy, it's usable as a spot.
- No other sourced road notes. Add your own.

## Sources
- [Sharpy Plus Instruction Manual 11.2020 (visiontwo.de)](https://www.visiontwo.de/fileadmin/user_upload/Claypaky_Sharpy_Plus_Manual_11.2020.pdf), [05.2023 (goknight.com)](https://goknight.com/content/documentation/SharpyPlus_InstructionManual_05.2023.pdf), [motion-rental mirror](https://motion-rental.de/downloads/artikelpdfs/20987-CP_Sharpy_PLUS_manual_ENG.pdf) — Advanced code 1234, pan/tilt lock steps, lamp handling, troubleshooting
- [Sharpy Plus Aqua User Menu 03.2023 (ltb.no)](https://ltb.no/media/multicase/documents/claypaky/brukermeny_claypaky_sharpyplusaqua_03.2023.pdf) — 1234 access code, Menu Locking default 1234
- [Sharpy Plus Datasheet 03/2024 (acson.com)](https://acson.com/pdf/DataSheets/CLAY-PAKY/SHARPY-PLUS.pdf), [Showtech datasheet](https://www.showtech.com.au/webdata/CLPSHA015/downloads/CLPSHA015%20SharpyPlus%20datasheet.pdf), [Claypaky product page](https://www.claypaky.it/products/sharpy-plus/) — 540 VA, 100-240 V PFC, lamp, gobo dims, weight, connectors, protocols, 31 ch
- [PLSN road test Sharpy Plus](https://plsn.com/articles/road-tests/claypaky-sharpy-plus/) — single 31-ch profile, data in/thru
- [ControlBooth: Sharpy Plus for theatre](https://www.controlbooth.com/threads/sharply-plus-for-theatre.51633/) — road note
- QLC+ Clay-Paky-Sharpy-Plus.qxf (github.com/mcallegari/qlcplus, commit 1ccdab8) — channel order, reset/function/lamp values (community)
- [Claypaky Sharpy Plus product page](https://www.claypaky.it/products/sharpy-plus/) — firmware upgrade via Web Server (via search summary)
- Claypaky instruction manuals (Sharpy [manuals.plus copy](https://manuals.plus/m/0dc75ba9bd5c288c40aa1eb565a0d3d88973ac670f2f407b78f1e04c1552d923), [A.leda B-EYE K10/K20 user guide (cpl.tech)](https://www.cpl.tech/wp-content/uploads/2018/10/Clay-Paky-A-leda-B-EYE-K10-User-Guide.pdf), [Sharpy Plus (ManualsLib)](https://www.manualslib.com/manual/1637972/Claypaky-Sharpy-Plus.html)) — Upload Firmware copies firmware from one fixture to the others on the line, same model only, 5/6 units at a time max (via search summary; the exact manual page wasn't pinned)
- [B&H: Claypaky C61206 Firmware Uploader USB/DMX interface](https://www.bhphotovideo.com/c/product/1827391-REG/claypaky_c61206_firmware_uploader_usb_dmx_interfacefor.html), [Lightspares: Claypaky Firmware Uploader Kit USB/DMX](https://lightspares.com/claypaky-firmware-uploader-kit-usbdmx-010-074) — the interface exists (retail listings; listed for Alpha-series fixtures)
- [Claypaky CloudIO Instruction Manual 01.2020 (visiontwo.de)](https://www.visiontwo.de/fileadmin/user_upload/Claypaky_CloudIO_Manual_01.2020.pdf), [06.2022 (ltb.no)](https://ltb.no/media/multicase/documents/claypaky/manual_claypaky_cloudio_06.2022.pdf), [CloudIO product page](https://www.claypaky.it/products/cloudio/) — Fixture Firmware Uploader app, `.img` on USB-key root, up to 31 lights on its DMX line, offline use (via search summary)
- Claypaky Tech Corner videos (titles only, not watched): [Firmware Update with FUL Uploader](https://www.youtube.com/watch?v=hyeRWUqLlTk), [Firmware Update with Web Server](https://www.youtube.com/watch?v=Jp4SJ3HJ9N4), [Firmware Update from Fixture to Fixture](https://www.youtube.com/watch?v=xGVPVCwnRPg)
