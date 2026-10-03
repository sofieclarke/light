---
title: "GLP impression X4 / X4 S / X4 L"
manufacturer: "GLP (German Light Products)"
model: "impression X4 (family: X4, X4 S, X4 L)"
aliases: ["x4", "impression x4", "glp x4", "x4 s", "x4s", "x4 small", "x4 l", "x4l", "x4 large", "impression x4 s", "impression x4 l"]
type: "wash"
light_source: null
ip_rating: null
weight_lb: null
weight_kg: null
dimensions: ""
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
  connectors: ""
  protocols: []
  modes: []
menu_password: null
firmware:
  latest_known: null
  checked: "2026-10-03"
  check_on_fixture: "Not found — the manual is labelled 'from software version 1.18/18/12/10/n'"
  methods: ["DMX link with GLP D3Prog ⚠️", "GLP iQ.Service Portal (X4 L file source)"]
  interface: "GLP D3Prog (USB/Sub-D 9 to PC; 5-pin + 3-pin XLR out) ⚠️"
  software: "D3Prog PC transfer (software name not found)"
  file_type: ".hex (Intel hex) or .bin, depending on firmware version ⚠️"
  download: "glp.de product page → Downloads, or GLP iQ.Service Portal; also germanlightproducts.com/downloads"
tools: []
verification: "unverified"
last_updated: "2026-10-03"
---

# GLP impression X4 / X4 S / X4 L

> **STUB — research cut short.** The web-search budget ran out before this page could be sourced. **No numbers on this page are verified.** Fill it in from the fixture or the manual links below.

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** Not found. On the GLP X4 *Bar*, Mode + Enter + Up toggles the key lock. That may carry over ⚠️ unverified.
> - **Power:** Not found. Read the label on the fixture. Don't guess.
> - **DMX:** Not found. Check the mode against the software version shown on the display.
> - **Won't move?** Look for pan/tilt locks. Locations: Not found.
> - **Tools:** TBD – check on next show

## Identity
- What crews call it: "X4", "X4 S" (small), "X4 L" (large) (general knowledge).
- Variants and how to tell them apart: all three are RGBW LED moving-head washes with zoom. The **X4 S** is the small/light one, the **X4** is the standard size, and the **X4 L** is the large one with more LEDs. A row/ring count on the front lens array tells them apart (general knowledge ⚠️ unverified). Counts: Not found — fill in from the fixture.
- The X4 *Bar* 10/20 is a different fixture (a tilt-only batten). See [impression-x4-bar-20.md](impression-x4-bar-20.md).
- Fixture library / profile names: Not found.

---

## impression X4 S
### Passwords, menu locks & hidden menus
- Not found — fill in from the fixture.
### Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found | Not found | Not found |
| Power (W) | Not found | | |
| Max power-link (manufacturer) | Not found | | |
| **Max per 20 A circuit** | — | — | — |
### Data & addressing
- Not found — fill in from the fixture.
### Rigging & hardware
- Not found — fill in from the fixture.

## impression X4 (standard)
### Passwords, menu locks & hidden menus
- Not found — fill in from the fixture.
### Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found | Not found | Not found |
| Power (W) | Not found | | |
| Max power-link (manufacturer) | Not found | | |
| **Max per 20 A circuit** | — | — | — |
### Data & addressing
- Manual found: "Instruction Manual from software version 1.18/18/12/10/n" (link below). Contents not retrieved.

## impression X4 L
### Passwords, menu locks & hidden menus
- Not found — fill in from the fixture.
### Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found | Not found | Not found |
| Power (W) | Not found | | |
| Max power-link (manufacturer) | Not found | | |
| **Max per 20 A circuit** | — | — | — |
### Data & addressing
- Not found — fill in from the fixture.

---

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD |
| Gobo / effects module access | n/a (LED wash) | — |
| Lens / front glass | TBD – check on next show | TBD |
| Omega bracket | TBD – check on next show | TBD |

## Optics & consumables
- RGBW LED wash with zoom (general knowledge). Zoom range, LED count, CTO: Not found.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Not found | | |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Not found | | |

## Maintenance
- Recalibrate / reset and fan / filter cleaning: Not found — fill in from the fixture.

## Firmware
- Installed version — where to see it on the fixture: Not found. The X4 manual is labelled "from software version **1.18/18/12/10/n**", which suggests several separate processor firmwares (main and sub-boards) ⚠️ interpretation.
- Latest known version (date checked) and where to download it: **Not found** (checked 2026-10-03). The glp.de X4 page has a firmware download dated **2014-08-20**. The X4 L page points to the **iQ.Service Portal** for the latest firmware. GLP also publishes an "impression X4 Software Update Manual" and "impression X4S Software Update Instructions" (germanlightproducts.com, not read). **Read those before updating:** they're the model-specific procedure.
- What you need:
  - **GLP D3Prog** (GLP's firmware programmer). Load the firmware into one of its memory slots from a PC over **USB (Type B)** or **Sub-D 9**, then plug it into the fixture's DMX in. It has **both 5-pin and 3-pin female XLR**, so no adapter needed. Runs on 2x 1.2 V Mignon (AA) rechargeables, so it works with no mains near it (glp.de). Retail part no. **9506** is listed for the "D-Prog" uploader ⚠️ (may be the older model). ⚠️ not confirmed by name for the X4 family in what was found.
  - USB port / Art-Net update: Not found.
- Update steps:
  1. On the PC, import the firmware into a D3Prog memory slot. Pick file type **Intel hex** or **BIN** to match the firmware file (GLP tech note, via search summary).
  2. **Unplug the console and anything else on the line that you aren't updating.** GLP says no other DMX receivers or consoles may be active (tech note, via search summary).
  3. D3Prog XLR out → DMX in of the first fixture, daisy-chain the rest. Fixtures powered.
  4. Choose the slot on the D3Prog and start the upload. The button sequence on the D3Prog: Not found.
  5. Don't power-cycle until it reports done ⚠️ (general practice), then check the version on each fixture.
- Updating a whole rig: D3Prog updates several fixtures on one DMX line at once (glp.de). **X4, X4 S and X4 L are different models with separate update documents: update each model on its own line** ⚠️. Per-line maximum: Not found.
- If it fails or bricks mid-update (recovery mode): Not found. The D3Prog can also program via AVR/ISP (service level). Contact support@glp.de.
- Release notes worth knowing: Not found.

## Road notes (community)
- PLSN did a road test of the impression X4 (link below); its content wasn't retrieved.

## Sources
- [impression X4 Instruction Manual v1.0 (SW 1.18/18/12/10/n) — Christie Lites mirror](https://www.christielites.com/file_uploads/Impression_X4_v1_0_User-Manual-EN.pdf) — found, not read
- [Same manual, GLP mirror](https://www.germanlightproducts.com/wp-content/uploads/2018/11/Impression_X4_v1_0_User-Manual-EN_080221.pdf) — found, not read
- [PLSN road test: GLP impression X4](https://plsn.com/articles/road-tests/glp-impression-x4-1/) — found, not read
- [GLP impression X4 product page](https://glp.de/en/products/entertainment-lighting/moving-lights/impression-x4-en) — X4 firmware download dated 2014-08-20; [impression X4 L product page](https://glp.de/en/products/entertainment-lighting/moving-lights/impression-x4-l-en) — latest firmware via iQ.Service Portal (via search summary)
- [impression X4 Software Update Manual](https://www.germanlightproducts.com/download/impression-x4-software-update-manual/) and [impression X4S Software Update Instructions](https://www.germanlightproducts.com/download/impression-x4s-software-update-instructions/) (germanlightproducts.com) — exist, not read
- [GLP D3Prog product page (glp.de)](https://glp.de/en/products/service-firmware/service-tools/d3prog-en) — D3Prog: USB / Sub-D 9 to PC, memory slots, DMX link or AVR/ISP output, XLR 5- and 3-pin female, 2x 1.2 V Mignon batteries, several fixtures at once (via search summary)
- GLP Tech News [2019/10/30](https://www.glp.de/en/service/tech-info-archive/archive/80-glp-tech-news-2019-10-30?tmpl=component) and [2019/01/14](https://www.glp.de/en/service/tech-info-archive/archive/73-glp-tech-news-2019-01-14) — hex vs BIN file type when importing to the D3Prog, daisy-chain via DMX with no other receivers or consoles active (via search summary; which note said what wasn't pinned)
- [GoKnight: GLP 9506 D-Prog Uploader](https://goknight.com/german-light-products-9506-d-prog-uploader/), [Solotech: GLP 9506 D-Prog Firmware Uploader](https://shop.solotech.com/products/glp-9506-d-prog-firmware-uploader) — retail part number 9506 (D-Prog; may be the older model, not D3Prog)
