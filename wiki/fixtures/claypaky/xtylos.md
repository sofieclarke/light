---
title: "Claypaky Xtylos"
manufacturer: "Claypaky"
model: "Xtylos"
aliases: ["xtylos", "cj3000", "claypaky xtylos", "clay paky xtylos", "laser beam"]
type: "beam"
light_source: "Custom RGB laser module (each colour under 100 W), ~20,000 h"
ip_rating: "IP20"
weight_lb: 52.13
weight_kg: 24
dimensions: "approx. 388 x 582 x 294 mm (W x H x D, QLC+ community data)"
power:
  input: "100-240 V, 50/60 Hz, electronic auto-range with active PFC"
  connector_in: ""
  connector_out: ""
  watts_max: 400
  amps_120v: null
  amps_208v: null
  amps_230v: null
  link_max_120v: null
  link_max_208v: null
  link_max_230v: null
  per_20a_120v: null
  per_20a_208v: null
  fuse: "Bipolar circuit breaker with thermal protection (manufacturer)"
dmx:
  connectors: "5-pin XLR (others not confirmed)"
  protocols: ["DMX", "RDM", "Art-Net", "sACN"]
  modes:
    - { name: "Standard", channels: 31 }
menu_password: null
tools: []
verification: "web-search"
last_updated: "2026-10-03"
---

# Claypaky Xtylos

> **2AM CARD** — the stuff you need first
> - **LASER FIXTURE (US):** using it in the US requires an **FDA CDRH variance** and trained staff. Claypaky runs a Laser Variance Program to help. The Mini Xtylos CJ3003 adjusted-output version is exempt. Big Xtylos isn't.
> - **Password / menu lock:** "Smart Mode" needs a password **from Claypaky** (user menu). Advanced menu code not confirmed for Xtylos. The Claypaky line uses **1234** ⚠️ unverified here.
> - **Power:** 400 VA max @230 V (manufacturer). Amps not published. Derived: ≈3.3 A @120 V → **4 per 20 A @120 V**, ≈1.9 A @208 V → **8 @208 V** ⚠️ derived (active PFC). Link limit not found.
> - **DMX:** one mode, **31 ch**. DMX/RDM/Art-Net/sACN. Reset ch: 128-255 complete.
> - **Tools:** TBD – check on next show

## Identity
- What crews call it: "Xtylos", "the laser Sharpy". Code CJ3000. Xtylos Aqua is CJ3001 (IP66).
- Mini Xtylos HPE = CJ3002 (needs the same FDA variance as Xtylos). Mini Xtylos = CJ3003 (adjusted output, homologated, no variance needed in the US).
- Fixture library / profile names: "Xtylos" single 31-ch mode. Mini Xtylos has 1 mode of 27 ch.

## Passwords, menu locks & hidden menus
- Operating modes in the user menu: **Standard Mode**, **Smart Mode** (password supplied by Claypaky), **Service Mode** (Xtylos User Menu 01.2021 via Christie Lites).
- Advanced menu code: Not found for Xtylos. Try **1234** (line-wide code, confirmed on Sharpy/Sharpy Plus/Mythos) ⚠️ unverified.
- Detailed documentation is on Claypaky's restricted-access Customer Care site.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not published. ≈3.3 A derived (400/120) ⚠️ | Not published. ≈1.9 A derived (400/208) ⚠️ | Not published as amps |
| Power (W) | — | — | 400 VA max @230 V 50 Hz |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | floor(16/3.3)=4 → **4** ⚠️ derived | floor(16/1.9)=8 → **8** ⚠️ derived | — |

- Input range / auto-ranging: 100-240 V 50/60 Hz, electronic auto-range, active PFC. The power supply is thermally protected against overheating and cooling failure.
- Connectors in / out: Not found — fill in from the fixture.
- Fuse: bipolar circuit breaker with thermal protection (no replaceable fuse quoted). If it trips, reset it after the fixture cools ⚠️ procedure unverified.
- Inrush / power-up notes: Not found.

## Data & addressing
- Connectors: 5-pin XLR (QLC+). Ethernet: Not found — fill in from the fixture.
- Protocols: DMX, Art-Net, RDM, sACN.
- DMX modes: one mode, 31 ch. Order (QLC+ community): Red, Red fine, Green, Green fine, Blue, Blue fine, CTO, Show Setup, Dimmer, Dimmer fine, Strobe, Static Gobo, Rotating Gobo, Gobo Rot, Gobo Rot fine, Prisms Wheel change, Prisms Wheel rot, Prism insert, Prism rot, Smart Fading, Focus, Focus fine, Pan, Pan fine, Tilt, Tilt fine, Function, Reset, Function 2, Frequency, BAZ Fading.
- Control values (QLC+ community): Reset 26-76 effects, 77-127 pan/tilt, 128-255 complete. Function 38-50 conventional dimmer curve, 63-75 CMY shortcut ON, 76-88 CMY shortcut OFF.
- Set the address: display menu. Not sourced for this model.
- Factory reset: Not found.

## Rigging & hardware
- Bracket / omega: Not found — fill in from the fixture.
- Transport locks: Not found — fill in from the fixture.
- Weight / dimensions: 24 kg (52.13 lb).
- Pan 540° / tilt 250° (QLC+ community).

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD – check on next show |
| Gobo / effects module access | TBD – check on next show | TBD – check on next show |
| Lens / front glass | TBD – check on next show | TBD – check on next show |
| Omega bracket | TBD – check on next show | TBD – check on next show |

## Optics & consumables
- Source: sealed custom RGB laser module, each colour under 100 W. Life about 20,000 h with minimal decay (manufacturer).
- Color system: RGB additive plus CTO.
- Gobo wheels: 7 rotating gobos. Static wheel with 12 slots (5 gobos + 7 beam reducers). Gobo size: Not found.
- Prism / zoom: prism wheel plus prism. Zoom 1-7°.
- Safety firmware: RGB colour calibration, RGB derating, and laser-driver safety logic that switches the output off safely if parameters leave the working range (manufacturer).

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Light output shuts off | Laser driver safety logic: a parameter (e.g. temperature) is out of range | Check fans and ambient temperature, let it cool, power-cycle. Call Claypaky service if it repeats ⚠️ inferred from manufacturer description |
| Specific error code strings | Not found — fill in from the fixture | |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Dead, breaker tripped | Thermal breaker tripped | Let it cool, reset the breaker, check airflow ⚠️ |
| Output dims over a long show | RGB derating (thermal) | Improve airflow / lower ambient temperature ⚠️ |

## Maintenance
- Recalibrate / reset: DMX Reset 128-255.
- Fan / filter cleaning: forced ventilation with heat sinks. Cleaning procedure: Not found.
- Firmware update method: see [_claypaky-common.md](_claypaky-common.md).

## Road notes (community)
- US variance paperwork has to be in place before the gig, not on the day. Rental houses usually hold the variance and require a trained operator on site (Claypaky/FDA variance summaries).
- No forum road notes sourced.

## Sources
- [Xtylos User Menu 01/2021 (Christie Lites)](https://www.christielites.com/file_uploads/Xtylos_UserMenu_01_2021.pdf) — Standard / Smart (Claypaky password) / Service modes
- [Xtylos User Information (lightwaveproductions mirror)](https://cdn.lightwaveproductions.co.uk/manuals/lighting/moving-lights/clay-paky-xtylos-manual.pdf), [ManualsLib Xtylos user information](https://www.manualslib.com/manual/1841066/Osram-Claypaky-Xtylos.html), [Xtylos datasheet (manualzz)](https://manualzz.com/doc/59296811/clay-paky-cj3000-xtylos-instruction-manual) — 100-240 V, 400 VA @230 V
- [Claypaky Xtylos product page](https://www.claypaky.it/products/xtylos/), [Mini Xtylos page](https://www.claypaky.it/products/mini-xtylos/), [Xtylos family](https://www.claypaky.it/family/xtylos/) — laser module, 20,000 h, PFC, FDA variance / Laser Variance Program, CJ3003 exemption
- [B&H Xtylos CJ3000](https://www.bhphotovideo.com/c/product/1787603-REG/astera_cj3000e41100s_xtylos_laser_beam_moving.html), [Farralane Xtylos](https://www.farralane.com/clay-paky-xtylos-rgb-laser-moving-head-beam.html) — weight, gobos, breaker, safety logic, 1-7° zoom, 31 ch
- [Mike Wood "Product In Depth: Xtylos" L&SA Aug 2020](https://www.mikewoodconsulting.com/articles/ClaypakyXtylos.pdf) — background (content not quoted)
- QLC+ Clay-Paky-Xtylos.qxf (github.com/mcallegari/qlcplus, commit 1ccdab8) — channel order, control values, dimensions (community)
