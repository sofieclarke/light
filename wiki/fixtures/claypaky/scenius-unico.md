---
title: "Claypaky Scenius Unico"
manufacturer: "Claypaky"
model: "Scenius Unico"
aliases: ["scenius unico", "unico", "scenius", "claypaky scenius unico"]
type: "profile"
light_source: "Osram Lok-it! HTI 1400/PS discharge, 6000 K (community data); lamp control offers 1200 W and 1400 W modes"
ip_rating: null
weight_lb: 100.5
weight_kg: 45.6
dimensions: "approx. 360 x 803 x 410 mm (W x H x D, QLC+ community data)"
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
  per_20a_120v: 1
  per_20a_208v: null
  fuse: ""
dmx:
  connectors: "5-pin XLR (community data)"
  protocols: ["DMX"]
  modes:
    - { name: "Standard", channels: 40 }
    - { name: "Vector", channels: 44 }
menu_password: null
firmware:
  latest_known: null
  checked: "2026-10-03"
  check_on_fixture: "Not found — likely the Information menu ⚠️"
  methods: ["Fixture-to-fixture over DMX (Upload Firmware)", "PC + Claypaky Firmware Uploader USB/DMX interface ⚠️", "CloudIO Box + USB stick ⚠️ compatibility unverified"]
  interface: "None for fixture-to-fixture; Claypaky Firmware Uploader USB/DMX interface ⚠️ for PC updates"
  software: "Claypaky FUL Uploader ⚠️ (name from a Claypaky video title)"
  file_type: ".img (CloudIO USB-stick update); other methods: Not found"
  download: "Claypaky Customer Care site (service.claypaky.it, restricted login) — ask your Claypaky distributor / rental house"
tools: []
verification: "community"
last_updated: "2026-10-03"
---

# Claypaky Scenius Unico

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** not sourced. The Claypaky line Advanced code is **1234** ⚠️ unverified for Unico.
> - **Power:** manufacturer amps not found. The lamp alone runs at up to **1400 W**, so 1400/120 = 11.7 A **minimum** → **1 per 20 A circuit @120 V**. At 208 V, the lamp alone is ≥6.7 A, so **1-2 per 20 A**. Read the label before doubling up. (QLC+ lists "1200 W", which is below the lamp's own 1400 W mode and must be too low.)
> - **DMX:** Standard **40** / Vector **44**. Lamp Control: 26-100 OFF, **101-179 ON @1200 W (quiet fans)**, **180-255 ON @1400 W**.
> - **Weight:** about 45.6 kg / 100 lb. Two-person lift.
> - **Tools:** TBD – check on next show

## Identity
- What crews call it: "Unico", "Scenius". A framing profile with CMY, iris, animation, autofocus and 4-blade framing.
- Fixture library / profile names: Standard (40), Vector (44, adds timing channels; Vector convention per Claypaky line).
- Variants: Scenius Spot / Scenius Profile are siblings (not covered here).

## Passwords, menu locks & hidden menus
- Not found — fill in from the fixture. See [_claypaky-common.md](_claypaky-common.md).

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found. Lamp alone ≥11.7 A (1400/120) ⚠️ | Not found. Lamp alone ≥6.7 A (1400/208) ⚠️ | Not found |
| Power (W) | Lamp 1200 W or 1400 W selectable (DMX chart). Whole fixture: Not found | — | — |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | floor(16/11.7)=1 → **1** (lower bound on draw, so this is a ceiling) | floor(16/6.7)=2 is a ceiling only; real draw is higher → **1-2, check label** ⚠️ | — |

- Input range / connectors / fuse: Not found — fill in from the fixture.
- Running the lamp at 1200 W (Lamp Control 101-179) also reduces fan noise (DMX chart). Good for theatre.

## Data & addressing
- Connectors: 5-pin XLR (community).
- DMX Standard 40 (QLC+): Cyan, Magenta, Yellow, CTO, Colour Wheel, Stopper/Strobe, Dimmer, Dimmer fine, Iris, Animation insert, Animation rot, Rotating Gobo, Gobo Rot, Gobo Rot fine, Prism insert, Prism rot, Light Frost, Blades 1A/1B/2A/2B/3A/3B/4A/4B, Framing Rotation, Focus, Focus fine, Zoom, Autofocus Distance, Autofocus Adjustment, Pan, Pan fine, Tilt, Tilt fine, Function, Reset, Lamp Control, Heavy Frost, Uniform Beam Field.
- Control values (QLC+): Reset 26-76 zoom, 77-127 pan/tilt, 128-255 complete. Function 38-50 conventional dimmer curve.
- Set the address / battery addressing: Not found.

## Rigging & hardware
- Not found — fill in from the fixture (omega, safety point, transport locks).
- Weight 45.6 kg. Pan 540°, tilt 270° (QLC+).

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD – check on next show |
| Gobo / effects module access | TBD – check on next show | TBD – check on next show |
| Lens / front glass | TBD – check on next show | TBD – check on next show |
| Omega bracket | TBD – check on next show | TBD – check on next show |

## Optics & consumables
- Source / lamp: Osram Lok-it! HTI 1400/PS, 6000 K, ~120,000 lm claimed (QLC+ community) ⚠️. Lamp life: Not found.
- Color: CMY + CTO + colour wheel. Iris. Animation disc. Rotating gobos. Prism. Light frost + heavy frost. 4-blade framing with rotation. Zoom 5-55°. Autofocus.
- Gobo size: Not found.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Not found — fill in from the fixture | | |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Breaker trips when two units share a 120 V circuit | 1400 W lamp: one per 20 A at 120 V | Re-circuit |
| Lamp won't strike from desk | Lamp Control channel not at ON value | Send 101-179 (1200 W) or 180-255 (1400 W) |

## Maintenance
- Recalibrate / reset and fan / filter cleaning: Not found — fill in from the fixture.

## Firmware
- Installed version — where to see it on the fixture: Not found — probably in the Information menu ⚠️. Fill in from the fixture.
- Latest known version (date checked) and where to download it: **Not found** (checked 2026-10-03). Claypaky doesn't publish version numbers openly. Files live on the restricted **Claypaky Customer Care** site (service.claypaky.it). Ask your distributor or the rental house's service department, and write the version you find here.
- Update features Claypaky lists for this model: **firmware upload from another fixture** (Scenius Unico datasheet). Web Server update isn't listed in what was found. **Scenius Spot / Profile are different models: don't mix them with Unico on the update line** ⚠️.
- What you need:
  - **Fixture-to-fixture (no PC):** one Scenius Unico already on the version you want, plus a DMX cable to the others. DMX connector type: see Data & addressing.
  - **From a PC:** Claypaky's **Firmware Uploader USB/DMX interface** (retail listings: "Firmware Uploader Kit USB/DMX", part **C61206** listed for the Alpha 1500). ⚠️ unverified which kit and which PC software suit this model. Claypaky's own Tech Corner video calls the PC tool **"FUL Uploader"** (video title only).
  - **CloudIO / CloudIO Box (CA8001):** copy the `.img` firmware file to the **root** of a USB stick, plug it into the CloudIO, open **Fixture Firmware Uploader**, press **CONTINUE**. Every compatible Claypaky fixture on its DMX OUT updates (CloudIO manual). ⚠️ unverified whether this model is on CloudIO's compatible list. USB stick format: Not found.
- Update steps (fixture-to-fixture, Advanced menu; menu path from Claypaky manuals):
  1. Unplug the console from the DMX line ⚠️ (general practice). Leave only fixtures of **the same model** on the line.
  2. Run DMX from the Scenius Unico that has the wanted firmware into the first fixture to update, and daisy-chain the rest.
  3. On the source fixture: menu → **Advanced** → enter access code **1234** → **Upload Firmware** → confirm.
  4. Don't touch or power-cycle anything until it finishes ⚠️ (general practice). Then check the version on every target (see above).
- Updating a whole rig: **same model only**, and Claypaky recommends **5–6 units at a time maximum** for fixture-to-fixture (manual, via search summary). CloudIO handles up to 31 lights on one DMX line (CloudIO page). Art-Net / sACN firmware update: Not found.
- If it fails or bricks mid-update (recovery mode): **Not found.** No bootloader or recovery procedure was found. Retry from a known-good fixture of the same model, then call Claypaky service. See [_claypaky-common.md](_claypaky-common.md#firmware-updates).
- Release notes worth knowing: Not found. A firmware change can add or renumber DMX modes, so check your console profile against the fixture's mode list after any update.

## Road notes (community)
- None sourced. Add your own.

## Sources
- QLC+ Clay-Paky-Scenius-Unico.qxf (github.com/mcallegari/qlcplus, commit 1ccdab8) — modes, channel order, lamp control 1200/1400 W values, weight, dims, lamp type (community)
- Note: the shared web-search budget ran out before this fixture was searched. No manufacturer-derived figures. Verify all against the label and manual.
- [Scenius Unico datasheet (proscene.ch)](https://www.proscene.ch/data/web/proscene.ch/uploads/database/L10010/scenius_unico_.pdf) — firmware upload from another fixture (via search summary)
- Claypaky instruction manuals (Sharpy [manuals.plus copy](https://manuals.plus/m/0dc75ba9bd5c288c40aa1eb565a0d3d88973ac670f2f407b78f1e04c1552d923), [A.leda B-EYE K10/K20 user guide (cpl.tech)](https://www.cpl.tech/wp-content/uploads/2018/10/Clay-Paky-A-leda-B-EYE-K10-User-Guide.pdf), [Sharpy Plus (ManualsLib)](https://www.manualslib.com/manual/1637972/Claypaky-Sharpy-Plus.html)) — Upload Firmware copies firmware from one fixture to the others on the line, same model only, 5/6 units at a time max (via search summary; the exact manual page wasn't pinned)
- [B&H: Claypaky C61206 Firmware Uploader USB/DMX interface](https://www.bhphotovideo.com/c/product/1827391-REG/claypaky_c61206_firmware_uploader_usb_dmx_interfacefor.html), [Lightspares: Claypaky Firmware Uploader Kit USB/DMX](https://lightspares.com/claypaky-firmware-uploader-kit-usbdmx-010-074) — the interface exists (retail listings; listed for Alpha-series fixtures)
- [Claypaky CloudIO Instruction Manual 01.2020 (visiontwo.de)](https://www.visiontwo.de/fileadmin/user_upload/Claypaky_CloudIO_Manual_01.2020.pdf), [06.2022 (ltb.no)](https://ltb.no/media/multicase/documents/claypaky/manual_claypaky_cloudio_06.2022.pdf), [CloudIO product page](https://www.claypaky.it/products/cloudio/) — Fixture Firmware Uploader app, `.img` on USB-key root, up to 31 lights on its DMX line, offline use (via search summary)
- Claypaky Tech Corner videos (titles only, not watched): [Firmware Update with FUL Uploader](https://www.youtube.com/watch?v=hyeRWUqLlTk), [Firmware Update with Web Server](https://www.youtube.com/watch?v=Jp4SJ3HJ9N4), [Firmware Update from Fixture to Fixture](https://www.youtube.com/watch?v=xGVPVCwnRPg)
