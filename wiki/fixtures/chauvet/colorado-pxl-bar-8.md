---
title: "Chauvet Professional COLORado PXL Bar 8"
manufacturer: "Chauvet Professional"
model: "COLORado PXL Bar 8"
aliases: ["pxl bar 8", "pxl 8", "colorado pxl 8", "coloradopxlbar8", "bar pxl 8", "half pxl", "pixel bar 8"]
type: "pixel-bar"
light_source: "LED 8x 45W RGBW"
ip_rating: IP65
weight_lb: 25.2
weight_kg: 11.5
dimensions: "19.69 x 5.47 x 10.75 in (500 x 139 x 273 mm)"
power:
  input: "100–240 VAC, 50/60 Hz, auto-ranging"
  connector_in: null
  connector_out: null
  watts_max: 422
  amps_120v: 3.497
  amps_208v: 2.013
  amps_230v: 1.830
  link_max_120v: 3
  link_max_208v: 5
  link_max_230v: 6
  per_20a_120v: 3
  per_20a_208v: 5
  fuse: null
dmx:
  connectors: "IP65 5-pin XLR in/out, IP65 Ethernet in/out (⚠️ assumed same as PXL Bar 16)"
  protocols: ["DMX", "RDM", "Art-Net", "sACN"]
  modes:
    - { name: "Single – Basic", channels: 19 }
    - { name: "Single – Standard", channels: 51 }
    - { name: "Single – Advanced", channels: 89 }
    - { name: "Single – Tour", channels: 105 }
    - { name: "Dual Movement – Basic", channels: 7 }
    - { name: "Dual Movement – Standard", channels: 19 }
    - { name: "Dual Movement – Advanced", channels: 25 }
    - { name: "Dual Pixels – Basic", channels: 24 }
    - { name: "Dual Pixels – Standard", channels: 32 }
    - { name: "Dual Pixels – Advanced", channels: 64 }
menu_password: "2323"
tools: []
verification: "web-search"
last_updated: "2026-10-03"
---

# Chauvet Professional COLORado PXL Bar 8

> **2AM CARD** — the stuff you need first
> - **Power:** 3.497 A @120 V / 2.013 A @208 V / 1.830 A @230 V → **3 per circuit @120 V, 5 @208 V, 6 @230 V** (Chauvet link limits 3 / 5 / 6, plus "never exceed 12 A on a single circuit")
> - **Not a PXL Bar 16.** The Bar 16 links **0 @120 V and 3 @208 V**. Check which bar you have before you chain.
> - **Password:** press and hold **MENU** → passcode screen → **2323** (Offset / Zero Adjust)
> - **DMX:** Single 19/51/89/105, Dual Movement 7/19/25, Dual Pixels 24/32/64. Dual modes need **two addresses**.
> - **Won't tilt / Y_op:** tilt optocoupler error. Check the head-to-base connection first.
> - **Tools:** TBD – check on next show.

## Identity
- What crews call it: "PXL Bar 8", "half PXL", "short PXL".
- Fixture library / profile names: Chauvet Professional "COLORado PXL Bar 8". Chauvet's GitHub repo: github.com/Chauvet-Pro/COLORADOPXLBAR8 (⚠️ unverified what it contains).
- Variants and how to tell them apart: 500 mm long with 8 cells. The PXL Bar 16 is 1 m with 16 cells ([page](colorado-pxl-bar-16.md)). The PXL Curve 12 has individually tilting heads ([page](colorado-pxl-curve-12.md)).

## Passwords, menu locks & hidden menus
- **Offset Mode / Zero Adjust: passcode 2323.** Press and hold **MENU** until the passcode screen appears, enter 2323, and you land in the Zero Adjust screen.
- Web server login: Not found for this model. The PXL Bar 16 uses admin / admin (⚠️ unverified for the Bar 8).
- Service / factory menu: Not found — fill in from the fixture.
- How to unlock a locked display: Not found — fill in from the fixture. The OLED display "offers password protection" per a retailer listing.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | 3.497 | 2.013 | 1.830 |
| Power (W) | 422 | 409 | 407 |
| Max power-link (manufacturer) | 3 | 5 | 6 |
| **Max per 20 A circuit** (16 A continuous) | floor(16/3.497)=4, Chauvet 12 A rule floor(12/3.497)=3 = link 3 → **3** | floor(16/2.013)=7, floor(12/2.013)=5 = link 5 → **5** | floor(16/1.830)=8, floor(12/1.830)=6 = link 6 → **6** |

- **How to read the link limit.** The manual says you can "power link 3 @ 120 V, 5 @ 208 V, 6 @ 230 V… before exceeding circuit breaker limits" and "never exceed 12 A on a single circuit". Each number equals the most bars that fit under 12 A (3 × 3.497 = 10.5 A, but 4 = 14.0 A; 5 × 2.013 = 10.1 A, but 6 = 12.1 A). So the count is **total bars on the circuit**, not bars after the first.
- Input range / auto-ranging: 100–240 VAC, 50/60 Hz, auto-ranging.
- Connectors in / out: Not found in the search excerpts. Probably TRUE1-compatible IP65 like the PXL Bar 16 (⚠️ unverified). Power-linking cables are sold separately.
- Fuse (type, rating, location): Not found — fill in from the fixture.
- Inrush / power-up notes: none found.

## Data & addressing
- Connectors: ⚠️ unverified. Expect IP65 DMX and Ethernet like the PXL Bar 16.
- Protocols: DMX, RDM, Art-Net, sACN (⚠️ from the family spec, unverified for this exact model).
- DMX modes / footprints:

| Family | Basic | Standard | Advanced | Tour |
|---|---|---|---|---|
| Single Mode | 19 | 51 | 89 | 105 |
| Dual Mode – Movement | 7 | 19 | 25 | — |
| Dual Mode – Pixels | 24 | 32 | 64 | — |

- Set the address: Not found — fill in from the fixture.
- Battery / unpowered addressing: Not found.
- Factory reset: listed as a fix in the error table. Menu location not found.
- Wireless / Ethernet setup notes: Not found.

## Rigging & hardware
- Bracket / omega type and clamp spacing: Not found. Probably the same slotted Omega bracket as the Bar 16 (⚠️ unverified).
- Fasteners: Not found.
- Safety cable point: Not found. Always use one overhead.
- Mounting orientations allowed: Not found.
- Transport / pan-tilt locks (location): Not found. On the Bar 16 the tilt lock is maintenance-only, not for transport (⚠️ unverified for the Bar 8).
- Weight / dimensions: 25.2 lb (11.5 kg). 19.69 x 5.47 x 10.75 in (500 x 139 x 273 mm).

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD – check on next show |
| Gobo / effects module access | n/a | n/a |
| Lens / front glass | TBD – check on next show | TBD – check on next show |
| Omega bracket | TBD – check on next show | TBD – check on next show |

## Optics & consumables
- Source: 8 × 45 W RGBW LEDs.
- Color system: RGBW.
- Gobo wheels: none.
- Zoom: **3.6°–47.3°** (single cell 4°–45.5°) per a rental/retailer spec. Farralane lists 3.5°–47.3°.
- Gobo / module change: n/a.

## Error codes
| Code / message | Meaning | Fix (from manual) |
|---|---|---|
| Base Fan1 | Base fan 1 error | Check fan connection → replace fan |
| FAN1 / FAN4 / FAN5 (FANx) | Fan error | Check fan connection → replace fan → check the head-to-base connection |
| Y_op | Tilt optocoupler error | Check the head-to-base connection → factory reset → update reset → replace sensor → replace motor |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Breaker trips with 4+ bars on one 120 V circuit | 4 × 3.497 = 14 A, over the link limit | 3 per 120 V circuit, or run 208 V (5 per circuit) |
| Y_op / no tilt | Tilt sensor / head-base connection | See error table |
| Half the functions dead | Dual mode with only one address patched | Patch both blocks, or use a Single mode |

## Maintenance
- Recalibrate: Zero Adjust via passcode 2323.
- Fan / filter cleaning: Not found.
- Firmware update method: USB. Same procedure as the PXL Bar 16 (USB UPDATE prompt → YES, don't pull the drive while the LED blinks) — ⚠️ assumed from the family, not confirmed in the Bar 8 excerpts.

## Road notes (community)
- No forum threads turned up in search. Add notes here.

## Sources
- [COLORado PXL Bar 8 User Manual Rev 9 (Chauvet)](https://www.chauvetprofessional.com/wp-content/uploads/2021/11/COLORado_PXL-Bar_8_UM_Rev9.pdf): current/power table, link limits, 12 A rule, passcode 2323, error codes
- [User Manual Rev 12 (voltlites mirror)](https://voltlites.com/wp-content/uploads/2026/03/COLORado_PXL-Bar_8_UM_Rev12.pdf), [Rev 11 (saleswl mirror)](https://saleswl.com/wp-content/uploads/2023/01/Chauvet-Professional-COLORado-PXL-Bar-8-User-Guide.pdf), [parlights mirror](https://parlights.com/wp-content/uploads/2024/03/COLORADO-PXL-BAR-8-MANUAL-1.pdf), [Rev 1 (Hibino)](https://www.hibinolighting.co.jp/hibino_wp/wp-content/uploads/2022/09/COLORado_PXL_Bar_8_UM_Rev1.pdf): electrical and error tables
- [4Wall rental listing](https://www.4wall.com/rentals/9759046/chauvet-professional-colorado-pxl-bar-8-ip65), [B&H](https://www.bhphotovideo.com/c/product/1691786-REG/chauvet_professional_coloradopxlbar8_colorado_pxl_bar_8_rgbw.html), [TS Stage](https://tsstage.com/products/colorado-pxl-bar-8): DMX modes, weight, dimensions, zoom
- [Farralane listing](https://www.farralane.com/chauvet-pro-colorado-pxl-bar-8-8-x-45w-rgbw-led-outdoor-motorized-tilting-batten-with-zoom.html): 3.5°–47.3° zoom (disagrees slightly)
