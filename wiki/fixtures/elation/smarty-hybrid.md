---
title: "Elation Smarty Hybrid"
manufacturer: "Elation Professional"
model: "Smarty Hybrid"
aliases: ["smarty hybrid", "smarty", "esh253", "smarty hybrid fil"]
type: "hybrid"
light_source: "Philips MSD Platinum 200 Flex discharge, selectable 190/240/280W"
ip_rating: null
weight_lb: 49.0
weight_kg: 22.2
dimensions: "15.2 in W x 15.9 in D x 24.0 in H"
power:
  input: "AC 100–240 V, 50/60 Hz, auto-switching"
  connector_in: "Neutrik powerCON TRUE1"
  connector_out: "Neutrik powerCON TRUE1"
  watts_max: 480
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
  connectors: null
  protocols: []
  modes:
    - { name: "20ch", channels: 20 }
    - { name: "34ch", channels: 34 }
menu_password: "038"
tools: []
verification: "web-search"
last_updated: "2026-10-03"
---

# Elation Smarty Hybrid

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** Lamp-hours reset passcode **038**: MODE/ESC → Information → Time Information → LampTime Password → 038. Service menu password on other Elation Proteus fixtures is **050** ⚠️ unverified on this one.
> - **Power:** Elation's amps per voltage not found. 480 W max (420 W typical). Estimate (⚠️ watts÷volts, not Elation's figure): 4.0 A @120 V → **4 per 20 A @120 V**; ~2.3 A @208 V → **6 per 20 A @208 V**. Has TRUE1 power out; Elation's link limit not found — don't exceed the circuit math.
> - **DMX:** 20 or 34 ch.
> - **Lamp warning:** YELLOW outline = 20 % lamp life left; RED = life exceeded. Clear the warning with **DMX value 250–251** (control channel ⚠️ check chart) or **OK** on the panel. After a lamp change, **reset lamp hours** or protection may shut the lamp off.
> - **Tools:** TBD – check on next show.

## Identity
- What crews call it: "Smarty", "Smarty Hybrid".
- Fixture library / profile names (MA3, GDTF, Hog, Eos): Not found — fill in from the console library.
- Variants and how to tell them apart: **Smarty Hybrid** (indoor; sold as "Smarty Hybrid FIL" with foam inlay, part ESH253). The **Proteus Smarty Hybrid** is a *different*, IP65 outdoor fixture with its own manual. **Smarty Max** is a bigger sibling. Check the label before using this page.

## Passwords, menu locks & hidden menus
- **Lamp-time reset password 038.** Path: press MODE/ESC → "Information" → ENTER → UP/DOWN to "Time Information" → "LampTime Password" → enter 038 (from the Smarty Hybrid manual, per search summary).
- Service / calibration menu: password not confirmed for this model. Elation Proteus manuals use **050** ⚠️ unverified here.
- Factory reset password: Proteus manuals use **011** ⚠️ unverified here.
- Unlock a locked display: Not found — fill in from the fixture.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found (est. 480/120 = 4.0 ⚠️) | Not found (est. 480/208 = 2.3 ⚠️) | Not found (est. 480/230 = 2.1 ⚠️) |
| Power (W) | 480 max / 420 typical | 480 max | 480 max |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | est. floor(16/4.0)=4 → **4** ⚠️ | est. floor(16/2.3)=6 → **6** ⚠️ | n/a |

- Input range / auto-ranging: AC 100–240 V, 50/60 Hz, universal auto-switching.
- Connectors in / out: Neutrik powerCON TRUE1 in / out.
- Fuse (type, rating, location): Not found — fill in from the fixture.
- Inrush / power-up notes: on power-up enters Reset/Test (homes all motors). Discharge-lamp fixture — expect a restrike/cool-down delay after a power blip (general knowledge).

## Data & addressing
- Connectors: Not found in sourced text — fill in from the fixture.
- Protocols: Not found in sourced text (RDM etc. unconfirmed).
- DMX modes / footprints: 20 / 34 ch.
- Set the address: Not found button-by-button — main menu is entered with MODE/ESC, navigate with UP/DOWN, ENTER to select (from the lamp-reset path).
- Battery / unpowered addressing: Not found for this model.
- Factory reset: Not found.
- Wireless / Ethernet setup notes: Not found.

## Rigging & hardware
- Bracket / omega type and clamp spacing: Not found.
- Fasteners: Not found.
- Safety cable point: Not found.
- Mounting orientations allowed: Not found.
- Transport / pan-tilt locks (location): Not found — TBD – check on next show.
- Weight / dimensions: 49.0 lb / 22.2 kg; 15.2" W × 15.9" D × 24.0" H.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD |
| Gobo / effects module access | TBD – check on next show | TBD |
| Lens / front glass | TBD – check on next show | TBD |
| Omega bracket | TBD – check on next show | TBD |

## Optics & consumables
- Source / lamp, lamp life: **Philips MSD Platinum 200 Flex**, runs at 190 / 240 / 280 W; up to 6,000 h lamp life (long-life mode). Replace when the display says so — manual warns overrun lamps risk the optics and lamp explosion.
- Color system: Full CMY + color wheel with 13 colors incl. quad color, CTB, CTO, UV.
- Gobo wheels: **8 rotating interchangeable glass gobos + 12 stamped static metal gobos** (two wheels).
- Gobo size: **OD 14 mm (−0.2 to −0.3 mm)**, **image 7 mm**, **thickness 1.1 mm ±0.1**, Borofloat glass.
- Prism / frost / zoom: 16-facet and 4-facet linear rotating prisms. Zoom 1°–18° beam, 3°–27° spot, 5°–33° wash.
- Gobo / module change procedure: Not found.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| `XXer` (flashing at startup) | Motor/function error; XX = function number (manual p.38) | Power-cycle; check for jam / locks; recalibrate |
| Yellow outline on display | ≤20 % lamp life remaining | Plan a lamp change |
| Red outline on display | Lamp life exceeded | Replace lamp; reset lamp hours (038). Warning clears with DMX 250–251 or OK |
| Ballast error | Ballast fault / bad lamp | Elation hybrid guidance: lamp off 3–5 min, then power-cycle (Proteus Hybrid manual) ⚠️ confirm for Smarty |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Lamp shuts off during show after lamp change | Lamp hours not reset → protection circuit | Reset lamp time, password 038 |
| Ballast errors | Bad lamp can cause it (Elation forum) | Try a known-good lamp |
| Fans loud | Fan mode | Set quieter fan mode in menu or via DMX (Elation forum/FAQ) |

## Maintenance
- Recalibrate / reset procedure: Not found for this model.
- Fan / filter cleaning: Not found.
- Firmware update method: Elation forum has a "Smarty Hybrid Firmware" thread. Elation methods: **E-LOADER III** over 3-pin DMX, or FAT32 USB on models with USB (⚠️ unconfirmed for this model). Note settings first; no downgrades.

## Road notes (community)
- Elation community forum: ballast sits in the base on Elation hybrids; a bad lamp can throw ballast errors — swap the lamp before condemning the ballast. (forums.elationlighting.com)

## Sources
- [Smarty Hybrid manual on ManualsLib](https://www.manualslib.com/manual/1429186/Elation-Smarty-Hybrid.html) and [error codes p.38](https://www.manualslib.com/manual/1429186/Elation-Smarty-Hybrid.html?page=38) — XXer error format, lamp warnings, lamp-time reset path and passcode 038
- [Smarty Hybrid user manual (Cloudfront)](https://d295jznhem2tn9.cloudfront.net/ItemRelatedFiles/12026/ELATION%20SMARTY%20HYBRID%20-%20USER%20MANUAL.pdf) and [prolighting.de manual 2023-06-15](https://images.prolighting.de/manuals/1237000180_smarty_hybrid_-_user_manual_4.pdf) — gobo dimensions, lamp replacement warning
- [Smarty Hybrid user manual (cdb S3)](https://cdb.s3.amazonaws.com/ItemRelatedFiles/11297/ELATION%20SMARTY%20HYBRID%20-%20USER%20MANUAL%20.pdf) — TRUE1 in/out, 480 W
- [elationlighting.com Smarty Hybrid](https://www.elationlighting.com/products/smarty-hybrid), [PLSN review](https://plsn.com/archives/august-2018/elation-smarty-hybrid/) — 480 W max / 420 W typical, lamp wattages
- [Full Compass](https://www.fullcompass.com/prod/563713-elation-smarty-hybrid-280w-long-life-discharge-hybrid-beam-spot-wash-fixture-with-zoom-and-cmy-fil-insert), [B&H](https://www.bhphotovideo.com/c/product/1454631-REG/elation_professional_smarty_hybrid_fil_cmy_280w_color_mixing.html), [Stage Lighting Store ESH253](https://www.stagelightingstore.com/Smarty-Hybrid-FIL) — weight, 20/34 ch, zoom ranges, prisms, colors, dimensions, gobo counts
- [Elation forum: Smarty Hybrid](https://forums.elationlighting.com/topic/smarty-hybrid?nc=1), [Proteus Beam Hybrid ballast error](https://forums.elationlighting.com/topic/proteous-beam-hybrid-ballast-error), [Elation FAQ/Troubleshooting](https://www.elationlighting.com/pages/faq-troubleshooting) — ballast/lamp and fan notes
- [Elation forum: Smarty Hybrid Firmware](https://forums.elationlighting.com/topic/smarty-hybrid-firmware?nc=1) — firmware thread
