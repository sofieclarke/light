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
firmware:
  latest_known: null
  checked: "2026-10-03"
  check_on_fixture: "Not found — likely the Information menu ⚠️"
  methods: ["Fixture-to-fixture over DMX (Upload Firmware)", "Web Server over Ethernet", "CloudIO Box + USB stick ⚠️ compatibility unverified"]
  interface: "None for fixture-to-fixture or Web Server; Claypaky Firmware Uploader USB/DMX interface ⚠️ for PC-over-DMX"
  software: "Web browser (built-in web server); Claypaky FUL Uploader ⚠️"
  file_type: ".img (CloudIO USB-stick update); other methods: Not found"
  download: "Claypaky Customer Care site (service.claypaky.it, restricted login) — ask your Claypaky distributor / rental house"
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

## Firmware
- Installed version — where to see it on the fixture: Not found — probably in the Information menu ⚠️. Fill in from the fixture.
- Latest known version (date checked) and where to download it: **Not found** (checked 2026-10-03). Claypaky doesn't publish version numbers openly. Files live on the restricted **Claypaky Customer Care** site (service.claypaky.it). Ask your distributor or the rental house's service department, and write the version you find here.
- Update features Claypaky lists for this model: **firmware upload from another fixture** and **firmware upgrade via web server** (Claypaky product page). **Xtylos (CJ3000), Xtylos Aqua (CJ3001) and Mini Xtylos (CJ3002/CJ3003) are different models: don't mix them on the update line** ⚠️. The laser safety logic is in firmware, so don't run a half-updated fixture.
- What you need:
  - **Fixture-to-fixture (no PC):** one Xtylos already on the version you want, plus a DMX cable to the others. DMX is 5-pin XLR (QLC+). Ethernet port: Not found on this page, but the web-server feature implies one.
  - **From a PC:** Claypaky's **Firmware Uploader USB/DMX interface** (retail listings: "Firmware Uploader Kit USB/DMX", part **C61206** listed for the Alpha 1500). ⚠️ unverified which kit and which PC software suit this model. Claypaky's own Tech Corner video calls the PC tool **"FUL Uploader"** (video title only).
  - **Web Server (Ethernet):** the Xtylos has a built-in web server and Claypaky lists "firmware upgrade via Web Server" (product page). Laptop on the fixture's RJ45, browser to the fixture. The exact steps and IP aren't sourced: see the Tech Corner "Firmware Update with Web Server" video.
  - **CloudIO / CloudIO Box (CA8001):** copy the `.img` firmware file to the **root** of a USB stick, plug it into the CloudIO, open **Fixture Firmware Uploader**, press **CONTINUE**. Every compatible Claypaky fixture on its DMX OUT updates (CloudIO manual). ⚠️ unverified whether this model is on CloudIO's compatible list. USB stick format: Not found.
- Update steps (fixture-to-fixture, Advanced menu; menu path from Claypaky manuals):
  1. Unplug the console from the DMX line ⚠️ (general practice). Leave only fixtures of **the same model** on the line.
  2. Run DMX from the Xtylos that has the wanted firmware into the first fixture to update, and daisy-chain the rest.
  3. On the source fixture: menu → **Advanced** → enter access code **1234** → **Upload Firmware** → confirm.
  4. Don't touch or power-cycle anything until it finishes ⚠️ (general practice). Then check the version on every target (see above).
- Updating a whole rig: **same model only**, and Claypaky recommends **5–6 units at a time maximum** for fixture-to-fixture (manual, via search summary). CloudIO handles up to 31 lights on one DMX line (CloudIO page). Art-Net / sACN firmware update: Not found.
- If it fails or bricks mid-update (recovery mode): **Not found.** No bootloader or recovery procedure was found. Retry from a known-good fixture of the same model, then call Claypaky service. See [_claypaky-common.md](_claypaky-common.md#firmware-updates).
- Release notes worth knowing: Not found. A firmware change can add or renumber DMX modes, so check your console profile against the fixture's mode list after any update.

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
- [Claypaky Xtylos product page](https://www.claypaky.it/products/xtylos/) — firmware upload from another fixture, firmware upgrade via web server (via search summary)
- Claypaky instruction manuals (Sharpy [manuals.plus copy](https://manuals.plus/m/0dc75ba9bd5c288c40aa1eb565a0d3d88973ac670f2f407b78f1e04c1552d923), [A.leda B-EYE K10/K20 user guide (cpl.tech)](https://www.cpl.tech/wp-content/uploads/2018/10/Clay-Paky-A-leda-B-EYE-K10-User-Guide.pdf), [Sharpy Plus (ManualsLib)](https://www.manualslib.com/manual/1637972/Claypaky-Sharpy-Plus.html)) — Upload Firmware copies firmware from one fixture to the others on the line, same model only, 5/6 units at a time max (via search summary; the exact manual page wasn't pinned)
- [B&H: Claypaky C61206 Firmware Uploader USB/DMX interface](https://www.bhphotovideo.com/c/product/1827391-REG/claypaky_c61206_firmware_uploader_usb_dmx_interfacefor.html), [Lightspares: Claypaky Firmware Uploader Kit USB/DMX](https://lightspares.com/claypaky-firmware-uploader-kit-usbdmx-010-074) — the interface exists (retail listings; listed for Alpha-series fixtures)
- [Claypaky CloudIO Instruction Manual 01.2020 (visiontwo.de)](https://www.visiontwo.de/fileadmin/user_upload/Claypaky_CloudIO_Manual_01.2020.pdf), [06.2022 (ltb.no)](https://ltb.no/media/multicase/documents/claypaky/manual_claypaky_cloudio_06.2022.pdf), [CloudIO product page](https://www.claypaky.it/products/cloudio/) — Fixture Firmware Uploader app, `.img` on USB-key root, up to 31 lights on its DMX line, offline use (via search summary)
- Claypaky Tech Corner videos (titles only, not watched): [Firmware Update with FUL Uploader](https://www.youtube.com/watch?v=hyeRWUqLlTk), [Firmware Update with Web Server](https://www.youtube.com/watch?v=Jp4SJ3HJ9N4), [Firmware Update from Fixture to Fixture](https://www.youtube.com/watch?v=xGVPVCwnRPg)
