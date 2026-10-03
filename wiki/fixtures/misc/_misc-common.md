---
title: "Misc makers — firmware reference (Astera, Solaris, SGM, MDG, Look Solutions, Antari)"
type: reference
last_updated: "2026-10-03"
---

# Misc makers: firmware reference

> **2AM CARD**
> - **Astera** (AX1, Titan): **AsteraApp + ART7 AsteraBox** over Bluetooth. **App Settings → Lights Background Update** → update button at the top right. Lights keep working while it runs. Latest found **V5.16.24**.
> - **Solaris Flare** (TMB): **Upload** menu cross-loads from one Flare to the others on the DMX line. **Password 111.** Flares only on that line.
> - **SGM P-5**: **SGM Firmware Tool** (Windows) + **SGM USB-to-5-pin-XLR uploader cable**.
> - **MDG theONE**: service-only. USB A-to-B to a Windows PC during the **4 s "Testing BootLoad"** window at power-up. Package from MDG Service.
> - **Look Unique 2.1 / Antari HZ-500**: no user firmware procedure found.
> - **DWE / molefay blinder**: no firmware (lamps and wiring only).

## Firmware updates

### Summary (checked 2026-10-03)
| Maker / fixture | Latest found | Interface | Software | Cable |
|---|---|---|---|---|
| Astera AX1 PixelTube, Titan Tube | **V5.16.24** ⚠️ product coverage of that release not confirmed | ART7 AsteraBox | AsteraApp (iOS/Android) | none (Bluetooth) |
| Solaris (TMB) Flare | not found (manuals up to software 11.3; OFL profile from 9.3C) | none (fixture to fixture) | none | DMX line |
| SGM P-5 | not found | SGM USB 5-pin XLR uploader cable | SGM Firmware Tool (Windows) | 5-pin XLR |
| MDG theONE | not found (service-only) | USB A-to-B cable | package from MDG Service (Windows) | USB |
| Look Solutions Unique 2.1 | none found | — | Look lists a "GPU-Updater" (Win/Mac), coverage not confirmed ⚠️ | — |
| Antari HZ-500 | none found | — | — | — |
| Generic DWE blinder | none (no electronics) | — | — | — |

### Astera
- **Tools:** the **AsteraApp** (iOS / Android) and an **ART7 AsteraBox**. The ART7 is the app's Bluetooth bridge to the lights, and the app needs one to control lights. The ART7 is also the CRMX transmitter for wireless DMX (general knowledge). There are no files or cables: the app downloads the firmware.
- **Check the version:** AsteraApp → Connected Lights view → **Firmware Version sorting mode**.
- **Procedure** (Astera / dealer instructions, via search summary):
  1. Update the AsteraApp from the app store.
  2. Connect the app to the ART7 over Bluetooth. Put the lights in **BlueMode**, press **Pair with Lights**, and wait until all are paired.
  3. **App Settings → Lights Background Update**, then press the update button in the **top right**.
  4. The lights update **in the background** and keep working. Keep the app open and turn on "Keep Screen On" in App Settings.
- **The ART7 itself** gets firmware through the app too: connect to it over Bluetooth, update when prompted, then reboot the ART7. (The dealer doc with this step is about beta firmware, so the exact prompts may differ ⚠️.)
- **Beta / custom firmware** (dealer doc): App Settings → toggle **TalkBack+** and **Keep Screen On** ON → Lights Background Update → **Auto Update OFF** → press and hold the Update button for a few seconds until a pop-up appears. Only do this if Astera or your dealer tells you to.
- **Batch:** background update covers all paired lights. No per-batch limit found.
- **Recovery:** none documented in what was found. Re-pair and run the update again ⚠️ unverified.
- **Release notes:** **5.14.84** fixed reported wired-DMX problems, added PowerBox wired DMX protocol v2, and fixed sound-to-light on the ART7 / ART7 WIFI. Astera's numbered DMX modes must match the console profile mode. Re-check them after an update (general knowledge).

### Solaris (TMB) Flare
- **Tools:** none found beyond the fixture itself. **No standalone "Solaris firmware updater" PC tool turned up**, and how the software first gets into a Flare wasn't found.
- **Procedure** (Flare manual, via search summary): the **Upload** function "uploads software and cross-loads software from one Flare to others in the DMX data chain". It's password-protected: **111**. Button steps weren't in the summary.
- **Gotcha:** **don't use it with other fixture types on the DMX line** (manual). Disconnect the console too (general knowledge).
- **Versions:** TMB's manuals cover software from 8.2 to **11.3** (the combined Flare Q+ / Q+ LR / Flare / Flare Jr manual). OFL's Flare profile was built from software 9.3C.

### SGM
- **Tools** (P-5 manual Rev J, via search summary): the **SGM USB-to-5-pin-XLR uploader cable**, a **Windows** PC and the **SGM Firmware Tool**, from sgmlight.com. The same cable works with SGM's **RDM Addressing Tool**, which changes fixture settings remotely. RDM is for settings, not firmware.
- **Procedure:** install the SGM Firmware Tool → cable into the fixture's 5-pin DMX in → load the model's file → upload. Button-level steps weren't in the summaries. See SGM's "Firmware Tool how-to" PDF and the "How to update firmware on SGM fixtures" video.
- **Batch, recovery:** not found. Keep one model per line and disconnect the console (general knowledge).
- **Gotcha:** newer P-5 firmware may add DMX modes. Check your console patch afterwards.

### MDG
- **theONE** (manual): connect a **USB A-to-B** cable from a **Windows PC** to the USB-B port. The PC has to catch the **4-second "Testing BootLoad"** window at power-up. The package comes from **MDG Service**. It's not a public download, and the MDG Terminal diagnostics package is also service-supplied.
- Since the bootloader runs at every power-up, a failed load should be retryable from power-up ⚠️ unverified. Call MDG Service.

### Look Solutions
- **Unique 2.1:** no user firmware procedure found in the manual summaries. Look's downloads page lists a **"GPU-Updater"** tool for Windows and Mac. Which machines it covers and how it connects weren't confirmed ⚠️. Ask Look Solutions or the distributor before trying.

### Antari
- **HZ-500:** **none found.** The manual summaries only cover rear-panel LCD settings (fog duration, interval, DMX address, door sensor).

### General gotchas (all makers)
- Disconnect the console from the line you're updating, keep **only the same model** on that line, and **never power-cycle mid-update** (general knowledge).
- A firmware update can add or renumber DMX modes and break the console patch. Note the mode before you update and check it after.

## Sources
- [Astera firmware release notes, "Firmware V5.16.24"](https://update.astera-led.com/firmwares/current/release_notes.html): latest version found (page title via search; not readable here)
- [Astera custom firmware update instructions (Wireless Film Lights)](https://wirelessfilmlights.com/wp-content/uploads/2024/07/Astera_Custom_Firmware_Update_Instructions_V1.pdf), [Astera FW 5.14 features and update instructions (Controllux)](https://controllux.com/downloads/2024050712758_5.14.61_Astera_Beta_Firmware_Features_and_update_instructions.pdf), [Ambersphere: Astera firmware update](https://www.ambersphere.com/astera-firmware-51484/): app procedure, ART7 update, 5.14.84 notes (search summary)
- [AsteraApp control manual](https://astera-led.com/Downloads/AsteraApp%20control.pdf), [ART7 AsteraBox manual](https://astera-led.com/wp-content/uploads/ART7_AsteraBox_Manual_EN_DE_IT_ES_FR_CN.pdf), [AsteraApp (App Store)](https://apps.apple.com/us/app/asteraapp/id1367867800): ART7 as Bluetooth bridge, firmware-version sorting (search summary)
- [Solaris Flare operation manual (ManualsLib)](https://www.manualslib.com/manual/1034357/Solaris-Flare.html), [Flare Q+ / Flare / Flare Jr manual (tmb.com)](https://tmb.com/docs/solaris/flare/Solaris-Flare-Manual.pdf): Upload cross-load, password 111, manual software versions (search summary)
- [SGM P-5 Series User Manual Rev J (TSL mirror)](https://www.tsllighting.com/wp-content/uploads/2018/12/SGMP-5SeriesUserManualSTDandPOIRev.J.pdf), [SGM RDM Addressing Tool](https://www.sgmlighting.com/products/architecture/rdm-addressing-tool), [SGM Firmware Tool how-to (benart.net)](http://www.benart.net/Images/Uploads/MyContents/F_20151127173350020911.pdf), [How to update firmware on SGM fixtures (YouTube)](https://www.youtube.com/watch?v=LL0BYBvD38w): SGM tools (search summary)
- [MDG theONE User Guide Rev A/f](https://mdgfog.s3.amazonaws.com/uploads/docs/theONE-User-Guide-Rev-Af.pdf): USB bootload procedure (manual, read in full by an earlier pass)
- [Look Solutions downloads](https://www.looksolutions.com/en/downloads-en.html): GPU-Updater listing (search summary)
- [Antari HZ-500 product page](https://antari.com/products/hz-500/), [HZ-500 manual (ManualsLib)](https://www.manualslib.com/manual/892121/Antari-Hz-500.html): no firmware procedure found
