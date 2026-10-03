---
title: "GLP impression X5"
manufacturer: "GLP (German Light Products)"
model: "impression X5"
aliases: ["x5", "impression x5", "glp x5"]
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
  latest_known: "1.1.3"
  checked: "2026-10-03"
  check_on_fixture: "Not found — check the fixture's information menu ⚠️"
  methods: ["DMX link with GLP D3Prog", "GLP iQ.Service (app / onboard iQ.Service module)", "Internal web interface", "Firmware Push (Fixture2Fixture) over DMX"]
  interface: "GLP D3Prog, or none (iQ.Service app / web interface / Firmware Push)"
  software: "GLP iQ.Service App; web browser (internal web interface)"
  file_type: null
  download: "glp.de product page → Downloads, or GLP iQ.Service Portal; also germanlightproducts.com/downloads"
tools: []
verification: "unverified"
last_updated: "2026-10-03"
---

# GLP impression X5

> **STUB — research cut short.** The web-search budget ran out before this page could be sourced. **No numbers on this page are verified.**

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** Not found
> - **Power:** Not found. Read the fixture label. Don't guess.
> - **DMX:** Not found
> - **Won't move?** Not found
> - **Tools:** TBD – check on next show

## Identity
- What crews call it: "X5". It's GLP's LED wash generation after the X4 (general knowledge). Size variants (e.g. X5 L / X5 Compact / IP versions) exist ⚠️ unverified. Check the label.
- The color system is reported as RGB + Lime ("RGBL") rather than RGBW (general knowledge ⚠️ unverified).
- Fixture library / profile names: Not found.

## Passwords, menu locks & hidden menus
- Not found — fill in from the fixture. For general GLP conventions see [_glp-common.md](_glp-common.md).

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
- Installed version — where to see it on the fixture: Not found — fill in from the fixture. The manuals print the fixture software version on the cover (e.g. "Fixture software version 1.1.3").
- Latest known version (date checked) and where to download it: **1.1.3** (latest found, checked 2026-10-03): the X5 User Manual Rev 20240207-01 and Safety Manual Rev 20231011-01 are written for fixture software 1.1.3. The X5 product page points to the **iQ.Service Portal** for the latest firmware, which may be newer. (The **X5 IP** variant is on **2.0.1** per its 2025 manual. Different fixture.)
- What you need:
  - **GLP D3Prog** (GLP's firmware programmer). Load the firmware into one of its memory slots from a PC over **USB (Type B)** or **Sub-D 9**, then plug it into the fixture's DMX in. It has **both 5-pin and 3-pin female XLR**, so no adapter needed. Runs on 2x 1.2 V Mignon (AA) rechargeables, so it works with no mains near it (glp.de). Retail part no. **9506** is listed for the "D-Prog" uploader ⚠️ (may be the older model).
  - **GLP iQ.Service:** the X5 has an onboard iQ.Service module that works with the **GLP iQ.Service App** on a phone/tablet (wireless firmware updates, info readout) (glp.de).
  - **Internal web interface:** listed as an upload method (manual). Steps and network setup: Not found.
  - **Firmware Push (Fixture2Fixture):** no extra hardware, just DMX cable from an X5 that has the wanted firmware (manual).
  - File type: Not found.
- Update steps:
  - **Firmware Push (fastest on a rig, manual via search summary):**
    1. Unplug the console from the line ⚠️ (general practice). DMX from the up-to-date X5 into the others.
    2. On the up-to-date fixture, open the **Firmware Push** menu item and confirm. The confirm is a **press-and-hold of about 2–3 s** (via search summary ⚠️).
    3. It pushes its flash firmware to every fixture of the same type on the DMX link. Leave power on until done ⚠️.
  - **D3Prog:**
    1. On the PC, import the firmware into a D3Prog memory slot. Pick file type **Intel hex** or **BIN** to match the firmware file (GLP tech note, via search summary).
    2. **Unplug the console and anything else on the line that you aren't updating.** GLP says no other DMX receivers or consoles may be active (tech note, via search summary).
    3. D3Prog XLR out → DMX in of the first fixture, daisy-chain the rest. Fixtures powered.
    4. Choose the slot on the D3Prog and start the upload. The button sequence on the D3Prog: Not found.
    5. Don't power-cycle until it reports done ⚠️ (general practice), then check the version on each fixture.
- Updating a whole rig: Firmware Push goes to every compatible fixture on the DMX link. GLP says an X5 push **also updates X5 Compact, X5 Bar 1000 and X5 IP Bar 1000** on the same line (manual), so pull any of those off the line if you don't want them changed. Per-line maximum: Not found.
- If it fails or bricks mid-update (recovery mode): Not found. Retry with D3Prog (it can also program via AVR/ISP, service level), or contact support@glp.de.
- Release notes worth knowing: Not found for 1.0.0 → 1.1.3. Check the mode list against your console profile after updating.

## Road notes (community)
- None retrieved. A Polish-language comparison of the X5 washes ("porownanie washy x5 od glp", technologiesceny.substack.com) turned up in search; its content wasn't read.

## Sources
- [technologiesceny substack: X5 wash comparison (PL)](https://technologiesceny.substack.com/p/porownanie-washy-x5-od-glp) — found, not read
- [impression X5 User Manual Rev 20240207-01, fixture software 1.1.3](https://www.germanlightproducts.com/wp-content/uploads/2022/01/GLP-impression-X5-User-Manual-Rev-20240207.pdf), [X5 Safety Manual Rev 20231011-01, software 1.1.3](https://www.germanlightproducts.com/wp-content/uploads/2022/01/GLP-impression-X5-Safety-Manual-Rev-20231011.pdf) — upload via D3Prog, GLP iQ.Service or internal web interface; Firmware Push (Fixture2Fixture) to X5 / X5 Compact / X5 Bar 1000 / X5 IP Bar 1000 (via search summary)
- [impression X5 IP User Manual Rev 20250129-01](https://glp.de/files/products/impression-x5-ip-product-data/GLP_impression_X5_IP_User_Manual_EN_Rev20250129-01.pdf), [X5 IP Safety Manual, software 2.0.1](https://www.germanlightproducts.com/wp-content/uploads/2025/07/GLP-impression-X5-IP-Safety-Manual-Rev-20250122.pdf) — X5 IP variant on software 2.0.1
- [GLP impression X5 product page](https://www.glp.de/en/products/moving-lights-led/impression-x5) — onboard iQ.Service module, latest firmware via iQ.Service Portal (via search summary)
- [GLP D3Prog product page (glp.de)](https://glp.de/en/products/service-firmware/service-tools/d3prog-en) — D3Prog: USB / Sub-D 9 to PC, memory slots, DMX link or AVR/ISP output, XLR 5- and 3-pin female, 2x 1.2 V Mignon batteries, several fixtures at once (via search summary)
- GLP Tech News [2019/10/30](https://www.glp.de/en/service/tech-info-archive/archive/80-glp-tech-news-2019-10-30?tmpl=component) and [2019/01/14](https://www.glp.de/en/service/tech-info-archive/archive/73-glp-tech-news-2019-01-14) — hex vs BIN file type when importing to the D3Prog, daisy-chain via DMX with no other receivers or consoles active (via search summary; which note said what wasn't pinned)
