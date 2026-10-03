---
title: "ETC — common conventions"
type: reference
last_updated: "2026-10-03"
---

# ETC: shared conventions

> **2AM CARD: firmware**
> - **Software:** **UpdaterAtor** (Windows only, no Mac). Some notes call it "UpdaterUpper" or "UpdateBox", but ETC's name is UpdaterAtor.
> - **Hardware:** ETC USB/DMX **Gadget** or **Gadget II** (part numbers 4267A1001 / 4267A1004), the ETC USB/DMX Service Cable, or a **Net3 / DMX-RDM gateway** on the network.
> - **Series 3 / newer:** a **USB drive** in the rear port. Path: **Menu → Local Settings > USB > Update Firmware**.
> - **Pull every non-ETC opto-splitter, isolator and DMX repeater out of the line.** ETC warns a failed load through one can leave the fixture needing repair at ETC.
> - **Tungsten Source Four: no firmware.**

## Firmware updates

### Latest versions found (checked 2026-10-03)
| Fixture | Latest found | Method |
|---|---|---|
| ColorSource PAR, CPU3 | **v4.0.2** (11 Dec 2023) | UpdaterAtor, fixture-to-fixture push |
| ColorSource PAR, CPU2 | **v3.0.0** (Dec 2021) | UpdaterAtor, fixture-to-fixture push |
| ColorSource PAR, original CPU | v1.7? ⚠️ inferred from the install-guide title | UpdaterAtor |
| Source Four LED Series 2 (Lustr, Daylight, Tungsten) + Selador Desire | **v1.8.2** (02-2022) | UpdaterAtor over DMX (Gadget) or Net3 gateway |
| Source Four LED Series 3 (Lustr X8 etc.) | **v1.3.0** | USB drive, or UpdaterAtor |
| Source Four (tungsten) | none, it has no electronics | — |

### The tools
- **UpdaterAtor**: ETC's free fixture-update software for Windows (7/8/10 listed; **Mac not supported**). It downloads the fixture software itself: **Setup Versions** shows what you have, and **Download All Latest Software** fetches the rest. Quick Guide v4.4.0 found.
- **Interfaces** UpdaterAtor can use (ETC support article):
  - ETC USB/DMX **Gadget** or **Gadget II** (part numbers **4267A1001 / 4267A1004**; which number is which wasn't confirmed). Gadget II has 5-pin XLR DMX ports (general knowledge).
  - ETC **USB/DMX Service Cable**.
  - ETC **Networked DMX/RDM Gateway**: a Net3 One, Two or Four Port Gateway can update Source Four LED fixtures over the network.
- **USB drive**: Source Four LED Series 3 (and fos/4) take firmware from a USB drive in the rear port. Get the file from etcconnect.com or export it from UpdaterAtor. A required drive format wasn't found.
- **Fixture-to-fixture push** (ColorSource): a fixture can send its software to others on the line, but **only to fixtures with the same CPU type**.
- **File type:** not confirmed. UpdaterAtor manages the files, so you rarely touch them.

### Procedure: UpdaterAtor over DMX (ETC's ColorSource v1.3.0 article, via search summary)
1. Read the release note for the version you're loading.
2. Install UpdaterAtor on a Windows PC.
3. Connect the PC to a Gadget / Gadget II, the service cable, or a gateway. Connect that to the fixture's DMX line. **Disconnect the console** from that line (general knowledge).
4. **Remove all non-ETC opto-isolators, opto-splitters and DMX repeaters** between the interface and the fixtures.
5. In UpdaterAtor press **Setup Versions** and check the needed software is installed. If not, press **Download All Latest Software**.
6. Find the fixtures and run the update. Don't power-cycle fixtures or unplug the line until it finishes (general knowledge).
- **ColorSource below v1.3.0:** update the **bootloader first** (ColorSource Family Bootloader 1.3.0.9.0.17 or higher), then the firmware (ColorSource Family v1.3.0+ 1.3.0.9.0.15 or higher).

### Procedure: USB drive (Source Four LED Series 3 manual, via search summary)
1. Save the firmware file to a USB drive.
2. Insert it in the **USB port on the rear** of the fixture.
3. Press **Menu**, then turn the **Intensity encoder** to **Local Settings > USB > Update Firmware**.
4. Turn the encoder to the file and **press the encoder** to start.
5. Wait through copying (progress meter), verifying (ETC logo) and installing. Don't cut power.

### Batch updates
- UpdaterAtor updates fixtures on a DMX line through a Gadget, or many lines through Net3 gateways. No per-batch limit was found.
- ColorSource fixture-to-fixture push: same CPU type only. A fixture with a different CPU just won't accept the code.
- USB is one fixture at a time.

### Recovery
- No field bootloader or recovery mode was found in the sources read. ETC says a fixture left without firmware (e.g. after a load through a non-ETC splitter) may have to go back to ETC for repair. So the splitter rule really matters.

### Gotchas
- **Opto-splitters / repeaters / non-ETC isolators**: take them out of the update path (ETC).
- **ColorSource CPU variants**: CPU2 takes only v3.x, CPU3 takes v4.x. Find out which board you have first (ETC article "Identify a CPU2 ColorSource PAR").
- **Source Four LED Series 2, v1.8.1+** added calibrated Direct mode. Fixtures on older software **won't color-match** newer ones in Direct mode, so put the whole rig on one version.
- **Mode changes:** a new version can add or change DMX modes. Check the release note and re-check the console patch afterwards (general knowledge).
- **Version on the fixture:** ColorSource and Source Four LED Series 2 show the software version on the display at power-up.

## Sources
- [ETC support: Updating ColorSource Par to v1.3.0](https://support.etcconnect.com/ETC/Fixtures/ColorSource/PAR/Updating_ColorSource_Par_to_v1.3.0): UpdaterAtor, interface list, Windows only, opto-splitter warning, bootloader-first rule (search summary)
- [ETC support: CPU Variants in ColorSource and S4WRD Color Fixtures](https://support.etcconnect.com/ETC/Fixtures/ColorSource/Software_and_Programming/CPU_Variants_in_ColorSource_and_S4WRD_Color_Fixtures), [Identify a CPU2 ColorSource PAR](https://support.etcconnect.com/ETC/Fixtures/ColorSource/PAR/Identify_a_CPU2_ColorSource_PAR), [ColorSource PAR CPU3 loud fan noise](https://support.etcconnect.com/ETC/Fixtures/ColorSource/PAR/ColorSource_PAR_CPU3_loud_fan_noise): CPU and software lines, v4.0.2, same-CPU push (search summary)
- [ETC ColorSource PAR Installation Guide v1.7/v3.0/v4.0 (voxel.org mirror)](https://voxel.org/pdf/technical-manual/cspar.pdf), [ColorSource PAR documentation](https://www.etcconnect.com/Products/Entertainment-Fixtures/ColorSource-PAR/Documentation.aspx): software lines, v3.0.0 release-note date (search summary)
- [ETC Source Four LED Series 2 documentation](https://www.etcconnect.com/Products/Entertainment-Fixtures/Source-Four-LED-Series-2/Documentation.aspx), [ETC support: Series 2 Direct-mode color match](https://support.etcconnect.com/ETC/Fixtures/Source_Four_LED/Series_2/My_New_Source_Four_LED_Series_2_Fixtures_Dont_Exactly_Match_My_Existing_Fixtures_in_Direct_Mode): v1.8.2 / v1.8.1 (search summary)
- [UpdaterAtor Quick Guide v4.4.0 (ControlBooth attachment)](https://www.controlbooth.com/attachments/updaterator_quickguide_v4-4-0_reva-pdf.15829/): Gadget / Net3 gateway paths, version at power-up (search summary)
- [ETC Source Four LED Series 3 user manual, Update Firmware (ManualsLib p.30)](https://www.manualslib.com/manual/2296552/Etc-Source-Four-Led-3-Series.html?page=30), [Series 3 Fixture Software v1.3.0 Release Note](https://www.etcconnect.com/workarea/DownloadAsset.aspx?id=10737515440): USB path and steps, latest version (search summary)
- [ETC Community: Source 4 series 2 Firmware](https://community.etcconnect.com/luminaires_fixtures/led-fixtures/f/source-four-led/53833/source-4-series-2-firmware): Gadget updates Source Four LED and Desire (search summary)
