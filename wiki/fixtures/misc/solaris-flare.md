---
title: "Solaris Flare"
manufacturer: "TMB / Solaris"
model: "Solaris Flare"
aliases: ["flare", "solaris flare", "tmb flare", "flare q+", "flare qplus", "solaris flare q+"]
type: "strobe"
light_source: "LED, 96 x 10 W RGBW Cree LEDs (OFL community data)"
ip_rating: null
weight_lb: 20.9
weight_kg: 9.5
dimensions: "210 x 232 x 497 mm (OFL community data)"
power:
  input: null
  connector_in: null
  connector_out: null
  watts_max: 1000
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
  protocols: ["DMX", "RDM"]
  modes:
    - { name: "Basic RGB 8bit", channels: 3 }
    - { name: "Basic RGB 16bit", channels: 6 }
    - { name: "Basic RGBW 8bit", channels: 4 }
    - { name: "Basic RGBW 16bit", channels: 8 }
    - { name: "Strobe Only", channels: 4 }
    - { name: "RGB Strobe", channels: 7 }
    - { name: "RGBW Strobe", channels: 8 }
    - { name: "Advanced RGB Strobe 1-Pixel", channels: 10 }
    - { name: "Advanced RGB Strobe 2V/2H-Pixel", channels: 13 }
    - { name: "Advanced RGBW Strobe 1-Pixel", channels: 12 }
    - { name: "Advanced RGBW Strobe 2V/2H-Pixel", channels: 16 }
menu_password: null
firmware:
  latest_known: null
  checked: "2026-10-03"
  check_on_fixture: null
  methods: ["Upload menu: cross-load from one Flare to others on the DMX line (password 111)"]
  interface: null
  software: null
  file_type: null
  download: null
tools: []
verification: "community"
last_updated: "2026-10-03"
---

# Solaris Flare

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** Not found. Fill in from the fixture.
> - **Power:** amps not found. Community data lists **1000 W** max (OFL) ⚠️. If that's right, it's roughly 8 A at 120 V. **Plan 1 per 20 A circuit at 120 V until you've read the label** (⚠️ estimate, not a manufacturer figure).
> - **DMX:** Strobe Only = 4 ch (Intensity, Duration, Rate, Effects). RGBW Strobe = 8 ch. Pixel modes run up to 16 ch plus pixel blocks.
> - **RDM:** only on units with **"14R" in the serial number** (e.g. xxxxxx-14R-xxxx), per OFL citing the TMB manual.
> - **Tools:** TBD – check on next show.

## Identity
- What crews call it: Flare, Solaris.
- Fixture library / profile names: OFL "Solaris Flare" (short name TMBFlare, RDM model ID 1703, software 9.3C). GDTF has manufacturer-released files for Flare Q+ Rayzr, Flare XL and XLR (not the original Flare).
- **Flare vs Flare Q+:** Q+ is the later model. **Differences weren't confirmed in this research** (search budget ran out). Don't assume the Q+ uses the same modes or power. Not found, fill in from the fixture or the Q+ manual.

## Passwords, menu locks & hidden menus
- Not found. Fill in from the fixture.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found | Not found | Not found |
| Power (W) | 1000 max (OFL) ⚠️ | 1000 max ⚠️ | — |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | Not found. ⚠️ Estimate: 1000/120 ≈ 8.3 A → floor(16/8.3)=1 | ⚠️ Estimate: 1000/208 ≈ 4.8 A → floor(16/4.8)=3 | — |

- These estimates use watts ÷ volts at PF 1. Real amps are higher if PF < 1. **Replace with the label value.**
- Input range / connectors / fuse: not found.
- Strobes draw peak current in bursts. Full-white strobe chases on many units at once are the worst case (general knowledge).

## Data & addressing
- Connectors: 5-pin XLR (OFL).
- Protocols: DMX; RDM on "14R" serials.
- Effect-channel values (OFL, from the TMB manual):
  - **Flash intensity:** 0–5 off, 6–255 dim to bright.
  - **Flash duration:** 0–254 = 0–650 ms, 255 = HYPER.
  - **Flash rate:** 0–5 closed, 6–255 = 0.5–25 Hz.
  - **Flash effects:** 5 = Wash Override (RGB/RGBW Strobe modes), 6–42 ramp up, 43–85 ramp down, 86–128 ramp up/down, 129–171 random strobe, 172–214 lightning, 215–240 spikes, 241–245 burst (rate at full), 246–250 Meltdown random pixels on solid background, 251–255 Meltdown on burst background.
- Modes (OFL):

| Mode | Ch |
|---|---|
| Basic RGB 8/16-bit | 3 / 6 |
| Basic RGBW 8/16-bit | 4 / 8 |
| Strobe Only | 4 |
| RGB Strobe / RGBW Strobe | 7 / 8 |
| Adv RGB Strobe 1-pix / 2V / 2H | 10 / 13 / 13 |
| Adv RGB Strobe 3/4/6V/6H/12-pix | 7 + pixel block (OFL doesn't expand these) |
| Adv RGBW Strobe 1-pix / 2V / 2H | 12 / 16 / 16 |
| Adv RGBW Strobe 3/4/6V/6H/12-pix | 8 + pixel block |

- Set the address: not found.

## Rigging & hardware
- Weight 9.5 kg, 210 × 232 × 497 mm (OFL). Bracket type not found.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD – check on next show |
| Gobo / effects module access | n/a | n/a |
| Lens / front glass | TBD – check on next show | TBD – check on next show |
| Omega bracket | TBD – check on next show | TBD – check on next show |

## Optics & consumables
- 96 × 10 W RGBW Cree LEDs, 36° (OFL) ⚠️.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Not found | — | Fill in from the fixture |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Console can't discover it via RDM | Older unit without "14R" serial | Address manually |
| Units stay dark in Strobe mode | Flash rate 0–5 = closed, or intensity 0–5 = off | Raise Rate and Intensity above 5 |

## Maintenance
- Not found.

## Firmware
- Installed version — where to see it on the fixture: menu path not found. OFL lists software **9.3C** for the profile it was built from.
- Latest known version (date checked) and where to download it: **not found** (checked 2026-10-03). TMB's Flare manuals exist for software versions from 8.2 up to **11.3** (the combined "Flare Q+, Flare Q+ LR, Flare, Flare Jr" manual on tmb.com). Whether 11.3 runs on an original Flare wasn't confirmed ⚠️. No standalone "Solaris firmware updater" PC tool was found.
- What you need: one Flare that already has the software you want, and a DMX cable to the others.
- Update steps (Flare manual via search summary): the **Upload** menu function cross-loads software from one Flare to the others on the DMX line. It asks for a **password: 111**. Detailed button steps weren't in the summary. Read the Upload section of the manual.
- Updating a whole rig: the Upload function sends to every Flare downstream on the line. **Don't use it with other fixture types on the line** (manual).
- If it fails or bricks mid-update: not found. Contact TMB.
- Release notes worth knowing: not found. RDM only works on units with "14R" in the serial number (see Data & addressing). That's a hardware revision, not something firmware adds ⚠️ unverified.

## Road notes (community)
- Nothing confirmed found. Search budget ran out.

## Sources
- [Open Fixture Library: tmb/solaris-flare.json](https://github.com/OpenLightingProject/open-fixture-library/blob/master/fixtures/tmb/solaris-flare.json): modes, channel values, 1000 W, 9.5 kg, dimensions, LED type, the RDM "14R" serial note. OFL cites the [archived TMB Solaris Flare manual](https://web.archive.org/web/20190219222320/http://pub.tmb.com/solaris/pdf/Solaris-Flare-Manual.pdf) (couldn't be fetched).
- [GDTF manufacturer-release files for Flare Q+ Rayzr / XL / XLR](https://github.com/Ai-Lampy/Lampy-Paperwork/tree/main/gdtf/fixtures/solaris): only confirms those variants exist. Not used for numbers.
- [Solaris Flare operation manual (ManualsLib)](https://www.manualslib.com/manual/1034357/Solaris-Flare.html), [Flare Q+ / Flare / Flare Jr operation manual (tmb.com)](https://tmb.com/docs/solaris/flare/Solaris-Flare-Manual.pdf), [Flare software 8.8 manual (4Wall)](https://cdn.4wall.com/cms/rentals/files/f56033c4bf1b65.pdf): Upload cross-load function, password 111, manual software versions 8.2–11.3 (search summary)
