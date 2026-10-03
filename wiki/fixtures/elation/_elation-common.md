---
title: "Elation Professional — common conventions"
manufacturer: "Elation Professional"
verification: "web-search"
last_updated: "2026-10-03"
---

# Elation Professional: shared conventions

> **2AM CARD**
> - **Service / calibration password: 050.** Default-reset password: **011.** These come from several Proteus manuals (Odeon, Excalibur, Hybrid Max, Rayzor 760, Radius). Older or non-Proteus models may differ. ⚠️ Check per model.
> - **Lamp-hours reset (hybrids): 038.** Path on the Smarty Hybrid: MODE/ESC → Information → Time Information → LampTime Password.
> - **Battery addressing (Proteus):** with no power, **hold MODE/ESC 10 s** or **hold ENTER 3 s** (manuals differ). The display sleeps after about 1 minute.
> - **Startup error format:** `XXer` flashing, where XX is the function number. `0Er` = pan.
> - **Firmware:** E-LOADER III over a 3-pin DMX cable, or a FAT32 USB stick on models with USB. **No downgrades.**

## Menu conventions
- Buttons are MODE/ESC, UP, DOWN and ENTER. Press MODE/ESC to open the main menu, UP/DOWN to move, ENTER to select. Source: Smarty Hybrid lamp-reset path and Proteus battery instructions.
- The DMX address is under **DMX Settings** in the main menu (range 001–512), per the Proteus Odeon and Proteus Hybrid manuals.
- Newer Proteus models have a color LCD menu display. Its lamp-life warnings on the Smarty Hybrid: **yellow outline** = 20 % life left, **red outline** = life exceeded. Clear it with DMX 250–251 or OK.

## Passwords & hidden menus
| Password | What it unlocks | Where it's documented |
|---|---|---|
| **050** | Service / calibration menus. The manual says it must be entered each time. | Proteus Odeon, Excalibur, Hybrid Max, Rayzor 760, Radius manuals |
| **011** | Restore factory default settings | Same Proteus manuals |
| **038** | Lamp-time (lamp hours) reset | Smarty Hybrid manual |

⚠️ Not confirmed on every model. If 050 fails, look in that model's manual.

## Battery / unpowered addressing
- Proteus fixtures have an internal battery that runs the display. You can set the DMX address, channel mode and other menu items without mains power.
- How to wake it: one Proteus manual says **hold MODE/ESC for 10 s**, another says **hold ENTER for 3 s**. Try both.
- The display turns off by itself about 1 minute after the last button press.

## Firmware update
- **E-LOADER III**: Elation's battery-powered uploader. It connects to the fixture with a **3-pin DMX cable**. Step-by-step instructions are on its product page.
- **USB**: on fixtures with a USB port, download the firmware from elationlighting.com, copy it to a **FAT32** USB stick, insert it and follow the screen.
- The older **CUE Software Uploader** also has an Elation product page. Which models it supports was not checked.
- Before updating, **write down your menu settings**. **Firmware cannot be downgraded.**
- Elation's support forum has a firmware thread for each model (e.g. "Proteus Maximus Firmware", "Smarty Hybrid Firmware", "Proteus Excalibur Firmware").

## Common error messages
| Message | Meaning | Fix |
|---|---|---|
| `XXer` flashing at startup | A motor or function failed to home. XX is the function number (the manual's example ties it to channel numbers). | The fixture retries by itself (a 2nd and then a 3rd reset attempt). If it persists: check transport locks, look for jams, recalibrate (050). |
| Several codes, e.g. `01Er` `02Er` `05Er` | Several functions failed. The list repeats 5 times. | Same as above. |
| `0Er` | Pan motor | Pan lock / obstruction |
| Ballast error (discharge models) | Ballast fault / heat / bad lamp | Lamp OFF 3–5 min. If it's still there, power the fixture off. If it's still there after that, call Elation support. A bad lamp can cause this (Elation forum). |
| "Replace the Lamp" flashing (Proteus Hybrid) | Lamp past its rated life (1,500 h) | You get 300 h of grace. At 1,800 h the fixture hibernates: no DMX response until the lamp is replaced **and** lamp hours are reset. |

## Power-linking caution (manual wording)
- "USE CAUTION WHEN POWER LINKING OTHER MODEL FIXTURES AS THE POWER CONSUMPTION OF OTHER MODEL FIXTURES MAY EXCEED THE MAX POWER OUTPUT ON THIS FIXTURE." (Proteus Hybrid manual)
- In this research pass, Elation's per-voltage amp tables did not show up in search summaries for any model. The fixture pages use watts ÷ volts estimates, flagged ⚠️. Replace them with the manual's electrical table numbers when you can.

## Sources
- [Proteus Odeon manual](https://goknight.com/content/documentation/ELATION%20PROTEUS%20ODEON%20-%20USER%20MANUAL.pdf): passwords 050/011, battery display
- [Proteus Excalibur manual](https://d295jznhem2tn9.cloudfront.net/ItemRelatedFiles/12937/ELATION%20PROTEUS%20EXCALIBUR%20-%20USER%20MANUAL.pdf), [Proteus Hybrid Max manual](https://d295jznhem2tn9.cloudfront.net/ItemRelatedFiles/13622/ELATION%20PROTEUS%20HYBRID%20MAX%20-%20USER%20MANUAL.pdf), [Proteus Radius manual](https://d295jznhem2tn9.cloudfront.net/ItemRelatedFiles/13604/ELATION%20PROTEUS%20RADIUS%20-%20USER%20MANUAL.pdf), [Proteus Rayzor 760 manual](https://shop.bmisupply.com/Resources/en/ItemDocuments/39E1016/BMI.Elation.Proteus.Rayzor.760.Manual.pdf): passwords 050/011
- [Proteus Hybrid manual](https://shop.bmisupply.com/Resources/en/ItemDocuments/39E1018/BMI.Elation.Proteus.Hybrid.Fixture.Manual.pdf): battery display, error format, ballast errors, lamp hibernation, power-link caution
- [Proteus Maximus manual (novelty.fr)](https://www.novelty.fr/wp-content/uploads/downloaded/downloads/materiel_manuels/elation_proteus-maximus_manuel.pdf): XXer format, retries, multiple errors
- [Smarty Hybrid manual (ManualsLib)](https://www.manualslib.com/manual/1429186/Elation-Smarty-Hybrid.html): lamp-time password 038, lamp warning colors
- [E-LOADER III](https://www.elationlighting.com/e-loader-iii-software-uploader), [CUE Software Uploader](https://www.elationlighting.com/cue-software-uploader): firmware tools
- Elation forum firmware threads: [Proteus Maximus](https://forums.elationlighting.com/topic/proteus-maximus-firmware?nc=1), [Smarty Hybrid](https://forums.elationlighting.com/topic/smarty-hybrid-firmware?nc=1), [Proteus Excalibur](https://forums.elationlighting.com/topic/proteus-excalibur-firmware?nc=1)
- [Elation forum: Proteus Beam Hybrid ballast error](https://forums.elationlighting.com/topic/proteous-beam-hybrid-ballast-error), [Elation FAQ/Troubleshooting](https://www.elationlighting.com/pages/faq-troubleshooting): ballast and lamp notes
