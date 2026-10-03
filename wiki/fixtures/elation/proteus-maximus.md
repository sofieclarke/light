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
firmware:
  latest_known: "V1.8.1"
  checked: "2026-10-03"
  check_on_fixture: null
  methods: ["E-LOADER III over 3-pin DMX"]
  interface: "Elation E-LOADER III (ELO601)"
  software: null
  file_type: null
  download: "https://forums.elationlighting.com/topic/proteus-maximus-firmware?nc=1"
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

## Firmware
- Installed version — where to see it on the fixture: menu path not found in the sources read. Look for it before you update so you know where you're starting from.
- Latest known version (date checked) and where to download it: **V1.8.1** (latest found, checked 2026-10-03) per Elation's forum thread ["Proteus Maximus Firmware"](https://forums.elationlighting.com/topic/proteus-maximus-firmware?nc=1) (seen as a search summary, not read in full). Files come from that thread or from Elation (firmware@elationlighting.com, per a search summary).
- What you need: the forum thread names the **E-LOADER III** as the upload tool for this fixture. It's a battery handheld (part number ELO601 in dealer listings) with a micro SD card, connected with a **3-pin DMX cable**. A USB service port on the Maximus was not confirmed.
- Update steps: see the E-LOADER III procedure in [_elation-common.md](_elation-common.md#firmware-updates). Short version: file on the micro SD → 3-pin DMX from the loader to the fixture → power the fixture → power the E-LOADER III **within 10 s** → pick the fixture folder and file → enter the loader password.
- Updating a whole rig: one fixture at a time with the E-LOADER III. No batch or network method found.
- If it fails or bricks mid-update: no recovery procedure found. Retry with a charged loader (at least two battery bars), then contact Elation service ⚠️ unverified.
- Release notes worth knowing (forum thread, via search summary):
  - V1.8.1: "Sun Protection updated" and "Hibernation updated".
  - You can update within the V1.6.x, V1.7.x and V1.8.x lines, but **you cannot go back down to V1.6.x or V1.7.x**.
  - The thread says a fixture on **V1.6.x** needs board **PCB1187-0-B** dealt with ("remove … first") before it can take V1.7.x or V1.8.x. ⚠️ Read the thread or ask Elation before touching a V1.6.x unit.
  - Write down your menu settings first. Firmware cannot be downgraded.

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
- [Elation Proteus Maximus WMG](https://www.elationlighting.com/proteus-maximus-wmg): WMG variant exists
- [Elation forum: Proteus Maximus Firmware](https://forums.elationlighting.com/topic/proteus-maximus-firmware?nc=1): V1.8.1, release notes, version-line rules, E-LOADER III as the tool (search summary)
- [E-LOADER III](https://www.elationlighting.com/e-loader-iii-software-uploader) and [E-LOADER III manual (manuals.plus)](https://manuals.plus/elation/professional-e-loader-iii-software-uploader-kit-manual): uploader procedure (search summary)
- [Adorama: E-LOADER III ELO601](https://www.adorama.com/elelo601.html): part number
