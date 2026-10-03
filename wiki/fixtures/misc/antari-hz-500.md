---
title: "Antari HZ-500"
manufacturer: "Antari"
model: "HZ-500"
aliases: ["hz-500", "hz500", "antari hz500", "antari hazer", "antari hz-500"]
type: "atmospheric"
light_source: null
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
  fuse: ""
dmx:
  connectors: "5-pin XLR (community data)"
  protocols: ["DMX"]
  modes:
    - { name: "1 Channel", channels: 1 }
menu_password: null
firmware:
  latest_known: null
  checked: "2026-10-03"
  check_on_fixture: null
  methods: []
  interface: null
  software: null
  file_type: null
  download: null
tools: []
verification: "unverified"
last_updated: "2026-10-03"
---

# Antari HZ-500

> **2AM CARD** — the stuff you need first
> - **Almost nothing manufacturer-confirmed was found.** Read the label and the manual on the unit.
> - **DMX:** community profiles show **1 channel** (haze). The community GDTF has 0 = no haze and 251–255 = haze ON ⚠️. **Unverified, test before the show.**
> - **Power:** **not found.** An old QLC+ profile says 400 W ⚠️, which is low for a heater-based hazer, so don't trust it. **Check the voltage label before plugging into 208 V.**
> - **Build:** "built-in flight case", "dual haze nozzles", "silent operation" (description text in the community GDTF).
> - **Fluid, warm-up, error codes:** not found.

## Identity
- What crews call it: HZ-500, Antari hazer.
- Fixture library / profile names: GDTF "Antari@HZ-500@rev1" (GDTF Builder, 2025, community). QLC+ "Antari HZ-500" (community repo r26D/dmx-fixtures, QLC+ 4.4.0).
- Variants: HZ-350 and HZ-400 are smaller Antari hazers. Differences not found.

## Passwords, menu locks & hidden menus
- Not found.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found | Not found | Not found |
| Power (W) | Not found (QLC+ community says 400 W ⚠️ doubtful) | Not found | Not found |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | Not found. Plan a dedicated circuit until you've read the label | Not found | — |

## Data & addressing
- Connectors: 5-pin XLR (QLC+ community).
- DMX: 1 channel, Haze (both community sources). Channel values: GDTF says 0 = No Haze, 251–255 = Haze On ⚠️. The QLC+ profile treats it as a 0–255 intensity. **They disagree, so test it.**
- Set the address: not found.

## Rigging & hardware
- Built-in flight case (GDTF description). Weight: both community files say 31.5 (kg presumably) ⚠️ unverified.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Covers | TBD – check on next show | TBD – check on next show |
| Fluid tank | TBD – check on next show | TBD – check on next show |
| Lens / front glass | n/a | n/a |
| Omega bracket | n/a | n/a |

## Optics & consumables
- Fluid: not found (Antari sells its own haze fluids, general knowledge ⚠️ check the manual for the specified type).
- Warm-up time: not found.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Not found | — | Fill in from the fixture |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| No haze at mid DMX values | Channel may only trigger at the top of its range (GDTF: 251–255) ⚠️ | Push to full and test |
| No haze at all | Still warming up, out of fluid, or pump/heater fault | Check fluid, wait, check the display. Error list not found |

## Maintenance
- Not found.

## Firmware
- **None found** (checked 2026-10-03). No firmware update procedure or tool for the HZ-500 turned up. The manual summaries only cover the rear-panel LCD settings (fog duration, interval, DMX address, door sensor).

## Road notes (community)
- Nothing found. Search budget ran out.

## Sources
- [GDTF Antari@HZ-500@rev1 (Lampy-Paperwork mirror)](https://github.com/Ai-Lampy/Lampy-Paperwork/tree/main/gdtf/fixtures/antari): 1-ch mode, channel sets (0 no haze / 251 haze on), weight 31.5, description text.
- [QLC+ Antari-HZ-500.qxf (r26D/dmx-fixtures)](https://github.com/r26D/dmx-fixtures/blob/master/QLC/Fixtures/Antari-HZ-500.qxf): 1 ch, 400 W, 31.5 weight, 375 × 350 × 510 mm (all community, unverified).
- [Antari HZ-500 product page](https://antari.com/products/hz-500/), [HZ-500 user manual (ManualsLib)](https://www.manualslib.com/manual/892121/Antari-Hz-500.html): no firmware procedure found (search summary)
