---
title: "Chauvet Professional Strike Array 4"
manufacturer: "Chauvet Professional"
model: "Strike Array 4"
aliases: ["strike array 4", "strike 4", "strike array", "4-lite led blinder", "strikearray4"]
type: "blinder"
light_source: null
ip_rating: null
weight_lb: null
weight_kg: null
dimensions: ""
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
  latest_known: "V1.3.0"
  checked: "2026-10-03"
  check_on_fixture: "Fixture Information"
  methods: ["USB stick (USB-C)", "USB stick + DMX to other fixtures (Multiple Fixture)"]
  interface: null
  software: null
  file_type: ".chl"
  download: "https://github.com/Chauvet-Pro/STRIKEARRAY4"
tools: []
verification: "unverified"
last_updated: "2026-10-03"
---

# Chauvet Professional Strike Array 4

> **2AM CARD** — the stuff you need first
> - **⚠️ STUB PAGE. Nothing here is verified.** The research session ran out of web-search budget before reaching this fixture. **Don't plan power from this page.** Read the amps off the fixture label or the manual's electrical table and fill them in.
> - **Password / menu lock:** Not found. Chauvet's usual offset/zero-adjust code is 2323 (⚠️ unverified for this model).
> - **Power:** Not found → per-circuit count unknown.
> - **DMX:** Not found.
> - **Tools:** TBD – check on next show.

## Identity
- What crews call it: "Strike Array 4", "Strike 4", "LED 4-lite" (general knowledge).
- Fixture library / profile names (MA3, GDTF, Hog, Eos): Chauvet Professional "Strike Array 4". Check the console library.
- Variants and how to tell them apart: Part of Chauvet's STRIKE blinder family. The **Strike 4** and the **Strike Array 4** may be different products, so check the label (⚠️ unverified). Arrays of 1/2/4 cells exist in the family (general knowledge, ⚠️ unverified).

## Passwords, menu locks & hidden menus
- Not found — fill in from the fixture.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found | Not found | Not found |
| Power (W) | Not found | Not found | Not found |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | Not found: floor(16 / amps) once known | Not found | Not found |

- Input range / auto-ranging: Not found. **Check the label before you plug into 208 V.**
- Connectors in / out: Not found.
- Fuse: Not found.
- Inrush / power-up notes: Not found. LED blinders replacing tungsten 4-lites are usually auto-ranging, but **old tungsten 4-lites wired for 120 V must never go on 208 V**. Confirm this is the LED unit and read the label (see power-math).

## Data & addressing
- Not found — fill in from the fixture.

## Rigging & hardware
- Not found — fill in from the fixture.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD – check on next show |
| Gobo / effects module access | n/a | n/a |
| Lens / front glass | TBD – check on next show | TBD – check on next show |
| Omega bracket | TBD – check on next show | TBD – check on next show |

## Optics & consumables
- Not found. As general knowledge (⚠️ unverified): an LED blinder with 4 individually controllable warm-white cells.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Not found | — | Fill in from the fixture |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Not found | — | Fill in from the fixture |

## Maintenance
- Not found — fill in from the fixture.

## Firmware
- Installed version — where to see it on the fixture: **Fixture Information** (GitHub README).
- Latest known version: **V1.3.0** (latest found 2026-10-03). Download from [github.com/Chauvet-Pro/STRIKEARRAY4](https://github.com/Chauvet-Pro/STRIKEARRAY4); the file is `Strike Array 4-V1.3.0.chl`. The **STRIKE Array 4C** is a different product with its own repo, STRIKEARRAY4C (latest tag found: V1.0.5). Don't cross-load.
- What you need: a FAT32 USB stick (≤32 GB) with USB-C or an adapter. For batch updates or recovery, a **5-pin** DMX cable to another fixture. No PC or UPLOAD 08 is needed.
- Update steps (GitHub README):
  1. Put the .chl file in the **root** of the stick.
  2. Power on and plug into the USB-C port.
  3. **"Upgrade Firmware"** appears → **ENTER**. If something else shows: main menu → **Update Firmware** → **Only This Fixture** / **Multiple Fixture** / **Other Fixture Type**.
  4. Select the file. **"Are you sure?"** → **ENTER**. A wrong file fails and returns to the main screen. Repeat with the right one.
  5. Don't power off or pull the stick (several minutes). It reboots itself.
  6. Check **Fixture Information**, then restart.
- Updating a whole rig: **Multiple Fixture** updates DMX-linked units of the same product line. **Other Fixture Type** updates a different Chauvet product. V1.210701 fixed using this unit to update a Silens fixture. Set the protocol to **DMX512** and unplug the console (general knowledge). No unit count is given ⚠️.
- If it fails or bricks mid-update: Chauvet says a **Force Upload** is needed (GitHub README).
  1. Run a 5-pin DMX cable from a working main fixture to the dead target, with the **target off**.
  2. Main fixture: protocol DMX512. Stick in → **Upgrade Firmware** → **Multiple Fixture** (or Other Fixture Type).
  3. Select the file → "Are you sure?" → ENTER. **Power the target on within 1–2 s.** Its display stays off while the main shows 0–100 %.
  4. The target shows "< UPDATE >" and then reboots. Check its version, then reboot it.
  - **One target at a time.**
- Release notes worth knowing (GitHub README):
  - **V1.3.0**: updated RDM PIDs.
  - **V1.230817: added a new mode with independent Amber control.** A new or renumbered mode means the console patch and fixture profile must match. Update the whole rig to the same version before programming.
  - V1.230206 (labeled "STRIKE Array 2" in the README): improved strobe dimming.
  - V1.220503 (the file is named V1.220523): fixed an OLED display issue.
  - V1.210701: fixed updating Silens fixtures from this unit.

## Road notes (community)
- None collected yet.

## Sources
- Only the Firmware section has been researched (sources below). For power and specs, start with the manual on chauvetprofessional.com (product page → Downloads → User Manual) and the electrical table in it.
- [github.com/Chauvet-Pro/STRIKEARRAY4](https://github.com/Chauvet-Pro/STRIKEARRAY4) — firmware versions, release notes, USB update and Force Upload procedures, .chl file name (checked 2026-10-03)
- [github.com/Chauvet-Pro/STRIKEARRAY4C](https://github.com/Chauvet-Pro/STRIKEARRAY4C) — firmware versions, release notes (tags only, 4C variant) (checked 2026-10-03)
