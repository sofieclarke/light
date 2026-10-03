---
title: "SGM P-5"
manufacturer: "SGM"
model: "P-5"
aliases: ["p5", "p-5", "sgm p5", "sgm p-5", "p-5 rgbw"]
type: "wash"
light_source: "LED, 44 x 10 W RGBW (OFL community data)"
ip_rating: null
weight_lb: 19.6
weight_kg: 8.9
dimensions: "497 x 268 x 122 mm (OFL community data)"
power:
  input: null
  connector_in: null
  connector_out: null
  watts_max: 450
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
  connectors: "5-pin XLR (OFL community data)"
  protocols: ["DMX"]
  modes:
    - { name: "3-channel Full Color Calibrated", channels: 3 }
    - { name: "4-channel RAW", channels: 4 }
    - { name: "6-channel RAW", channels: 6 }
    - { name: "6-channel CTC", channels: 6 }
    - { name: "8-channel RAW 16bit", channels: 8 }
    - { name: "9-channel RAW 16bit", channels: 9 }
    - { name: "10-channel RAW 16bit", channels: 10 }
    - { name: "10-channel CTC", channels: 10 }
menu_password: null
tools: []
verification: "community"
last_updated: "2026-10-03"
---

# SGM P-5

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** Not found. Fill in from the fixture.
> - **Power:** amps not found. Community data lists **450 W** (OFL, imported from QLC+) ⚠️. Read the label.
> - **DMX (OFL, older mode list):** 3ch calibrated RGB · 4ch RAW RGBW · 6ch RAW (Shutter, Int, RGBW) · 6ch CTC · 8/9/10ch 16-bit RAW · 10ch CTC. **Newer firmware may have more modes.** Check the menu.
> - **Tools:** TBD – check on next show.
> - **SGM Q-7: no data found** in this research. Separate page still to do.

## Identity
- What crews call it: P-5, SGM wash/flood.
- Fixture library / profile names: OFL "SGM P-5". QLC+ "SGM-P-5". GDTF variants: P-5 TW and P-5 W (15/21/43° lens).
- Variants: P-5 (RGBW), P-5 TW (tunable white), P-5 W (white). The **POI** version is mentioned in the manual title ("STD and POI") ⚠️ meaning not confirmed.

## Passwords, menu locks & hidden menus
- Not found. Fill in from the fixture.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found | Not found | Not found |
| Power (W) | 450 (OFL) ⚠️ | 450 ⚠️ | 450 ⚠️ |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | Not found — read the label | Not found | — |

- Input range / connectors / fuse: not found.

## Data & addressing
- Connectors: 5-pin XLR (OFL).
- DMX modes (OFL, from SGM DMX protocol Rev4):

| Mode | Ch | Layout |
|---|---|---|
| 3ch Full Color Calibrated | 3 | R, G, B |
| 4ch RAW | 4 | R, G, B, W |
| 6ch RAW | 6 | Shutter, Int, R, G, B, W |
| 6ch CTC | 6 | Shutter, Int, CTC, R, G, B |
| 8ch RAW 16-bit | 8 | R, Rf, G, Gf, B, Bf, W, Wf |
| 9ch RAW 16-bit | 9 | Int, R, Rf, G, Gf, B, Bf, W, Wf |
| 10ch RAW 16-bit | 10 | Int, Intf, R, Rf, G, Gf, B, Bf, W, Wf |
| 10ch CTC | 10 | Shutter, Int, Intf, CTC, R, Rf, G, Gf, B, Bf |

- Wireless: not found.

## Rigging & hardware
- 8.9 kg, 497 × 268 × 122 mm (OFL). Bracket not found.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD – check on next show |
| Gobo / effects module access | n/a | n/a |
| Lens / front glass | TBD – check on next show | TBD – check on next show |
| Omega bracket | TBD – check on next show | TBD – check on next show |

## Optics & consumables
- 44 × 10 W RGBW, 20,031 lm, 15–43° depending on lens (OFL) ⚠️.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Not found | — | Fill in from the fixture |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| No output in 6ch/10ch mode | Shutter channel closed | Open the Shutter (channel 1) |

## Maintenance
- Not found.

## Road notes (community)
- Nothing confirmed found. Search budget ran out.

## Sources
- [Open Fixture Library: sgm/p-5.json](https://github.com/OpenLightingProject/open-fixture-library/blob/master/fixtures/sgm/p-5.json) (imported from QLC+ 4.12): modes, 450 W, 8.9 kg, dimensions, LED count. OFL links the [SGM P-5 Series User Manual Rev J](https://sgmlight.com/Files/Files/Perfion/StrRDDATAUserManualFileGroup/P-5/FileRDDATAUserManualP5SeriesWEB/SGM%20P-5%20Series%20User%20Manual%20STD%20and%20POI%20(Rev.%20J).pdf) and [DMX protocol Rev4](https://sgmlight.com/Files/Files/Perfion/StrRDDATADMXFileGroup/P-5%20RGBW/FileRDDATADMXChartsP5RGBWRnD/DMX_Protocol_P_5_Rev4.pdf) (sgmlight.com blocked, not read).
