---
title: "GLP JDC Line 1000"
manufacturer: "GLP (German Light Products)"
model: "JDC Line 1000"
aliases: ["jdc line", "jdc line 1000", "jdc line 1m", "jdc line 500"]
type: "strobe"
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
  latest_known: "1.0.0"
  checked: "2026-10-03"
  check_on_fixture: "Not found"
  methods: ["DMX link with GLP D3Prog"]
  interface: "GLP D3Prog (USB/Sub-D 9 to PC; 5-pin + 3-pin XLR out)"
  software: "D3Prog PC transfer (software name not found)"
  file_type: ".hex (Intel hex) or .bin, depending on firmware version ⚠️"
  download: "glp.de product page → Downloads, or GLP iQ.Service Portal; also germanlightproducts.com/downloads"
tools: []
verification: "unverified"
last_updated: "2026-10-03"
---

# GLP JDC Line 1000

> **STUB — research cut short.** The web-search budget ran out. The manual has been located (link below) but not read. **No numbers on this page are verified.**

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** Not found
> - **Power:** Not found. Read the fixture label. Don't guess. Don't assume it power-links: its sibling, the **JDC1, has no AC thru**.
> - **DMX:** Not found
> - **Won't move?** Not found. Look for a tilt lock before power-up.
> - **Tools:** TBD – check on next show

## Identity
- What crews call it: "JDC Line". It's a linear (1 m) strobe/wash batten built on the JDC idea: a white strobe line plus RGB, with motorized tilt (general knowledge ⚠️ unverified).
- Variants: the **JDC Line 500** is the half-length version (a manual for it exists, link below).
- Fixture library / profile names: Not found.

## Passwords, menu locks & hidden menus
- Not found — fill in from the fixture. For the JDC1 conventions (Service menu Key Code, battery display), see [jdc1.md](jdc1.md) and [_glp-common.md](_glp-common.md). ⚠️ Not confirmed for the Line.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found | Not found | Not found |
| Power (W) | Not found | | |
| Max power-link (manufacturer) | Not found | | |
| **Max per 20 A circuit** (16 A continuous) | — | — | — |

## Data & addressing
- Not found — fill in from the fixture.

## Rigging & hardware
- Not found — fill in from the fixture.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD |
| Gobo / effects module access | n/a | — |
| Lens / front glass | TBD – check on next show | TBD |
| Omega bracket | TBD – check on next show | TBD |

## Optics & consumables
- Not found.

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
- Installed version — where to see it on the fixture: Not found — fill in from the fixture.
- Latest known version (date checked) and where to download it: **1.0.0** (latest found, checked 2026-10-03): the JDC Line 1000 DMX Channel Index Rev 20240618-01 is titled "Firmware v. 1.0.0". Check glp.de for anything newer.
- What you need:
  - **GLP D3Prog** (GLP's firmware programmer). Load the firmware into one of its memory slots from a PC over **USB (Type B)** or **Sub-D 9**, then plug it into the fixture's DMX in. It has **both 5-pin and 3-pin female XLR**, so no adapter needed. Runs on 2x 1.2 V Mignon (AA) rechargeables, so it works with no mains near it (glp.de). Retail part no. **9506** is listed for the "D-Prog" uploader ⚠️ (may be the older model).
  - GLP: the JDC Line 1000 firmware update is done **via DMX link using the D3Prog** (via search summary).
  - USB port / Art-Net update / iQ.Service: Not found.
- Update steps:
  1. On the PC, import the firmware into a D3Prog memory slot. Pick file type **Intel hex** or **BIN** to match the firmware file (GLP tech note, via search summary).
  2. **Unplug the console and anything else on the line that you aren't updating.** GLP says no other DMX receivers or consoles may be active (tech note, via search summary).
  3. D3Prog XLR out → DMX in of the first fixture, daisy-chain the rest. Fixtures powered.
  4. Choose the slot on the D3Prog and start the upload. The button sequence on the D3Prog: Not found.
  5. Don't power-cycle until it reports done ⚠️ (general practice), then check the version on each fixture.
- Updating a whole rig: D3Prog updates several fixtures on one DMX line at once (glp.de). **Keep JDC Line 500s off a JDC Line 1000 update line** unless GLP says they share firmware ⚠️. Per-line maximum: Not found.
- If it fails or bricks mid-update (recovery mode): Not found. The D3Prog can also program via AVR/ISP (service level). Contact support@glp.de.
- Release notes worth knowing: Not found.

## Road notes (community)
- None retrieved.

## Sources
- [JDC Line 1000 User Manual Rev. 20220317-01](https://www.germanlightproducts.com/wp-content/uploads/2020/05/GLP-JDC-Line-1000-User-Manual-EN-Rev-20220317-01.pdf) — found, not read
- [JDC Line 500 manual, Rev. 20210318-02, SW 1.0.0 (readkong mirror)](https://www.readkong.com/page/jdc-line-500-rev-20210318-02-software-v-1-0-0-glp-8761602) — found, not read
- [JDC Line 1000 User Manual Rev 20240618-01](https://glp.de/files/products/jdc-line-1000-product-data/JDC_Line_1000_User_Manual_EN_Rev_20240618-01.pdf), [DMX Channel Index Rev 20240618-01, firmware v1.0.0](https://glp.de/files/products/jdc-line-1000-product-data/JDC_Line_1000_DMX_Channel_Index_Rev_20240618-01.pdf), [product page](https://glp.de/en/products/entertainment-lighting/strobes/jdc-line-1000-en) — firmware 1.0.0; update via DMX link with the D3Prog (via search summary)
- [GLP D3Prog product page (glp.de)](https://glp.de/en/products/service-firmware/service-tools/d3prog-en) — D3Prog: USB / Sub-D 9 to PC, memory slots, DMX link or AVR/ISP output, XLR 5- and 3-pin female, 2x 1.2 V Mignon batteries, several fixtures at once (via search summary)
- GLP Tech News [2019/10/30](https://www.glp.de/en/service/tech-info-archive/archive/80-glp-tech-news-2019-10-30?tmpl=component) and [2019/01/14](https://www.glp.de/en/service/tech-info-archive/archive/73-glp-tech-news-2019-01-14) — hex vs BIN file type when importing to the D3Prog, daisy-chain via DMX with no other receivers or consoles active (via search summary; which note said what wasn't pinned)
- [GoKnight: GLP 9506 D-Prog Uploader](https://goknight.com/german-light-products-9506-d-prog-uploader/), [Solotech: GLP 9506 D-Prog Firmware Uploader](https://shop.solotech.com/products/glp-9506-d-prog-firmware-uploader) — retail part number 9506 (D-Prog; may be the older model, not D3Prog)
