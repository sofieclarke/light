---
title: "ETC Source Four LED Series 2 Lustr"
manufacturer: "ETC"
model: "Source Four LED Series 2 Lustr"
aliases: ["lustr 2", "series 2 lustr", "s4 led series 2", "source four led series 2", "lustr+", "s4 lustr"]
type: "ellipsoidal"
light_source: "LED, 60 7-color Lumileds LUXEON Rebel emitters"
ip_rating: null
weight_lb: 18.3
weight_kg: 8.3
dimensions: "338 x 615 x 631 mm (OFL community data)"
power:
  input: null
  connector_in: null
  connector_out: null
  watts_max: 171
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
  protocols: ["DMX", "RDM"]
  modes:
    - { name: "Direct", channels: 10 }
    - { name: "HSI", channels: 6 }
    - { name: "HSIC", channels: 7 }
    - { name: "RGB", channels: 6 }
    - { name: "Studio", channels: 6 }
    - { name: "HSI Plus 7", channels: 15 }
    - { name: "HSIC Plus 7", channels: 16 }
    - { name: "RGB Plus 7", channels: 15 }
menu_password: null
tools: []
verification: "community"
last_updated: "2026-10-03"
---

# ETC Source Four LED Series 2 Lustr

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** Not found. Fill in from the fixture.
> - **Power:** amps not found. Community data lists **171 W** max (OFL) ⚠️. Read the label.
> - **DMX modes (OFL community data):** Direct 10 · HSI 6 · HSIC 7 · RGB 6 · Studio 6 · HSI+7 15 · HSIC+7 16 · RGB+7 15.
> - **Not the same as Series 3 Lustr X8.** The mode lists differ, so check the label before patching.
> - **Tools:** TBD – check on next show.

## Identity
- What crews call it: Lustr 2, Series 2, S4 LED.
- Fixture library / profile names: OFL "Source Four LED Series 2 Lustr" (short name EtcSF2Lustr).
- Variants: Series 2 Daylight HD and Tungsten HD use the same body with different arrays. Series 3 Lustr X8 has its own page: [source-four-led-series-3-lustr-x8.md](source-four-led-series-3-lustr-x8.md).

## Passwords, menu locks & hidden menus
- Not found. Fill in from the fixture.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found | Not found | Not found |
| Power (W) | 171 max (OFL) ⚠️ | 171 max ⚠️ | 171 max ⚠️ |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | Not found — read the label | Not found | — |

- Input range, connectors, fuse: not found. Fill in from the fixture.

## Data & addressing
- Connectors: 5-pin XLR (OFL).
- DMX modes (OFL; "?" marks a channel OFL lists without a usable name):

| Mode | Ch | Layout |
|---|---|---|
| Direct | 10 | Red, Lime, Amber, Green, Cyan, Blue, Indigo, Intensity, Strobe, Fan |
| HSI | 6 | Hue, Hue fine, Sat, Int, Strobe, Fan |
| HSIC | 7 | Hue, Hue fine, Sat, Int, Strobe, Fan, Color Point |
| RGB | 6 | R, G, B (emulated), ?, Strobe, Fan |
| Studio | 6 | Int, Color Point, Tint, ?, Strobe, Fan |
| HSI Plus 7 | 15 | HSI block + Plus 7 control + 7 direct colors |
| HSIC Plus 7 | 16 | HSIC block + Plus 7 control + 7 direct colors |
| RGB Plus 7 | 15 | RGB block + Plus 7 control + 7 direct colors |

- Set the address, factory reset: not found.

## Rigging & hardware
- Yoke and C-clamp (general knowledge). Weight 8.3 kg (OFL).

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD – check on next show |
| Gobo / effects module access | TBD – check on next show | TBD – check on next show |
| Lens / front glass | TBD – check on next show | TBD – check on next show |
| Yoke / clamp | TBD – check on next show | TBD – check on next show |

## Optics & consumables
- 60 × 7-color LUXEON Rebel emitters, 8,667 lm (OFL) ⚠️. Lens tubes 5–90° (OFL).

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Not found | — | Fill in from the fixture |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Patched as X8 but colors are wrong | It's a Series 2, so the channel layout differs | Repatch with the Series 2 profile |

## Maintenance
- Not found.

## Road notes (community)
- Nothing confirmed found. Search budget ran out.

## Sources
- [Open Fixture Library: source-four-led-series-2-lustr.json](https://github.com/OpenLightingProject/open-fixture-library/blob/master/fixtures/etc/source-four-led-series-2-lustr.json): modes, 171 W, 8.3 kg, dimensions, LED count. OFL links the ETC manuals at etcconnect.com DownloadAsset id=10737483869 and 10737501163, which couldn't be fetched.
