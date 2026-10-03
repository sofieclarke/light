---
title: "Martin Atomic 3000 DMX"
manufacturer: "Martin"
model: "Atomic 3000 DMX"
aliases: ["atomic", "atomic 3000", "atomic 3k", "atomic strobe", "atomic dmx", "atomic colors", "atomic 3000 led", "atomic led"]
type: "strobe"
light_source: "3000 W xenon flash tube, 5600 K"
ip_rating: null
weight_lb: null
weight_kg: null
dimensions: "about 425–450 x 239–245 x 234–240 mm (community libraries disagree slightly)"
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
  fuse: null
dmx:
  connectors: "3-pin and 5-pin XLR (community libraries)"
  protocols: ["DMX"]
  modes:
    - { name: "Mode 1 (simple)", channels: 1 }
    - { name: "Mode 2", channels: 3 }
    - { name: "Mode 3", channels: 4 }
    - { name: "Mode 1 + Atomic Colors", channels: 2 }
    - { name: "Mode 2 + Atomic Colors", channels: 4 }
    - { name: "Mode 3 + Atomic Colors", channels: 5 }
    - { name: "Mode 1 + Atomic Colors + fan", channels: 3 }
    - { name: "Mode 2 + Atomic Colors + fan", channels: 5 }
    - { name: "Mode 3 + Atomic Colors + fan", channels: 6 }
menu_password: null
firmware:
  latest_known: null
  checked: "2026-10-03"
  check_on_fixture: null
  methods: []
  interface: null
  software: null
  file_type: null
  download: null
tools: []
verification: "community"
last_updated: "2026-10-03"
---

# Martin Atomic 3000 DMX

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** none expected. No passcode found in any source.
> - **Power:** amps **not found**. "3000 W" is the flash-tube class. **Give each one its own 20 A circuit until you've read the label** (⚠️ unverified rule of thumb). Also check the label's **voltage**. Classic strobes may be built for a set voltage rather than auto-ranging. ⚠️ unverified
> - **DMX:** 1 ch (simple) · 3 ch (intensity, duration, rate) · 4 ch (+ effects). **The Atomic Colors scroller adds a color channel (+1), and the scroller fan adds another (+1).** 3-pin and 5-pin XLR.
> - **Won't flash?** Check the mode and footprint. In the 3/4-ch modes, **intensity, duration AND rate** all need values.
> - **Tools:** TBD – check on next show

## Identity
- What crews call it: "Atomic", "Atomics", "Atomic 3K" (general knowledge). It is the classic touring xenon strobe.
- Fixture library / profile names: Open Fixture Library "Atomic 3000" (1 / 3 / 4 ch). QLC+ "Atomic 3000" has nine modes, including the "with Colour" and "with Colour and Fan" versions for the scroller.
- Variants:
  - **Atomic 3000** (original, analog / Martin protocol) vs **Atomic 3000 DMX**. How to tell them apart and whether control differs: Not found. ⚠️ Check the label.
  - **Atomic Colors**: a color-scroller accessory that fits on the front of the Atomic. It takes an extra DMX channel for color, and optionally one for its fan (see Data).
  - **Atomic 3000 LED**: a different, LED-based fixture (see the section below).

## Passwords, menu locks & hidden menus
- None found. How the address and mode are set on the classic Atomic 3000 DMX: Not found — fill in from the fixture. (DIP switches on the classic unit are general knowledge, ⚠️ unverified.)

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found | Not found | Not found |
| Power (W) | "3000 W" (lamp class, community libraries) | — | — |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | Not found. Plan **1 per circuit** ⚠️ unverified | Not found. Plan **1 per circuit** ⚠️ unverified | — |

- Xenon strobes draw in short, heavy pulses, so average watts tell you little about the peak current. The safe call until you read the label: one per circuit. ⚠️ unverified (general knowledge)
- Input range / voltage version, connectors, fuse: Not found — **read the label before plugging into 208 V.**

## Data & addressing
- Connectors: **3-pin and 5-pin XLR** (Open Fixture Library and QLC+).
- Channels (QLC+ / Open Fixture Library, which cites manual rev G):
  - **Mode 1 (1 ch):** simple strobe.
  - **Mode 2 (3 ch):** intensity, flash duration, flash rate.
  - **Mode 3 (4 ch):** intensity, duration, rate, effects.
  - Each mode can add **Colour** (Atomic Colors scroller), and then **Fan** (scroller fan).
- **Effects channel:** 0–5 none · 6–42 ramp up · 43–85 ramp down · 86–128 ramp up-down · 129–171 random · 172–214 lightning · 215–255 spikes.
- **Atomic Colors channel (QLC+):** 0–25 white · 26–50 straw · 51–76 pale amber gold · 77–104 orange · 105–129 red · 130–155 Broadway pink · 156–180 light lavender · 181–206 aquamarine · 207–229 green blue · 230–254 light green · 255 blue grass.
- **Atomic Colors fan channel (QLC+):** 0–61 level 4 · 62–127 level 3 · 128–190 level 2 · 191–255 level 1.
- Set the address: Not found — fill in from the fixture.

## Rigging & hardware
- Bracket: Not found.
- Weight / dimensions: about 7.5 kg (Open Fixture Library) or 8 kg (QLC+). About 425–450 x 239–245 x 234–240 mm.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD |
| Gobo / effects module access | n/a | — |
| Lens / front glass | TBD – check on next show | TBD |
| Omega bracket / yoke | TBD – check on next show | TBD |
| Atomic Colors scroller mount | TBD – check on next show | TBD |

## Optics & consumables
- 3000 W xenon flash tube, 5600 K. Tube part number and life: Not found.
- Color: white only, unless the Atomic Colors scroller is fitted (11 named colors, above).

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Not found | — | — |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Scroller doesn't move | Patched without "Colour", so the footprint is 1 ch short | Repatch the "+ Colour" mode at the same address and check the next address is free |
| Strobe fires once then nothing, or rate seems stuck | Mode 2/3 with rate or duration at 0 | Bring up intensity, duration and rate |
| Breaker trips when several fire together | Too many on one circuit | 1 per circuit until amps are confirmed |

## Maintenance
- Recalibrate / fan / filter cleaning: Not found.

## Firmware
- Installed version — where to see it on the fixture: Not found for the xenon Atomic 3000 DMX.
- Latest known version (date checked) and where to download it: Not found for the xenon Atomic 3000 DMX (2026-10-03).
- **Atomic 3000 LED** (different fixture): latest found **1.4.0** (2026-10-03, via search summary of martin.com; martin.com also has a v1.1.0 page). Update by **USB type-A memory stick** or over DMX with **Martin Companion + Companion Cable (P/N 91616091)**. Don't switch it off during an update.
- What you need / steps / rig updates: see [Martin common](./_martin-common.md#firmware-updates).
- If it fails or bricks mid-update: Not found.
- Release notes worth knowing: Not captured.

## Road notes (community)
- None captured (search budget ran out).

---

## Atomic 3000 LED (separate fixture)
- LED strobe with a separate RGB "Aura" backlight (general knowledge plus the QLC+ channel names). QLC+ lists **740 W** and 7.8 kg, about 425 x 240 x 245 mm.
- **Modes (QLC+):** 3-ch (beam intensity, duration, rate), 4-ch (+ beam effects), **Extended 14-ch** (+ control, FX select / adjust / sync, Aura shutter, Aura dimmer, Aura R/G/B, Aura color presets). The 3 and 4-ch modes copy the classic Atomic layout, so it drops into an old Atomic patch.
- **Control channel (Extended):** 10–14 reset (5 s). 23–26 dimming curves. 36/37 video tracking on/off. 52/53 display on/off. 54–58 fan modes (54 regulated fan / full output … 58 ultra-low fan). **59 = strobe behaves like an LED, 60 = behaves like xenon.**
- Aura color presets: 36 LEE-referenced colors at DMX 11–190, then rotation and random effects at 191–255.
- Power amps and link limits: Not found.

## Sources
- [Open Fixture Library: atomic-3000.json](https://github.com/OpenLightingProject/open-fixture-library/blob/master/fixtures/martin/atomic-3000.json): 1/3/4-ch modes, 3-pin + 5-pin, 7.5 kg, dims. Cites [UM_Atomic3000DMX_EN_G](https://www.martin.com/files/files/productdocuments/11_MANUALS/999/35000094G%20UM_Atomic3000DMX_EN_G.pdf).
- [QLC+ Martin-Atomic-3000.qxf and Martin-Atomic-3000-LED.qxf](https://github.com/mcallegari/qlcplus/tree/master/resources/fixtures/Martin): nine modes with Colour/Fan, effects, Atomic Colors and fan channel values, Atomic 3000 LED modes, control channel, 740 W.
- [Martin firmware page](https://www.martin.com/en-US/firmware) — latest firmware versions and update methods (via web-search summary, checked 2026-10-03)
- [Atomic 3000 LED product page](https://www.martin.com/en-US/products/atomic-3000-led) and [Atomic 3000 LED firmware v1.1.0](https://www.martin.com/en/softwares/atomic-3000-led-firmware-v1-1-0) — LED version update by USB or Companion Cable
