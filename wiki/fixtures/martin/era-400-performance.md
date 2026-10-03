---
title: "Martin ERA 400 Performance"
manufacturer: "Martin"
model: "ERA 400 Performance"
aliases: ["era 400", "era400", "era 400 performance", "era performance", "era"]
type: "profile"
light_source: "White LED (wattage not confirmed)"
ip_rating: null
weight_lb: null
weight_kg: 22.5
dimensions: "about 237 x 632 x 379 mm (QLC+, W x H x D, unverified)"
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
  connectors: "5-pin XLR (QLC+)"
  protocols: ["DMX"]
  modes:
    - { name: "Standard", channels: 30 }
    - { name: "Extended", channels: 32 }
menu_password: null
tools: []
verification: "community"
last_updated: "2026-10-03"
---

# Martin ERA 400 Performance

> ⚠️ This page covers the **ERA 400 Performance**. Of the ERA 400 / ERA 600 Profile pair, it is the only one with sourceable data (QLC+). The ERA 600 Profile is a different, bigger fixture. Don't use these numbers for it.

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** No passcode found in any source. ⚠️ unverified
> - **Power:** amps **not found**. QLC+ lists 362 W, which is unverified and looks low for this class. **Read the rating label.**
> - **DMX:** Standard **30 ch** · Extended **32 ch** (Extended adds zoom fine + focus fine). Control is on the last channel: **200–209 reset all, 210–219 reset effects, 220–229 reset pan/tilt** (QLC+, ⚠️ community).
> - **Won't move?** Transport locks: Not found — TBD – check on next show
> - **Tools:** TBD – check on next show

## Identity
- What crews call it: "ERA 400", "ERA" (general knowledge). Martin's ERA line is the more affordable range, below the MAC line (general knowledge).
- Fixture library / profile names: QLC+ "ERA 400 Performance" (Std. 30 channel / EXT 32 channel). Not in Open Fixture Library.
- Variants: ERA 150 Wash, ERA 300 Profile and ERA 400 Performance are all in QLC+. Martin also makes the ERA 600 Profile / Performance (general knowledge). Details: Not found.

## Passwords, menu locks & hidden menus
- Not found — fill in from the fixture. See [Martin common](./_martin-common.md).

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found | Not found | Not found |
| Power (W) | 362 W (QLC+, ⚠️ unverified) | — | — |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | Not found | Not found | — |

- Input, connectors, fuse: Not found — fill in from the fixture.

## Data & addressing
- Connectors: 5-pin XLR (QLC+). Other protocols: Not found.
- **Standard 30 ch (QLC+):** 1 shutter · 2–3 dimmer + fine · 4–6 C / M / Y · 7 color wheel · 8 gobo 1 (rotating) · 9 gobo 1 rotation · 10 gobo 2 · 11 prism · 12 prism rotation · 13 iris · 14 zoom · 15 focus · 16–23 blades 1–4 (angle + position) · 24 blade system rotation · 25–28 pan, pan fine, tilt, tilt fine · 29 pan/tilt speed · 30 special function.
- **Extended 32 ch:** the same, plus zoom fine (after zoom) and focus fine (after focus).
- Note: QLC+ lists blade 1 as **angle then position**, and blades 2–4 as **position then angle**. Check against the console library.
- Shutter: 0–19 blackout · 20–24 open · 25–64 strobe 1 · 70–84 opening pulse · 90–104 closing pulse · 110–124 random · 130–144 random opening pulse · 145–255 open.
- **Special function (last channel):** 70–79 / 80–89 blackout-while-pan/tilt-moves enable / disable. 90–109 same for color. 110–129 same for gobo. **200–209 reset all, 210–219 reset effects, 220–229 reset pan/tilt.** ⚠️ community, not checked against the manual.
- Set the address: Not found — fill in from the fixture.

## Rigging & hardware
- Weight 22.5 kg. About 237 x 632 x 379 mm. Pan 540°, tilt 260° (QLC+, ⚠️ unverified).
- Bracket, safety point, transport locks: Not found — TBD – check on next show.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD |
| Gobo / effects module access | TBD – check on next show | TBD |
| Lens / front glass | TBD – check on next show | TBD |
| Omega bracket | TBD – check on next show | TBD |

## Optics & consumables
- LED, about 10,000 lm and 6500 K listed by QLC+. Zoom about 13–28° per QLC+, which looks narrow, ⚠️ unverified.
- CMY + color wheel, rotating gobo wheel 1, a second gobo wheel (7 gobos with shake, plus wheel rotation in QLC+), prism with rotation, iris, 4-blade framing with rotation.
- Gobo size: Not found.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Not found | — | See [Martin common](./_martin-common.md) |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Light blacks out every time the head moves | "Blackout while pan/tilt moves" is enabled | Special function 80–89 to disable (QLC+) |
| Framing blades act swapped (angle ↔ position) | Library blade order differs (see Data note) | Check the profile against the fixture |

## Maintenance
- Not found. See [Martin common](./_martin-common.md) for firmware tools.

## Road notes (community)
- None found.

## Sources
- [QLC+ Martin-ERA-400-Performance.qxf](https://github.com/mcallegari/qlcplus/tree/master/resources/fixtures/Martin) (author "Yestalgia"): modes, channel list, shutter and special-function values, weight, dims, W, lumens, zoom. Community only. Not checked against a Martin manual.
- No web-search results captured for ERA fixtures (search budget ran out).
