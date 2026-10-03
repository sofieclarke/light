---
title: "Chauvet Professional Rogue R3X Wash"
manufacturer: "Chauvet Professional"
model: "Rogue R3X Wash"
aliases: ["r3x wash", "r3x", "rogue r3x", "rogue r3x wash", "roguer3xwash"]
type: "wash"
light_source: null
ip_rating: null
weight_lb: null
weight_kg: null
dimensions: null
power:
  input: null
  connector_in: "Neutrik powerCON NAC3MPA-1 (blue), per BOM"
  connector_out: "Neutrik powerCON NAC3MPB-1 (grey), per BOM"
  watts_max: null
  amps_120v: null
  amps_208v: null
  amps_230v: null
  link_max_120v: null
  link_max_208v: null
  link_max_230v: null
  per_20a_120v: null
  per_20a_208v: null
  fuse: "12 A, 250 V (BOM: 'fuse 12A 520 250V', likely 5x20 mm)"
dmx:
  connectors: "3-pin and 5-pin XLR in/out (BOM)"
  protocols: ["DMX", "RDM"]
  modes:
    - { name: "15CH", channels: 15 }
    - { name: "21CH", channels: 21 }
    - { name: "27CH", channels: 27 }
    - { name: "33MS", channels: 33 }
    - { name: "54MS", channels: 54 }
    - { name: "62CH", channels: 62 }
    - { name: "71CH", channels: 71 }
    - { name: "107CH", channels: 107 }
menu_password: "2323"
firmware:
  latest_known: "V1.250331"
  checked: "2026-10-03"
  check_on_fixture: "MENU → Sys Info → Ver"
  methods: ["DMX cable + UPLOAD 08"]
  interface: "Chauvet UPLOAD 08"
  software: "UPLOAD 08 PC software (Windows)"
  file_type: ".chl"
  download: "https://github.com/Chauvet-Pro/ROGUER3XWASH"
tools: []
verification: "web-search"
last_updated: "2026-10-03"
---

# Chauvet Professional Rogue R3X Wash

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** **2323**. From the main screen, press and hold the menu button (MENU, per the sibling R2X manual) until the passcode screen appears → 2323 → ENTER → Zero Adjust (offset). The R3X Wash manual Rev 4 was the top result for this procedure.
> - **Power:** amps **Not found — fill in from the fixture label**. Link limit not found.
> - **DMX:** firmware modes 15 / 21 / 27 / 33MS / 54MS / 62 / 71 / 107. 27CH was added in V1.250331. 3-pin and 5-pin XLR.
> - **Won't move?** **Pan lock and tilt lock** (BOM). Release both.
> - **Tools:** TBD – check on next show.

## Identity
- What crews call it: "R3X", "R3X Wash".
- Not the same as the **R3 Wash** (older) or the **Outcast 3X Wash** (IP65).

## Passwords, menu locks & hidden menus
- **2323**: from the main level, press and hold the menu button until the passcode screen appears. UP raises the value, DOWN moves to the next digit. ENTER → offset / Zero Adjust.
- Firmware strings: "Password", "Zero Adjust".

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found | Not found | Not found |
| Power (W) | Not found | Not found | Not found |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | Can't compute | Can't compute | Can't compute |

- Connectors (BOM): powerCON NAC3MPA-1 in and NAC3MPB-1 out.
- Fuse (BOM): "fuse 12A 520 250V" in an FH1-B-MW holder. The R2X and R3 Spot use 7 A, so this fuse is NOT interchangeable with them. Carry the right spare.
- PSU (BOM): H08-UP450S30.

## Data & addressing
- DMX: 3-pin and 5-pin (DMX012A Amphenol board, BOM).
- Modes (firmware strings): 15CH, 21CH, 27CH, 33MS, 54MS, 62CH, 71CH, 107CH ⚠️ (check against the menu and console library; strings can include unused modes).
- Address: MENU → Address → 001–512 → ENTER.

## Rigging & hardware
- Omega bracket (BOM): several revisions exist, and they are not identical:
  - V2: CD-D13 140 mm, shorter, with 6 mm washer.
  - V3: CD-D13, taller.
  - V4: CD-D23-140, the current one.
  - There is also a "Quick Lock Hanging Bracket – 140V".
  - If a clamp/omega combo won't seat, it may be a mixed bracket revision.
- **Locks (BOM):** tilt lock (wheel, pick, axis, plus a complete Tilt Lock Assembly part) and pan lock (post, pick).
- Weight / dimensions: Not found.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | Not found | TBD – check on next show |
| Gobo / effects module access | n/a | n/a |
| Lens / front glass | Not found | TBD – check on next show |
| Omega bracket | Quarter-turn quick lock | TBD – check on next show |

The BOM lists M8×30 and M8×90 screws, location not stated.

## Optics & consumables
- LED count and wattage: Not found. BOM: LED PCBs ALJB061A / ALJB062A, a lens cluster, and a frost filter assembly (Ø13 mm 10° frost filters).

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Thermistor Open / Thermistor Short | Firmware strings. Probably a temperature sensor fault ⚠️ | Service |
| Lamp Hot / Hot | Firmware string. Probably over-temperature ⚠️ | Check fans |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Grinding at power-up | Locks engaged | Release pan and tilt locks |
| Full output differs between dimmer modes | Old firmware | V1.191202+ |
| No 27CH mode | Old firmware | V1.250331 |

## Maintenance
- Firmware: see the Firmware section below.

## Firmware
- Installed version — where to see it on the fixture: **MENU → Sys Info → Ver**. The firmware has "Sys Info" / "System Information" screens. The exact field isn't confirmed in this model's manual ⚠️.
- Latest known version: **V1.250331** (latest found 2026-10-03). Download from [github.com/Chauvet-Pro/ROGUER3XWASH](https://github.com/Chauvet-Pro/ROGUER3XWASH); the file is `R3XW-V1.250331-250401-1.CHL`. The repo's newest commit (2026-09-04) only added a BOM PDF.
- What you need: a **Chauvet UPLOAD 08**, a Windows PC with its software, and a DMX cable (3-pin or 5-pin). The repo has no USB instructions ⚠️.
- Update steps (UPLOAD 08 over DMX; full PC setup in `_chauvet-common.md`):
  1. On a Windows PC, install the UPLOAD 08 software (v4.5.2 or later), Microsoft .NET Framework and the Silicon Labs **CP210x** driver.
  2. Plug in the UPLOAD 08 with its USB cable. In Device Manager → Ports, set the "Silicon Labs CP210x USB to UART Bridge" to **COM129**.
  3. Unplug the console. Run a DMX cable from the UPLOAD 08 to the first fixture, then daisy-chain fixtures of **this model only**.
  4. Power the fixtures on.
  5. In the app, click **Open** and select the .CHL (or older .CL) file. Follow the on-screen steps.
  6. Any fixture that doesn't take it → **Force Upload** (see recovery below).
  7. Check the version afterwards.
  - Source: UPLOAD 08 Instructions Rev 4. "Unplug the console" is general knowledge.
- Updating a whole rig: UPLOAD 08 does **up to 10 fixtures of the same product** per pass (Instructions Rev 4). The product page says up to 12, but plan on 10. Don't mix models on the line.
- If it fails or bricks mid-update: use the UPLOAD 08's **Force Upload**.
  1. Power the fixture off, but leave it connected.
  2. Check that the UPLOAD 08 LED is flashing.
  3. Select the file.
  4. Click **Force Upload** and follow the prompts.
  - Source: UPLOAD 08 Instructions Rev 4. If that fails, call Chauvet service.
- Release notes worth knowing (GitHub README):
  - **V1.250331: added the new 27CH mode.** Older units won't offer it. A new or renumbered mode means the console patch and fixture profile must match. Update the whole rig to the same version before programming.
  - V1.241121: internal only, no changes.
  - **V1.231016**: improved dimming.
  - V1.211122: works on fixtures with both old and new ICs.
  - V1.191202: fixed full output differing between dim modes.

## Road notes (community)
- No specific notes found.

## Sources
- [Rogue R3X Wash User Manual Rev 4](https://www.chauvetprofessional.com/wp-content/uploads/2019/10/Rogue_R3X_Wash_UM_Rev4.pdf) — passcode procedure (top search result for "press and hold … 2323")
- [github.com/Chauvet-Pro/ROGUER3XWASH](https://github.com/Chauvet-Pro/ROGUER3XWASH) — firmware history, BOM (12 A fuse, powerCON, DMX board, Omega revisions, locks), firmware strings (modes, messages) — firmware versions and release notes re-checked 2026-10-03
- [UPLOAD 08 Instructions Rev 4](https://www.chauvetprofessional.com/wp-content/uploads/2015/12/UPLOAD_08_Instructions_Rev4.pdf) — UPLOAD 08 PC setup, COM129, up to 10 same-product fixtures, Force Upload
