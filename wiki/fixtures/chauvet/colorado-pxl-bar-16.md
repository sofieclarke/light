---
title: "Chauvet Professional COLORado PXL Bar 16"
manufacturer: "Chauvet Professional"
model: "COLORado PXL Bar 16"
aliases: ["pxl bar 16", "pxl 16", "pxl bar", "pxl line", "colorado pxl 16", "coloradopxlbar16", "bar pxl 16", "pixel bar 16"]
type: "pixel-bar"
light_source: "LED 16x 45W RGBW"
ip_rating: IP65
weight_lb: 45.6
weight_kg: 20.7
dimensions: "39.37 x 5.47 x 10.75 in (1000 x 139 x 273 mm)"
power:
  input: "100–240 VAC, 50/60 Hz, auto-ranging"
  connector_in: "powerCON TRUE1-compatible (IP65)"
  connector_out: "powerCON TRUE1-compatible (IP65)"
  watts_max: 790
  amps_120v: 6.60
  amps_208v: 3.821
  amps_230v: 3.485
  link_max_120v: 0
  link_max_208v: 3
  link_max_230v: 3
  per_20a_120v: 1
  per_20a_208v: 3
  fuse: null
dmx:
  connectors: "IP65 5-pin XLR in/out, IP65 Ethernet (TCP/IP) in/out, IP65 USB-C (firmware)"
  protocols: ["DMX", "RDM", "Art-Net", "sACN", "Kling-Net"]
  modes:
    - { name: "Single Control – Basic2", channels: 19 }
    - { name: "Single Control – Basic", channels: 20 }
    - { name: "Single Control – Standard", channels: 84 }
    - { name: "Single Control – Advanced", channels: 154 }
    - { name: "Single Control – Tour", channels: 186 }
    - { name: "Dual Control Movement – Basic2", channels: 7 }
    - { name: "Dual Control Movement – Basic", channels: 8 }
    - { name: "Dual Control Movement – Standard", channels: 20 }
    - { name: "Dual Control Movement – Advanced", channels: 26 }
    - { name: "Dual Control Pixels – Basic", channels: 48 }
    - { name: "Dual Control Pixels – Standard", channels: 64 }
    - { name: "Dual Control Pixels – Advanced", channels: 128 }
menu_password: "2323"
firmware:
  latest_known: "V1.260709"
  checked: "2026-10-03"
  check_on_fixture: "MENU → Sys Info → Firmware Version (README says 'Fixture Information'); also shown on the web server page"
  methods: ["USB stick (USB-C)", "Web server (Ethernet)", "DMX cable + UPLOAD 08 (recovery)"]
  interface: null
  software: "Web browser (fixture web server, admin/admin)"
  file_type: ".chl"
  download: "https://github.com/Chauvet-Pro/COLORADOPXLBAR16"
tools: []
verification: "web-search"
last_updated: "2026-10-03"
---

# Chauvet Professional COLORado PXL Bar 16

> **2AM CARD** — the stuff you need first
> - **How many on 208 V? → 3 per circuit / power-link chain.** Manual: 3.821 A @208 V, "power linking 3 units @ 208 V", and "never exceed 12 A on a single circuit". 3 × 3.821 = 11.5 A ✓ · 4 × 3.821 = 15.3 A ✗ (over Chauvet's 12 A). Don't jump a 4th even though a 20 A breaker would hold it.
> - **120 V: 1 per feed. No power linking.** Manual says "0 units @ 120 V" (6.60 A each). Each bar needs its own home run. Two bars on one 20 A/120 V circuit = 13.2 A, which is also over Chauvet's 12 A rule.
> - **230 V: 3 per chain** (3.485 A each).
> - **Password:** from the Main Level, **press and hold MENU** → passcode screen → **2323** (Zero Adjust / offset menu). Web server login **admin / admin**.
> - **DMX:** 12 modes in 3 families (Single 19/20/84/154/186, Dual Movement 7/8/20/26, Dual Pixels 48/64/128). Dual Control uses **two start addresses**: one for tilt/zoom, one for pixels.
> - **Won't tilt / "Y_op":** tilt optocoupler error. Check the head-to-base connection, then factory reset. The tilt lock is **for maintenance only, not for transport**.
> - **Tools:** TBD – check on next show.

## Identity
- What crews call it: "PXL Bar", "PXL 16", "PXL line" (a row of them), "COLORado PXL".
- Fixture library / profile names (MA3, GDTF, Hog, Eos): look under Chauvet Professional "COLORado PXL Bar 16". Chauvet keeps a public GitHub repo for this fixture (github.com/Chauvet-Pro/COLORADOPXLBAR16), which probably holds profiles and docs. ⚠️ unverified what it contains. Pick the mode that matches the fixture, and in Dual modes patch **two** fixtures (movement + pixels).
- Variants and how to tell them apart:
  - **PXL Bar 8** is the half-length version (500 mm, 8 cells, 25.2 lb). See [colorado-pxl-bar-8.md](colorado-pxl-bar-8.md). Its power numbers are **different**, so don't mix them up on the plot.
  - **PXL Curve 12** has 12 heads that tilt individually. See [colorado-pxl-curve-12.md](colorado-pxl-curve-12.md).
  - Some retailers (e.g. Adorama) list it as "Chauvet DJ". It is a Chauvet **Professional** product.

## Passwords, menu locks & hidden menus
- **Zero Adjust / offset passcode: 2323.** From the Main Level screen, **press and hold MENU** until the passcode screen appears, then enter 2323. This menu adjusts the tilt home offset.
- **Web server:** default user name **admin**, password **admin**.
- **USB update lock:** Setup → **USB Update** → YES (allows USB updating) / NO (blocks it). If a stick does nothing, check this first.
- Service / factory menu access: Not found — fill in from the fixture.
- How to unlock a locked display: Not found — fill in from the fixture. On sibling Chauvet fixtures the same press-and-hold-MENU passcode screen is used (general knowledge, ⚠️ unverified for this model).

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | 6.60 | 3.821 (some copies round to 3.82) | 3.485 (some copies round to 3.48) |
| Power (W) | 790 | 771 | 768 |
| Max power-link (manufacturer) | **0** ("0 unit @ 120 V") | **3** | **3** |
| **Max per 20 A circuit** (16 A continuous) | floor(16/6.60)=2, link limit 0 → no linking → **1** (2 on separate feeds = 13.2 A, over Chauvet's 12 A rule) | floor(16/3.821)=4, but Chauvet's 12 A rule: floor(12/3.821)=3 = link limit 3 → **3** | floor(16/3.485)=4, Chauvet 12 A: floor(12/3.485)=3 = link limit 3 → **3** |

Also in the manual: 100 V 8.35 A (link 0) and 240 V 3.50 A (link 3).

**Why 3, not 4, at 208 V.** Read this before you argue with the ME.
- The manual's wording is "Power Linking: 0 unit @ 120 V; 3 units @ 208 V; 3 units @ 230 V". Other copies say "it is possible to link up to 0 products at 100 V, 0 at 120 V, 3 at 208 V, 3 at 230 V, or 3 at 240 V… never exceed this number". The same section says **"Never exceed 12 A on a single circuit."**
- If "3" meant 3 linked *after* the first, a chain would be 4 × 3.821 = 15.3 A, which breaks Chauvet's own 12 A line. Read as 3 bars **in total**, the chain is 11.5 A, which fits.
- The PXL Bar 8 and PXL Curve 12 manuals work out the same way: their link counts are the **total** number of fixtures on a circuit under 12 A. See those pages.
- The wiki's generic power-math sheet reads Chauvet's limits as "X + 1" and gets 4 for this bar. For this fixture, the manual's 12 A rule makes **3** the correct number.
- The breaker-only math (4 bars = 15.3 A on a 20 A breaker) won't trip. Running 4, though, goes against the manufacturer's guidance and the published link limit. Use **3**.

- Input range / auto-ranging: 100–240 VAC, 50/60 Hz, auto-ranging.
- Connectors in / out: powerCON TRUE1-compatible input and output ("TRUE1 compatible input and output ports for secure power daisy-chaining", per the Chauvet product page). Power-linking cables are sold separately.
- Fuse (type, rating, location): Not found — fill in from the fixture.
- Inrush / power-up notes: no model-specific note found. With big rows, bring circuits up one at a time (see [power-math](../../reference/power-math.md)).

## Data & addressing
- Connectors: IP65-rated 5-pin DMX in/out, IP65 TCP/IP (Ethernet) in/out, IP65 USB-C (software updates).
- Protocols: DMX, RDM, Art-Net, sACN. A retailer listing also names Kling-Net (⚠️ unverified in the manual).
- DMX modes / footprints (12 total):

| Family | Basic2 | Basic | Standard | Advanced | Tour |
|---|---|---|---|---|---|
| Single Control (one address does everything) | 19 | 20 | 84 | 154 | 186 |
| Dual Control – Movement (tilt/zoom/etc.) | 7 | 8 | 20 | 26 | — |
| Dual Control – Pixels | — | 48 | 64 | 128 | — |

  - In Dual Control you set **two start addresses**: one for the movement block, one for the pixel block. This lets you put pixels in a separate universe or a pixel-mapping server. If pixels respond but tilt doesn't (or the other way round), you've probably patched only one half (general knowledge of the dual-mode concept, ⚠️ unverified menu wording).
  - Two dimmer modes and four dimmer curves are available.
- Set the address (menu path, button by button): Not found — fill in from the fixture. The OLED display uses MENU / UP / DOWN / ENTER buttons (general knowledge, ⚠️ unverified).
- Battery / unpowered addressing: Not found — fill in from the fixture.
- Factory reset: the manual lists "Factory reset" as a fix for errors, so the option exists. Menu location not found — fill in from the fixture.
- Wireless / Ethernet setup notes: the web server login is admin/admin. IP settings menu: Not found — fill in from the fixture.

## Rigging & hardware
- Bracket / omega type and clamp spacing: comes with slotted Omega brackets. Clamps are sold separately and attach straight to the bracket. The Omega bracket holder has a torque rating of **12.2 kgf·cm (10.6 lbf·in)**, so don't over-tighten. Clamp spacing: Not found — fill in from the fixture.
- Fasteners (quarter-turn camlocks etc.): Not found — fill in from the fixture.
- Safety cable point: the manual says to use a safety cable when hanging overhead. Attachment point: Not found — fill in from the fixture.
- Mounting orientations allowed: Not found — fill in from the fixture.
- Transport / pan-tilt locks (location): there is a **tilt lock**. The manual says it is **for maintenance only and not for shipping or transportation**. Location: TBD – check on next show.
- Weight / dimensions: 45.6 lb (20.7 kg). 39.37 x 5.47 x 10.75 in (1000 x 139 x 273 mm). Tilt range 200°.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD – check on next show |
| Gobo / effects module access | n/a (no gobos) | n/a |
| Lens / front glass | TBD – check on next show | TBD – check on next show |
| Omega bracket | TBD – check on next show (torque rating 10.6 lbf·in) | TBD – check on next show |

## Optics & consumables
- Source / lamp, lamp life: 16 × 45 W RGBW LEDs, each one a pixel. Lamp life: Not found.
- Color system: RGBW additive mixing with color macros.
- Gobo wheels: none.
- Prism / frost / zoom / iris / shutters: motorized zoom **5.8°–47.9°**. Motorized tilt 200°. Strobe through the shutter channel (general knowledge).
- Gobo / module change procedure: n/a.

## Error codes
| Code / message | Meaning | Fix (from manual) |
|---|---|---|
| **Y_op** | Tilt optocoupler error | Check the head-to-base connection → factory reset → update reset → replace sensor → replace motor |
| Base Fan1 | Base fan 1 error | Check fan connection → replace fan. ⚠️ Taken from the PXL Bar 8 manual. Likely the same on the 16 but not confirmed |
| FAN1 – FAN5 | Fan error | Check fan connection / head-to-base connection → replace fan. ⚠️ From the PXL Bar 8 manual, as above |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Breaker trips on a 120 V circuit with 2 bars | 2 × 6.6 A = 13.2 A, and Chauvet says 0 links at 120 V | 1 bar per 120 V feed, or move the row to 208 V (3 per circuit) |
| Breaker trips at 208 V with 4+ chained | 4 × 3.821 = 15.3 A, over the 12 A rule and the link limit | Max 3 per chain |
| Shows Y_op / won't tilt | Tilt optocoupler / head-base connection | See error table. Then check the tilt lock is released (it's for maintenance only) |
| Pixels work, tilt/zoom dead (or the other way round) | Dual Control mode with only one of the two addresses patched | Patch both, or switch to a Single Control mode |
| USB stick ignored | USB Update set to NO, or the stick isn't FAT32 | Setup → USB Update → YES. Use a FAT32 stick (≤32 GB per the sibling Curve 12 manual, ⚠️ unverified for Bar 16) |
| Bar dead after an interrupted update | Power or USB pulled while the USB LED was blinking | Needs Chauvet's **UPLOAD 08** device. Call Chauvet support |

## Maintenance
- Recalibrate / reset procedure: Zero Adjust (passcode 2323) for the tilt offset. Factory reset: menu location not found.
- Fan / filter cleaning: Not found — fill in from the fixture.

## Firmware
- Installed version — where to see it on the fixture: the firmware has **Sys Info** and **Firmware Version** screens. The GitHub README says to check "Fixture Information" ⚠️, so check both names. The web server page also shows "Version:".
- Latest known version: **V1.260709** (latest found 2026-10-03). Download from [github.com/Chauvet-Pro/COLORADOPXLBAR16](https://github.com/Chauvet-Pro/COLORADOPXLBAR16) as `Firmware/V1.260709.zip`, which holds `A4073F-COLORADO PXL BAR 16-V1.2607C-260709-1.CHL`. Chauvet's note: **"Please update all units as soon as possible."** A git tag V1.250911 also exists, but it has no README entry.
- What you need: a FAT32 USB stick (≤32 GB) with USB-C or an adapter, **or** a laptop and Ethernet cable for the web server. Keep an UPLOAD 08 for recovery.
- If the stick does nothing: Setup → **USB Update** must be **YES** (manual).
- Update steps (USB stick, from Chauvet's GitHub README; the PXL Bar 16 manual says to set Setup → **USB Update** → YES first):
  1. Unzip the download. Copy only the **.CHL** file to the **root** of a **FAT32** stick, **32 GB or smaller**. The GitHub zip also has a `__MACOSX` folder. Don't copy it.
  2. Power on and plug the stick into the IP65 **USB-C** port. You need a USB-C stick or an adapter.
  3. **"USB UPDATE"** appears → **YES**.
  4. Pick the version with **UP / DOWN** → **ENTER**.
  5. **"USB UPDATE"** appears again → **YES**.
  6. **"USB Update Wait"** shows. **Don't cut power or pull the stick while the USB LED blinks.** Some units then show **"DO NOT UNPLUG, UPDATING"**.
  7. The bar reboots by itself.
  8. Confirm the version, then restart.
- Web server route (the manual says the Upgrade page updates the firmware):
  1. Set the Control Protocol to **Art-Net** and the IP mode to **Static**.
  2. Cable the fixture to a computer. Give the computer an IP address with the same first 3 numbers as the fixture's.
  3. Browse to the fixture's IP address. Log in as **admin / admin**.
  4. Open the **Upgrade** page → choose the file → **Upload File**.
  5. The page warns "Fixture updating, please wait and do not power off the fixture", then "FILE UPLOAD SUCCESS, PLEASE WAIT FOR FIXTURE TO FINISH THE UPGRADE".
  - The button and message text come from the web page built into the firmware.
- Updating a whole rig: the GitHub README and manual excerpts give one bar at a time, by stick or web server. A batch method for this model wasn't found ⚠️ unverified.
- If it fails or bricks mid-update: pulling power or the stick while the LED blinks causes partial or total firmware failure. Recovery needs the **UPLOAD 08** (GitHub README). Use Force Upload: see `_chauvet-common.md`.
- Release notes worth knowing (GitHub README):
  - **V1.260709**: fixed voltage fluctuations for stability and reliability. Chauvet says update all units ASAP.
  - **V1.251014**: strobe refreshes on every value change. **Fixed bars moving randomly in MA3 Art-Net mode with RDM on.** The web server now works in any control mode.
  - V1.241023: fixed control-channel values.
  - V1.241014: fixed the flash-button timing on network control.
  - V1.240830: new PWM firmware. Fixed Single Zoom.
  - **V1.240719**: fixed the thermistor error.
  - **V1.240219**: fixed IGMP subscription (sACN multicast).
  - V1.230522: Factory Reset no longer wipes the pixel color calibration.
  - V1.230321: fixed dimming issues.
  - V1.220627: fixed Red Shift and a web server display message.
  - V1.220411: fixed a strobe issue.

## Road notes (community)
- No forum threads (Reddit / ControlBooth / Blue Room) on this fixture turned up in search. Add your own notes here.
- Retailer/rental notes: the IP65 data and USB ports have caps. Keep them on outdoors (general knowledge).

## Sources
- [COLORado PXL Bar 16 User Manual Rev 10 (Chauvet)](https://www.chauvetprofessional.com/wp-content/uploads/2021/11/COLORado_PXL_16_UM_Rev10.pdf): current draw table (100/120/208/230/240 V), power-linking limits, "never exceed 12 A on a single circuit", Y_op error, Omega torque, tilt range, zoom, firmware/USB update procedure, UPLOAD 08
- [COLORado PXL Bar 16 User Manual Rev 11](https://www.chauvetprofessional.com/wp-content/uploads/2021/11/COLORado_PXL_16_UM_Rev11.pdf) and [Rev 7](https://www.chauvetprofessional.com/wp-content/uploads/2021/11/COLORado_PXL_Bar-16_UM_Rev7.pdf): link limits "0 @ 100/120 V, 3 @ 208/230/240 V… never exceed this number"
- [COLORado PXL Bar 16 User Manual Rev 4 (hirewl mirror)](https://hirewl.com/wp-content/uploads/2022/11/Chauvet-Professional_COLORado-PXL-Bar-16_User-Guide.pdf) and [Chauvet copy](https://www.chauvetprofessional.com/wp-content/uploads/2021/11/COLORado_PXL_16_UM_Rev4.pdf): passcode 2323 via press-and-hold MENU, tilt lock maintenance-only, web server admin/admin
- [COLORado PXL Bar 16 QRG Rev 4](https://www.chauvetprofessional.com/wp-content/uploads/2021/11/COLORado-PXL-Bar-16_QRG_ML5_Rev4.pdf): power and link figures
- [COLORado PXL Bar 16 product page](https://chauvetprofessional.com/product/colorado-pxl-bar-16/): 790 W / 6.60 A, 771 W / 3.821 A, 768 W / 3.485 A, TRUE1-compatible in/out
- [COLORado PXL Bar 16 data sheet (hirewl)](https://hirewl.com/wp-content/uploads/2022/11/Chauvet-Professional_COLORado-PXL-Bar-16_Data-Sheet.pdf) and [gemmiluci mirror](https://www.gemmiluci.it/upload_pdf4/11234.pdf): power and linking
- [manualslib user manual](https://www.manualslib.com/manual/2548073/Chauvet-Colorado-Pxl-Bar-16.html): DMX personalities (Single / Dual Movement / Dual Pixels, channel counts)
- [B&H listing](https://www.bhphotovideo.com/c/product/1691785-REG/chauvet_professional_coloradopxlbar16_colorado_pxl_bar_16_rgbw.html), [SoundPro](https://www.soundpro.com/chauvet-pro-colorado-pxl-bar-16-motorized-ip65-batten/), [usedlighting](https://www.usedlighting.com/51765/new-chauvet-professional-colorado-pxl-bar-16): weight, dimensions, 12 modes, IP65 ports, USB-C, dim modes/curves
- [Adorama listing](https://www.adorama.com/chauvet-dj-colorado-pxl-bar-16-rgbw-led-batten-light-black/p/chcpxlbar16): protocol list including Kling-Net (retailer, unverified)
- [PXL Bar 8 User Manual Rev 9](https://www.chauvetprofessional.com/wp-content/uploads/2021/11/COLORado_PXL-Bar_8_UM_Rev9.pdf): fan error codes (sibling model)
- [PXL Curve 12 manual on manualslib (USB update page)](https://www.manualslib.com/manual/3395060/Chauvet-Colorado-Pxl-Curve-12.html?page=13): .chl / FAT32 / 32 GB (sibling model)
- [github.com/Chauvet-Pro/COLORADOPXLBAR16](https://github.com/Chauvet-Pro/COLORADOPXLBAR16) — firmware versions, release notes, USB update procedure, .CHL file name; web server upgrade page text from the firmware file (checked 2026-10-03)
- [COLORado PXL Bar 16 User Manual Rev 10](https://www.chauvetprofessional.com/wp-content/uploads/2021/11/COLORado_PXL_16_UM_Rev10.pdf) — web server Upgrade page, admin/admin, Art-Net + static IP setup (via search summary)
- [UPLOAD 08 Instructions Rev 4](https://www.chauvetprofessional.com/wp-content/uploads/2015/12/UPLOAD_08_Instructions_Rev4.pdf) — UPLOAD 08 PC setup, COM129, up to 10 same-product fixtures, Force Upload
