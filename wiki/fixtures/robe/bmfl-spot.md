---
title: "Robe BMFL Spot"
manufacturer: "Robe"
model: "Robin BMFL Spot"
aliases: ["bmfl", "bmfl spot", "robin bmfl spot", "bmfl blade", "bmfl washbeam", "bmfl wb"]
type: "spot"
light_source: "Osram Lok-it! HTI 1700/PS discharge lamp (general knowledge, unverified)"
ip_rating: null
weight_lb: null
weight_kg: null
dimensions: null
power:
  input: null
  connector_in: null
  connector_out: null
  watts_max: null
  amps_120v: null
  amps_208v: null
  amps_230v: null
  link_max_120v: null
  link_max_208v: null
  link_max_230v: null
  per_20a_120v: null
  per_20a_208v: null
  fuse: null
dmx:
  connectors: null
  protocols: []
  modes: []
menu_password: "7623"
firmware:
  latest_known: null
  checked: "2026-10-03"
  check_on_fixture: "Information → Software Versions"
  methods: ["DMX + Robe Universal Interface", "ROBE Uploader (Ethernet / RDM)"]
  interface: "Robe Universal Interface (RUNIT); none for ROBE Uploader over Ethernet"
  software: "ROBE Uploader; DSU uploader (in the DSU package)"
  file_type: "DSU package (.zip)"
  download: "robe.cz product page"
tools: []
verification: "unverified"
last_updated: 2026-10-03
---

# Robe BMFL Spot

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** Service password **7623** is Robe-wide (⚠️ unverified for BMFL specifically). REAP **robe / 2479**. Button lock gesture: see [_robe-common](_robe-common.md).
> - **Power:** Not found — fill in from the fixture's label. 1700 W-class lamp fixture (general knowledge): **do not stack these on a 120 V circuit without the real amp figure.**
> - **DMX:** modes not found — fill in from the fixture
> - **Won't move?** Transport lock locations not found. Pan/Tilt Error meanings: see common page.
> - **Tools:** TBD – check on next show

⚠️ **This page is mostly empty.** The research session ran out of web-search budget before BMFL could be researched. Everything below is general knowledge or a placeholder.

## Identity
- What crews call it: "BMFL" ("Best Moving Fixture Light" is a commonly repeated expansion, ⚠️ unverified).
- Fixture library / profile names: Not found.
- Variants and how to tell them apart (general knowledge, ⚠️ unverified):
  - **BMFL Spot**: gobo/spot fixture with iris, no framing shutters.
  - **BMFL Blade**: Spot plus a framing-shutter module (4 blades). Same lamp family.
  - **BMFL WashBeam**: wash/beam version with a wider zoom and a beam/wash optical path. Has gobos but no framing shutters.
  - Also BMFL FollowSpot (with the RoboSpot system) exists. Manual on manualslib, not read.

## Passwords, menu locks & hidden menus
- See [_robe-common.md](_robe-common.md). ⚠️ Not confirmed in the BMFL manual.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found | Not found | Not found |
| Power (W) | Not found | Not found | Not found |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | Not found — do not guess | Not found | — |

- Input / connectors / fuse: Not found — fill in from the fixture.

## Data & addressing
- Connectors / protocols / modes: Not found — fill in from the fixture.
- Address: Robe touchscreen convention (see common page).
- Battery addressing: Robe battery-backed display convention (⚠️ unverified for BMFL).

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
- Lamp: 1700 W short-arc discharge (general knowledge, ⚠️ unverified). Lamp life: Not found.
- Gobo sizes: Not found (check the [Robe gobo overview PDF](https://www.robelighting.com/res/downloads/gobo_config/Robe_Fixtures_Gobos_overview.pdf)).

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| See [_robe-common.md](_robe-common.md) | Pan/Tilt Error, effect errors, Lamp Error conventions | — |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Not researched | — | — |

## Maintenance
- Recalibrate / fan / filter cleaning: Not found.

## Firmware
- Installed version — where to see it on the fixture: **Information → Software Versions**. It lists each processor module separately (e.g. Display System, Module M = pan/tilt). Menu confirmed in the Spiider and MegaPointe manuals; for other touchscreen Robins it is the same convention (⚠️ check on the fixture).
- Latest known version (date checked) and where to download it: **Not found** (2026-10-03) — no version number captured for this model. Download the DSU package from this fixture's page on robe.cz.
- What you need: PC (Robe lists Windows; Linux/macOS also supported) · DSU package (.zip with the uploader) · **either** a **Robe Universal Interface / RUNIT** (USB-to-DMX box, also the WTX wireless version) and a DMX cable, **or** an Ethernet connection for **ROBE Uploader**. No USB-stick update method found for Robe. Details: [_robe-common.md](_robe-common.md#firmware-updates).
- Update steps — DMX with the Robe Universal Interface (RUI manual):
  1. Download and unzip the DSU package. Close other PC programs.
  2. **Unplug the console** from the line — the fixture's DMX in must come only from the RUI.
  3. RUI to PC by USB; DMX cable from RUI DMX out to the fixture's DMX in.
  4. Fixture: **Service → Update Software** (touchscreen Robins; older displays: Special Functions → Updating Software).
  5. Run the uploader on the PC, choose **Robe Universal Interface**, Connect, start the update.
  6. Don't touch power or cables until it finishes. Check Information → Software Versions afterwards.
- Update steps — ROBE Uploader (TB54): set the PC to a **2.x.x.x** address (e.g. 2.0.0.1, mask 255.0.0.0) if going over Ethernet. Discover the fixtures (RDM automatic or manual discovery, or build the setup by hand), select them and update. The Uploader puts fixtures into update mode itself. Exact button names: see TB54.
- Updating a whole rig: **ROBE Uploader updates several units in parallel over Ethernet** with no RUNIT needed. Over DMX with the RUI: how many per line is not found. Keep only one model on the line (⚠️ unverified, general practice).
- If it fails or bricks mid-update (TB54): a unit left in update mode **is not re-discovered automatically** — update it by hand with **DSU Mode / "Fix broken device with RUNIT"** in ROBE Uploader (one-to-one, needs the RUNIT). If it restarted mid-update (power cut), fixtures with **Display System 3.0** wait in the **bootloader** for an update on a **10.x.x.x** IP address.
- Release notes worth knowing: Not found for this model. Read the notes in the DSU package before a show — a software change can change DMX modes and break your console patch.

## Road notes (community)
- None gathered.

## Sources
- None BMFL-specific. Robe-wide conventions are sourced on [_robe-common.md](_robe-common.md).
- [Robin BMFL FollowSpot manual p27 (manualslib)](https://www.manualslib.com/manual/2395150/Robe-Robin-Bmfl-Followspot.html?page=27) — showed up in a screen-lock search; contents not extracted.
- [TB54 ROBE Uploader manual v1.0.9](https://www.robelighting.de/res/downloads/tech_bulletins/TB54_ROBE_Uploader_manual_EN.pdf) — Ethernet/RDM parallel update, 2.x.x.x PC address, DSU Mode / Fix broken device with RUNIT, bootloader recovery (via search summary)
- [Robe Universal Interface manual v1.7](https://www.robe.cz/res/downloads/user_manuals/User_manual_Robe_Universal_Interface.pdf) — DMX update via RUI, Special Functions → Updating Software
- [Robin Spiider manual v3.3](https://www.robelighting.com/res/downloads/user_manuals/User_manual_Robin_Spiider.pdf) — Information → Software Versions, Service → Update software (Robe touchscreen convention)
