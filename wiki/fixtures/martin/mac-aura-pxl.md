---
title: "Martin MAC Aura PXL"
manufacturer: "Martin"
model: "MAC Aura PXL"
aliases: ["aura pxl", "mac aura pxl", "pxl", "aura pixel"]
type: "wash"
light_source: "LED, 19x 40 W RGBW beam pixels + RGB Aura backlight (141 Aura pixels)"
ip_rating: null
weight_lb: null
weight_kg: null
dimensions: null
power:
  input: "100–240 VAC nominal, 50/60 Hz"
  connector_in: "Neutrik powerCON TRUE1"
  connector_out: "Neutrik powerCON TRUE1 (AC throughput)"
  watts_max: 560
  amps_120v: 6.4
  amps_208v: 2.8
  amps_230v: 2.8
  link_max_120v: null
  link_max_208v: null
  link_max_230v: null
  per_20a_120v: 2
  per_20a_208v: 5
  fuse: null
dmx:
  connectors: null
  protocols: ["DMX", "P3"]
  modes:
    - { name: "Compact", channels: 17 }
    - { name: "Basic", channels: 32 }
    - { name: "Extended", channels: 89 }
    - { name: "Ludicrous", channels: 512 }
menu_password: null
tools: []
verification: "web-search"
last_updated: "2026-10-03"
---

# Martin MAC Aura PXL

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** No passcode found in any source. ⚠️ unverified
> - **Power:** maximum is 6.4 A @100–120 V / 2.8 A @200–240 V. Typical at full intensity is 4.1 A @120 V / 2.4 A @208 V. → **2 per 20 A circuit @120 V, 5 @208 V** (worked from the maximum figures). **Link limit not found.**
> - **DMX:** Compact 17 · Basic 32 · Extended 89 · **Ludicrous 512** (a whole universe per fixture). Also takes P3 video pixel data.
> - **Won't move?** Transport locks: Not found — TBD – check on next show
> - **Tools:** TBD – check on next show

## Identity
- What crews call it: "PXL", "Aura PXL" (general knowledge).
- Fixture library / profile names: not in the community libraries checked (Open Fixture Library, QLC+). Use the console's own library or the Martin website.
- Variants and how to tell them apart: there is an "EPS" listing from resellers (for example "MAC Aura PXL EPS"). What it means is not confirmed. ⚠️ unverified. Sister fixtures are the smaller [MAC Aura XB](./mac-aura-xb.md) and the IP-rated MAC Aura XIP.

## Passwords, menu locks & hidden menus
- Default passcode: none found. Not found — fill in from the fixture.
- Service / factory menu access: Not found — fill in from the fixture.
- How to unlock a locked display: Not found.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | **6.4 A max** (100–120 V). Typical at full: 4.1 A @120 V, 5.0 A @100 V | **2.8 A max** (200–240 V). Typical at full: 2.4 A | 2.8 A max. Typical: 2.2 A |
| Power (W) | 560 W max total, 500 W typical | 560 / 500 W | 560 / 500 W |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | Max: floor(16/6.4)=2 → **2**. With typical 4.1 A it would be floor(16/4.1)=3. | Max: floor(16/2.8)=5 → **5**. With typical 2.4 A it would be floor(16/2.4)=6. | — |

- Input: 100–240 VAC nominal, 50/60 Hz.
- Connectors: Neutrik powerCON TRUE1, with AC throughput (spec sheet).
- The spec sheet heads the maximum-current figures as "AC power throughput … maximum total current". It is not clear if that is the per-fixture maximum or a throughput rating. This page uses them as per-fixture maximums, which is the safe reading. ⚠️ Check the manual's power-linking section and fill in the link limit.
- Fuse: Not found — fill in from the fixture.

## Data & addressing
- Connectors: Not found — fill in from the fixture.
- Protocols: DMX and P3 (Martin's video-pixel protocol over Ethernet). The Basic mode has a "P3 Mix" channel that sets the color source: DMX, P3 video pixels, or a mix of both. RDM, Art-Net and sACN are not confirmed.
- DMX modes / footprints (user manual via search):
  - **Compact, 17 ch.**
  - **Basic, 32 ch:** everything in Compact, plus the P3 Mix channel.
  - **Extended, 89 ch:** adds RGB control of each beam pixel on channels 33–89, with virtual dimmers on each beam pixel.
  - **Ludicrous, 512 ch:** channels 1–89 are the same as Extended, plus RGB for each of the 141 Aura pixels. It takes **one whole universe per fixture.**
- Cabling limits from the manual (search summary): **up to 32 devices on one DMX serial link.** On Ethernet, avoid more than **50 devices in one daisy chain or branch.**
- Set the address: Not found — fill in from the fixture.
- Battery / unpowered addressing: Not found.
- Factory reset: Not found.

## Rigging & hardware
- Bracket / omega type: Not found.
- Safety cable point: Not found.
- Transport / pan-tilt locks: Not found — TBD – check on next show.
- Weight / dimensions: Not found — fill in from the fixture.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD |
| Gobo / effects module access | n/a (wash) | — |
| Lens / front glass | TBD – check on next show | TBD |
| Omega bracket | TBD – check on next show | TBD |

## Optics & consumables
- Source: 19 RGBW LED beam pixels (40 W class per resellers) plus the Aura backlight with 141 pixels (manual). Resellers list CCT control from 2000–10000 K and zoom of about 6–59°. ⚠️ unverified (reseller copy).
- Gobos / prism: none.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| (list exists) | The user manual has an "Error Messages" section (manualslib p.44). The codes were not captured. | Not found — fill in from the fixture |

Error display behaviour is the same as other Martin MACs: flashing, and a red LED indicator. See [Martin common](./_martin-common.md).

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Pixel content ignored / fixture only does DMX color | P3 Mix channel set to DMX only, or wrong mode | Use Basic or higher. Set P3 Mix to P3 or mix. |
| Patch runs out of universe | Ludicrous mode = 512 ch | Use Extended (89) unless every Aura pixel needs control |
| Breaker trips on 120 V with 3 or more fixtures | 6.4 A maximum each | 2 per 20 A circuit @120 V, or move to 208 V |

## Maintenance
- Recalibrate: Not found.
- Firmware update method: Not found for this model. Martin's newer fixtures use Martin Companion (see [Martin common](./_martin-common.md)).

## Road notes (community)
- None found.

## Sources
- [MAC Aura PXL spec sheet (martin.com)](https://www.martin.com/en/site_elements/martin-specifications-mac-aura-pxl-spec-sheet) / [AVC Group copy](https://www.avc-group.com/assets/products/Martin/pdfs/martin-ds-mac_aura_pxl.pdf): powerCON TRUE1 throughput, 560 W max, maximum and typical currents at each voltage.
- [MAC Aura PXL User Manual (Full Compass)](https://www.fullcompass.com/common/files/86975-MACAuraPXLUserManual.pdf): typical and maximum current, the 32-device DMX limit, the 50-device Ethernet branch advice.
- [MAC Aura PXL User Guide rev B (Christie Lites)](https://www.christielites.com/file_uploads/UM_MACAuraPXL_EN_B.pdf) / [manualslib](https://www.manualslib.com/manual/1976037/Harman-Martin-Mac-Aura-Pxl.html): the four DMX modes and their channel counts, P3 Mix, 141 Aura pixels, Error Messages section (p.44).
- [Farralane listing](https://www.farralane.com/martin-professional-mac-aura-pxl-19-x-40-watt-rgbw-aura-led-moving-head-wash.html): 19x 40 W, 6–59° zoom, 2000–10000 K (reseller, unverified).
