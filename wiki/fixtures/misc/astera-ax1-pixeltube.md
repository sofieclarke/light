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
- Firmware: AsteraApp (general knowledge) ⚠️.

## Road notes (community)
- Nothing confirmed found. Search budget ran out.

## Sources
- [GDTF Astera_LED_Technology@AX1_PixelTube "tested by Astera / V3" (Lampy-Paperwork mirror)](https://github.com/Ai-Lampy/Lampy-Paperwork/tree/main/gdtf/fixtures/astera): mode names and numbering, product description.
