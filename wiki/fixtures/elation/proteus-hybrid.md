---
title: "Elation Proteus Hybrid"
manufacturer: "Elation Professional"
model: "Proteus Hybrid"
aliases: ["proteus hybrid", "proteus hybrid wmg", "proteus 3-in-1"]
type: "hybrid"
light_source: "Philips MSD Platinum 21R 470W discharge, 8,000K"
ip_rating: IP65
weight_lb: 84
weight_kg: 38
dimensions: null
power:
  input: "AC 100–240 V, 50/60 Hz, auto-switching"
  connector_in: "Neutrik powerCON TRUE1"
  connector_out: null
  watts_max: 700
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
  connectors: "IP-rated 5-pin XLR in/out, RJ45 ethernet in/out"
  protocols: ["DMX", "RDM", "Art-Net", "sACN", "E-FLY wireless"]
  modes:
    - { name: "24ch", channels: 24 }
    - { name: "26ch", channels: 26 }
    - { name: "37ch", channels: 37 }
menu_password: "050"
firmware:
  latest_known: null
  checked: "2026-10-03"
  check_on_fixture: null
  methods: ["E-LOADER III over 3-pin DMX (Elation's general method, not confirmed for this model)"]
  interface: "Elation E-LOADER III (ELO601)"
  software: null
  file_type: null
  download: null
tools: []
verification: "web-search"
last_updated: "2026-10-03"
---

# Elation Proteus Hybrid

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** Service/calibration password **050**, factory-reset password **011** (Proteus-series manuals ⚠️ not confirmed in this exact manual). Lamp hours on Elation hybrids are reset behind a lamp-time password; the Smarty Hybrid uses **038** ⚠️ unverified for the Proteus Hybrid.
> - **Power:** Elation's amps per voltage not found. Max 700 W. Estimate (⚠️ watts÷volts, not Elation's figure): ~5.8 A @120 V → **2 per 20 A @120 V**; ~3.4 A @208 V → **4 per 20 A @208 V**. Power-link limit: not found.
> - **DMX:** 24 / 26 / 37 ch. DMX, RDM, Art-Net, sACN, E-FLY wireless built in. Battery display lets you address it unpowered.
> - **Lamp:** 1,500 h rated. "Replace the Lamp" warning, then **hard shutdown/hibernation at 1,800 h** until the lamp is changed **and** lamp hours reset.
> - **Ballast error:** lamp OFF 3–5 min → still there? power-cycle fixture → still there? call Elation.
> - **Tools:** TBD – check on next show.

## Identity
- What crews call it: "Proteus Hybrid".
- Fixture library / profile names (MA3, GDTF, Hog, Eos): Not found — fill in from the console library.
- Variants and how to tell them apart: **Proteus Hybrid** and **Proteus Hybrid WMG** (Elation sells a separate WMG product, white housing per general knowledge). Not the same fixture as the **Proteus Hybrid Max** (bigger, separate manual) or the **Proteus Smarty Hybrid** (smaller).

## Passwords, menu locks & hidden menus
- **Service password 050**: required each time you open the calibration/service menus. From Proteus-series manuals (Odeon, Excalibur, Hybrid Max, Rayzor 760, Radius). ⚠️ unverified for this model.
- **Reset-defaults password 011**: same source and caveat.
- **Lamp-hours reset**: required after a lamp change, or the fixture keeps hibernating. Menu path / password for this model: Not found. The Smarty Hybrid uses Information → Time Information → LampTime Password **038** ⚠️ unverified here.
- Unlock a locked display: Not found — fill in from the fixture.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found (est. 700/120 = 5.8 ⚠️) | Not found (est. 700/208 = 3.4 ⚠️) | Not found (est. 700/230 = 3.0 ⚠️) |
| Power (W) | 700 max | 700 max | 700 max |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | est. floor(16/5.8)=2 → **2** ⚠️ | est. floor(16/3.4)=4 → **4** ⚠️ | n/a |

- Input range / auto-ranging: AC 100–240 V, 50/60 Hz, universal auto-switching.
- Connectors in / out: powerCON TRUE1 in. Sources conflict on a power-out: one dealer summary said input only, but the manual warns "USE CAUTION WHEN POWER LINKING OTHER MODEL FIXTURES AS THE POWER CONSUMPTION OF OTHER MODEL FIXTURES MAY EXCEED THE MAX POWER OUTPUT ON THIS FIXTURE", which implies a TRUE1 out exists. Check the fixture.
- Fuse (type, rating, location): Not found — fill in from the fixture.
- Inrush / power-up notes: on power-up the fixture enters Reset/Test (homes all motors).

## Data & addressing
- Connectors: IP-rated 5-pin XLR and RJ45 ethernet in/out (B&H / Full Compass listings).
- Protocols: DMX, RDM, Art-Net, sACN; built-in Elation **E-FLY** wireless DMX transceiver.
- DMX modes / footprints: 24 / 26 / 37 ch.
- Set the address: Main menu → DMX Settings → DMX Address (001–512) (Proteus manuals) ⚠️ verify button path.
- Battery / unpowered addressing: internal battery powers the display for setting address/mode with no mains. Wake it by **holding MODE/ESC 10 s** (one Proteus manual) or **holding ENTER 3 s** (another). Display sleeps ~1 min after the last press.
- Factory reset: reset menu, password 011 (Proteus series ⚠️).
- Wireless / Ethernet setup notes: Not found.

## Rigging & hardware
- Bracket / omega type and clamp spacing: Not found — fill in from the fixture.
- Fasteners: Not found.
- Safety cable point: Not found.
- Mounting orientations allowed: Not found.
- Transport / pan-tilt locks (location): Not found — TBD – check on next show.
- Weight / dimensions: 84 lb / 38 kg; dimensions not found.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD |
| Gobo / effects module access | TBD – check on next show | TBD |
| Lens / front glass | TBD – check on next show | TBD |
| Omega bracket | TBD – check on next show | TBD |

## Optics & consumables
- Source / lamp, lamp life: Philips **MSD Platinum 21R 470 W**, 8,000 K, 23,000 lumens (Full Compass / B&H). Rated life 1,500 h; fixture allows 300 h grace, then hibernates at 1,800 h (manual text per search summary — ⚠️ the summary may have mixed in a sibling Proteus manual; confirm on the fixture's info menu).
- Color system: Not found in sourced text.
- Gobo wheels: **8 rotating interchangeable glass & metal gobos + 14 static stamped gobos.**
- Gobo size: **OD 16.6 mm / ID (image) 9.0 mm**. Thickness: Not found.
- Prism / frost / zoom / iris / shutters: Not found in sourced text.
- Gobo / module change procedure: Not found.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| `XXer` (flashing) | Motor/function error; XX = function number | Auto-retry; then power-cycle, check for jam/lock |
| `0Er` | Pan motor error | Check pan lock / obstruction |
| Pan Er, Tilt Er, Cyan Wheel Er, Dimmer Er … | Named function errors listed in manual p.48 | Recalibrate (service password 050) or service |
| Ballast error | Ballast fault / overheat / bad lamp | Lamp OFF 3–5 min; if still present power fixture off; if still present call Elation support |
| "Replace the Lamp" (flashing) | Lamp past 1,500 h rated life | Change lamp within 300 h; reset lamp hours |
| Hibernation / no DMX response | Lamp past 1,800 h | Replace lamp **and** reset lamp clock — only a few menu items work until then |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Fixture ignores DMX, menu mostly dead | Lamp clock over 1,800 h → hibernation | Lamp change + lamp-hours reset |
| Old lamp flickers then strikes after ~5 min | Lamp at end of life (manual describes this) | Run temporarily, replace ASAP |
| Ballast error after hot restrike | Ballast needs to cool | Lamp off 3–5 min |

## Maintenance
- Recalibrate / reset procedure: calibration menu behind password 050 (Proteus series).
- Fan / filter cleaning: Not found.

## Firmware
- Installed version — where to see it on the fixture: not found in the sources read.
- Latest known version (date checked) and where to download it: **not found** (checked 2026-10-03). No Elation forum firmware thread for the plain Proteus Hybrid turned up. Don't load **Proteus Hybrid MAX** files (the MAX thread lists V1.3.7, and V1.3.6 for the MAX OPS). That's a different fixture.
- What you need: Elation's general tool is the **E-LOADER III** (battery handheld, micro SD card, **3-pin DMX cable**) ⚠️ not confirmed for this model. Whether this model has a USB service port was not confirmed.
- Update steps: see the E-LOADER III procedure in [_elation-common.md](_elation-common.md#firmware-updates).
- Updating a whole rig: one fixture at a time with the E-LOADER III. No batch method found.
- If it fails or bricks mid-update: no recovery procedure found. Contact Elation service.
- Release notes worth knowing: none found. Write down your menu settings first. **Firmware cannot be downgraded** (Elation general rule).

## Road notes (community)
- None found in this pass (Reddit/ControlBooth searches returned nothing model-specific). ⚠️ Add from techs.
- Elation forum (general hybrids): a bad lamp can itself cause ballast errors; the ballast is in the base of the hybrid fixtures (forums.elationlighting.com — community).

## Sources
- [Proteus Hybrid user manual 4-2 (BMI Supply mirror)](https://shop.bmisupply.com/Resources/en/ItemDocuments/39E1018/BMI.Elation.Proteus.Hybrid.Fixture.Manual.pdf) — error code format, ballast error recovery, lamp life/hibernation, battery display
- [Proteus Hybrid manual on ManualsLib, error codes p.48](https://www.manualslib.com/manual/2938151/Elation-Proteus-Hybrid.html?page=48) — named error list, power-linking caution
- [Proteus Hybrid manual (ADJ media S3)](http://adjmedia.s3-website-eu-west-1.amazonaws.com/binaries/ELATION%20PROTEUS%20HYBRID%20-%20USER%20MANUAL.pdf) — battery display operation
- [Proteus Hybrid manual (4Wall CDN)](https://cdn01.4wall.com/cms/rentals/files/f5c587735059ca.pdf) — XLR/RJ45 connectors, 700 W, 100–240 V
- [Full Compass listing](https://www.fullcompass.com/prod/531452-elation-proteus-hybrid-470w-discharge-ip65-rated-hybrid-moving-head-beam-spot-wash-fixture), [B&H listing](https://www.bhphotovideo.com/c/product/1335510-REG/elation_professional_proteus_hybrid_ip.html) — 84 lb/38 kg, 24/26/37 ch, lamp, gobo OD/ID, gobo counts, E-FLY, TRUE1 input
- [elationlighting.com Proteus Hybrid](https://www.elationlighting.com/products/proteus-hybrid) — 700 W, 100–240 V
- Proteus-series manuals for passwords 050/011: [Odeon](https://goknight.com/content/documentation/ELATION%20PROTEUS%20ODEON%20-%20USER%20MANUAL.pdf), [Excalibur](https://d295jznhem2tn9.cloudfront.net/ItemRelatedFiles/12937/ELATION%20PROTEUS%20EXCALIBUR%20-%20USER%20MANUAL.pdf), [Hybrid Max](https://d295jznhem2tn9.cloudfront.net/ItemRelatedFiles/13622/ELATION%20PROTEUS%20HYBRID%20MAX%20-%20USER%20MANUAL.pdf)
- [Elation forum: Proteus Beam Hybrid ballast error](https://forums.elationlighting.com/topic/proteous-beam-hybrid-ballast-error) — community ballast notes
- [Elation forum: Proteus Hybrid MAX Firmware](https://forums.elationlighting.com/topic/proteus-hybrid-max-firmware?nc=1): MAX versions, so you don't load the wrong file (search summary)
- [E-LOADER III](https://www.elationlighting.com/e-loader-iii-software-uploader) and [E-LOADER III manual (manuals.plus)](https://manuals.plus/elation/professional-e-loader-iii-software-uploader-kit-manual): uploader procedure (search summary)
