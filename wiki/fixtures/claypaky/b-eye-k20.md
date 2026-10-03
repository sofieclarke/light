---
title: "Claypaky A.leda B-EYE K20"
manufacturer: "Claypaky"
model: "A.leda B-EYE K20"
aliases: ["b-eye k20", "beye k20", "b eye", "k20", "a.leda b-eye k20", "b-eye", "beye"]
type: "beam-wash"
light_source: "LED 37x Osram Ostar 15W RGBW (LED count derived from pixel-mode footprint; LED type per Open Fixture Library)"
ip_rating: null
weight_lb: 46.3
weight_kg: 21
dimensions: "approx. 395 x 476 x 330 mm (OFL); QLC+ lists height 589 mm"
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
  connectors: "3-pin and 5-pin XLR (community data)"
  protocols: ["DMX"]
  modes:
    - { name: "Standard", channels: 21 }
    - { name: "Shapes", channels: 35 }
    - { name: "Extended RGB", channels: 132 }
    - { name: "Extended RGBW", channels: 169 }
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

# Claypaky A.leda B-EYE K20

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** not sourced for this model. The Claypaky line Advanced code is **1234** ⚠️ unverified for B-EYE.
> - **Power:** manufacturer amps not found. Community max-power figures **disagree**: 750 W (QLC+) vs 555 W (Open Fixture Library). Worst case 750/120 ≈ 6.3 A → **2 per 20 A @120 V**. At 208 V, 750/208 ≈ 3.6 A → **4** ⚠️ derived from community data. Read the label.
> - **DMX:** Standard 21 / Shapes 35 / Extended RGB 132 / Extended RGBW 169. Reset ch: 128-255 complete, 77-127 pan/tilt, 26-76 zoom.
> - **K10 vs K20:** K10 = 19 LEDs, ~14.5-15 kg. K20 = 37 LEDs, 21 kg. Same 21/35-ch base modes.
> - **Tools:** TBD – check on next show

## Identity
- What crews call it: "B-EYE", "B-Eye K20", "K20". Full name A.leda B-EYE K20.
- Fixture library / profile names: Standard (21), Shapes (35), Extended RGB / Extended RGBW pixel modes (QLC+).
- **K10 / K15 / K20 differences:**
  - **K10:** 19 LEDs (pixel modes 78 = 21+19x3, 97 = 21+19x4). 14.5 kg (QLC+) or 15 kg (OFL). 358 x 494 x 253 mm. Rated 450 W (both community sources). ~5500 lm (QLC+). Same Standard 21 / Shapes 35 modes.
  - **K20:** 37 LEDs (132 = 21+37x3, 169 = 21+37x4). 21 kg. ~9800 lm (both community sources).
  - **K15:** not found as an A.leda B-EYE in the sources. QLC+ has an **HY B-EYE K15**, which is a different hybrid fixture: 20 kg, rated 600 W, modes Standard 21 / Shapes 35 / RGB 57 / RGBW 76, 4-60° (community). Confirm which "K15" you're looking at from the label.
- Both K10 and K20 zoom 4-60°. Pan 540°, tilt 210° (QLC+).

## Passwords, menu locks & hidden menus
- Not found — fill in from the fixture. See [_claypaky-common.md](_claypaky-common.md) for line conventions (Advanced code 1234 on other models).

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found. ≈6.3 A derived from 750 W (QLC+) / ≈4.6 A from 555 W (OFL) ⚠️ | Not found. ≈3.6 A / ≈2.7 A derived ⚠️ | Not found |
| Power (W) | 750 W (QLC+) vs 555 W (OFL), conflicting community data | — | — |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | Worst case floor(16/6.3)=2 → **2** ⚠️ | Worst case floor(16/3.6)=4 → **4** ⚠️ | — |

- Input range / connectors / fuse: Not found — fill in from the fixture.

## Data & addressing
- Connectors: 3-pin and 5-pin XLR (community).
- DMX modes: Standard 21 = R, R fine, G, G fine, B, B fine, W, W fine, Linear CTO, Macro Color, Strobe, Dimmer, Dimmer fine, Pan, Pan fine, Tilt, Tilt fine, Function, Reset, Zoom, Zoom Rotation (QLC+; "Zoom Rotation" is the front-lens "B-EYE" rotation effect).
- Control values (QLC+): Reset 26-76 zoom reset, 77-127 pan/tilt, 128-255 complete. Function 73-77 halogen lamp simulation off (default).
- Set the address / battery addressing: Not found.

## Rigging & hardware
- Not found — fill in from the fixture (omega, safety point, transport locks).
- Weight 21 kg (K20), 14.5-15 kg (K10).

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD – check on next show |
| Gobo / effects module access | n/a (no gobos) | — |
| Lens / front glass | TBD – check on next show | TBD – check on next show |
| Omega bracket | TBD – check on next show | TBD – check on next show |

## Optics & consumables
- Source: RGBW LEDs (OFL lists Osram Ostar 15 W RGBW). K20 37 cells, K10 19 cells.
- Color system: RGBW + linear CTO + colour macros.
- Zoom 4-60°. Rotating front lens ("Zoom Rotation" channel) for the B-EYE effects (general knowledge).

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Not found — fill in from the fixture | | |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Not found | | |

## Maintenance
- Recalibrate / reset and fan / filter cleaning: Not found — fill in from the fixture.

## Firmware
- Installed version — where to see it on the fixture: Not found — probably in the Information menu ⚠️. Fill in from the fixture.
- Latest known version (date checked) and where to download it: **Not found** (checked 2026-10-03). Claypaky doesn't publish version numbers openly. Files live on the restricted **Claypaky Customer Care** site (service.claypaky.it). Ask your distributor or the rental house's service department, and write the version you find here.
- Update features Claypaky lists for this model: firmware upgrade **without mains power** and **firmware transfer from one light to another** (Claypaky product page). The B-EYE K10/K20 user guide appears to be one of the manuals that limits fixture-to-fixture upload to the same model, 5–6 units at a time (via search summary).
- What you need:
  - **Fixture-to-fixture (no PC):** one B-EYE K20 already on the version you want, plus a DMX cable to the others. **K10 and K20 are different models: don't mix them on the update line** ⚠️ (they share a manual but have different LED counts).
  - **From a PC:** Claypaky's **Firmware Uploader USB/DMX interface** (retail listings: "Firmware Uploader Kit USB/DMX", part **C61206** listed for the Alpha 1500). ⚠️ unverified which kit and which PC software suit this model. Claypaky's own Tech Corner video calls the PC tool **"FUL Uploader"** (video title only).
  - **CloudIO / CloudIO Box (CA8001):** copy the `.img` firmware file to the **root** of a USB stick, plug it into the CloudIO, open **Fixture Firmware Uploader**, press **CONTINUE**. Every compatible Claypaky fixture on its DMX OUT updates (CloudIO manual). ⚠️ unverified whether this model is on CloudIO's compatible list. USB stick format: Not found.
- Update steps (fixture-to-fixture, Advanced menu; menu path from Claypaky manuals):
  1. Unplug the console from the DMX line ⚠️ (general practice). Leave only fixtures of **the same model** on the line.
  2. Run DMX from the B-EYE K20 that has the wanted firmware into the first fixture to update, and daisy-chain the rest.
  3. On the source fixture: menu → **Advanced** → enter access code **1234** → **Upload Firmware** → confirm.
  4. Don't touch or power-cycle anything until it finishes ⚠️ (general practice). Then check the version on every target (see above).
- Updating a whole rig: **same model only**, and Claypaky recommends **5–6 units at a time maximum** for fixture-to-fixture (manual, via search summary). CloudIO handles up to 31 lights on one DMX line (CloudIO page). Art-Net / sACN firmware update: Not found.
- If it fails or bricks mid-update (recovery mode): **Not found.** No bootloader or recovery procedure was found. Retry from a known-good fixture of the same model, then call Claypaky service. See [_claypaky-common.md](_claypaky-common.md#firmware-updates).
- Release notes worth knowing: Not found. A firmware change can add or renumber DMX modes, so check your console profile against the fixture's mode list after any update.

## Road notes (community)
- None sourced. Add your own.

## Sources
- Open Fixture Library a-leda-b-eye-k20.json / a-leda-b-eye-k10.json (github.com/OpenLightingProject/open-fixture-library, commit 1424c7a) — weight, dimensions, 555 W / 450 W, LED type; manual link listed there: https://e-assist.tech/servlet/checkDocumentsFile?Id=729 (not reachable from here)
- QLC+ Clay-Paky-A.leda-B-EYE-K20.qxf, -K10.qxf, Clay-Paky-HY-B-EYE-K15.qxf (github.com/mcallegari/qlcplus, commit 1ccdab8) — modes and footprints, 750 W / 450 W / 600 W, weights, control values
- Note: the shared web-search budget ran out before this fixture was searched. No manufacturer-derived figures here. Verify everything against the label and manual.
- [Claypaky A.leda B-EYE K20 product page](https://www.claypaky.it/en/products/b-eye-k20) — firmware upgrade without mains power, firmware transfer from one light to another (via search summary)
- Claypaky instruction manuals (Sharpy [manuals.plus copy](https://manuals.plus/m/0dc75ba9bd5c288c40aa1eb565a0d3d88973ac670f2f407b78f1e04c1552d923), [A.leda B-EYE K10/K20 user guide (cpl.tech)](https://www.cpl.tech/wp-content/uploads/2018/10/Clay-Paky-A-leda-B-EYE-K10-User-Guide.pdf), [Sharpy Plus (ManualsLib)](https://www.manualslib.com/manual/1637972/Claypaky-Sharpy-Plus.html)) — Upload Firmware copies firmware from one fixture to the others on the line, same model only, 5/6 units at a time max (via search summary; the exact manual page wasn't pinned)
- [B&H: Claypaky C61206 Firmware Uploader USB/DMX interface](https://www.bhphotovideo.com/c/product/1827391-REG/claypaky_c61206_firmware_uploader_usb_dmx_interfacefor.html), [Lightspares: Claypaky Firmware Uploader Kit USB/DMX](https://lightspares.com/claypaky-firmware-uploader-kit-usbdmx-010-074) — the interface exists (retail listings; listed for Alpha-series fixtures)
- [Claypaky CloudIO Instruction Manual 01.2020 (visiontwo.de)](https://www.visiontwo.de/fileadmin/user_upload/Claypaky_CloudIO_Manual_01.2020.pdf), [06.2022 (ltb.no)](https://ltb.no/media/multicase/documents/claypaky/manual_claypaky_cloudio_06.2022.pdf), [CloudIO product page](https://www.claypaky.it/products/cloudio/) — Fixture Firmware Uploader app, `.img` on USB-key root, up to 31 lights on its DMX line, offline use (via search summary)
- Claypaky Tech Corner videos (titles only, not watched): [Firmware Update with FUL Uploader](https://www.youtube.com/watch?v=hyeRWUqLlTk), [Firmware Update with Web Server](https://www.youtube.com/watch?v=Jp4SJ3HJ9N4), [Firmware Update from Fixture to Fixture](https://www.youtube.com/watch?v=xGVPVCwnRPg)
