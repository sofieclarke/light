---
title: "Astera Titan Tube (FP1)"
manufacturer: "Astera"
model: "FP1 Titan Tube"
aliases: ["titan", "titan tube", "astera titan", "fp1", "astera tube", "astera"]
type: "pixel-bar"
light_source: "LED, tunable white plus RGB pixels (16 pixels)"
ip_rating: null
weight_lb: 3.0
weight_kg: 1.35
dimensions: "1035 x 42 x 42 mm (OFL community data)"
power:
  input: null
  connector_in: null
  connector_out: null
  watts_max: 48
  amps_120v: null
  amps_208v: null
  amps_230v: null
  link_max_120v: null
  link_max_208v: null
  link_max_230v: null
  per_20a_120v: null
  per_20a_208v: null
  fuse: ""
dmx:
  connectors: "5-pin XLR (OFL community data)"
  protocols: ["DMX", "CRMX"]
  modes:
    - { name: "1: RGB", channels: 3 }
    - { name: "2: RGBW", channels: 4 }
    - { name: "4: DIM RGB", channels: 4 }
    - { name: "5: DIM RGBW", channels: 5 }
    - { name: "7: RGB CCT DIM IND", channels: 6 }
    - { name: "15: Effect Mode Fix", channels: 13 }
    - { name: "17: RGB.RGB. 4pix", channels: 15 }
    - { name: "41: RGB.RGB. 16pix", channels: 63 }
    - { name: "89: D CCT GM CRO RGB", channels: 7 }
    - { name: "90: D CCT GM HUE SAT", channels: 5 }
menu_password: null
firmware:
  latest_known: "V5.16.24"
  checked: "2026-10-03"
  check_on_fixture: "AsteraApp \u2192 Connected Lights view \u2192 Firmware Version sorting mode"
  methods: ["AsteraApp background update over Bluetooth via ART7 AsteraBox"]
  interface: "Astera ART7 AsteraBox"
  software: "AsteraApp (iOS / Android)"
  file_type: null
  download: "Delivered by AsteraApp (release notes: https://update.astera-led.com/firmwares/current/release_notes.html)"
tools: []
verification: "community"
last_updated: "2026-10-03"
---

# Astera Titan Tube (FP1)

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** Not found. Fill in from the fixture.
> - **Power:** battery or AC (GDTF description: "AC-powered or on battery"). **48 W** per OFL ⚠️. Runtimes not found.
> - **DMX:** numbered modes. Mode number on the tube must match the console. Common ones: 1 RGB (3) · 5 DIM RGBW (5) · 7 RGB CCT DIM IND (6) · 41 16-pixel RGB (63) · 89 D CCT GM CRO RGB (7).
> - **Wireless:** "wired or wireless DMX" (GDTF description). CRMX (general knowledge) ⚠️. AsteraApp on the go.
> - **Tools:** none usually needed (general knowledge).

## Identity
- What crews call it: Titan, Titan Tube, Astera.
- Fixture library / profile names: OFL "FP1 Titan Tube". QLC+ "Astera-Titan-Tube-FP1". GDTF "Astera_LED_Technology@FP1_Titan_Tube".
- Variants: Helios (FP2, shorter), Hyperion (FP3), and AX1 PixelTube (older, separate page: [astera-ax1-pixeltube.md](astera-ax1-pixeltube.md)).

## Passwords, menu locks & hidden menus
- Not found. Fill in from the fixture.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found | Not found | Not found |
| Power (W) | 48 (OFL) ⚠️ | — | — |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | Not found | Not found | — |

- Battery and charging-case specs: not found.

## Data & addressing
- Connectors: 5-pin XLR per OFL ⚠️ (Astera tubes often use a different DMX/power input, so check).
- Protocols: DMX, wireless (CRMX, general knowledge ⚠️), AsteraApp.
- DMX modes (OFL, from Astera "Titan Tube DMX Profiles" PDF):

| # | Mode | Ch |
|---|---|---|
| 1 | RGB | 3 |
| 2 | RGBW | 4 |
| 3 | RGBAW | 5 |
| 4 | Dim RGB | 4 |
| 5 | Dim RGBW | 5 |
| 6 | Dim RGBAW | 6 |
| 7 | RGB CCT Dim Ind (Ind = LEE gel index) | 6 |
| 8–14 | Same as 1–7 + Strobe | +1 |
| 15 | Effect Fix | 13 |
| 16 | Effect RGB | 10 (OFL) / 12 (GDTF) ⚠️ |
| 17–40 | 4-pixel versions | e.g. 17 RGB.RGB. 4pix = 15 |
| 41–64 | 16-pixel versions | e.g. 41 RGB.RGB. 16pix = 63 |
| 89 | D CCT GM CRO RGB | 7 |
| 90 | D CCT GM HUE SAT | 5 |
| 91 | D16 CCT GM CRO RGB | 8 |
| 92 | D16 CCT GM H SAT | 7 |

- Set the address: AsteraApp or the on-tube display (the GDTF filename mentions a "display") ⚠️. Menu path not found.

## Rigging & hardware
- 1.35 kg, 1035 × 42 × 42 mm (OFL, GDTF weight agrees). Clips/brackets not found.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Mounting clips | TBD – check on next show | TBD – check on next show |
| End caps | TBD – check on next show | TBD – check on next show |
| Lens / front glass | n/a | n/a |
| Omega bracket | n/a | n/a |

## Optics & consumables
- 2,900 lm, 120° (OFL) ⚠️. 16 pixels (OFL matrix).

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Not found | — | Fill in from the fixture |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Pixels map wrong | 4-pix vs 16-pix mode mismatch | Match the mode number |
| No wireless response | Not linked to the transmitter | Re-link (unlink/link from the transmitter) ⚠️ procedure not found |

## Maintenance

## Firmware
- Installed version — where to see it: in the **AsteraApp**. The Connected Lights view has a **Firmware Version sorting mode** that shows each light's version (search summary). No on-fixture menu path found.
- Latest known version (date checked) and where to download it: **V5.16.24** (latest found, checked 2026-10-03). That's the title of Astera's "current" firmware release-notes page. Which product families it covers wasn't confirmed for the Titan Tube ⚠️. There's no file to download: the AsteraApp fetches the firmware.
- What you need: a phone or tablet with the latest **AsteraApp** (iOS / Android) and an **ART7 AsteraBox**, the app's Bluetooth bridge to the lights. Full details in [_misc-common.md](_misc-common.md#astera).
- Update steps (Astera / dealer instructions via search summary):
  1. Update the AsteraApp from the app store.
  2. Connect the app to the ART7 over Bluetooth. Put the lights in BlueMode and press **Pair with Lights**. Wait until all of them are paired.
  3. **App Settings → Lights Background Update**, then press the update button at the **top right**.
  4. The lights update in the background and keep working while they do. Keep the app open and the phone awake ("Keep Screen On" in App Settings).
- Updating a whole rig: background update goes to all paired lights. A per-batch limit wasn't found.
- If it fails or bricks mid-update: no recovery mode found. Re-pair and run Lights Background Update again ⚠️ unverified.
- Release notes worth knowing: **5.14.84** fixed reported wired-DMX problems and added support for PowerBox wired DMX protocol version 2. Astera's DMX mode numbers have to match your console profile. Check the mode list after a big update.

## Road notes (community)
- Nothing confirmed found. Search budget ran out.

## Sources
- [Open Fixture Library: astera/fp1-titan-tube.json](https://github.com/OpenLightingProject/open-fixture-library/blob/master/fixtures/astera/fp1-titan-tube.json): modes, 48 W, 1.35 kg, dimensions, lumens. OFL links the [Astera Titan Tube manual](https://astera-led.com/Downloads/manual/FP1_TitanTube_Manual.pdf) and [DMX profiles PDF](https://astera-led.com/Downloads/Profile/Titan%20Tube%20DMX%20Profiles.pdf) (astera-led.com blocked, not read).
- [GDTF FP1 Titan Tube (Lampy-Paperwork mirror)](https://github.com/Ai-Lampy/Lampy-Paperwork/tree/main/gdtf/fixtures/astera): mode names, 1.35 kg, product description (battery/AC, wired/wireless, AsteraApp).
- [Astera firmware release notes, "Firmware V5.16.24"](https://update.astera-led.com/firmwares/current/release_notes.html): latest version found (page title via search; site not readable here)
- [Astera custom firmware update instructions (Wireless Film Lights)](https://wirelessfilmlights.com/wp-content/uploads/2024/07/Astera_Custom_Firmware_Update_Instructions_V1.pdf), [Astera FW 5.14 features and update instructions (Controllux)](https://controllux.com/downloads/2024050712758_5.14.61_Astera_Beta_Firmware_Features_and_update_instructions.pdf), [Ambersphere: Astera firmware update](https://www.ambersphere.com/astera-firmware-51484/): app update procedure, 5.14.84 notes (search summary)
- [AsteraApp control manual](https://astera-led.com/Downloads/AsteraApp%20control.pdf), [ART7 AsteraBox manual](https://astera-led.com/wp-content/uploads/ART7_AsteraBox_Manual_EN_DE_IT_ES_FR_CN.pdf): ART7 as the app's Bluetooth bridge, firmware-version sorting (search summary)
