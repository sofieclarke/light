---
title: "Chauvet Professional Maverick MK3 Wash"
manufacturer: "Chauvet Professional"
model: "Maverick MK3 Wash"
aliases: ["mk3 wash", "maverick mk3 wash", "mav mk3 wash", "maverick mk 3 wash", "maverickmk3wash"]
type: "wash"
light_source: "LED 27x 40W RGBW"
ip_rating: null
weight_lb: 68.2
weight_kg: 31
dimensions: ""
power:
  input: "100–240 VAC, 50/60 Hz, auto-ranging"
  connector_in: null
  connector_out: null
  watts_max: 1120
  amps_120v: 9.51
  amps_208v: 5.35
  amps_230v: null
  link_max_120v: null
  link_max_208v: null
  link_max_230v: null
  per_20a_120v: 1
  per_20a_208v: 2
  fuse: null
dmx:
  connectors: "3-pin and 5-pin XLR in/out, 2x Amphenol XLRnet (Ethernet) through ports"
  protocols: ["DMX", "W-DMX", "Art-Net", "sACN", "Kling-Net"]
  modes:
    - { name: "Single", channels: 20 }
    - { name: "Single", channels: 129 }
    - { name: "Single", channels: 243 }
    - { name: "Single", channels: 297 }
    - { name: "Dual – Function", channels: 9 }
    - { name: "Dual – Function", channels: 21 }
    - { name: "Dual – Function", channels: 27 }
    - { name: "Dual – Pixel", channels: 81 }
    - { name: "Dual – Pixel", channels: 108 }
    - { name: "Dual – Pixel", channels: 216 }
menu_password: null
tools: []
verification: "web-search"
last_updated: "2026-10-03"
---

# Chauvet Professional Maverick MK3 Wash

> **2AM CARD** — the stuff you need first
> - **Power:** 9.51 A @120 V / 5.35 A @208 V → **1 per 20 A circuit @120 V, 2 @208 V** (manufacturer link limit not found)
> - **Password:** Not found. Try Chauvet's usual offset code **2323** (⚠️ unverified for this model).
> - **DMX:** Single 20/129/243/297 · Dual Function 9/21/27 · Dual Pixel 81/108/216. Dual modes need **two addresses**.
> - **Data:** 3- and 5-pin DMX in/out plus **2 × Amphenol XLRnet** Ethernet ports (not etherCON), so carry the right patch cables.
> - **Tools:** TBD – check on next show.

## Identity
- What crews call it: "MK3 Wash", "Mav Wash".
- Fixture library / profile names: Chauvet Professional "Maverick MK3 Wash". Pick Single or Dual (Function + Pixel).
- Variants and how to tell them apart: 27-cell RGBW pixel wash. The MK3 Spot/Profile are the CMY/gobo siblings ([page](maverick-mk3-spot.md)). The MK2 Wash is the older generation.

## Passwords, menu locks & hidden menus
- Default passcode: Not found — fill in from the fixture. Sibling MK3 models use **2323** for Offset/Zero Adjust (⚠️ unverified here).
- Service menu: Not found.
- Display unlock: Not found. The MK3 Profile uses UP, DOWN, UP, DOWN, ENTER (⚠️ sibling model).

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | 9.51 | 5.35 | Not found |
| Power (W) | 1,120 | 1,090 | Not found |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | floor(16/9.51)=1 → **1** | floor(16/5.35)=2 → **2** | Not found |

- If Chauvet's 12 A rule applies: floor(12/9.51)=1 and floor(12/5.35)=2, which gives the same answer.
- Input range: 100–240 VAC, 50/60 Hz, auto-ranging.
- Connectors in / out: Not found — fill in from the fixture.
- Fuse: Not found.

## Data & addressing
- Connectors: 3-pin and 5-pin DMX in and out. 2 × Amphenol XLRnet (RJ45 in an XLR-style locking shell) through ports.
- Protocols: DMX, W-DMX, Art-Net, sACN, Kling-Net.
- DMX modes / footprints: Single 20 / 129 / 243 / 297. Dual Function 9 / 21 / 27. Dual Pixel 81 / 108 / 216.
- Set the address: Not found.
- Battery addressing: Not found.
- Factory reset: Not found.
- Wireless / Ethernet: W-DMX built in. Ethernet through XLRnet ports.

## Rigging & hardware
- Bracket / omega: Not found.
- Fasteners: Not found.
- Safety cable point: Not found.
- Orientations: Not found.
- Transport / pan-tilt locks: Not found — TBD check on next show.
- Weight / dimensions: 68.2 lb (31 kg). Dimensions not found.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD – check on next show |
| Gobo / effects module access | n/a | n/a |
| Lens / front glass | TBD – check on next show | TBD – check on next show |
| Omega bracket | TBD – check on next show | TBD – check on next show |

## Optics & consumables
- Source: 27 × 40 W RGBW LEDs, pixel-controllable.
- Color system: RGBW.
- Zoom: yes (per retailer title). Range not found.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Not found | — | Fill in from the fixture |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| 2 on one 120 V circuit trip the breaker | 2 × 9.51 = 19 A | 1 per 120 V circuit. Use 208 V (2 per circuit) |
| Pixels respond, pan/tilt don't (or the other way round) | Dual mode with only one address patched | Patch Function + Pixel, or use Single mode |
| No Art-Net/sACN | Using an etherCON cable into an XLRnet port | XLRnet takes plain RJ45 or XLRnet cable. Check seating (general knowledge) |

## Maintenance
- Not found — fill in from the fixture.

## Road notes (community)
- No forum threads turned up in search. Add notes here.

## Sources
- [Maverick MK3 Wash User Manual Rev 1 (Chauvet)](https://www.chauvetprofessional.com/wp-content/uploads/2017/03/Maverick_MK3_Wash_UM_Rev1_WO-1.pdf): 1,120 W / 9.51 A @120 V, 1,090 W / 5.35 A @208 V, auto-ranging, DMX modes, protocols, connectors, weight
- [Maverick MK3 Wash User Manual Rev 6 (Musson mirror)](https://media.musson.com/mti/docs/m/a/maverick_mk3_wash_um_rev6_wo.pdf): same data
- [Maverick MK3 Wash QRG Rev 5](https://media.musson.com/mti/docs/m/a/maverick_mk3_wash_qrg_rev5_ml4_wo.pdf)
- [Full Compass listing](https://www.fullcompass.com/prod/549558-chauvet-pro-maverick-mk-3-wash-27x40w-rgbw-led-moving-head-wash-with-zoom-and-pixel-control): 27 × 40 W RGBW, zoom, pixel control
