---
title: "Martin MAC Aura XB"
manufacturer: "Martin"
model: "MAC Aura XB"
aliases: ["aura xb", "mac aura xb", "aura", "auras", "xb"]
type: "wash"
light_source: "LED, RGBW beam LEDs + RGB Aura backlight (exact LED count not confirmed)"
ip_rating: null
weight_lb: 14.4
weight_kg: 6.5
dimensions: "302 x 302 x 360 mm (11.9 x 11.9 x 14.2 in), L x W across yoke x H head straight up"
power:
  input: "100–240 VAC, 50/60 Hz, auto-ranging"
  connector_in: null
  connector_out: null
  watts_max: 400
  amps_120v: 3.2
  amps_208v: 1.8
  amps_230v: null
  link_max_120v: 3
  link_max_208v: 8
  link_max_230v: 8
  per_20a_120v: 3
  per_20a_208v: 8
  fuse: null
dmx:
  connectors: null
  protocols: ["DMX"]
  modes:
    - { name: "Standard (STD)", channels: 14 }
    - { name: "Extended (EXT)", channels: 25 }
menu_password: null
firmware:
  latest_known: "1.3.0"
  checked: "2026-10-03"
  check_on_fixture: null
  methods: ["DMX + Martin Companion Cable", "Ethernet (Martin Companion)"]
  interface: "Martin Companion Cable P/N 91616091"
  software: "Martin Companion"
  file_type: null
  download: "martin.com/en-US/firmware or Martin Companion"
tools: []
verification: "web-search"
last_updated: "2026-10-03"
---

# Martin MAC Aura XB

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** No passcode found in any source. ⚠️ unverified — if a display is locked, see [Martin common](./_martin-common.md).
> - **Power:** 3.2 A @120 V / 1.8 A @208 V → **3 per 20 A circuit @120 V, 8 @208 V**. The manual's limit is **3 fixtures *in total* on one feed at 100–120 V, 8 *in total* at 200–240 V**. At 120 V the link limit is the cap, not the breaker.
> - **DMX:** 14 ch (STD) or 25 ch (EXT). Pick the mode in **CONTROL MODE**. Default address is 1.
> - **Won't move?** No transport lock is described in any source. If pan or tilt fails at reset, look for **PAN FBACK ERR / TILT FBACK ERR** (or FBEP / FBET) on the display. Those are sensor errors.
> - **Tools:** TBD – check on next show

## Identity
- What crews call it: "Aura", "Aura XB", "XB" (general knowledge). The XB is the brighter version of the original MAC Aura. The original Aura is a separate fixture with different power figures (see below).
- Fixture library / profile names: QLC+ and Open Fixture Library only have the original **MAC Aura** (14 / 25 ch). The XB modes have the same channel counts (see Sources). ⚠️ Patching an XB with an original-Aura profile is unverified. Check the channel order against the XB manual.
- Variants and how to tell them apart:
  - **MAC Aura** (original): about 5.6 kg, about 245–260 W per community fixture libraries. Firmware goes on with Martin Uploader + USB Duo.
  - **MAC Aura XB**: 6.5 kg, 400 W max. Firmware goes on over DMX with Martin Companion.
  - **MAC Aura XIP**: the IP-rated outdoor version. **MAC Aura PXL**: the bigger pixel version (see [mac-aura-pxl](./mac-aura-pxl.md)).

## Passwords, menu locks & hidden menus
- Default passcode: none found. Not found — fill in from the fixture.
- Service menu: the user manual lists **SERVICE → CALIBRATION** (for example PAN OFFSET) as part of the onboard menu (manualslib menu page). How to get in: Not found — fill in from the fixture.
- Factory settings: the menu has a **FACTORY SETTING** entry (manualslib onboard menus page).
- Unlocking a locked display: Not found — fill in from the fixture.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | 3.2 A (355 W measured @120 V/60 Hz) | 1.8 A (350 W measured @208 V/60 Hz) | Not found |
| Power (W) | 400 W max, under 25 W idle | 400 W max | 400 W max |
| Max power-link (manufacturer) | **3 fixtures in total** at 100–120 V | **8 fixtures in total** at 200–240 V | 8 in total |
| **Max per 20 A circuit** (16 A continuous) | floor(16/3.2)=5, but the link limit is 3 in total → **3** | floor(16/1.8)=8 (link limit 8 in total) → **8** | — |

- Input range: auto-ranging 100–240 VAC (manual).
- Link-limit wording: the manual says "maximum three (3) MAC Aura XB fixtures **in total**". That count includes the first fixture, so do **not** add 1.
- Connectors in / out: Not found — fill in from the fixture.
- Fuse: Not found — fill in from the fixture.
- Inrush / power-up notes: Not found.

## Data & addressing
- Connectors: Not found — fill in from the fixture.
- Protocols: DMX. RDM support is not confirmed.
- DMX modes / footprints (manual via search):
  - **STD, 14 ch:** channels 1–14 drive the Beam and the Aura together, and both behave the same.
  - **EXT, 25 ch:** channels 1–14 drive the Beam, 15–19 are FX (preset effects using Beam and Aura together), and 20–25 drive the Aura on its own.
- Set the address: use the onboard control panel and the backlit graphic display, menu **DMX ADDRESS**. The address shows on the display after power-up and reset. Default is 1. The fixture limits the address range so the whole footprint always fits in 512.
- Other top-level menus named in the manual: DMX ADDRESS, CONTROL MODE, COLOR MODE, PERSONALITY, FACTORY SETTING, SERVICE.
- Battery / unpowered addressing: Not found.
- Factory reset: the **FACTORY SETTING** menu (exact steps not found).
- Original-Aura control channel (Open Fixture Library, may also apply to the XB, ⚠️ unverified for XB): DMX 10–14 resets the fixture. 40–54 sets pan/tilt speed NORM / FAST / SLOW. 60–64 sets the fan to FULL, 70–74 to REGULATED. 90–94 turns COLOR CALIB on. With Color Calib on, the "Beam White" channel does nothing, because white comes from RGB mixing.

## Rigging & hardware
- Bracket / omega type: an Omega bracket with trigger clamp, or an Omega bracket with a 28 mm spigot for a monopole (spec sheet). A quick surface-mounting bracket comes as a set of 5, P/N 91606018.
- Fasteners: Not found.
- Safety cable point: Not found — fill in from the fixture.
- Mounting orientations allowed: Not found.
- Transport / pan-tilt locks: none found in any source. TBD – check on next show.
- Weight / dimensions: 6.5 kg (14.4 lb) without accessories. 302 mm across the yoke each way, 360 mm tall with the head straight up. Pan 540°, tilt 232°.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD |
| Gobo / effects module access | n/a (wash) | — |
| Lens / front glass | TBD – check on next show | TBD |
| Omega bracket | TBD – check on next show | TBD |

## Optics & consumables
- Source: LED. Light comes from the Beam LEDs plus a separate Aura backlight behind the front lens. LED life: Not found.
- Color system: RGBW mixing on the beam, RGB on the Aura. There is a COLOR MODE menu. COLOR CALIB lines up color between fixtures (Open Fixture Library, original Aura).
- Gobos / prism / frost: none (wash). Zoom range for the original Aura is listed as 11–58° (community libraries). Not confirmed for the XB.

## Error codes
Errors flash on the display, 1 s on and 1 s off. If there is more than one, each one flashes three times before the next one shows. Errors override a blanked display (HARMAN help center).

| Code / message | Meaning | Fix |
|---|---|---|
| MAIN TMP SEN ERR | The temperature sensor circuit on the main PCB in the head has failed. LEDs will not turn on. | Service manual: if the main PCB is overheating, replace the fan. If the wire between the main PCB and the LED PCBs is faulty, replace harness P/N 11860396. |
| BEAM TMP SEN ERR | The Beam LED temperature sensor circuit has failed. The Beam LEDs will not turn on. | Service |
| AURA TMP SEN ERR | The Aura LED temperature sensor circuit has failed. | Service |
| MAIN TMP CUT OFF | The main PCB temperature is too high, so power to the LEDs is cut. | Check the fan and airflow. Let it cool. |
| AURA TMP CUT OFF | The Aura is overheating. LEDs cannot be turned on. | Check the fan and airflow |
| PAN FBACK ERR / TILT FBACK ERR | The optical pan or tilt feedback circuit has failed (for example a bad sensor). | Service: check the sensor PCB and timing belt (service manual covers belt and sensor replacement) |
| Pan / Tilt Sensor Error | Fails the reset, the reset sounds wrong, or pan/tilt positions are off. | Service manual troubleshooting |
| FBEP / FBET | Fails the reset because pan (P) or tilt (T) keeps moving until it times out. | Pan/tilt feedback: check the sensor and belt |
| Voltage error | Reset is fine but an error shows, or the Aura works but the Beam LEDs will not light. | Service manual |
| Fan error | A fan has stopped, so the LEDs will not turn on. | Check or replace the fan |
| Beam Calib Err | Resets fine and the LEDs work, but beam color does not match other fixtures. | Recalibrate (service) |
| MEMORY ERROR | The EEPROM cannot be read. | Service |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| A 4th fixture on a 120 V link misbehaves or the breaker trips | Over the manual's limit of 3 in total at 120 V | Re-feed: 3 per feed at 120 V, 8 at 208 V |
| Aura lights but Beam doesn't | Voltage error or BEAM TMP SEN ERR | Read the display. See error table. |
| LEDs won't come on at all | Fan error, MAIN TMP SEN ERR, or a temperature cutoff | Check the fan and airflow. Read the display. |
| Beam color mismatched vs neighbours | Beam Calib Err, or COLOR CALIB set differently between fixtures | Match the COLOR CALIB / COLOR MODE settings |
| Aura and beam do the same thing | Fixture is in STD mode | Switch CONTROL MODE to EXT (25 ch) and repatch |

## Maintenance
- Recalibrate: SERVICE → CALIBRATION (for example PAN OFFSET).
- Fan / filter cleaning: Not found.

## Firmware
- Installed version — where to see it on the fixture: Not found — check the INFORMATION menu (⚠️ unverified).
- Latest known version (date checked) and where to download it: **1.3.0** latest found (2026-10-03, via search summary of martin.com). Free from martin.com/en-US/firmware or inside Martin Companion.
- What you need: Windows PC with **Martin Companion** (free) and the **Martin Companion Cable, P/N 91616091**, on the DMX line — or Martin Companion over Ethernet (martin.com lists both). No USB socket method found for the XB. The original MAC Aura used **Martin Uploader + USB Duo** instead.
- Update steps: connect the Companion Cable (USB on the PC, DMX into the fixture's DMX in, console unplugged), open Martin Companion, find the fixture, choose the firmware, update. Exact screens: ⚠️ unverified — see [Martin common](./_martin-common.md#firmware-updates).
- Updating a whole rig: Companion can work on many selected fixtures; per-line firmware limit not found.
- If it fails or bricks mid-update: Not found for the XB.
- Release notes worth knowing: **1.3.0 is needed for units built with an alternative component on the Beam LED board** (end-of-life part), and fixes **no blue on the Aura (back-light) in Extended mode at DMX address 2**. Don't load older firmware on newer-built units (⚠️ inference from that note). Firmware can add or renumber DMX modes — re-check your console patch/profile after updating.

## Road notes (community)
- No XB-specific road notes found in searches.
- Martin documentation says the Aura LED PWM frequency was picked to avoid flicker on camera. With unusual camera settings you may have to adjust the PWM frequency by hand (Martin XIP manual text, also in search summaries). The XB menu location for this is not confirmed.

## Sources
- [MAC Aura XB User Manual rev B (HARMAN ADN PDF)](https://adn.harmanpro.com/site_elements/executables/6742_1526699551/35000280b_UM_MACAuraXB_EN_B_original.pdf): amps at 120/208 V, link limits (3 / 8 in total), 400 W max, under 25 W idle, auto-ranging. Also at [martin.com](https://www.martin.com/en/site_elements/martin-mac-aura-xb-user-manual).
- [manualslib: MAC Aura XB User Manual p.14](https://www.manualslib.com/manual/889904/Martin-Mac-Aura-Xb.html?page=14), [p.30 onboard menus](https://www.manualslib.com/manual/889904/Martin-Mac-Aura-Xb.html?page=30), [p.32 display messages](https://www.manualslib.com/manual/889904/Martin-Mac-Aura-Xb.html?page=32): DMX modes and their meaning, menu names, error messages.
- [MAC Aura XB Service Manual rev A](https://adn.harmanpro.com/site_elements/executables/3917_1526136318/ServiceManual_MAC_Aura_XB_RevA_original.pdf) / [manualslib p.6](https://www.manualslib.com/manual/1404416/Martin-Mac-Aura-Xb.html?page=6): error-code overview, harness P/N 11860396.
- [MAC Aura XB spec sheet](https://www.martin.com/en-US/site_elements/mac-aura-xb-spec-sheet-english) / [product page](https://www.martin.com/en-US/products/mac-aura-xb): weight, dimensions, pan/tilt range, omega and surface-bracket P/N.
- [HARMAN help: Martin MAC fixture display error messages explained](https://help.harmanpro.com/en_US/general-mac-inquiries/martin-mac-fixture-display-error-messages-explained): how errors flash.
- [Martin firmware page](https://www.martin.com/en-US/firmware): Martin Companion and cable P/N 91616091.
- [Open Fixture Library: martin/mac-aura.json](https://github.com/OpenLightingProject/open-fixture-library/blob/master/fixtures/martin/mac-aura.json) and [QLC+ Martin-MAC-Aura.qxf](https://github.com/mcallegari/qlcplus/tree/master/resources/fixtures/Martin): original-Aura control channel and weight (community, original Aura only).
- [Martin Companion Cable user guide](https://www.martin.com/en-US/site_elements/martin-manuals-martin-companion-cable-user-manual) — PC + Companion Desktop to fixtures over DMX/RDM, firmware upgrades
- [MAC Aura XB product page](https://www.martin.com/en-US/products/mac-aura-xb/1000) — firmware 1.3.0 notes (via search summary)
