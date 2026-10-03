---
title: "Martin MAC Ultra Performance"
manufacturer: "Martin"
model: "MAC Ultra Performance"
aliases: ["ultra", "mac ultra", "ultra performance", "ultra perf"]
type: "profile"
light_source: "LED (wattage not confirmed)"
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
  fuse: null
dmx:
  connectors: null
  protocols: []
  modes: []
menu_password: null
firmware:
  latest_known: "2.3.0"
  checked: "2026-10-03"
  check_on_fixture: "Control panel: SW VERSION / FW VERSION (exact menu path not captured)"
  methods: ["USB stick (USB → FIRMWARE)", "DMX + Martin Companion Cable", "Ethernet (P3 System Controller)"]
  interface: "None for USB stick; Martin Companion Cable P/N 91616091; or P3 System Controller"
  software: "Martin Companion"
  file_type: null
  download: "Martin Companion (cloud) or martin.com/en-US/firmware"
tools: []
verification: "unverified"
last_updated: "2026-10-03"
---

# Martin MAC Ultra Performance

> ⚠️ **Thin page.** The session's web-search budget ran out before this fixture was researched, and no community fixture library had it. Almost everything here is "Not found". Fill it in from the fixture or manual.

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** Not found — fill in from the fixture
> - **Power:** Not found. **Read the rating label.** This is a high-output LED profile (general knowledge), so assume few per 120 V circuit until checked.
> - **DMX:** Not found — fill in from the fixture
> - **Won't move?** Transport locks: Not found — TBD – check on next show
> - **Tools:** TBD – check on next show

## Identity
- What crews call it: "Ultra", "MAC Ultra" (general knowledge).
- Fixture library / profile names: not in Open Fixture Library or QLC+ (checked October 2026).
- Variants: Martin also sells a MAC Ultra Wash (general knowledge). How it differs from the Performance: Not found.

## Passwords, menu locks & hidden menus
- Not found — fill in from the fixture. See [Martin common](./_martin-common.md).

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found | Not found | Not found |
| Power (W) | Not found | Not found | Not found |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | Not found | Not found | — |

- Input, connectors, fuse: Not found — fill in from the fixture.

## Data & addressing
- Connectors, protocols, modes: Not found — fill in from the fixture.
- Set the address: Not found.

## Rigging & hardware
- Not found — fill in from the fixture.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD |
| Gobo / effects module access | TBD – check on next show | TBD |
| Lens / front glass | TBD – check on next show | TBD |
| Omega bracket | TBD – check on next show | TBD |

## Optics & consumables
- Profile with framing (general knowledge). Details: Not found.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| (list exists) | The user manual has an error-message list near the end (manualslib p.39 of 41). The codes were not captured. | Not found — fill in from the fixture |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| — | — | — |

## Maintenance
- Recalibrate / fan / filter cleaning: Not found.

## Firmware
- Installed version — where to see it on the fixture: control-panel item **SW VERSION / FW VERSION** (user guide); exact menu path not captured.
- Latest known version (date checked) and where to download it: **2.3.0** latest found (2026-10-03, via search summary of martin.com). Downloads from the cloud in Martin Companion.
- What you need: USB 2.0 stick, **or** PC + Martin Companion + Companion Cable (P/N 91616091) on DMX, **or** a P3 System Controller over Ethernet (Safety and Installation Manual).
- Update steps (USB): export the firmware from Martin Companion to a stick, disconnect the console, insert the stick, run **USB → FIRMWARE** in the control panel and confirm. The user guide has the full guide (⚠️ screen-by-screen steps not captured). **Don't switch off or remove the stick/source mid-update — the firmware will be corrupted.**
- Updating a whole rig: P3 System Controller over Ethernet, or Companion; limit not found.
- If it fails or bricks mid-update: Not found.
- Release notes worth knowing: **2.0.0** added continuous gobo-wheel scrolling, an **Extended Gamut color mode** and new calibration options (via search summary). Firmware can add or renumber DMX modes — re-check your console patch/profile after updating.

## Road notes (community)
- None found.

## Sources
- [manualslib: Harman Martin MAC Ultra Performance User Manual](https://www.manualslib.com/manual/2079889/Harman-Martin-Mac-Ultra-Performance.html) and [p.39 of 41](https://www.manualslib.com/manual/2079889/Harman-Martin-Mac-Ultra-Performance.html?page=39): shows the manual exists and has an error-message page. No contents captured.
- [Martin firmware page](https://www.martin.com/en-US/firmware) — latest firmware versions and update methods (via web-search summary, checked 2026-10-03)
- [MAC Ultra Performance Safety and Installation Manual rev B](https://www.christielites.com/file_uploads/SFTY_MACUltraPerformance_EN_B.pdf) — USB / Companion / P3 update methods, don't switch off warning
- [MAC Ultra Performance user guide](https://www.christielites.com/file_uploads/UM_MACUltraPerformance_EN_A.pdf) — USB → FIRMWARE, SW/FW VERSION
