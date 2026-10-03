---
title: "Elation Proteus Maximus"
manufacturer: "Elation Professional"
model: "Proteus Maximus"
aliases: ["proteus maximus", "maximus", "proteus max profile", "proteus maximus wmg", "prm992"]
type: "profile"
light_source: "LED 950W white engine, 6,500K, CRI 70+"
ip_rating: IP65
weight_lb: 117
weight_kg: 53
dimensions: null
power:
  input: "AC 100–240 V, 50/60 Hz (one summary of the same manual says 120–240 V)"
  connector_in: null
  connector_out: null
  watts_max: 1400
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
  protocols: ["DMX", "RDM", "Art-Net", "sACN"]
  modes:
    - { name: "37ch", channels: 37 }
    - { name: "61ch", channels: 61 }
menu_password: "050"
tools: []
verification: "web-search"
last_updated: "2026-10-03"
---

# Elation Proteus Maximus

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** Service/calibration menu password **050**; factory-default reset password **011**. Both are from other Proteus-series manuals (Odeon, Excalibur, Hybrid Max, Rayzor, Radius). ⚠️ unverified on the Maximus itself.
> - **Power:** Elation's amps at each voltage: **not found**. Max draw is **1,400 W**. Planning estimate from watts ÷ volts (⚠️ not Elation's figure): about 11.7 A @120 V → **1 per 20 A circuit @120 V**, about 6.7 A @208 V → **2 per 20 A @208 V**. One dealer listing says **Power Linking: No**, so plan one feed per fixture.
> - **DMX:** 37 ch or 61 ch modes. DMX/RDM/Art-Net/sACN. To address without mains power, use the battery display (see Data & addressing).
> - **Won't move?** Check the **pan lock and tilt lock** first. Startup errors flash as `XXer` (e.g. `0Er` = pan motor).
> - **Tools:** TBD – check on next show. Rigging needs an **M10 or M12** bolt through the omega bracket center hole.

## Identity
- What crews call it: "Maximus", "Proteus Maximus".
- Fixture library / profile names (MA3, GDTF, Hog, Eos): Not found — fill in from the console library.
- Variants and how to tell them apart: **Proteus Maximus** (standard) and **Proteus Maximus WMG** (Elation sells a separate WMG product page; WMG means a white housing (general knowledge)). B&H lists the standard model as part number PRM992.

## Passwords, menu locks & hidden menus
- **Service password 050.** The Proteus manuals say it "MUST be entered" every time you open the calibration/service menus. Source: Proteus Odeon, Excalibur, Hybrid Max, Rayzor 760 and Radius manuals, via a search summary. ⚠️ unverified on the Maximus.
- **Reset-to-default password 011.** Entered each time you restore factory defaults. Same source and caveat.
- How to unlock a locked display: Not found — fill in from the fixture.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found (estimate 1400/120 = 11.7 ⚠️) | Not found (estimate 1400/208 = 6.7 ⚠️) | Not found (estimate 1400/230 = 6.1 ⚠️) |
| Power (W) | 1,400 max (950 W LED engine) | 1,400 max | 1,400 max |
| Max power-link (manufacturer) | "Power Linking: No" per a dealer spec listing ⚠️ | same | same |
| **Max per 20 A circuit** (16 A continuous) | estimate floor(16/11.7) = 1 → **1** ⚠️ | estimate floor(16/6.7) = 2 → **2** ⚠️ | n/a |

- Input range / auto-ranging: AC 100–240 V, 50/60 Hz. One search summary of the same manual said 120–240 V, so check the label on the fixture.
- Connectors in / out: Not found — fill in from the fixture. If the dealer's "Power Linking: No" is right, there is no power out.
- Fuse (type, rating, location): Not found — fill in from the fixture.
- Inrush / power-up notes: At power-up the fixture runs a reset/test (all motors go home). If a motor errors, it retries up to 3 times (Proteus manual error section).

## Data & addressing
- Connectors: Not found. Proteus fixtures generally have IP-rated 5-pin XLR and RJ45 ethernet in/out (general knowledge from the Proteus Hybrid listing) ⚠️ unverified for the Maximus.
- Protocols: DMX, RDM, Art-Net, sACN.
- DMX modes / footprints: 37 ch and 61 ch.
- Set the address: Main menu → DMX Settings → DMX Address (001–512). Path is from Proteus-series manuals ⚠️ unverified button-by-button for the Maximus.
- Battery / unpowered addressing: An internal battery runs the display, so you can set mode and address with the fixture unplugged. Proteus manuals differ on how to wake it: **hold MODE/ESC for 10 s**, or **hold ENTER for 3 s**, depending on which manual. Try both. The display turns off about 1 minute after the last button press.
- Factory reset: Menu reset function, password **011** (Proteus series; ⚠️ unverified on Maximus).
- Wireless / Ethernet setup notes: Not found.

## Rigging & hardware
- Bracket / omega type and clamp spacing: 2 omega brackets in the box. Use only the original omega brackets. Bolt a rated clamp through the bracket's center hole with an **M10 or M12** screw. Clamp spacing: Not found.
- Fasteners (quarter-turn camlocks etc.): Not found — fill in from the fixture.
- Safety cable point: Not found — fill in from the fixture.
- Mounting orientations allowed: Not found.
- Transport / pan-tilt locks (location): Has a **Pan Lock and Tilt Lock**. Engage them for transport and maintenance. Location on the yoke: TBD – check on next show.
- Weight / dimensions: 117 lb / 53 kg. Dimensions not found.
- Ships in a cardboard box with a custom polyurethane foam inlay (FIL) that also fits a custom-sized road case.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD |
| Gobo / effects module access | TBD – check on next show | TBD |
| Lens / front glass | TBD – check on next show | TBD |
| Omega bracket | TBD – check on next show | Clamp bolt M10 or M12 through center hole (manual) |

## Optics & consumables
- Source / lamp, lamp life: 950 W white LED engine, 6,500 K, CRI 70+, up to 50,000 lumens. LED life: Not found.
- Color system: Not found in sourced text. Elation describes it as having color mixing.
- Gobo wheels: 2 wheels, **6 rotating + 7 fixed glass gobos**, plus a full animation wheel.
- Gobo size: **OD 29.8 mm max**, **image 25.0 mm max**, holder 30.0 mm, **thickness 1.1 mm ±0.1**. B&H lists 1.2" / 1" / 0.04".
- Prism / frost / zoom / iris / shutters: Zoom 5.5°–55°. Has framing shutters and animation. 16-bit pan, tilt and dimmer.
- Gobo / module change procedure: Not found — fill in from the fixture.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| `XXer` (flashing) | Motor or function error. XX is the function number. | The fixture retries automatically (up to 3 attempts). Then power-cycle and check for a mechanical jam or an engaged lock. |
| `0Er` | Pan motor error | Check that the pan lock is released and the yoke moves freely. |
| Several `XXer` codes flashing (e.g. `01Er`, `02Er`, `05Er`) | Several functions failed homing at once. The list repeats 5 times. | Check locks. Then use the calibration menu (password 050) or call service. |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Pan/tilt error at startup | Pan or tilt lock still engaged | Release the locks and power-cycle. |
| Breaker trips at 120 V with 2 units on one circuit | Combined draw of about 23 A (estimate) is over a 20 A circuit | One unit per 20 A circuit at 120 V. |

## Maintenance
- Recalibrate / reset procedure: Calibration menu behind password 050 (Proteus series).
- Fan / filter cleaning: Not found.
- Firmware update method: Elation's forum has a "Proteus Maximus Firmware" thread. Elation's general methods are the **E-LOADER III** (battery-powered uploader over a 3-pin DMX cable) or a **FAT32 USB stick** on fixtures that have a USB port. ⚠️ Not confirmed whether the Maximus has USB. Write down your menu settings before updating. **Firmware cannot be downgraded.**

## Road notes (community)
- None found in this research pass. ⚠️ Add notes from techs.

## Sources
- [Elation Proteus Maximus user manual (BMI Supply mirror)](https://shop.bmisupply.com/Resources/en/ItemDocuments/39E1019/ELATION%20PROTEUS%20MAXIMUS%20-%20USER%20MANUAL.pdf): 1,400 W, AC input range, pan/tilt locks, omega brackets, M10/M12 clamp bolt, FIL foam inlay
- [Elation Proteus Maximus user manual (novelty.fr mirror)](https://www.novelty.fr/wp-content/uploads/downloaded/downloads/materiel_manuels/elation_proteus-maximus_manuel.pdf): error code format (`XXer`, `0Er`, retries, multiple errors)
- [Elation EU manual download](https://www.elationlighting.eu/mwdownloads/download/link/id/9132/): pan/tilt locks, omega brackets
- [Proteus Maximus manual (B&H lit file)](https://www.bhphotovideo.com/lit_files/828723.pdf) and [B&H product page PRM992](https://www.bhphotovideo.com/c/product/1700696-REG/elation_professional_prm992_proteus_maximus_950w_led.html): gobo dimensions, 6 rotating + 7 fixed gobos, part number
- [4Wall rental listing](https://www.4wall.com/rentals/9758866/elation-proteus-maximus-ip65), [GoKnight](https://goknight.com/elation-proteus-maximus-ip65-950w-led-profile/), [idjnow](https://www.idjnow.com/elation-professional-proteus-maximus-fixture.html): 37/61 ch, 117 lb / 53 kg, IP65, 50,000 lm, 5.5–55° zoom, protocols
- Dealer spec listings ([kpodj](https://kpodj.com/elation-proteus-maximus-p-111223), [Illumination Dynamics](https://www.illuminationdynamics.com/automated-lighting1/scenius-profile-pnnd7), [elationlighting.com](https://www.elationlighting.com/products/proteus-maximus)): "Power Linking: No". The search summary didn't say which page.
- [Proteus Odeon manual](https://goknight.com/content/documentation/ELATION%20PROTEUS%20ODEON%20-%20USER%20MANUAL.pdf), [Proteus Excalibur manual](https://d295jznhem2tn9.cloudfront.net/ItemRelatedFiles/12937/ELATION%20PROTEUS%20EXCALIBUR%20-%20USER%20MANUAL.pdf), [Proteus Hybrid Max manual](https://d295jznhem2tn9.cloudfront.net/ItemRelatedFiles/13622/ELATION%20PROTEUS%20HYBRID%20MAX%20-%20USER%20MANUAL.pdf), [Proteus Radius manual](https://d295jznhem2tn9.cloudfront.net/ItemRelatedFiles/13604/ELATION%20PROTEUS%20RADIUS%20-%20USER%20MANUAL.pdf): service password 050, reset password 011, battery display operation
- [Elation forum: Proteus Maximus Firmware](https://forums.elationlighting.com/topic/proteus-maximus-firmware?nc=1) and [E-LOADER III](https://www.elationlighting.com/e-loader-iii-software-uploader): firmware method, no downgrade
- [Elation Proteus Maximus WMG](https://www.elationlighting.com/proteus-maximus-wmg): WMG variant exists
