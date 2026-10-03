---
title: "Robe Spiider"
manufacturer: "Robe"
model: "Robin Spiider"
aliases: ["spiider", "spider", "robin spiider", "spiider washbeam"]
type: "beam-wash"
light_source: "LED: 1x 60W RGBW centre (Flower effect) + 18x RGBW ring LEDs (30 W per datasheet; some listings say 40 W)"
ip_rating: null
weight_lb: 29.2
weight_kg: 13.3
dimensions: "H 477 mm (18.7 in) x W 390 mm (15.3 in) x D 252 mm (9.9 in)"
power:
  input: null
  connector_in: "Neutrik powerCON TRUE1"
  connector_out: null
  watts_max: 660
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
  connectors: "Locking 3-pin and 5-pin XLR in/out (DMX/RDM)"
  protocols: ["DMX", "RDM"]
  modes:
    - { name: "Mode 1 (3-zones)", channels: 49 }
    - { name: "Mode 2 (Basic)", channels: 27 }
    - { name: "Mode 3", channels: 33 }
    - { name: "Mode 4", channels: 90 }
    - { name: "Mode 5", channels: 27 }
    - { name: "Mode 6", channels: 47 }
    - { name: "Mode 7", channels: 91 }
    - { name: "Mode 8", channels: 110 }
    - { name: "Mode 9", channels: 104 }
    - { name: "Mode 10", channels: 123 }
menu_password: "7623"
tools: []
verification: "web-search"
last_updated: 2026-10-03
---

# Robe Spiider

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** Service password **7623** (Robe-wide, ⚠️ not confirmed in the Spiider manual itself). Buttons locked → circular slide (see [_robe-common](_robe-common.md)).
> - **Power:** **max 660 W** (PF 0.99), older datasheets say 600 W. No amps table found. ⚠️ ESTIMATE ONLY (W÷V): ~5.5 A @120 V / ~3.2 A @208 V → about **2 per 20 A @120 V, 5 @208 V**. Link limit: not found.
> - **DMX:** 10 modes: 49 / 27 / 33 / 90 / 27 / 47 / 91 / 110 / 104 / 123 ch. Mode 1 = "3-zones" 49 ch, Mode 2 = "Basic" 27 ch. 3-pin AND 5-pin XLR.
> - **Won't move?** Pan Error 1/2 = yoke not home after reset. Check the transport lock (location TBD).
> - **Tools:** TBD – check on next show

## Identity
- What crews call it: "Spiider", often misspelt "Spider" (general knowledge).
- Fixture library / profile names: Robin Spiider + mode name (⚠️ unverified).
- Variants: **Spiider TW** (separate manual), **iSpiider** (IP65 outdoor version, 1x 60 W + 18x 40 W RGBW per Solotech listing). The 30 W vs 40 W ring LED figure differs between listings ⚠️.

## Passwords, menu locks & hidden menus
- Service password 7623 and REAP defaults: Robe-wide (see [_robe-common.md](_robe-common.md)). ⚠️ Not quoted from the Spiider manual itself.
- Errors: touch the warning icon or press [ESCAPE]. History: Service → Fixture Errors (Spiider manual).

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not in sources. ⚠️ est. 660/120 ≈ 5.5 | Not in sources. ⚠️ est. 660/208 ≈ 3.2 | Not in sources. ⚠️ est. 660/230 ≈ 2.9 |
| Power (W) | max 660 W (current datasheet). Older sheets: 600 W | same | same |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | ⚠️ est. floor(16/5.5)=2 → **2 (estimate)** | ⚠️ est. floor(16/3.2)=5 → **5 (estimate)** | — |

- Input range: Not found (⚠️ likely 100–240 V auto-ranging like other Robins, unverified).
- Connector in: Neutrik powerCON TRUE1. Out: not found.
- Fuse: Not found — fill in from the fixture.
- Estimates are watts ÷ volts using the stated PF 0.99. Not a Robe figure. Meter one first.

## Data & addressing
- Connectors: locking 3-pin and 5-pin XLR, DMX/RDM in/out.
- Protocols: DMX-512, RDM. Ethernet / wireless: Not found.
- Modes: 10, with 49, 27, 33, 90, 27, 47, 91, 110, 104, 123 channels (manual). Mode 1 "3-zones" (49 ch): 16-bit pan/tilt, 3 rings separately, 16-bit RGBW per ring, 16-bit dimmer, pixel effects, no individual pixel control. Mode 2 "Basic" (27 ch).
- Set the address: touchscreen Address screen ([ENTER/Display On]), Robe convention.
- Battery addressing: Robe battery-backed display convention (⚠️ not confirmed for Spiider specifically).
- Colour: RGBW or CMY mixing modes, virtual colour wheel with 66 preset swatches.

## Rigging & hardware
- Bracket / omega: Not found — fill in from the fixture.
- Transport lock: Not found — TBD – check on next show.
- Weight 13.3 kg (29.2 lb). H 477 × W 390 × D 252 mm (Robe datasheet).
- Max ambient 45 °C, max housing surface 75 °C (manual).

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD |
| Gobo / effects module access | n/a (no gobos) | — |
| Lens / front glass | TBD – check on next show | TBD |
| Omega bracket | TBD – check on next show | TBD |

## Optics & consumables
- Source: 1x 60 W RGBW multichip centre LED driving the "Flower Effect" (sharp multicolour spikes, rotates both ways), plus 18 RGBW ring LEDs (30 W per datasheet, 40 W per some listings).
- Zoom: 4°–50° (4Wall rental listing).
- No gobos. Pixel control of the rings in the higher modes.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Pan Error 1 / 2 | Yoke not in its default position after reset | Remove the lock, check for obstruction, reset |
| Zoom Error 1 / 2 | Zoom module not in its default position after reset | Reset. If it repeats, service. |
| Air filter icon | Filter cleaning period has run out | Clean the filters |
| Tilt Error | ⚠️ Robe-wide meaning (see common page) | — |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Overheat / dimming in hot rigs | Above 45 °C ambient or clogged filters | Clean the filters. Check the ambient temperature. |
| Wrong pixel layout on console | Mode mismatch (10 modes) | Match the mode to the patch |

## Maintenance
- Air filters: cleaning reminder icon (manual). Interval and procedure: Not found.
- Firmware: see [_robe-common.md](_robe-common.md).

## Road notes (community)
- None found (search budget ran out).

## Sources
- [Robin Spiider manual v3.3](https://www.robe.cz/res/downloads/user_manuals/User_manual_Robin_Spiider.pdf) (also [v2.6 mirror](https://hirewl.com/wp-content/uploads/2020/01/Robe_Spiider_User_Manual.pdf), [v2.9 mirror](https://enlx.co.uk/wptemp/wp-content/uploads/2024/05/User_manual_Robin_Spiider.pdf)) — 660 W PF 0.99, 10 DMX modes, connectors, Pan/Zoom errors, 45/75 °C, filter icon
- [Spiider DMX charts](https://www.robe.cz/res/downloads/dmx_charts/Robin_SPIIDER_DMX_charts.pdf) — Mode 1 "3-zones", Mode 2 "Basic"
- [Spiider product PDF 2025](https://cdn.aws.robe.cz/print/en_product_667.pdf), [HireWL datasheet](https://hirewl.com/wp-content/uploads/2020/01/Robe_Spiider_Data_Sheet.pdf) — weight, dimensions, 660 W vs older 600 W
- [Spiider leaflet](https://www.robe.cz/res/downloads/catalogues/ROBE_Spiider_leaflet_online_version.pdf) — LEDs, Flower effect, 66-swatch virtual wheel
- [4Wall Spiider rental](https://www.4wall.com/rentals/9758371/robe-spiider) — 4–50° zoom
- [Spiider TW manual](https://www.robe.cz/res/downloads/user_manuals/User_manual_Robin_Spiider_TW.pdf) — TW variant exists
- [Solotech iSpiider](https://shop.solotech.com/products/robe-ispiider-1x-60w-rgbw-and-18x-40w-rgbw-led-ip65-washbeam) — iSpiider IP65, 18x 40 W
