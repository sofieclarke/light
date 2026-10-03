---
title: "Claypaky Scenius Unico"
manufacturer: "Claypaky"
model: "Scenius Unico"
aliases: ["scenius unico", "unico", "scenius", "claypaky scenius unico"]
type: "profile"
light_source: "Osram Lok-it! HTI 1400/PS discharge, 6000 K (community data); lamp control offers 1200 W and 1400 W modes"
ip_rating: null
weight_lb: 100.5
weight_kg: 45.6
dimensions: "approx. 360 x 803 x 410 mm (W x H x D, QLC+ community data)"
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
  per_20a_120v: 1
  per_20a_208v: null
  fuse: ""
dmx:
  connectors: "5-pin XLR (community data)"
  protocols: ["DMX"]
  modes:
    - { name: "Standard", channels: 40 }
    - { name: "Vector", channels: 44 }
menu_password: null
tools: []
verification: "community"
last_updated: "2026-10-03"
---

# Claypaky Scenius Unico

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** not sourced. The Claypaky line Advanced code is **1234** ⚠️ unverified for Unico.
> - **Power:** manufacturer amps not found. The lamp alone runs at up to **1400 W**, so 1400/120 = 11.7 A **minimum** → **1 per 20 A circuit @120 V**. At 208 V, the lamp alone is ≥6.7 A, so **1-2 per 20 A**. Read the label before doubling up. (QLC+ lists "1200 W", which is below the lamp's own 1400 W mode and must be too low.)
> - **DMX:** Standard **40** / Vector **44**. Lamp Control: 26-100 OFF, **101-179 ON @1200 W (quiet fans)**, **180-255 ON @1400 W**.
> - **Weight:** about 45.6 kg / 100 lb. Two-person lift.
> - **Tools:** TBD – check on next show

## Identity
- What crews call it: "Unico", "Scenius". A framing profile with CMY, iris, animation, autofocus and 4-blade framing.
- Fixture library / profile names: Standard (40), Vector (44, adds timing channels; Vector convention per Claypaky line).
- Variants: Scenius Spot / Scenius Profile are siblings (not covered here).

## Passwords, menu locks & hidden menus
- Not found — fill in from the fixture. See [_claypaky-common.md](_claypaky-common.md).

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found. Lamp alone ≥11.7 A (1400/120) ⚠️ | Not found. Lamp alone ≥6.7 A (1400/208) ⚠️ | Not found |
| Power (W) | Lamp 1200 W or 1400 W selectable (DMX chart). Whole fixture: Not found | — | — |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | floor(16/11.7)=1 → **1** (lower bound on draw, so this is a ceiling) | floor(16/6.7)=2 is a ceiling only; real draw is higher → **1-2, check label** ⚠️ | — |

- Input range / connectors / fuse: Not found — fill in from the fixture.
- Running the lamp at 1200 W (Lamp Control 101-179) also reduces fan noise (DMX chart). Good for theatre.

## Data & addressing
- Connectors: 5-pin XLR (community).
- DMX Standard 40 (QLC+): Cyan, Magenta, Yellow, CTO, Colour Wheel, Stopper/Strobe, Dimmer, Dimmer fine, Iris, Animation insert, Animation rot, Rotating Gobo, Gobo Rot, Gobo Rot fine, Prism insert, Prism rot, Light Frost, Blades 1A/1B/2A/2B/3A/3B/4A/4B, Framing Rotation, Focus, Focus fine, Zoom, Autofocus Distance, Autofocus Adjustment, Pan, Pan fine, Tilt, Tilt fine, Function, Reset, Lamp Control, Heavy Frost, Uniform Beam Field.
- Control values (QLC+): Reset 26-76 zoom, 77-127 pan/tilt, 128-255 complete. Function 38-50 conventional dimmer curve.
- Set the address / battery addressing: Not found.

## Rigging & hardware
- Not found — fill in from the fixture (omega, safety point, transport locks).
- Weight 45.6 kg. Pan 540°, tilt 270° (QLC+).

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD – check on next show |
| Gobo / effects module access | TBD – check on next show | TBD – check on next show |
| Lens / front glass | TBD – check on next show | TBD – check on next show |
| Omega bracket | TBD – check on next show | TBD – check on next show |

## Optics & consumables
- Source / lamp: Osram Lok-it! HTI 1400/PS, 6000 K, ~120,000 lm claimed (QLC+ community) ⚠️. Lamp life: Not found.
- Color: CMY + CTO + colour wheel. Iris. Animation disc. Rotating gobos. Prism. Light frost + heavy frost. 4-blade framing with rotation. Zoom 5-55°. Autofocus.
- Gobo size: Not found.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Not found — fill in from the fixture | | |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Breaker trips when two units share a 120 V circuit | 1400 W lamp: one per 20 A at 120 V | Re-circuit |
| Lamp won't strike from desk | Lamp Control channel not at ON value | Send 101-179 (1200 W) or 180-255 (1400 W) |

## Maintenance
- Firmware: see [_claypaky-common.md](_claypaky-common.md).

## Road notes (community)
- None sourced. Add your own.

## Sources
- QLC+ Clay-Paky-Scenius-Unico.qxf (github.com/mcallegari/qlcplus, commit 1ccdab8) — modes, channel order, lamp control 1200/1400 W values, weight, dims, lamp type (community)
- Note: the shared web-search budget ran out before this fixture was searched. No manufacturer-derived figures. Verify all against the label and manual.
