---
title: "GLP JDC1"
manufacturer: "GLP (German Light Products)"
model: "JDC1"
aliases: ["jdc1", "jdc-1", "jdc 1", "jdc", "glp strobe", "jdc1 strobe", "hybrid strobe"]
type: "strobe"
light_source: "LED: cool-white linear tube (12 beam pixels) + RGB plates (12 plate pixels)"
ip_rating: null
weight_lb: 24
weight_kg: 10.8
dimensions: "154 x 390 x 284 mm (L x W x H, head horizontal)"
power:
  input: "100–240 VAC, 50/60 Hz, autosensing"
  connector_in: "Neutrik powerCON TRUE1 (20 A)"
  connector_out: "none (no AC thru per search summary)"
  watts_max: 1200
  amps_120v: null
  amps_208v: 5.8
  amps_230v: 5.3
  link_max_120v: 0
  link_max_208v: 0
  link_max_230v: 0
  per_20a_120v: 1
  per_20a_208v: 2
  fuse: ""
dmx:
  connectors: "5-pin XLR in/thru; etherCON (unconfirmed for JDC1)"
  protocols: ["DMX", "RDM", "Art-Net", "sACN"]
  modes:
    - { name: "Mode 6 Easy (SW 1.78+)", channels: 11 }
    - { name: "Mode 1 Compressed Pro", channels: 14 }
    - { name: "Mode 5 1Pix Pro", channels: 17 }
    - { name: "Mode 2 Normal", channels: 23 }
    - { name: "Mode 4 SPix Pro", channels: 62 }
    - { name: "Mode 3 SPix", channels: 68 }
menu_password: null
firmware:
  latest_known: "1.95"
  checked: "2026-10-03"
  check_on_fixture: "Information → SW/HW versions (main and distributed)"
  methods: ["DMX link with GLP D3Prog", "GLP iQ.Service Portal (file source) ⚠️"]
  interface: "GLP D3Prog (USB/Sub-D 9 to PC; 5-pin + 3-pin XLR out)"
  software: "D3Prog PC transfer (software name not found)"
  file_type: ".bin (3 driver files, updated in sequence) ⚠️"
  download: "glp.de product page → Downloads, or GLP iQ.Service Portal; also germanlightproducts.com/downloads"
tools: []
verification: "web-search"
last_updated: "2026-10-03"
---

# GLP JDC1

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** No user passcode found. The **Service** menu needs a Key Code (0–255) and is meant for GLP Service only; the code isn't published.
> - **Power:** 1200 W. **5.3 A @230 V** (spec), **5.8 A @208 V** (rental spec), 120 V not published (1200/120 ≈ 10 A, estimate only) → **1 per 20 A circuit @120 V, 2 @208 V**. **There's no power thru, so each unit gets its own feed.** One source says it "can draw 10 amps at 100 volts" and so can't daisy-chain.
> - **DMX:** 6 modes: Easy 11 · Compressed Pro 14 · 1Pix Pro 17 · **Normal 23** · SPix Pro 62 · SPix 68. Address via the 4-button LCD (Mode / Enter / Up / Down). **The display runs off a battery, so you can address it unpowered.**
> - **Won't move?** **Tilt lock lever** locks the head horizontal. Slide it to unlocked before power-up.
> - **Error on screen?** Errors flash alternately with the DMX address and **stay up until the next power cycle or reset**. Go to Information → System Errors List.
> - **Tools:** Omega bracket (GLP part 87036) bolts to the rear. Screw sizes: TBD – check on next show.

## Identity
- What crews call it: "JDC", "JDC1", "the GLP strobe", "hybrid strobe". It's on almost every big tour rig.
- Successor: the **JDC Burst 1** (2025). Search summaries say it has legacy JDC1 emulation modes ⚠️. Check which one you have: they're different fixtures with different manuals.
- Fixture library / profile names: the Open Fixture Library has "GLP JDC1". MA / Hog / Eos names: Not found — fill in from the fixture. **Match the mode to the software version.** Easy mode (11 ch) only exists from SW 1.78 (manual "SW 178-69-19") onward.
- Variants: there's no physical variant of the JDC1 itself. Don't confuse it with JDC2 IP, JDC Burst 1 or JDC Line 500/1000.

## Passwords, menu locks & hidden menus
- Default passcode: **none found** for normal use.
- Service menu: **password-protected**. You enter a code (0–255) in the **Key Code** field. The manual says it's for GLP Service. The code is not published: Not found.
- How to unlock a locked display: Not found in sources. On the X4 Bar, Mode + Enter + Up toggles the key lock, but that's ⚠️ unverified for the JDC1.
- Navigation (manual): **Mode** = escape / back to the top of the menu, **Enter** = select / run / open a submenu, **Up/Down** = scroll.
- A separate **technical service manual** exists (rev 2.0, Aug 30 2023). See Sources.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not published. Estimate 1200 W/120 V ≈ 10 A. One source says "10 amps at 100 volts" ⚠️ | 5.8 A (rental-house spec, ⚠️ not manual table) | 5.3 A @230 V 50 Hz (spec / catalog) |
| Power (W) | 1200 W max (spec, rated @230 V) | 1200 W | 1200 W |
| Max power-link (manufacturer) | **None: no AC thru** | None | None |
| **Max per 20 A circuit** (16 A continuous) | floor(16/10)=1 (estimate amps; no thru) → **1** | floor(16/5.8)=2 → **2** (on a distro, not linked) | floor(16/5.3)=3 → 3 on a 20 A circuit (EU 16 A breaker: floor(16/5.3)=3, tight) |

- Input range: autosensing 100–240 V, 50/60 Hz.
- Connectors: **one 20 A Neutrik powerCON TRUE1 in** (3-conductor). It doesn't power-link. The source wording: "Because it can draw 10 amps at 100 volts, these fixtures cannot daisy chain their AC."
- Fuse: Not found — fill in from the fixture.
- Inrush / power-up: Not found. With full-white strobe on a 120 V show, put one per circuit and don't share the circuit with movers.

## Data & addressing
- Connectors: 5-pin XLR DMX in and thru (manual). Some summaries also list **etherCON in/out A & B (failsafe)**, but that may come from the JDC Burst 1 datasheet ⚠️. The JDC1 manual does mention the display "shows network IP addresses below the DMX Address", so it has some Ethernet input. Check the connector panel.
- Protocols: DMX512-A, RDM (E1.20), Art-Net, sACN, GLP iQ.Mesh (summaries; ⚠️ iQ.Mesh may be Burst-1-only).
- **DMX modes.** Channels 1–14 are laid out the same in Modes 1–5:
  - **Mode 1 Compressed Pro: 14 ch.** These are the standard 14 channels used in every mode except Easy:
    - ch 1–2: 16-bit tilt (185°)
    - beam (tube) shutter effects: strobe, ramp up/down, etc.
    - ch 8–11: plate shutter effects, with variable intensity, duration and rate
    - ch 12–14: plate RGB
  - **Mode 2 Normal: 23 ch.**
  - **Mode 3 SPix: 68 ch.** Pixel-level control.
  - **Mode 4 SPix Pro: 62 ch.**
    - ch 1–14: standard
    - ch 15–50: RGB for plate pixels 1–12
    - ch 51–62: white intensity for beam pixels 1–12
  - **Mode 5 1Pix Pro: 17 ch.**
    - ch 1–14: standard
    - ch 15–17: grouped plate RGB
  - **Mode 6 Easy: 11 ch** (SW 1.78 and later).
    - ch 1–7: standard control without plate shutter effects
    - ch 8–11: grouped plate color (the summary says RGBW)
- Older manuals (SW 1.35 / 1.70) list only 5 modes. If Easy is missing, the fixture is on old software.
- Set the address: Mode → **DMX Address** → Enter → Up/Down (001–512; the highest valid address depends on the mode) → Enter.
- Battery / unpowered addressing: **yes.** The graphic LCD has a **self-charging battery**, so you can change settings with mains off (manual).
- Information menu (manual) shows:
  - internal errors (System Errors List)
  - main and distributed SW/HW versions
  - temperature sensors
  - operating hours and boot count
  - whether it's running on AC or battery
- Factory reset: Not found — fill in from the fixture.
- Ethernet setup: Not found for the JDC1 specifically. The Burst 1 has Auto 2.x.x.x / Auto 10.x.x.x / Custom IP, Art-Net port, sACN universe, and Protocol Setup → Data In ⚠️ (Burst 1 manual, may differ).

## Rigging & hardware
- Bracket: an **omega bracket (part no. 87036)** mounts to the rear of the fixture. For head-down or sideways hanging, bolt **two half-couplers** to the omega attachment (manual).
- Safety cable point: there are eyelets for safety cables (spec / listing). Exact location: TBD.
- Orientations: **any orientation**, or stood on a level surface on its rubber feet (manual).
- Transport / tilt lock: a **tilt lock lever** locks the head horizontal. Slide it to locked for transport and **release it before operating**. Search summaries mention a 2023 manual revision about releasing the tilt lock; details weren't found.
- Weight: **10.8 kg / 24 lb**, or **12 kg / 26.5 lb with bracket**.
- Dimensions: 154 L x 390 W x 284 H mm with the head horizontal.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD |
| Gobo / effects module access | n/a | — |
| Lens / front glass | TBD – check on next show | TBD |
| Omega bracket | TBD – check on next show | TBD |

## Optics & consumables
- Source: a central cool-white LED **tube** (beam, 12 pixels) plus surrounding **RGB plates** (12 pixels). They run independently or together. Listings disagree on LED counts: Farralane says 1320 RGB + 216 cool white; 4Wall says "1,440 LEDs". ⚠️
- Beam angle: 86° (Farralane listing) ⚠️.
- Tilt: **185°** (manual) with self-correcting position feedback. One spec source says 182°.
- No gobos, prism, frost or zoom.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| (any error text) | Self-diagnosis found a fault. It flashes alternately with the DMX address and **stays on screen until a power cycle or reset** | Read Information → **System Errors List**. Power-cycle; if it comes back, the fault is real |
| Specific message list | Not found in search excerpts | Fill in from the manual's error section |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Head won't tilt / tilt error at boot | Tilt lock lever still locked | Slide the lever to unlocked, then reset or power-cycle |
| Breaker trips at 120 V | More than one JDC1 on a 20 A circuit (≈10 A each at full) | One per 20 A circuit @120 V |
| Some features missing vs. the console profile (no Easy mode) | Old software (pre-1.78) | Update the firmware or use a matching profile/mode |
| Old error still showing after the fix | Errors are sticky | Power-cycle or reset |
| Plates and tube out of step | Wrong mode, e.g. a Normal profile on SPix | Check mode vs. patch |

## Maintenance
- Recalibrate / reset: Not found in excerpts.
- Fan / cooling: the Information menu lets you watch fan operation and temperatures (manual).
- A technical service manual (rev 2.0, 2023) exists for GLP service partners.

## Firmware
- Installed version — where to see it on the fixture: **Information** menu → main and distributed **SW/HW versions** (manual). Software strings look like **178-69-19** (= 1.78) in the manual.
- Latest known version (date checked) and where to download it: **1.95** (latest found, checked 2026-10-03): a GLP download page titled "JDC-1 Firmware 1.95" exists on germanlightproducts.com (title only, not read). V1.90 and 1.61_67_18 pages also exist. The JDC1 product page on glp.de points to the **iQ.Service Portal** for the latest firmware.
- What you need:
  - **GLP D3Prog** (GLP's firmware programmer). Load the firmware into one of its memory slots from a PC over **USB (Type B)** or **Sub-D 9**, then plug it into the fixture's DMX in. It has **both 5-pin and 3-pin female XLR**, so no adapter needed. Runs on 2x 1.2 V Mignon (AA) rechargeables, so it works with no mains near it (glp.de). Retail part no. **9506** is listed for the "D-Prog" uploader ⚠️ (may be the older model).
  - Files: the JDC-1 update is **BIN files: all 3 driver files have to be updated in sequence**. Choose file type **BIN** when importing to the D3Prog (GLP firmware note, via search summary ⚠️ unverified wording).
  - USB port on the fixture / Art-Net update: Not found for the JDC1.
- Update steps:
  1. On the PC, import the firmware into a D3Prog memory slot. Pick file type **Intel hex** or **BIN** to match the firmware file (GLP tech note, via search summary).
  2. **Unplug the console and anything else on the line that you aren't updating.** GLP says no other DMX receivers or consoles may be active (tech note, via search summary).
  3. D3Prog XLR out → DMX in of the first fixture, daisy-chain the rest. Fixtures powered.
  4. Choose the slot on the D3Prog and start the upload. The button sequence on the D3Prog: Not found.
  5. Don't power-cycle until it reports done ⚠️ (general practice), then check the version on each fixture.
  6. Repeat for each of the 3 driver files in the order GLP gives in the release note ⚠️ (order not found).
- Updating a whole rig: Daisy-chain over DMX with the D3Prog; GLP says several fixtures on a line can be done at once. A per-line maximum: Not found. Keep the line JDC1-only ⚠️.
- If it fails or bricks mid-update (recovery mode): A GLP firmware page says: **if your fixture is on V1.78 or below, update the Bootloader first** before the main application (via search summary, and it wasn't pinned to the JDC-1 page ⚠️). The D3Prog can also program over **AVR/ISP**, which is a service-level route (glp.de); details are in the JDC1 technical service manual (rev 2.0, not read). Otherwise contact support@glp.de.
- Release notes worth knowing: **SW 1.78 added Mode 6 Easy (11 ch).** Older fixtures (1.35 / 1.70) only have 5 modes. Updating a mixed rig changes which modes exist, so check your console patch. Detailed release notes for 1.90 / 1.95: Not found.

## Road notes (community)
- No Reddit, ControlBooth or Blue Room threads were found in the searches.
- Search summaries of PLSN / spec material say it **can't daisy-chain AC**. That's the most common rookie mistake with these on 120 V shows.
- Soundlightup ran a road test, "GLP JDC1, the LED strobe that tilts"; its content wasn't retrieved.

## Sources
- [JDC1 User Manual Rev 20240830-01 (SW 178-69-19), glp.de](https://glp.de/files/products/jdc1-product-data/GLP_JDC1_User_Manual_EN_Rev20240830-01.pdf) — 100–240 V, 1200 W @230 V, TRUE1, menu buttons, Service Key Code, battery display, sticky errors, Information menu, tilt lock lever, rigging
- [JDC1 User Manual SW 1.70-68-18 (Full Compass)](https://www.fullcompass.com/common/files/45303-JDC1UserManual.pdf) / [ShowTools mirror](https://www.showtools.com.au/wp-content/uploads/2024/05/JDC1-User-Manual-EN-v3.0-SW1.70-68-18.pdf) — 5 modes, 14–68 ch
- [JDC1 Manual SW 1.35 (v1.0)](https://germanlightproducts.com/wp-content/uploads/2018/03/JDC1-User-Manual-EN-v1.0.pdf) — earliest manual
- [JDC1 DMX Channel Index V4.0 (SW 178-69-19)](https://glp.de/files/products/jdc1-product-data/JDC1_DMX_Channel_Index_EN_V.4.0_Rev.20191023.pdf) — 6 modes incl. Easy 11 ch, mode channel layouts
- [ManualsLib JDC1 p.15 (DMX), p.24 (specs)](https://www.manualslib.com/manual/1293811/Glp-Jdc1.html)
- [JDC1 spec sheet](https://www.germanlightproducts.com/wp-content/uploads/2017/04/PDF-Spec-Sheet-JDC1.pdf) and [ArchiExpo catalog](https://pdf.archiexpo.com/pdf/glp/jdc1/60940-304597.html) — 5.3 A @230 V, weight, dimensions, 182°/185° tilt, omega 87036
- [Christie Lites JDC1 listing](https://www.christielites.com/glp-jdc1-strobe/228w2w14w20w408) — 5.8 A @208 V (attributed in search summary)
- [PLSN JDC1 product spotlight](https://plsn.com/articles/product-spotlight/glp-jdc1-strobe/) — likely source of "10 amps at 100 volts… cannot daisy chain" (search summary didn't pin the exact URL)
- [Farralane listing](https://www.farralane.com/glp-jdc1-strobe-1320-x-rgb-216-x-white-led-hybrid-strobe.html) — LED counts, 86° beam
- [4Wall JDC1 rental](https://www.4wall.com/rentals/9758615/glp-jdc1) — 185° tilt, "1,440 LEDs"
- [JDC1 technical service manual rev 2.0](https://germanlightproducts.com/wp-content/uploads/2025/03/Service-manual-of-JDC-1-rev2.0-Aug.30th-2023.pdf) — exists; contents not retrieved
- [JDC Burst 1 User Manual](https://www.germanlightproducts.com/wp-content/uploads/2025/06/GLP-JDC-Burst1-User-Manual-EN-Rev20250606-02.pdf) — successor; Ethernet menu structure (used only as a ⚠️ hint)
- [Soundlightup road test](https://en.soundlightup.com/archives-3/tests/glp-jdc1-the-led-strobe-that-tilts.html) — not read
- [Open Fixture Library: GLP JDC1](https://open-fixture-library.org/glp/jdc1)
- GLP download pages (germanlightproducts.com, titles only, not read): [JDC-1 Firmware 1.95](https://www.germanlightproducts.com/download/jdc-1-firmware-1-95/), [JDC-1 Firmware V1.90](https://www.germanlightproducts.com/download/jdc-1-firmware-v1-90/), [JDC-1 Software Version 1.61_67_18](https://www.germanlightproducts.com/download/jdc-1-software-version-1-61_67_18/)
- [GLP D3Prog product page (glp.de)](https://glp.de/en/products/service-firmware/service-tools/d3prog-en) — D3Prog: USB / Sub-D 9 to PC, memory slots, DMX link or AVR/ISP output, XLR 5- and 3-pin female, 2x 1.2 V Mignon batteries, several fixtures at once (via search summary)
- GLP Tech News [2019/10/30](https://www.glp.de/en/service/tech-info-archive/archive/80-glp-tech-news-2019-10-30?tmpl=component) and [2019/01/14](https://www.glp.de/en/service/tech-info-archive/archive/73-glp-tech-news-2019-01-14) — hex vs BIN file type when importing to the D3Prog, daisy-chain via DMX with no other receivers or consoles active (via search summary; which note said what wasn't pinned)
- [GoKnight: GLP 9506 D-Prog Uploader](https://goknight.com/german-light-products-9506-d-prog-uploader/), [Solotech: GLP 9506 D-Prog Firmware Uploader](https://shop.solotech.com/products/glp-9506-d-prog-firmware-uploader) — retail part number 9506 (D-Prog; may be the older model, not D3Prog)
- [JDC Burst 1 User Manual Rev 20250606-02](https://www.germanlightproducts.com/wp-content/uploads/2025/06/GLP-JDC-Burst1-User-Manual-EN-Rev20250606-02.pdf) — successor: update via DMX link with D-Prog, GLP iQ.Mesh or GLP iQ.Tool; Burst 1 firmware V0.3.4.0 (Aug 2025) (via search summary)
