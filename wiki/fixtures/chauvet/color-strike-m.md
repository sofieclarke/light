---
title: "Chauvet Professional Color STRIKE M"
manufacturer: "Chauvet Professional"
model: "Color STRIKE M"
aliases: ["color strike m", "colour strike m", "strike m", "colorstrikem"]
type: "strobe"
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
  latest_known: "V4.0.7"
  checked: "2026-10-03"
  check_on_fixture: "Fixture Information → Display Ver (also Drv-Y, LED-A, LED-C and Net Ver)"
  methods: ["USB stick", "USB stick + DMX to other fixtures (Multiple Fixture)", "Web server ⚠️"]
  interface: null
  software: null
  file_type: ".chl"
  download: "https://github.com/Chauvet-Pro/COLORSTRIKEMV2"
tools: []
verification: "unverified"
last_updated: "2026-10-03"
---

# Chauvet Professional Color STRIKE M

> **2AM CARD** — the stuff you need first
> - **⚠️ STUB PAGE. Nothing here is verified.** The research session ran out of web-search budget before reaching this fixture. **Don't plan power from this page.** Read the amps off the fixture label or the manual's electrical table and fill them in.
> - **Password / menu lock:** Not found. Chauvet's usual offset/zero-adjust code is 2323 (⚠️ unverified for this model).
> - **Power:** Not found → per-circuit count unknown.
> - **DMX:** Not found.
> - **Tools:** TBD – check on next show.

## Identity
- What crews call it: "Color Strike M", "Strike M" (general knowledge).
- Fixture library / profile names (MA3, GDTF, Hog, Eos): Chauvet Professional "Color STRIKE M". Check the console library.
- Variants and how to tell them apart: Part of Chauvet's STRIKE strobe/blinder family. As general knowledge (⚠️ unverified), the "M" is the motorized-tilt version of the Color STRIKE strobe-wash. Don't confuse it with the non-motorized Color STRIKE or the white-only STRIKE blinders.

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
- Inrush / power-up notes: Not found. Strobes at full output pull peak current in bursts, so size circuits on the manual's maximum figure (general knowledge).

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
- Not found. As general knowledge (⚠️ unverified): an LED strobe/wash with separate color and white zones and motorized tilt.

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
- Installed version — where to see it on the fixture: **Fixture Information** (manual).
  - **Display Ver** = the main software version.
  - Drv-Y Ver = tilt PCB. LED-A Ver and LED-C Ver = LED boards.
  - **Net Ver** = network board. After V4.0.7, Net Ver reads **2.6 or 4.3** depending on the chip fitted (2.6 = earlier production). Both are correct.
- Latest known version: **V4.0.7** (latest found 2026-10-03). Download from [github.com/Chauvet-Pro/COLORSTRIKEMV2](https://github.com/Chauvet-Pro/COLORSTRIKEMV2) (github.com/Chauvet-Pro/COLORSTRIKEM points to the same repo). The file is `Color Strike M_V4.0.7.chl`.
- What you need: a FAT32 USB stick (≤32 GB per the STRIKE family README ⚠️) and a 5-pin DMX cable to update other units from this one. No PC needed.
- Update steps (USB, from the manual via search summary):
  1. Copy the .chl to the stick. **The manual says to put it in a folder named `STRIKE`.** The STRIKE Array 4 GitHub README says the root folder ⚠️. If the fixture doesn't list the file, try the other location.
  2. Power on and plug in the stick.
  3. **"Upgrade Firmware"** appears → **ENTER**. If something else shows, go to the main-menu firmware update item and choose **Only This Unit**, **Multiple Fixture** or **Other Fixture Type**.
  4. Select the file. **"Are you sure?"** appears → **ENTER**. A wrong file fails and returns to the main screen.
  5. Don't power off or pull the stick. It reboots when done.
  6. Check **Fixture Information**.
- Updating a whole rig: **Multiple Fixture** sends the update from this unit over DMX to linked units of the same product line. **Other Fixture Type** updates a different Chauvet product, e.g. a Maverick Silens 2 Profile updating a Color STRIKE M. Set the main fixture's protocol to **DMX512** and disconnect the console (general knowledge). Unit limit not found ⚠️. The firmware also has "Dmx Update" and "Webserver Update" strings, so a web update probably exists ⚠️ unverified.
- If it fails or bricks mid-update (**Force Upload** from another fixture, per the STRIKE Array 4 README and the Color STRIKE M manual):
  1. Run a 5-pin DMX cable from a working "main" fixture to the dead "target". Leave the target **off**.
  2. On the main fixture: protocol **DMX512**. Plug the stick in → **Upgrade Firmware** → **Multiple Fixture** (or **Other Fixture Type** if the main is a different product).
  3. Select the file → **"Are you sure?"** → ENTER. **Turn on the target within 1–2 s.** Its display stays off while the main shows 0–100 %.
  4. The target shows "< UPDATE >" and then reboots. Check its version.
  - **One target at a time.**
- Release notes worth knowing (GitHub README):
  - **V4.0.7: added the 96CH mode.** When plate priority is set to pixels (ch 25 at 129–255), the color masters (ch 10–12) are now ignored completely. Strobe always works, even on pixel priority. **Pixel-priority looks programmed on older firmware will look different.**
  - **V4.0.6**: sACN universe limit raised from 256 to 32000. Fixed malformed Art-Net packets.
  - V4.0.5: fixed Beam FX in 30CH mode.
  - V4.0.3: fixed IGMP subscription.
  - **V4.0.0** (Jan 2024): **new 68CH personality** for easier cloning; "Enable Bump Flash" menu item; manual self-test; better Beam FX Lightning/Spikes; truly random strobe; Beam FX on the plate; better dimming and crossfades; better power management and network sync. A new DMX chart and manual came with it. A new or renumbered mode means the console patch and fixture profile must match. Update the whole rig to the same version before programming.

## Road notes (community)
- None collected yet.

## Sources
- Only the Firmware section has been researched (sources below). For power and specs, start with the manual on chauvetprofessional.com (product page → Downloads → User Manual) and the electrical table in it.
- [github.com/Chauvet-Pro/COLORSTRIKEMV2](https://github.com/Chauvet-Pro/COLORSTRIKEMV2) — firmware versions, release notes (also reachable as COLORSTRIKEM), .chl file name; firmware strings (checked 2026-10-03)
- [Color STRIKE M User Manual Rev 12](https://www.chauvetprofessional.com/wp-content/uploads/2021/09/Color_STRIKE_M_UM_Rev12.pdf) and [Rev 13 (impact-even mirror)](https://impact-even.com/userfiles/files/telechargement/eclairage/chauvet_colorstrikem_manuel.pdf) — USB update steps, STRIKE folder, Only This Unit / Multiple Fixture / Other Fixture Type, Fixture Information fields (via search summary)
- [GitHub STRIKEARRAY4 README](https://github.com/Chauvet-Pro/STRIKEARRAY4) — Force Upload procedure shared by the STRIKE family
