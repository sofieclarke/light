---
title: "Claypaky Sharpy X Frame"
manufacturer: "Claypaky"
model: "Sharpy X Frame"
aliases: ["sharpy x frame", "sharpy xframe", "x frame", "xframe", "claypaky sharpy x frame"]
type: "hybrid"
light_source: "Discharge 550 W, 8000 K (retailer listing); QLC+ wrongly lists LED"
ip_rating: null
weight_lb: 61.7
weight_kg: 28
dimensions: "approx. 350 x 668 x 306 mm (W x H x D, QLC+ community data)"
power:
  input: ""
  connector_in: ""
  connector_out: ""
  watts_max: null
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
  connectors: "5-pin XLR (community data)"
  protocols: ["DMX"]
  modes:
    - { name: "Standard", channels: 43 }
menu_password: null
firmware:
  latest_known: null
  checked: "2026-10-03"
  check_on_fixture: "Not found — likely the Information menu ⚠️"
  methods: ["Web Server over Ethernet (RJ45)", "Fixture-to-fixture over DMX (Advanced → Upload Firmware) ⚠️ family pattern", "CloudIO Box + USB stick ⚠️ compatibility unverified"]
  interface: "None for Web Server; Claypaky Firmware Uploader USB/DMX interface ⚠️ for PC-over-DMX"
  software: "Web browser (built-in web server); Claypaky FUL Uploader ⚠️"
  file_type: ".img (CloudIO USB-stick update); other methods: Not found"
  download: "Claypaky Customer Care site (service.claypaky.it, restricted login) — ask your Claypaky distributor / rental house"
tools: []
verification: "community"
last_updated: "2026-10-03"
---

# Claypaky Sharpy X Frame

(I chose this over the Skylos because the Sharpy X Frame is a touring framing hybrid. The Skylos is a large outdoor sky-beam fixture, much rarer on tour rigs. That choice is general knowledge.)

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** not sourced. The Claypaky line Advanced code is **1234** ⚠️ unverified for X Frame.
> - **Power:** manufacturer amps not found. The 550 W lamp alone is 4.6 A @120 V, so **no more than 3 per 20 A @120 V** and **no more than 6 @208 V** (2.6 A). The whole fixture draws more, so plan **2 @120 V** until you've read the label ⚠️.
> - **DMX:** Standard **43 ch** (community). Lamp Control 26-100 OFF / 101-255 ON. Reset 128-255 complete.
> - **Display stays dark?** Function ch 171-180 = Display ON, 161-170 = Display OFF (default) (community profile).
> - **Tools:** TBD – check on next show

## Identity
- What crews call it: "X Frame", "Sharpy X Frame". Sibling of Sharpy X Spot (no framing).
- Fixture library / profile names: Standard 43 (QLC+). Other modes: Not found.

## Passwords, menu locks & hidden menus
- Not found — fill in from the fixture. See [_claypaky-common.md](_claypaky-common.md).

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found. Lamp alone ≈4.6 A (550/120) ⚠️ | Not found. Lamp alone ≈2.6 A ⚠️ | Not found |
| Power (W) | Lamp 550 W. Fixture total: Not found | — | — |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | ceiling floor(16/4.6)=3 (real draw higher) → **≤3, plan 2** ⚠️ | ceiling floor(16/2.6)=6 → **≤6** ⚠️ | — |

- Input range / connectors / fuse: Not found — fill in from the fixture.

## Data & addressing
- Connectors: 5-pin XLR (community).
- DMX Standard 43 (QLC+): Cyan, Magenta, Yellow, CTO, Colour Function, Full Color, Strobe, Dimmer, Dimmer fine, Iris, Static Gobo, Animation insert, Animation rot, Rotating Gobo, Gobo Rot, Gobo Rot fine, 4-facet prism in/rot, 8-facet prism in/rot, Frost, Zoom, Focus, Focus fine, Beam mode, Blade 1-4 movement + swivel (8 ch), Framing Rotation, Framing Macro, Framing Macro speed, Pan, Pan fine, Tilt, Tilt fine, Function, Reset, Lamp Control.
- Control values (QLC+): Reset 26-76 effects, 77-127 pan/tilt, 128-255 complete. Function 161-170 display off (default), 171-180 display on, 181-190 framing dimming delay on, 191-200 off (default). Lamp 26-100 off, 101-255 on.
- Address / battery addressing: Not found.

## Rigging & hardware
- Not found — fill in from the fixture.
- Weight 28 kg. Pan 540°, tilt 270° (QLC+).

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD – check on next show |
| Gobo / effects module access | TBD – check on next show | TBD – check on next show |
| Lens / front glass | TBD – check on next show | TBD – check on next show |
| Omega bracket | TBD – check on next show | TBD – check on next show |

## Optics & consumables
- Source: 550 W discharge, 8000 K (Farralane listing). ~18,800 lm (QLC+). Lamp model and life: Not found.
- Zoom: 2-52° (Farralane) vs 3-52° (QLC+).
- CMY, CTO, colour wheel, static and rotating gobos, animation wheel, 4- and 8-facet prisms, frost, iris, 4-blade framing with rotation.
- Gobo size: Not found.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Not found — fill in from the fixture | | |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Lamp won't strike from desk | Lamp Control not at ON | Send 101-255 |
| Display dark during show | Display-off function set (default) | Function 171-180 → display on |

## Maintenance
- Recalibrate / reset and fan / filter cleaning: Not found — fill in from the fixture.

## Firmware
- Installed version — where to see it on the fixture: Not found — probably in the Information menu like the rest of the Sharpy line ⚠️. Fill in from the fixture.
- Latest known version (date checked) and where to download it: **Not found** (checked 2026-10-03). Claypaky doesn't publish version numbers openly. Files live on the restricted **Claypaky Customer Care** site (service.claypaky.it). Ask your distributor or the rental house's service department, and write the version you find here.
- Update features Claypaky lists for this model: **built-in web server** with "firmware upgrade via Web Server" and an RJ45 Ethernet port (Claypaky product page). Fixture-to-fixture upload isn't stated for this model, so the steps below are the Claypaky family pattern ⚠️.
- What you need:
  - **Fixture-to-fixture (no PC):** one Sharpy X Frame already on the version you want, plus a DMX cable to the others. DMX connector type: Not found.
  - **From a PC:** Claypaky's **Firmware Uploader USB/DMX interface** (retail listings: "Firmware Uploader Kit USB/DMX", part **C61206** listed for the Alpha 1500). ⚠️ unverified which kit and which PC software suit this model. Claypaky's own Tech Corner video calls the PC tool **"FUL Uploader"** (video title only).
  - **Web Server (Ethernet):** the Sharpy X Frame has a built-in web server and Claypaky lists "firmware upgrade via Web Server" (product page). Laptop on the fixture's RJ45, browser to the fixture. The exact steps and IP aren't sourced: see the Tech Corner "Firmware Update with Web Server" video.
  - **CloudIO / CloudIO Box (CA8001):** copy the `.img` firmware file to the **root** of a USB stick, plug it into the CloudIO, open **Fixture Firmware Uploader**, press **CONTINUE**. Every compatible Claypaky fixture on its DMX OUT updates (CloudIO manual). ⚠️ unverified whether this model is on CloudIO's compatible list. USB stick format: Not found.
- Update steps (fixture-to-fixture, Advanced menu; menu path from Claypaky manuals):
  1. Unplug the console from the DMX line ⚠️ (general practice). Leave only fixtures of **the same model** on the line.
  2. Run DMX from the Sharpy X Frame that has the wanted firmware into the first fixture to update, and daisy-chain the rest.
  3. On the source fixture: menu → **Advanced** → enter access code **1234** → **Upload Firmware** → confirm.
  4. Don't touch or power-cycle anything until it finishes ⚠️ (general practice). Then check the version on every target (see above).
- Updating a whole rig: **same model only**, and Claypaky recommends **5–6 units at a time maximum** for fixture-to-fixture (manual, via search summary). CloudIO handles up to 31 lights on one DMX line (CloudIO page). Art-Net / sACN firmware update: Not found.
- If it fails or bricks mid-update (recovery mode): **Not found.** No bootloader or recovery procedure was found. Retry from a known-good fixture of the same model, then call Claypaky service. See [_claypaky-common.md](_claypaky-common.md#firmware-updates).
- Release notes worth knowing: Not found. A firmware change can add or renumber DMX modes, so check your console profile against the fixture's mode list after any update.

## Road notes (community)
- None sourced. Add your own.

## Sources
- QLC+ Clay-Paky-Sharpy-X-Frame.qxf (github.com/mcallegari/qlcplus, commit 1ccdab8) — 43-ch mode, channel order, control values, weight, dims (community; its "LED" bulb field is wrong: the profile has a Lamp Control channel)
- [Farralane: Clay Paky Sharpy X Frame 550W discharge](https://www.farralane.com/clay-paky-sharpy-x-frame-550w-discharge-moving-head-spot-beam-hybrid-in-black-finish.html) — 550 W, 8000 K, 2-52° zoom (title via search)
- [Claypaky Sharpy X Frame product page](https://www.claypaky.it/products/sharpy-xframe/) — exists (no figures extracted)
- Note: the shared web-search budget ran out before this fixture was searched in depth.
- [Claypaky Sharpy X Frame product page](https://www.claypaky.it/products/sharpy-xframe/) — built-in web server, firmware upgrade via Web Server, RJ45 (via search summary)
- Claypaky instruction manuals (Sharpy [manuals.plus copy](https://manuals.plus/m/0dc75ba9bd5c288c40aa1eb565a0d3d88973ac670f2f407b78f1e04c1552d923), [A.leda B-EYE K10/K20 user guide (cpl.tech)](https://www.cpl.tech/wp-content/uploads/2018/10/Clay-Paky-A-leda-B-EYE-K10-User-Guide.pdf), [Sharpy Plus (ManualsLib)](https://www.manualslib.com/manual/1637972/Claypaky-Sharpy-Plus.html)) — Upload Firmware copies firmware from one fixture to the others on the line, same model only, 5/6 units at a time max (via search summary; the exact manual page wasn't pinned)
- [B&H: Claypaky C61206 Firmware Uploader USB/DMX interface](https://www.bhphotovideo.com/c/product/1827391-REG/claypaky_c61206_firmware_uploader_usb_dmx_interfacefor.html), [Lightspares: Claypaky Firmware Uploader Kit USB/DMX](https://lightspares.com/claypaky-firmware-uploader-kit-usbdmx-010-074) — the interface exists (retail listings; listed for Alpha-series fixtures)
- [Claypaky CloudIO Instruction Manual 01.2020 (visiontwo.de)](https://www.visiontwo.de/fileadmin/user_upload/Claypaky_CloudIO_Manual_01.2020.pdf), [06.2022 (ltb.no)](https://ltb.no/media/multicase/documents/claypaky/manual_claypaky_cloudio_06.2022.pdf), [CloudIO product page](https://www.claypaky.it/products/cloudio/) — Fixture Firmware Uploader app, `.img` on USB-key root, up to 31 lights on its DMX line, offline use (via search summary)
- Claypaky Tech Corner videos (titles only, not watched): [Firmware Update with FUL Uploader](https://www.youtube.com/watch?v=hyeRWUqLlTk), [Firmware Update with Web Server](https://www.youtube.com/watch?v=Jp4SJ3HJ9N4), [Firmware Update from Fixture to Fixture](https://www.youtube.com/watch?v=xGVPVCwnRPg)
