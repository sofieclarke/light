---
title: "Astera AX1 PixelTube"
manufacturer: "Astera"
model: "AX1 PixelTube"
aliases: ["ax1", "astera ax1", "pixeltube", "pixel tube", "astera tube", "astera"]
type: "pixel-bar"
light_source: "LED RGBW, pixel controllable"
ip_rating: null
weight_lb: null
weight_kg: null
dimensions: null
power:
  input: null
  connector_in: null
  connector_out: null
  watts_max: null
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
  connectors: null
  protocols: ["DMX", "CRMX"]
  modes: []
menu_password: null
firmware:
  latest_known: "V5.16.24"
  checked: "2026-10-03"
  check_on_fixture: "AsteraApp → Connected Lights view → Firmware Version sorting mode"
  methods: ["AsteraApp background update over Bluetooth via ART7 AsteraBox"]
  interface: "Astera ART7 AsteraBox"
  software: "AsteraApp (iOS / Android)"
  file_type: null
  download: "Delivered by AsteraApp (release notes: https://update.astera-led.com/firmwares/current/release_notes.html)"
tools: []
verification: "community"
last_updated: "2026-10-03"
---

# Astera AX1 PixelTube

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** Not found. Fill in from the fixture.
> - **Power:** battery-powered tube. Charger and adapter specs not found. Runtimes not found, so don't guess.
> - **DMX:** about 100 numbered modes (1: RGB … 105: D16 CCT GM H SAT S) in **1, 4 and 16-pixel** versions. **Mode number must match the console profile mode.**
> - **Wireless:** CRMX receiver built in (general knowledge) ⚠️. AsteraApp control goes through an Astera Bluetooth/CRMX bridge box (general knowledge) ⚠️.
> - **Tools:** none usually needed (general knowledge).

## Identity
- What crews call it: AX1, Astera, PixelTube.
- Fixture library / profile names: GDTF "Astera_LED_Technology@AX1_PixelTube" ("tested by Astera / V3"). MA, Eos and Hog have Astera AX1 profiles (general knowledge).
- Variants: **Titan Tube (FP1)** is the newer, longer tube, with a separate page: [astera-titan-tube.md](astera-titan-tube.md). AX2 is the PixelBar. Helios (FP2) and Hyperion (FP3) are other tube lengths.

## Passwords, menu locks & hidden menus
- Not found. Fill in from the fixture.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found | Not found | Not found |
| Power (W) | Not found | Not found | Not found |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | Not found | Not found | — |

- Internal battery; charging case available (general knowledge) ⚠️. Charging specs not found.

## Data & addressing
- Protocols: DMX (wired), CRMX wireless (general knowledge) ⚠️.
- DMX modes: GDTF lists modes numbered 1–105. Families:
  - 1–16: single-pixel "master" modes (RGB, RGBW, RGBAW, DIM variants, RGB CCT DIM IND, + S = strobe). Effect Mode Fix 13 ch, Effect Mode RGB 12 ch.
  - 17–40: 4-pixel modes. 41–64: 16-pixel modes. 65–88: another pixel set (8-pixel inferred from footprints) ⚠️.
  - 89–105: D/D16 CCT GM + RGB / Hue-Sat / XY modes.
- Set the address: AsteraApp or the on-tube menu (general knowledge) ⚠️. Menu path not found.

## Rigging & hardware
- Not found. Fill in from the fixture.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Mounting clips | TBD – check on next show | TBD – check on next show |
| End caps | TBD – check on next show | TBD – check on next show |
| Lens / front glass | n/a | n/a |
| Omega bracket | n/a | n/a |

## Optics & consumables
- RGBW LED, pixel controllable (GDTF description).

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Not found | — | Fill in from the fixture |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Tube ignores the console | Not linked to the CRMX transmitter, or the wrong mode number | Re-link CRMX. Check the mode number matches the patch |
| Only part of the tube responds | Pixel mode mismatch (4 vs 16 pixel) | Match the mode |

## Maintenance

## Firmware
- Installed version — where to see it: in the **AsteraApp**. The Connected Lights view has a **Firmware Version sorting mode** that shows each light's version (search summary). No on-fixture menu path found.
- Latest known version (date checked) and where to download it: **V5.16.24** (latest found, checked 2026-10-03). That's the title of Astera's "current" firmware release-notes page. Which product families it covers wasn't confirmed for the AX1 ⚠️. There's no file to download: the AsteraApp fetches the firmware.
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
- [GDTF Astera_LED_Technology@AX1_PixelTube "tested by Astera / V3" (Lampy-Paperwork mirror)](https://github.com/Ai-Lampy/Lampy-Paperwork/tree/main/gdtf/fixtures/astera): mode names and numbering, product description.
- [Astera firmware release notes, "Firmware V5.16.24"](https://update.astera-led.com/firmwares/current/release_notes.html): latest version found (page title via search; site not readable here)
- [Astera custom firmware update instructions (Wireless Film Lights)](https://wirelessfilmlights.com/wp-content/uploads/2024/07/Astera_Custom_Firmware_Update_Instructions_V1.pdf), [Astera FW 5.14 features and update instructions (Controllux)](https://controllux.com/downloads/2024050712758_5.14.61_Astera_Beta_Firmware_Features_and_update_instructions.pdf), [Ambersphere: Astera firmware update](https://www.ambersphere.com/astera-firmware-51484/): app update procedure, 5.14.84 notes (search summary)
- [AsteraApp control manual](https://astera-led.com/Downloads/AsteraApp%20control.pdf), [ART7 AsteraBox manual](https://astera-led.com/wp-content/uploads/ART7_AsteraBox_Manual_EN_DE_IT_ES_FR_CN.pdf): ART7 as the app's Bluetooth bridge, firmware-version sorting (search summary)
