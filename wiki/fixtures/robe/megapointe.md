---
title: "Robe MegaPointe"
manufacturer: "Robe"
model: "Robin MegaPointe"
aliases: ["megapointe", "mega pointe", "robin megapointe", "mega"]
type: "hybrid"
light_source: "Osram Sirius HRI 470W discharge lamp (Standard 470 W / Eco 380 W)"
ip_rating: null
weight_lb: 48.5
weight_kg: 22
dimensions: "H 640 mm (25.2 in, head vertical) x W 396 mm (15.6 in) x D 230 mm (9.1 in)"
power:
  input: "100–240 VAC, 50/60 Hz, auto-switching"
  connector_in: "Neutrik powerCON TRUE1"
  connector_out: null
  watts_max: 670
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
  protocols: ["DMX", "RDM", "Art-Net", "MA-Net", "MA-Net2", "sACN", "CRMX (wireless version)"]
  modes:
    - { name: "Mode 1", channels: 39 }
    - { name: "Mode 2", channels: 34 }
menu_password: "7623"
firmware:
  latest_known: null
  checked: "2026-10-03"
  check_on_fixture: "Information → Software Versions"
  methods: ["DMX + Robe Universal Interface", "ROBE Uploader (Ethernet / RDM)"]
  interface: "Robe Universal Interface (RUNIT); none for ROBE Uploader over Ethernet"
  software: "ROBE Uploader; DSU uploader (in the DSU package)"
  file_type: "DSU package (.zip)"
  download: "robe.cz product page"
tools: []
verification: "web-search"
last_updated: 2026-10-03
---

# Robe MegaPointe

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** Service password **7623** (fixed). REAP web login **robe / 2479**. Buttons locked → circular slide on the ROBE logo screen (see [_robe-common](_robe-common.md)).
> - **Power:** manual gives **670 W @230 V** only, no amps table. ⚠️ ESTIMATE ONLY (W÷V): ~5.6 A @120 V / ~3.2 A @208 V → about **2 per 20 A @120 V, 5 @208 V**. Not a manufacturer figure; meter it. Power link limit: not found.
> - **DMX:** 39 ch (Mode 1) or 34 ch (Mode 2) · DMX/RDM/Art-Net/sACN/MA-Net · address on the touchscreen (works on battery with no mains)
> - **Won't move / Pan Error?** Pan and tilt transport locks are fitted. Release both before power-up.
> - **Lamp won't strike?** "Lamp Error" after 3 failed ignitions. Let it cool.
> - **Tools:** TBD – check on next show

## Identity
- What crews call it: "Mega", "MegaPointe" (general knowledge).
- Fixture library / profile names: Robin MegaPointe, Mode 1 / Mode 2 (⚠️ unverified naming in MA3/GDTF/Hog/Eos libraries).
- Variants: standard and **Wireless DMX** version (LumenRadio CRMX module and antenna, 2.4 GHz).
- Do NOT put Pointe gobos in a MegaPointe. The manual says they are not designed for the MegaPointe's heat.

## Passwords, menu locks & hidden menus
- Service menu password: **7623**, "cannot be changed" (MegaPointe manual summary).
- REAP (Robe Ethernet Access Portal): user **robe**, password **2479**. Service → Reset Web Password restores it.
- Button lock / Touchscreen Lock: see [_robe-common.md](_robe-common.md).

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not in manual. ⚠️ est. 670/120 ≈ 5.6 | Not in manual. ⚠️ est. 670/208 ≈ 3.2 | Not in manual. ⚠️ est. 670/230 ≈ 2.9 |
| Power (W) | Not found | Not found | 670 W (manual) |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | ⚠️ est. floor(16/5.6)=2 → **2 (estimate)** | ⚠️ est. floor(16/3.2)=5 → **5 (estimate)** | — |

- Input: auto-switching, 100–240 V, 50–60 Hz (manual).
- Connector in: Neutrik powerCON TRUE1 (Robe product page). Power out: not found — check the fixture.
- Fuse: Not found — fill in from the fixture.
- Lamp modes: Standard 470 W (1500 h lamp life) / Eco 380 W (2000 h) (manual).
- Estimates above are watts ÷ volts at a power factor of about 1. They are not from Robe and ignore discharge-lamp strike current. Meter a unit before you load a circuit.

## Data & addressing
- Connectors: Not found — fill in from the fixture (⚠️ likely 5-pin XLR + etherCON, general knowledge).
- Protocols: USITT DMX-512, RDM, ArtNet, MA Net, MA Net2, sACN. Wireless version: CRMX.
- DMX modes: 39 channels or 34 channels (manual: "2 DMX protocol modes").
- Set the address: touch the screen or press [ENTER/Display On]. The Address screen comes up first (Robin convention, see common page).
- Battery / unpowered addressing: yes, battery-backed touchscreen. [ENTER/Display On] wakes it.
- Factory reset: Not found — fill in from the fixture.

## Rigging & hardware
- Bracket: 2x Omega adaptors with 1/4-turn quick locks, included (Robe spec).
- Safety cable point: Not found — fill in from the fixture.
- Transport locks: pan and tilt transport locks fitted (Robe spec). Exact location: TBD – check on next show.
- Pan 540° / Tilt 265°.
- Weight 22 kg (48.5 lb). H 640 × W 396 × D 230 mm.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD |
| Gobo / effects module access | TBD – check on next show | TBD |
| Lens / front glass | TBD – check on next show | TBD |
| Omega bracket | 1/4-turn quick locks (spec) | TBD |

## Optics & consumables
- Source: discharge lamp, 470 W Standard / 380 W Eco. Lamp life 1500 h / 2000 h (manual). Osram Sirius HRI 470W (general knowledge).
- Colour: colour wheel with 13 dichroic filters + white. CMY: ⚠️ unverified, general knowledge.
- Static gobo wheel: 14 gobos + open.
- Rotating gobo wheel: 9 rotating, indexable, replaceable glass gobos + open, "Slot & Lock" holders.
  - **Rotating gobo: OD 15.9 mm, image 12.5 mm, thickness 1.1 mm**, high-temperature borofloat or better.
- Gobo change: Slot & Lock. After you replace one, calibrate it: **Service → Calibration → Calibrate effects → R. Gobo Index 1…9**. Use only MegaPointe gobos, never Pointe gobos.
- Prism / frost / zoom / iris: Not found in sources — fill in from the fixture.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Pan Error 1 | Pan sensor not in function state "connected". Yoke magnetic-indexing circuit fault (sensor failed / magnet missing) or a bad stepper. | Remove the pan lock, reset, then service |
| Pan Error 2 | Pan sensor not in function state "unconnected" (same causes) | As above |
| Pan Error 3 | Pan feedback error | Reset, then service |
| Tilt Error | ⚠️ Robe-wide meaning: head indexing sensor/magnet or stepper/driver fault | Remove the tilt lock, reset |
| Gobo Carousel Error | Rotating gobo wheel not at its default position after reset | Check gobo seating, reset |
| Gobo Rotation Error | Rotating gobos not at their default positions after reset | Check the gobos, recalibrate the index |
| Lamp Error | Lamp failed to ignite 3 times: lamp damaged or missing, or lamp driver failure | Cool down, re-strike, check the lamp |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Pan Error on first power-up | Pan transport lock still on | Unlock, reset |
| Gobo indexing off after a swap | Not calibrated | Service → Calibration → Calibrate effects → R. Gobo Index |
| Can't change settings | Buttons locked | Circular-slide gesture (common page) |

## Maintenance
- Recalibrate: Service → Calibrations (see common page).
- Fan / filter cleaning: Not found — fill in from the fixture.

## Firmware
- Installed version — where to see it on the fixture: **Information → Software Versions**. It lists each processor module separately (e.g. Display System, Module M = pan/tilt, Module G = gobo/effect-wheel processor). Menu confirmed in the Spiider and MegaPointe manuals; for other touchscreen Robins it is the same convention (⚠️ check on the fixture).
- Latest known version (date checked) and where to download it: **Not found** (2026-10-03) — no version number captured for this model. Download the DSU package from this fixture's page on robe.cz.
- What you need: PC (Robe lists Windows; Linux/macOS also supported) · DSU package (.zip with the uploader) · **either** a **Robe Universal Interface / RUNIT** (USB-to-DMX box, also the WTX wireless version) and a DMX cable, **or** an Ethernet connection for **ROBE Uploader**. No USB-stick update method found for Robe. Details: [_robe-common.md](_robe-common.md#firmware-updates).
- Update steps — DMX with the Robe Universal Interface (RUI manual):
  1. Download and unzip the DSU package. Close other PC programs.
  2. **Unplug the console** from the line — the fixture's DMX in must come only from the RUI.
  3. RUI to PC by USB; DMX cable from RUI DMX out to the fixture's DMX in.
  4. Fixture: **Service → Update Software** (touchscreen Robins; older displays: Special Functions → Updating Software).
  5. Run the uploader on the PC, choose **Robe Universal Interface**, Connect, start the update.
  6. Don't touch power or cables until it finishes. Check Information → Software Versions afterwards.
- Update steps — ROBE Uploader (TB54): set the PC to a **2.x.x.x** address (e.g. 2.0.0.1, mask 255.0.0.0) if going over Ethernet. Discover the fixtures (RDM automatic or manual discovery, or build the setup by hand), select them and update. The Uploader puts fixtures into update mode itself. Exact button names: see TB54.
- Updating a whole rig: **ROBE Uploader updates several units in parallel over Ethernet** with no RUNIT needed. Over DMX with the RUI: how many per line is not found. Keep only one model on the line (⚠️ unverified, general practice).
- If it fails or bricks mid-update (TB54): a unit left in update mode **is not re-discovered automatically** — update it by hand with **DSU Mode / "Fix broken device with RUNIT"** in ROBE Uploader (one-to-one, needs the RUNIT). If it restarted mid-update (power cut), fixtures with **Display System 3.0** wait in the **bootloader** for an update on a **10.x.x.x** IP address.
- Release notes worth knowing: A MegaPointe software update added pre-programmed Effect Wheel animations, better priority handling between Optical/Prism/Frost (prevents some frost problems) and internal-communication fixes (Robe news; version number not captured). Read the DSU notes before a show — a software change can change DMX modes and break your console patch.

## Road notes (community)
- No community notes found (search budget ran out). Fill in from experience.

## Sources
- [Robin MegaPointe user manual](https://www.robe.cz/res/downloads/user_manuals/User_manual_Robin_MegaPointe.pdf) — auto-switching PSU, 670 W @230 V, 39/34 ch, protocols, lamp modes, Pan Error 1/2/3, gobo carousel/rotation errors, Lamp Error, 7623, REAP 2479, gobo calibration path, Pointe-gobo warning
- [manualslib MegaPointe Wireless DMX manual](https://www.manualslib.com/manual/1344625/Robe-Robin-Megapointe-Wireless-Dmx.html) — CRMX wireless version
- [Robe MegaPointe product page](https://www.robe.cz/megapointe) / [product PDF](https://cdn.aws.robe.cz/print/en_product_635.pdf) — weight, dimensions, pan/tilt, transport locks, omegas, powerCON TRUE1
- [Replaceable gobos in Robe fixtures](https://www.robelighting.com/res/downloads/gobo_config/Robe_Fixtures_Gobos_overview.pdf) and [MegaPointe leaflet](https://www.robe.cz/res/downloads/catalogues/ROBE_MegaPointe_leaflet.pdf) — gobo dimensions, wheel counts
- [Storm DMX chart](https://cdn.stormltd.co.uk/content/2018/09/Robe_megaPointe_DMX.pdf) — DMX protocol (not read directly)
- [Robe news: Software improvements for Robin MegaPointe](https://www.robe.cz/news/software-improvements-for-robin-megapointe-documentation-updates) — effect-wheel animations, frost priority fix
- [TB54 ROBE Uploader manual v1.0.9](https://www.robelighting.de/res/downloads/tech_bulletins/TB54_ROBE_Uploader_manual_EN.pdf) — Ethernet/RDM parallel update, 2.x.x.x PC address, DSU Mode / Fix broken device with RUNIT, bootloader recovery (via search summary)
- [Robe Universal Interface manual v1.7](https://www.robe.cz/res/downloads/user_manuals/User_manual_Robe_Universal_Interface.pdf) — DMX update via RUI, Special Functions → Updating Software
- [Robin Spiider manual v3.3](https://www.robelighting.com/res/downloads/user_manuals/User_manual_Robin_Spiider.pdf) — Information → Software Versions, Service → Update software (Robe touchscreen convention)
