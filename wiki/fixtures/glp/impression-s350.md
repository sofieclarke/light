---
title: "GLP impression S350"
manufacturer: "GLP (German Light Products)"
model: "impression S350"
aliases: ["s350", "impression s350", "glp s350"]
type: "profile"
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
  latest_known: "V53 (Rev20200203)"
  checked: "2026-10-03"
  check_on_fixture: "Not found"
  methods: ["DMX link with GLP D3Prog", "GLP iQ.Service"]
  interface: "GLP D3Prog (USB/Sub-D 9 to PC; 5-pin + 3-pin XLR out)"
  software: "D3Prog PC transfer (software name not found); GLP iQ.Service"
  file_type: ".hex (Intel hex) or .bin, depending on firmware version ⚠️"
  download: "glp.de product page → Downloads, or GLP iQ.Service Portal; also germanlightproducts.com/downloads"
tools: []
verification: "unverified"
last_updated: "2026-10-03"
---

# GLP impression S350

> **STUB — research cut short.** The web-search budget ran out before any source was found. **Nothing on this page is verified.** The S350 was picked over the KNV Cube as the more likely rental-stock fixture. That's a judgment call, not sourced.

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** Not found
> - **Power:** Not found. Read the fixture label. Don't guess.
> - **DMX:** Not found
> - **Won't move?** Not found. Look for pan/tilt locks.
> - **Tools:** TBD – check on next show

## Identity
- What crews call it: "S350". It's an LED profile moving head from GLP's impression range, with framing shutters (general knowledge ⚠️ unverified).
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
| Gobo / effects module access | TBD – check on next show | TBD |
| Lens / front glass | TBD – check on next show | TBD |
| Omega bracket | TBD – check on next show | TBD |

## Optics & consumables
- Not found (gobo sizes, wheels, shutter details).

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
- Latest known version (date checked) and where to download it: **V53 (Rev20200203)** (latest found, checked 2026-10-03): listed on the glp.de S350 product page (via search summary). The user manual found covers software 48 / manual V50 Rev C. The product page also links the **iQ.Service Portal** for the latest firmware, which may be newer.
- What you need:
  - **GLP D3Prog** (GLP's firmware programmer). Load the firmware into one of its memory slots from a PC over **USB (Type B)** or **Sub-D 9**, then plug it into the fixture's DMX in. It has **both 5-pin and 3-pin female XLR**, so no adapter needed. Runs on 2x 1.2 V Mignon (AA) rechargeables, so it works with no mains near it (glp.de). Retail part no. **9506** is listed for the "D-Prog" uploader ⚠️ (may be the older model).
  - **GLP iQ.Service** is the other listed upload method (glp.de). Hardware/app steps for the S350: Not found.
  - USB port / Art-Net update / fixture-to-fixture push: Not found.
- Update steps:
  1. On the PC, import the firmware into a D3Prog memory slot. Pick file type **Intel hex** or **BIN** to match the firmware file (GLP tech note, via search summary).
  2. **Unplug the console and anything else on the line that you aren't updating.** GLP says no other DMX receivers or consoles may be active (tech note, via search summary).
  3. D3Prog XLR out → DMX in of the first fixture, daisy-chain the rest. Fixtures powered.
  4. Choose the slot on the D3Prog and start the upload. The button sequence on the D3Prog: Not found.
  5. Don't power-cycle until it reports done ⚠️ (general practice), then check the version on each fixture.
- Updating a whole rig: D3Prog updates several fixtures on one DMX line at once (glp.de). Keep the line S350-only ⚠️; don't include the **S350 Wash** (a different fixture) unless GLP says they share firmware. Per-line maximum: Not found.
- If it fails or bricks mid-update (recovery mode): Not found. The D3Prog can also program via AVR/ISP (service level). Contact support@glp.de.
- Release notes worth knowing: Not found. Check the mode list against your console profile after updating.

## Road notes (community)
- None retrieved.

## Sources
- [GLP impression S350 product page](https://www.glp.de/en/products/entertainment-lighting/moving-lights-led/impression-s350) — firmware V53 Rev20200203 listed; manual V50 Rev C; upload via D3Prog or GLP iQ.Service; iQ.Service Portal link (via search summary)
- [GLP impression S350 User Manual (protolight.com mirror)](https://protolight.com/files/2019/08/GLP-S350_Manual.pdf) — covers fixture software 48 (via search summary)
- [GLP D3Prog product page (glp.de)](https://glp.de/en/products/service-firmware/service-tools/d3prog-en) — D3Prog: USB / Sub-D 9 to PC, memory slots, DMX link or AVR/ISP output, XLR 5- and 3-pin female, 2x 1.2 V Mignon batteries, several fixtures at once (via search summary)
- GLP Tech News [2019/10/30](https://www.glp.de/en/service/tech-info-archive/archive/80-glp-tech-news-2019-10-30?tmpl=component) and [2019/01/14](https://www.glp.de/en/service/tech-info-archive/archive/73-glp-tech-news-2019-01-14) — hex vs BIN file type when importing to the D3Prog, daisy-chain via DMX with no other receivers or consoles active (via search summary; which note said what wasn't pinned)
- [GoKnight: GLP 9506 D-Prog Uploader](https://goknight.com/german-light-products-9506-d-prog-uploader/), [Solotech: GLP 9506 D-Prog Firmware Uploader](https://shop.solotech.com/products/glp-9506-d-prog-firmware-uploader) — retail part number 9506 (D-Prog; may be the older model, not D3Prog)
