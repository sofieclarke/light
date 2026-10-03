---
title: "Robe Forte"
manufacturer: "Robe"
model: "Robin Forte"
aliases: ["forte", "robin forte", "forte profile"]
type: "profile"
light_source: "LED engine, white (general knowledge: ~1000 W TE engine, unverified)"
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

# Robe Forte

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** Service password **7623** is Robe-wide and quoted in the Forte manual summary ("set to 7623 and cannot be changed"). REAP **robe / 2479**. Button lock gesture: see [_robe-common](_robe-common.md).
> - **Power:** Not found — fill in from the fixture's label/manual. Do not guess circuit counts.
> - **DMX:** modes not found — fill in from the fixture
> - **Won't move?** Transport lock locations not found. Pan/Tilt Error meanings: see common page.
> - **Gobos:** 2 rotating wheels, glass 30.9 (+0.1) mm OD / max 25 mm image / 1–3.5 mm thick.
> - **Followspot:** Forte LightMaster controller default password **5242** (controller only).
> - **Tools:** TBD – check on next show

⚠️ **Thin page: the research session ran out of web-search budget. Only the items cited in Sources were confirmed. Everything else is a placeholder or general knowledge.**

## Identity
- What crews call it: "Forte" (general knowledge).
- Fixture library / profile names: Not found.
- Variants (general knowledge, ⚠️ unverified): Forte, **iFORTE** (IP65, see [iforte.md](iforte.md)), Forte FollowSpot / **Forte LightMaster** controller (own manual, default password 5242), FORTE FS.

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
- Two rotating gobo wheels. Glass gobos: **OD 30.9 +0.1 mm, max image 25 mm, thickness 1–3.5 mm** (Robe gobo overview).
- Framing / zoom / iris / prism / colour system: Not found in sources.

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
- [Robin Forte manual v3.8](https://www.robe.cz/res/downloads/user_manuals/User_manual_Robin_Forte.pdf) — 7623 password ("Password Protection" / service, cannot be changed), button names, Address screen. Power and DMX tables not extracted.
- [Robin Forte LightMaster manual v1.2](https://www.robe.cz/res/downloads/user_manuals/User_manual_Robin_Forte_LightMaster.pdf) — LightMaster default password 5242
- [Replaceable gobos in Robe fixtures](https://www.robelighting.com/res/downloads/gobo_config/Robe_Fixtures_Gobos_overview.pdf) — gobo dimensions
