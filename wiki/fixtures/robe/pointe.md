---
title: "Robe Pointe"
manufacturer: "Robe"
model: "Robin Pointe"
aliases: ["pointe", "robin pointe"]
type: "hybrid"
light_source: "Osram Sirius HRI 280W discharge lamp (general knowledge, unverified)"
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

# Robe Pointe

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** Service password **7623** is Robe-wide and quoted in the Pointe manual search summaries. REAP **robe / 2479**. Button lock gesture: see [_robe-common](_robe-common.md).
> - **Power:** Not found — fill in from the fixture's label/manual. Do not guess circuit counts.
> - **DMX:** modes not found — fill in from the fixture
> - **Won't move?** Transport lock locations not found. Pan/Tilt Error meanings: see common page.
> - **Gobos:** Pointe gobos must NOT go in a MegaPointe (MegaPointe manual: not designed for its heat).
> - **Tools:** TBD – check on next show

⚠️ **Thin page: the research session ran out of web-search budget. Only the items cited in Sources were confirmed. Everything else is a placeholder or general knowledge.**

## Identity
- What crews call it: "Pointe" (general knowledge).
- Fixture library / profile names: Not found.
- Variants: Pointe; the successor is the MegaPointe ([megapointe.md](megapointe.md)); MiniPointe is a separate smaller fixture with its own manual.

## Passwords, menu locks & hidden menus
- Service password 7623, REAP robe/2479, button lock, Touchscreen Lock: see [_robe-common.md](_robe-common.md).

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found | Not found | Not found |
| Power (W) | Not found | Not found | Not found |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | Not found — do not guess | Not found | — |

- Input range / connectors / fuse: Not found — fill in from the fixture.

## Data & addressing
- Connectors / protocols / DMX modes: Not found — fill in from the fixture.
- Set the address: Robe touchscreen Address screen ([ENTER/Display On]). See common page.
- Battery / unpowered addressing: Robe battery-backed display convention (⚠️ unverified for this model).
- Factory reset: Not found.

## Rigging & hardware
- Bracket / omega, safety point, transport locks, weight / dimensions: Not found — fill in from the fixture.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD |
| Gobo / effects module access | TBD – check on next show | TBD |
| Lens / front glass | TBD – check on next show | TBD |
| Omega bracket | TBD – check on next show | TBD |

## Optics & consumables
- Source: 280 W discharge lamp (general knowledge, ⚠️ unverified).
- Gobo sizes: Not found (see the [Robe gobo overview PDF](https://www.robelighting.com/res/downloads/gobo_config/Robe_Fixtures_Gobos_overview.pdf)).
- Do not move Pointe gobos into MegaPointes (MegaPointe manual).

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| See [_robe-common.md](_robe-common.md) | Robe Pan/Tilt Error 1/2, effect errors, temperature/fan messages | — |
| Tilt Error | Head magnetic-indexing circuit fault (sensor or magnet) or a defective stepper or its driver IC (Robe manual wording; the Pointe manual was among the cited results, ⚠️ not pinned to Pointe) | Remove the tilt lock, reset, then service |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Can't change settings | Buttons locked | Circular-slide gesture (see common page) |

## Maintenance
- Recalibrate: Service → Calibrations (Robe convention, see common page).
- Fan / filter cleaning: Not found.

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
- None gathered (research search budget ran out).

## Sources
- [Robin Pointe manual v2.5](https://www.robe.cz/res/downloads/user_manuals/User_manual_Robin_Pointe.pdf) ([v1.4 mirror](https://enlx.co.uk/wptemp/wp-content/uploads/2024/05/User_manual_Robin_Pointe.pdf), [v1.8 R90 mirror](https://www.r90lighting.com/wp-content/uploads/2025/08/robe-pointe.pdf)) — 7623 service password, Service tab (Fixture Errors / Calibrations), screen lock
- [manualslib Pointe Service tab p28](https://www.manualslib.com/manual/829894/Robe-Robin-Pointe.html?page=28)
- [MegaPointe manual](https://www.robe.cz/res/downloads/user_manuals/User_manual_Robin_MegaPointe.pdf) — warning about Pointe gobos in MegaPointe
- [MA Lighting forum: Robe Pointe gobo rotation](https://forum.malighting.com/forum/thread/63190-robe-pointe-gobo-rotation/) — thread exists, contents not extracted
- [TB54 ROBE Uploader manual v1.0.9](https://www.robelighting.de/res/downloads/tech_bulletins/TB54_ROBE_Uploader_manual_EN.pdf) — Ethernet/RDM parallel update, 2.x.x.x PC address, DSU Mode / Fix broken device with RUNIT, bootloader recovery (via search summary)
- [Robe Universal Interface manual v1.7](https://www.robe.cz/res/downloads/user_manuals/User_manual_Robe_Universal_Interface.pdf) — DMX update via RUI, Special Functions → Updating Software
- [Robin Spiider manual v3.3](https://www.robelighting.com/res/downloads/user_manuals/User_manual_Robin_Spiider.pdf) — Information → Software Versions, Service → Update software (Robe touchscreen convention)
