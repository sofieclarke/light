---
title: "Robe Esprite"
manufacturer: "Robe"
model: "Robin Esprite"
aliases: ["esprite", "robin esprite", "esprite profile"]
type: "profile"
light_source: "LED engine, white (general knowledge: ~650 W TE engine, unverified)"
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

# Robe Esprite

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** Service password **7623** is Robe-wide (⚠️ not confirmed in the Esprite manual itself). REAP **robe / 2479**. Button lock gesture: see [_robe-common](_robe-common.md).
> - **Power:** Not found — fill in from the fixture's label/manual. Do not guess circuit counts.
> - **DMX:** modes not found — fill in from the fixture
> - **Won't move?** Transport lock locations not found. Pan/Tilt Error meanings: see common page.
> - **Gobos:** static glass 26.8 mm OD / 23.5 mm image / 1.1 mm thick. **No metal gobos** (thermal stress).
> - **Tools:** TBD – check on next show

⚠️ **Thin page: the research session ran out of web-search budget. Only the items cited in Sources were confirmed. Everything else is a placeholder or general knowledge.**

## Identity
- What crews call it: "Esprite" (general knowledge).
- Fixture library / profile names: Not found.
- Variants (general knowledge, ⚠️ unverified): Esprite (framing profile), **Esprite Fresnel** and **Esprite PC** (separate manual, User_manual_Robin_Esprite_Fresnel_Esprite_PC.pdf), iEsprite (IP65).

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
- Source: LED engine (general knowledge, ⚠️ unverified wattage).
- Static gobo wheel: 9 gobos. **Static gobo: OD 26.8 mm, image 23.5 mm, thickness 1.1 mm**, high-temperature borofloat or better. Metal or aluminium gobos cannot be used because of thermal stress (Robe gobo overview).
- Rotating gobo wheel: 7 glass gobos. Rotating gobo dimensions: Not found.
- Gobo holders: Robe patented Slot & Lock.
- Framing shutters / zoom / iris / prism: Not found in sources (⚠️ framing shutters, general knowledge).

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| See [_robe-common.md](_robe-common.md) | Robe Pan/Tilt Error 1/2, effect errors, temperature/fan messages | — |

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
- [Replaceable gobos in Robe fixtures](https://www.robelighting.com/res/downloads/gobo_config/Robe_Fixtures_Gobos_overview.pdf) — static gobo dimensions, no metal gobos, wheel counts
- [Robe Esprite product page](https://www.robe.cz/esprite) and [PLSN review](https://plsn.com/archives/december-2019/robe-esprite/) — 9 static / 7 rotating gobos, Slot & Lock
- [Robin Esprite manual](https://www.robe.cz/res/downloads/user_manuals/User_manual_Robin_Esprite.pdf) ([BMI mirror](https://shop.bmisupply.com/Resources/en/ItemDocuments/3971044/BMI.Robe.Robin.Esprite.Manual.pdf), [manualslib](https://www.manualslib.com/manual/1995929/Robe-Robin-Esprite.html)) — button names / battery display (common conventions). Power and DMX tables not extracted.
- [Esprite DMX chart](https://www.robelighting.de/res/downloads/dmx_charts/Robin_Esprite_DMX_charts.pdf) — exists, not read
- [Esprite Fresnel / PC manual](https://www.robe.cz/res/downloads/user_manuals/User_manual_Robin_Esprite_Fresnel_Esprite_PC.pdf) — variant exists
