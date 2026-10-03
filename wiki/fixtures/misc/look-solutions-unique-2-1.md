---
title: "Look Solutions Unique 2.1"
manufacturer: "Look Solutions"
model: "Unique 2.1"
aliases: ["unique", "unique 2.1", "unique 2", "look unique", "look hazer", "look solutions unique"]
type: "atmospheric"
light_source: null
ip_rating: null
weight_lb: 19.2
weight_kg: 8.7
dimensions: "250 x 250 x 470 mm (QLC+ community data)"
power:
  input: null
  connector_in: null
  connector_out: null
  watts_max: 1500
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
  connectors: "5-pin XLR (QLC+ community data)"
  protocols: ["DMX"]
  modes:
    - { name: "2 Channel", channels: 2 }
menu_password: null
tools: []
verification: "community"
last_updated: "2026-10-03"
---

# Look Solutions Unique 2.1

> **2AM CARD** — the stuff you need first
> - **DMX, 2 ch:** **1 = Haze (pump) output**, **2 = Fan speed**. 0 = off on both (community GDTF: 0 Haze Off, 255 Full; 0 Fan Off, 255 Full).
> - **Warm-up:** "a few minutes" before it will haze (community, newtheatre wiki). Manufacturer figure not found.
> - **Power:** **1500 W** per QLC+ community data ⚠️. If right, that's about 12.5 A at 120 V. **Give it its own 20 A circuit** (⚠️ estimate). **Check the label voltage.** Not every unit is 120 V or 208 V capable. Not found.
> - **Fluid:** Look Solutions fluid ⚠️. Exact type not confirmed. Not found, fill in from the fixture.
> - **Shutdown (community):** press MENU repeatedly to **OFF**, then ENTER. Or **pull the DMX cable**, which also starts the power-down sequence. Wait for it to finish, then switch off.

## Identity
- What crews call it: Unique, Unique 2.1, Look hazer.
- Fixture library / profile names: QLC+ "Look Solutions Unique 2.1" (Pump, Fan). GDTF "Look_Solutions@Look_Solutions_Unique_2_1" (community, "Haze1, Fan1").
- Variants: Unique 2 (older) ⚠️ differences not found.

## Passwords, menu locks & hidden menus
- Not found. Menu has a MENU and an ENTER button (community wiki).

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found. ⚠️ Estimate: 1500/120 ≈ 12.5 A | Not found | Not found |
| Power (W) | 1500 (QLC+) ⚠️ | — | — |
| Max power-link (manufacturer) | No thru power known | — | — |
| **Max per 20 A circuit** (16 A continuous) | ⚠️ floor(16/12.5)=**1**, estimate. Use a dedicated circuit | Not found. **Check the voltage label first** | — |

- **Don't plug into 208 V unless the label says it's rated for it.** Hazer heaters are a classic 120-V-only item (see reference/power-math.md).

## Data & addressing
- Connectors: 5-pin XLR (QLC+).
- DMX (2 ch):

| Ch | Function | Values (community GDTF channel sets) |
|---|---|---|
| 1 | Haze / pump output | 0 off · rising · 255 full |
| 2 | Fan | 0 off · 127 half · 255 full |

- Community setting: **fan 15%, haze 7–10%** gives "a good misty stage" in a small theatre. Fan on full is loud (newtheatre wiki).
- **Pulling DMX = power-down sequence** (community). Don't hot-swap DMX mid-show expecting it to keep hazing.
- Set the address: not found.

## Rigging & hardware
- 8.7 kg, 250 × 250 × 470 mm (QLC+) ⚠️.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Covers | TBD – check on next show | TBD – check on next show |
| Fluid tank | TBD – check on next show | TBD – check on next show |
| Lens / front glass | n/a | n/a |
| Omega bracket | n/a | n/a |

## Optics & consumables
- Fluid: not confirmed. Fill in from the fixture or the manual.
- Fill time: "fills the auditorium in about 10 minutes, depending on settings" (community, small UK theatre).

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Not found | — | Fill in from the fixture |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| No haze right after power-up | Still warming up | Wait a few minutes (community) |
| Stops hazing when DMX is unplugged | By design, starts power-down (community) | Reconnect DMX and wait for it to re-heat |
| No haze, fan runs | Out of fluid, or pump/heater fault | **Check the fluid first** (community: "make sure there is fluid in the machine before use"). Pump and heater error codes: not found |

## Maintenance
- Always shut down via MENU → OFF or DMX removal so it runs the power-down sequence. This "keeps it clean and will help it last" (community).

## Road notes (community)
- newtheatre (Nottingham New Theatre) wiki: 2-channel; few-minute warm-up; fan loud at full; fan 15% / haze 7–10% for misty stage; the two power-off methods above.

## Sources
- [QLC+ Look-Solutions-Unique-2.1.qxf](https://github.com/mcallegari/qlcplus/blob/master/resources/fixtures/Look_Solutions/Look-Solutions-Unique-2.1.qxf): 2 ch (Pump, Fan), 1500 W, 8.7 kg, dimensions.
- [GDTF Look Solutions Unique 2.1 (community, Lampy-Paperwork mirror)](https://github.com/Ai-Lampy/Lampy-Paperwork/tree/main/gdtf/fixtures/look_solutions): channel sets (Haze off/40/60/full, Fan off/half/full).
- [newtheatre wiki: Atmospherics and Effects](https://github.com/newtheatre/wiki/blob/master/_content/tech-guides/atmos.md): road notes, shutdown procedure, settings.
