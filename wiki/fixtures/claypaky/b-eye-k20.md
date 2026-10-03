---
title: "Claypaky A.leda B-EYE K20"
manufacturer: "Claypaky"
model: "A.leda B-EYE K20"
aliases: ["b-eye k20", "beye k20", "b eye", "k20", "a.leda b-eye k20", "b-eye", "beye"]
type: "beam-wash"
light_source: "LED 37x Osram Ostar 15W RGBW (LED count derived from pixel-mode footprint; LED type per Open Fixture Library)"
ip_rating: null
weight_lb: 46.3
weight_kg: 21
dimensions: "approx. 395 x 476 x 330 mm (OFL); QLC+ lists height 589 mm"
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
  connectors: "3-pin and 5-pin XLR (community data)"
  protocols: ["DMX"]
  modes:
    - { name: "Standard", channels: 21 }
    - { name: "Shapes", channels: 35 }
    - { name: "Extended RGB", channels: 132 }
    - { name: "Extended RGBW", channels: 169 }
menu_password: null
tools: []
verification: "community"
last_updated: "2026-10-03"
---

# Claypaky A.leda B-EYE K20

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** not sourced for this model. The Claypaky line Advanced code is **1234** ⚠️ unverified for B-EYE.
> - **Power:** manufacturer amps not found. Community max-power figures **disagree**: 750 W (QLC+) vs 555 W (Open Fixture Library). Worst case 750/120 ≈ 6.3 A → **2 per 20 A @120 V**. At 208 V, 750/208 ≈ 3.6 A → **4** ⚠️ derived from community data. Read the label.
> - **DMX:** Standard 21 / Shapes 35 / Extended RGB 132 / Extended RGBW 169. Reset ch: 128-255 complete, 77-127 pan/tilt, 26-76 zoom.
> - **K10 vs K20:** K10 = 19 LEDs, ~14.5-15 kg. K20 = 37 LEDs, 21 kg. Same 21/35-ch base modes.
> - **Tools:** TBD – check on next show

## Identity
- What crews call it: "B-EYE", "B-Eye K20", "K20". Full name A.leda B-EYE K20.
- Fixture library / profile names: Standard (21), Shapes (35), Extended RGB / Extended RGBW pixel modes (QLC+).
- **K10 / K15 / K20 differences:**
  - **K10:** 19 LEDs (pixel modes 78 = 21+19x3, 97 = 21+19x4). 14.5 kg (QLC+) or 15 kg (OFL). 358 x 494 x 253 mm. Rated 450 W (both community sources). ~5500 lm (QLC+). Same Standard 21 / Shapes 35 modes.
  - **K20:** 37 LEDs (132 = 21+37x3, 169 = 21+37x4). 21 kg. ~9800 lm (both community sources).
  - **K15:** not found as an A.leda B-EYE in the sources. QLC+ has an **HY B-EYE K15**, which is a different hybrid fixture: 20 kg, rated 600 W, modes Standard 21 / Shapes 35 / RGB 57 / RGBW 76, 4-60° (community). Confirm which "K15" you're looking at from the label.
- Both K10 and K20 zoom 4-60°. Pan 540°, tilt 210° (QLC+).

## Passwords, menu locks & hidden menus
- Not found — fill in from the fixture. See [_claypaky-common.md](_claypaky-common.md) for line conventions (Advanced code 1234 on other models).

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found. ≈6.3 A derived from 750 W (QLC+) / ≈4.6 A from 555 W (OFL) ⚠️ | Not found. ≈3.6 A / ≈2.7 A derived ⚠️ | Not found |
| Power (W) | 750 W (QLC+) vs 555 W (OFL), conflicting community data | — | — |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | Worst case floor(16/6.3)=2 → **2** ⚠️ | Worst case floor(16/3.6)=4 → **4** ⚠️ | — |

- Input range / connectors / fuse: Not found — fill in from the fixture.

## Data & addressing
- Connectors: 3-pin and 5-pin XLR (community).
- DMX modes: Standard 21 = R, R fine, G, G fine, B, B fine, W, W fine, Linear CTO, Macro Color, Strobe, Dimmer, Dimmer fine, Pan, Pan fine, Tilt, Tilt fine, Function, Reset, Zoom, Zoom Rotation (QLC+; "Zoom Rotation" is the front-lens "B-EYE" rotation effect).
- Control values (QLC+): Reset 26-76 zoom reset, 77-127 pan/tilt, 128-255 complete. Function 73-77 halogen lamp simulation off (default).
- Set the address / battery addressing: Not found.

## Rigging & hardware
- Not found — fill in from the fixture (omega, safety point, transport locks).
- Weight 21 kg (K20), 14.5-15 kg (K10).

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD – check on next show |
| Gobo / effects module access | n/a (no gobos) | — |
| Lens / front glass | TBD – check on next show | TBD – check on next show |
| Omega bracket | TBD – check on next show | TBD – check on next show |

## Optics & consumables
- Source: RGBW LEDs (OFL lists Osram Ostar 15 W RGBW). K20 37 cells, K10 19 cells.
- Color system: RGBW + linear CTO + colour macros.
- Zoom 4-60°. Rotating front lens ("Zoom Rotation" channel) for the B-EYE effects (general knowledge).

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Not found — fill in from the fixture | | |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Not found | | |

## Maintenance
- Firmware: see [_claypaky-common.md](_claypaky-common.md).

## Road notes (community)
- None sourced. Add your own.

## Sources
- Open Fixture Library a-leda-b-eye-k20.json / a-leda-b-eye-k10.json (github.com/OpenLightingProject/open-fixture-library, commit 1424c7a) — weight, dimensions, 555 W / 450 W, LED type; manual link listed there: https://e-assist.tech/servlet/checkDocumentsFile?Id=729 (not reachable from here)
- QLC+ Clay-Paky-A.leda-B-EYE-K20.qxf, -K10.qxf, Clay-Paky-HY-B-EYE-K15.qxf (github.com/mcallegari/qlcplus, commit 1ccdab8) — modes and footprints, 750 W / 450 W / 600 W, weights, control values
- Note: the shared web-search budget ran out before this fixture was searched. No manufacturer-derived figures here. Verify everything against the label and manual.
