---
title: "Claypaky Sharpy X Frame"
manufacturer: "Claypaky"
model: "Sharpy X Frame"
aliases: ["sharpy x frame", "sharpy xframe", "x frame", "xframe", "claypaky sharpy x frame"]
type: "hybrid"
light_source: "Discharge 550 W, 8000 K (retailer listing); QLC+ wrongly lists LED"
ip_rating: null
weight_lb: 61.7
weight_kg: 28
dimensions: "approx. 350 x 668 x 306 mm (W x H x D, QLC+ community data)"
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
  connectors: "5-pin XLR (community data)"
  protocols: ["DMX"]
  modes:
    - { name: "Standard", channels: 43 }
menu_password: null
tools: []
verification: "community"
last_updated: "2026-10-03"
---

# Claypaky Sharpy X Frame

(I chose this over the Skylos because the Sharpy X Frame is a touring framing hybrid. The Skylos is a large outdoor sky-beam fixture, much rarer on tour rigs. That choice is general knowledge.)

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** not sourced. The Claypaky line Advanced code is **1234** ⚠️ unverified for X Frame.
> - **Power:** manufacturer amps not found. The 550 W lamp alone is 4.6 A @120 V, so **no more than 3 per 20 A @120 V** and **no more than 6 @208 V** (2.6 A). The whole fixture draws more, so plan **2 @120 V** until you've read the label ⚠️.
> - **DMX:** Standard **43 ch** (community). Lamp Control 26-100 OFF / 101-255 ON. Reset 128-255 complete.
> - **Display stays dark?** Function ch 171-180 = Display ON, 161-170 = Display OFF (default) (community profile).
> - **Tools:** TBD – check on next show

## Identity
- What crews call it: "X Frame", "Sharpy X Frame". Sibling of Sharpy X Spot (no framing).
- Fixture library / profile names: Standard 43 (QLC+). Other modes: Not found.

## Passwords, menu locks & hidden menus
- Not found — fill in from the fixture. See [_claypaky-common.md](_claypaky-common.md).

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found. Lamp alone ≈4.6 A (550/120) ⚠️ | Not found. Lamp alone ≈2.6 A ⚠️ | Not found |
| Power (W) | Lamp 550 W. Fixture total: Not found | — | — |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | ceiling floor(16/4.6)=3 (real draw higher) → **≤3, plan 2** ⚠️ | ceiling floor(16/2.6)=6 → **≤6** ⚠️ | — |

- Input range / connectors / fuse: Not found — fill in from the fixture.

## Data & addressing
- Connectors: 5-pin XLR (community).
- DMX Standard 43 (QLC+): Cyan, Magenta, Yellow, CTO, Colour Function, Full Color, Strobe, Dimmer, Dimmer fine, Iris, Static Gobo, Animation insert, Animation rot, Rotating Gobo, Gobo Rot, Gobo Rot fine, 4-facet prism in/rot, 8-facet prism in/rot, Frost, Zoom, Focus, Focus fine, Beam mode, Blade 1-4 movement + swivel (8 ch), Framing Rotation, Framing Macro, Framing Macro speed, Pan, Pan fine, Tilt, Tilt fine, Function, Reset, Lamp Control.
- Control values (QLC+): Reset 26-76 effects, 77-127 pan/tilt, 128-255 complete. Function 161-170 display off (default), 171-180 display on, 181-190 framing dimming delay on, 191-200 off (default). Lamp 26-100 off, 101-255 on.
- Address / battery addressing: Not found.

## Rigging & hardware
- Not found — fill in from the fixture.
- Weight 28 kg. Pan 540°, tilt 270° (QLC+).

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD – check on next show |
| Gobo / effects module access | TBD – check on next show | TBD – check on next show |
| Lens / front glass | TBD – check on next show | TBD – check on next show |
| Omega bracket | TBD – check on next show | TBD – check on next show |

## Optics & consumables
- Source: 550 W discharge, 8000 K (Farralane listing). ~18,800 lm (QLC+). Lamp model and life: Not found.
- Zoom: 2-52° (Farralane) vs 3-52° (QLC+).
- CMY, CTO, colour wheel, static and rotating gobos, animation wheel, 4- and 8-facet prisms, frost, iris, 4-blade framing with rotation.
- Gobo size: Not found.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Not found — fill in from the fixture | | |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Lamp won't strike from desk | Lamp Control not at ON | Send 101-255 |
| Display dark during show | Display-off function set (default) | Function 171-180 → display on |

## Maintenance
- Firmware: see [_claypaky-common.md](_claypaky-common.md).

## Road notes (community)
- None sourced. Add your own.

## Sources
- QLC+ Clay-Paky-Sharpy-X-Frame.qxf (github.com/mcallegari/qlcplus, commit 1ccdab8) — 43-ch mode, channel order, control values, weight, dims (community; its "LED" bulb field is wrong: the profile has a Lamp Control channel)
- [Farralane: Clay Paky Sharpy X Frame 550W discharge](https://www.farralane.com/clay-paky-sharpy-x-frame-550w-discharge-moving-head-spot-beam-hybrid-in-black-finish.html) — 550 W, 8000 K, 2-52° zoom (title via search)
- [Claypaky Sharpy X Frame product page](https://www.claypaky.it/products/sharpy-xframe/) — exists (no figures extracted)
- Note: the shared web-search budget ran out before this fixture was searched in depth.
