---
title: "GLP impression FR10 Bar"
manufacturer: "GLP (German Light Products)"
model: "impression FR10 Bar"
aliases: ["fr10", "fr10 bar", "impression fr10 bar", "glp fr10"]
type: "pixel-bar"
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
  latest_known: "V64 (Rev20230526-1)"
  checked: "2026-10-03"
  check_on_fixture: "Not found"
  methods: ["DMX link with GLP D3Prog / D-Prog"]
  interface: "GLP D3Prog (USB/Sub-D 9 to PC; 5-pin + 3-pin XLR out)"
  software: "D3Prog PC transfer (software name not found)"
  file_type: ".hex (Intel hex) or .bin, depending on firmware version ⚠️"
  download: "glp.de product page → Downloads, or GLP iQ.Service Portal; also germanlightproducts.com/downloads"
tools: []
verification: "unverified"
last_updated: "2026-10-03"
---

# GLP impression FR10 Bar

> **STUB — research cut short.** The web-search budget ran out before any source was found for this fixture. **Nothing on this page is verified.**

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** Not found
> - **Power:** Not found. Read the fixture label. Don't guess.
> - **DMX:** Not found
> - **Won't move?** Not found. Look for a tilt/rotation lock before power-up.
> - **Tools:** TBD – check on next show

## Identity
- What crews call it: "FR10", "FR10 Bar". It's a motorized LED batten from GLP's FR range, related to the single-cell FR1 (general knowledge ⚠️ unverified).
- Fixture library / profile names: Not found.

## Passwords, menu locks & hidden menus
- Not found — fill in from the fixture. See [_glp-common.md](_glp-common.md).

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
- Latest known version (date checked) and where to download it: **V64 (Rev20230526-1)** (latest found, checked 2026-10-03): listed on the glp.de FR10 Bar product page (via search summary). The user manual found is written for software **V46** (Rev 20220727-1), so a bar on V46 is well behind.
- What you need:
  - **GLP D3Prog** (GLP's firmware programmer). Load the firmware into one of its memory slots from a PC over **USB (Type B)** or **Sub-D 9**, then plug it into the fixture's DMX in. It has **both 5-pin and 3-pin female XLR**, so no adapter needed. Runs on 2x 1.2 V Mignon (AA) rechargeables, so it works with no mains near it (glp.de). Retail part no. **9506** is listed for the "D-Prog" uploader ⚠️ (may be the older model).
  - GLP describes the FR10 Bar update as **software update via DMX link with Dprog** (glp.de).
  - USB port / Art-Net update / iQ.Service / fixture-to-fixture push: Not found.
- Update steps:
  1. On the PC, import the firmware into a D3Prog memory slot. Pick file type **Intel hex** or **BIN** to match the firmware file (GLP tech note, via search summary).
  2. **Unplug the console and anything else on the line that you aren't updating.** GLP says no other DMX receivers or consoles may be active (tech note, via search summary).
  3. D3Prog XLR out → DMX in of the first fixture, daisy-chain the rest. Fixtures powered.
  4. Choose the slot on the D3Prog and start the upload. The button sequence on the D3Prog: Not found.
  5. Don't power-cycle until it reports done ⚠️ (general practice), then check the version on each fixture.
- Updating a whole rig: D3Prog updates several fixtures on one DMX line at once (glp.de). Keep the line FR10-only ⚠️. Per-line maximum: Not found.
- If it fails or bricks mid-update (recovery mode): Not found. The D3Prog can also program via AVR/ISP (service level). Contact support@glp.de.
- Release notes worth knowing: Not found for V46 → V64. Check the mode list against your console profile after updating.

## Road notes (community)
- None retrieved.

## Sources
- [GLP impression FR10 Bar product page](https://glp.de/en/products/entertainment-lighting/moving-lights/impression-fr10-bar-en) — firmware V64 Rev20230526-1 listed; software update via DMX link with D-Prog (via search summary)
- [impression FR10 Bar User Manual V46 Rev 20220727-1 (Volt Lites mirror)](https://voltlites.com/wp-content/uploads/2026/03/GLP-impression-FR10-Bar-User-Manual-V46-EN-Rev-20220727-1.pdf) — manual written for software V46
- [GLP D3Prog product page (glp.de)](https://glp.de/en/products/service-firmware/service-tools/d3prog-en) — D3Prog: USB / Sub-D 9 to PC, memory slots, DMX link or AVR/ISP output, XLR 5- and 3-pin female, 2x 1.2 V Mignon batteries, several fixtures at once (via search summary)
- GLP Tech News [2019/10/30](https://www.glp.de/en/service/tech-info-archive/archive/80-glp-tech-news-2019-10-30?tmpl=component) and [2019/01/14](https://www.glp.de/en/service/tech-info-archive/archive/73-glp-tech-news-2019-01-14) — hex vs BIN file type when importing to the D3Prog, daisy-chain via DMX with no other receivers or consoles active (via search summary; which note said what wasn't pinned)
- [GoKnight: GLP 9506 D-Prog Uploader](https://goknight.com/german-light-products-9506-d-prog-uploader/), [Solotech: GLP 9506 D-Prog Firmware Uploader](https://shop.solotech.com/products/glp-9506-d-prog-firmware-uploader) — retail part number 9506 (D-Prog; may be the older model, not D3Prog)
