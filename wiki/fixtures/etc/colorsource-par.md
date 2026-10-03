---
title: "ETC ColorSource PAR"
manufacturer: "ETC"
model: "ColorSource PAR"
aliases: ["colorsource par", "cs par", "colorsource", "etc par", "color source par"]
type: "par"
light_source: "LED, 40 Lumileds LUXEON Z, RGB-L (red, green, blue, lime)"
ip_rating: null
weight_lb: 8.3
weight_kg: 3.77
dimensions: "203 x 310 x 240 mm (OFL / QLC+ community data)"
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
  protocols: ["DMX", "RDM"]
  modes:
    - { name: "5ch (default)", channels: 5 }
    - { name: "6ch Direct", channels: 6 }
    - { name: "3ch RGB", channels: 3 }
    - { name: "1ch", channels: 1 }
menu_password: null
tools: []
verification: "community"
last_updated: "2026-10-03"
---

# ETC ColorSource PAR

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** Not found. Fill in from the fixture.
> - **Power:** amps not found. **Community sources disagree on watts: OFL says 90 W, QLC+ says 120 W** ⚠️. Read the label.
> - **DMX modes:** **5ch default** (Int, R, G, B, Strobe) · 6ch Direct (Int, R, G, B, Lime, Strobe) · 3ch RGB · 1ch Intensity.
> - **Tools:** TBD – check on next show.

## Identity
- What crews call it: ColorSource PAR, CS PAR.
- Fixture library / profile names: GDTF "ETC@ColorSource_Par" (community file). OFL "ColorSource PAR" (RDM model ID 513). QLC+ "ETC ColorSource PAR".
- Variants: **ColorSource PAR Deep Blue** (different emitter mix, its own OFL profile). ColorSource PAR V Zoom and ColorSource Spot are separate fixtures.

## Passwords, menu locks & hidden menus
- Not found. Fill in from the fixture.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found | Not found | Not found |
| Power (W) | 90 (OFL) / 120 (QLC+) ⚠️ | — | — |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | Not found — read the label | Not found | — |

- Input range / connectors / fuse: not found. Fill in from the fixture.

## Data & addressing
- Connectors: 5-pin XLR (OFL, QLC+).
- Protocols: DMX, RDM (OFL lists an RDM model ID).
- DMX modes (OFL, QLC+ and GDTF all agree):

| Mode | Ch | Layout |
|---|---|---|
| 5ch (default) | 5 | Intensity, Red, Green, Blue, Strobe |
| 6ch Direct | 6 | Intensity, Red, Green, Blue, Lime, Strobe |
| 3ch RGB | 3 | Red, Green, Blue |
| 1ch | 1 | Intensity (of a preset color) |

- Set the address: not found. Fill in from the fixture.

## Rigging & hardware
- Yoke with C-clamp (general knowledge). Weight 3.77 kg (OFL/QLC+), 3.8 kg (GDTF).

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Yoke / clamp | TBD – check on next show | TBD – check on next show |
| Lens / front glass | TBD – check on next show | TBD – check on next show |
| Top / head covers | TBD – check on next show | TBD – check on next show |
| Omega bracket | TBD – check on next show | TBD – check on next show |

## Optics & consumables
- 40 LUXEON Z LEDs, 3,039 lm (OFL) ⚠️. Beam listed as 14.5° in OFL ⚠️ unverified. ETC sells diffusion/lens accessories (general knowledge).

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Not found | — | Fill in from the fixture |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| No lime / colors look thin | Fixture is in 5ch mode (no Lime channel) | Use 6ch Direct if you want Lime control |
| Units in 1ch mode show the wrong color | 1ch drives a preset color | Set the preset on the fixture, or use 5ch |

## Maintenance
- Not found.

## Road notes (community)
- Nothing confirmed found. Search budget ran out.

## Sources
- [Open Fixture Library: colorsource-par.json](https://github.com/OpenLightingProject/open-fixture-library/blob/master/fixtures/etc/colorsource-par.json): modes, 90 W, 3.77 kg, dimensions, LED type, RDM ID. OFL links ETC manuals at etcconnect.com DownloadAsset id=10737484145 and 10737494638, which couldn't be fetched.
- [QLC+ ETC-ColorSource-PAR.qxf](https://github.com/mcallegari/qlcplus/blob/master/resources/fixtures/ETC/ETC-ColorSource-PAR.qxf): modes, **120 W** (disagrees with OFL), 3.77 kg.
- [GDTF ETC@ColorSource_Par (community, Lampy-Paperwork mirror)](https://github.com/Ai-Lampy/Lampy-Paperwork/tree/main/gdtf/fixtures/etc): modes, 3.8 kg.
