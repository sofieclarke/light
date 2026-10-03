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
- Firmware: DSU via Robe Universal Interface or ROBE Uploader. See [_robe-common.md](_robe-common.md).

## Road notes (community)
- None gathered (research search budget ran out).

## Sources
- [Robin Pointe manual v2.5](https://www.robe.cz/res/downloads/user_manuals/User_manual_Robin_Pointe.pdf) ([v1.4 mirror](https://enlx.co.uk/wptemp/wp-content/uploads/2024/05/User_manual_Robin_Pointe.pdf), [v1.8 R90 mirror](https://www.r90lighting.com/wp-content/uploads/2025/08/robe-pointe.pdf)) — 7623 service password, Service tab (Fixture Errors / Calibrations), screen lock
- [manualslib Pointe Service tab p28](https://www.manualslib.com/manual/829894/Robe-Robin-Pointe.html?page=28)
- [MegaPointe manual](https://www.robe.cz/res/downloads/user_manuals/User_manual_Robin_MegaPointe.pdf) — warning about Pointe gobos in MegaPointe
- [MA Lighting forum: Robe Pointe gobo rotation](https://forum.malighting.com/forum/thread/63190-robe-pointe-gobo-rotation/) — thread exists, contents not extracted
