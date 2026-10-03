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
> - **Firmware:** E-LOADER III (micro SD card, 3-pin DMX cable, power the loader within 10 s of the fixture), or a USB stick in the UPDATE/SERVICE PORT on models that have one. **No downgrades. Write down settings first.**

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

## Firmware updates
| Fixture | Latest found (checked 2026-10-03) | Method |
|---|---|---|
| Proteus Maximus | **V1.8.1** | E-LOADER III (forum thread) |
| Proteus Hybrid MAX (not the plain Proteus Hybrid) | V1.3.7 (MAX OPS: V1.3.6) | E-LOADER (forum thread) |
| Proteus Smarty Hybrid (IP65, not the indoor Smarty Hybrid) | V1.4.1 | E-LOADER III / USB (forum thread) |
| Proteus Hybrid, Smarty Hybrid (indoor) | not found | see the fixture pages |

### The tools
- **E-LOADER III** (dealer part number **ELO601**): Elation's battery-powered handheld uploader. The update files go on its **micro SD card**, and it connects to the fixture's DMX input with a **3-pin DMX cable**. It's the method for fixtures **without a USB service port**.
- **USB flash drive** in the fixture's **UPDATE/SERVICE PORT**, on newer models that have one (e.g. the Smarty Hybrid manual). The manual says to put **only the update file** on the drive. The existing wiki notes say **FAT32** ⚠️ not confirmed in the manual summary.
- **CUE Software Uploader**: the older Elation handheld uploader, also battery-powered and connected over a 3-pin DMX cable. Which models it still covers wasn't checked.
- A **Windows PC** is needed to download files. The Smarty Hybrid manual says "PC only" (no Mac).
- **Where the files are:** each model has a firmware thread on Elation's support forum (e.g. "Proteus Maximus Firmware", "Proteus Hybrid MAX Firmware", "Proteus Smarty Hybrid Firmware", "Proteus Excalibur Firmware"). It lists the current version, the tool and the release notes. Elation also gives firmware@elationlighting.com (address from a search summary).
- **File type:** the E-LOADER III manual summary calls the update file a "GSD file". The exact extension wasn't confirmed.

### E-LOADER III procedure (manual, via search summary)
1. Check the loader's battery shows **at least two bars**. A flat loader mid-update is the thing to avoid.
2. Put the update file on the micro SD card in the folder for that fixture, then insert the card in the slot on the **bottom** of the E-LOADER III.
3. Unplug the console's DMX from the fixture. Connect the loader's signal output to the fixture with a **3-pin DMX cable**.
4. Power up the fixture, then power up the E-LOADER III **within 10 seconds**.
5. In the Browser menu, pick the fixture folder → ENTER, then pick the file → ENTER.
6. Enter the loader password. The manual text shows the default as "OOOOOO" (probably six zeros ⚠️ unverified).
7. Wait for it to finish. Don't power-cycle either unit during the upload (general knowledge).

### USB procedure (Smarty Hybrid manual, via search summary)
1. Copy the update file from a PC to a USB flash drive. Nothing else on the drive.
2. **Disconnect DMX, Art-Net and E-FLY**, then power the fixture on.
3. Insert the drive in the **UPDATE/SERVICE PORT** on the rear panel.
4. Menu: **Personality → Service Setting → USB Update**.
5. Select the file → ENTER → **YES**. The display shows "Updating…%".

### Batch updates
- Both methods are **one fixture at a time**. No network (Art-Net/sACN) or RDM firmware method was found for these models.

### Recovery
- No bootloader or recovery mode was found in the sources read. If an update fails, retry with a charged loader or a fresh USB drive, then contact Elation service ⚠️ unverified.

### Gotchas
- **No downgrades.** "Fixture software cannot be downgraded" (manual). On the Proteus Maximus, the forum says you can't go back to V1.6.x or V1.7.x.
- **Write down every menu setting first** (manual).
- Elation says only qualified technicians should do this (manual).
- **Disconnect the console and wireless** (DMX, Art-Net, E-FLY) before updating (manual, USB procedure).
- Don't load a sibling model's file: Proteus Hybrid ≠ Proteus Hybrid MAX, and Smarty Hybrid ≠ Proteus Smarty Hybrid.
- A firmware update can add or renumber DMX modes. Re-check the fixture's mode against the console patch afterwards (general knowledge).
- Proteus Maximus on V1.6.x: the forum mentions removing board PCB-PCB1187-0-B before V1.7/V1.8. See the [Proteus Maximus page](proteus-maximus.md#firmware).

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
- [E-LOADER III manual (manuals.plus)](https://manuals.plus/elation/professional-e-loader-iii-software-uploader-kit-manual): micro SD, 3-pin DMX, 10 s power-up window, browser/file/password steps, two-bar battery rule (search summary). [Adorama ELO601](https://www.adorama.com/elelo601.html): part number
- [Smarty Hybrid user manual (Cloudfront)](https://d295jznhem2tn9.cloudfront.net/ItemRelatedFiles/12026/ELATION%20SMARTY%20HYBRID%20-%20USER%20MANUAL.pdf): USB update procedure, no-downgrade and PC-only warnings (search summary)
- [Elation forum: Proteus Hybrid MAX Firmware](https://forums.elationlighting.com/topic/proteus-hybrid-max-firmware?nc=1): V1.3.7 / V1.3.6 (search summary). The Maximus and Proteus Smarty Hybrid threads below gave V1.8.1 and V1.4.1
- Elation forum firmware threads: [Proteus Maximus](https://forums.elationlighting.com/topic/proteus-maximus-firmware?nc=1), [Smarty Hybrid](https://forums.elationlighting.com/topic/smarty-hybrid-firmware?nc=1), [Proteus Excalibur](https://forums.elationlighting.com/topic/proteus-excalibur-firmware?nc=1)
- [Elation forum: Proteus Beam Hybrid ballast error](https://forums.elationlighting.com/topic/proteous-beam-hybrid-ballast-error), [Elation FAQ/Troubleshooting](https://www.elationlighting.com/pages/faq-troubleshooting): ballast and lamp notes
