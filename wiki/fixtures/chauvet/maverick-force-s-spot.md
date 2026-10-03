---
title: "Chauvet Professional Maverick Force S Spot"
manufacturer: "Chauvet Professional"
model: "Maverick Force S Spot"
aliases: ["force s spot", "force s", "maverick force s", "mav force s", "maverickforcesspot"]
type: "spot"
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
  link_max_120v: 2
  link_max_208v: null
  link_max_230v: 5
  per_20a_120v: null
  per_20a_208v: null
  fuse: null
dmx:
  connectors: null
  protocols: []
  modes: []
menu_password: null
firmware:
  latest_known: "V1.240826"
  checked: "2026-10-03"
  check_on_fixture: "Fixture Information → firmware version"
  methods: ["USB stick", "USB stick + DMX daisy chain (multi-unit)", "DMX cable + UPLOAD 08 (recovery)"]
  interface: null
  software: null
  file_type: ".chl"
  download: "https://github.com/Chauvet-Pro/MAVERICKFORCESSPOT"
tools: []
verification: "unverified"
last_updated: "2026-10-03"
---

# Chauvet Professional Maverick Force S Spot

> **2AM CARD** — the stuff you need first
> - **Power links (manual):** "link up to 2 @100 V, **2 @120 V**, **5 @208 V** (one source summary said **4**), 5 @230 V, 5 @240 V". **Amps per unit not found.** Until you've read the label or the manual, use **4 @208 V** (the lower figure) and 2 @120 V.
> - **Password:** Not found. Chauvet's usual offset code is 2323 (⚠️ unverified for this model).
> - **DMX:** Not found — fill in from the fixture.
> - **Tools:** TBD – check on next show.

> Picked over the Maverick Storm 1 Wash because the Force S Spot came up repeatedly in Chauvet manual searches. This page is thin: the search budget ran out before it could be researched properly. **Treat everything here as a starting point.**

## Identity
- What crews call it: "Force S", "Force S Spot".
- Fixture library / profile names: Chauvet Professional "Maverick Force S Spot".
- Variants and how to tell them apart: The Maverick **Force 1 Spot** is a different, larger fixture with its own manual (Rev 8 exists). Don't use its numbers here. **MK3 Spot**: [page](maverick-mk3-spot.md).

## Passwords, menu locks & hidden menus
- Not found — fill in from the fixture.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found | Not found | Not found |
| Power (W) | Not found | Not found | Not found |
| Max power-link (manufacturer) | 2 | **5 or 4 (sources disagree)** | 5 |
| **Max per 20 A circuit** (16 A continuous) | amps unknown → link limit 2 → **2** ⚠️ | amps unknown → use the lower figure, **4** ⚠️ | amps unknown → link limit 5 ⚠️ |

- Manual wording, as quoted by search: "It is possible to link up to 2 Maverick Force S Spot products at 100 V, 2 products at 120 V, 5 products at 208 V, 5 products at 230 V, or 5 products at 240 V." Two separate searches gave this. A third summary of the same manuals gave "4 products at 208 V". **Check the manual's electrical table** and fill in the amps, then redo the per-circuit math.
- Chauvet's link counts are usually the **total number of fixtures on the circuit** under a 12 A ceiling (see [PXL Bar 16](colorado-pxl-bar-16.md) for the reasoning).
- Input range / connectors / fuse: Not found.

## Data & addressing
- Not found — fill in from the fixture.

## Rigging & hardware
- Not found — fill in from the fixture.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD – check on next show |
| Gobo / effects module access | TBD – check on next show | TBD – check on next show |
| Lens / front glass | TBD – check on next show | TBD – check on next show |
| Omega bracket | TBD – check on next show | TBD – check on next show |

## Optics & consumables
- Not found — fill in from the fixture.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Not found | — | Fill in from the fixture |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| 3+ on one 120 V circuit trip the breaker | Over the link limit (2 @120 V) | 2 per 120 V circuit, or move to 208 V |

## Maintenance
- Not found — fill in from the fixture.

## Firmware
- Installed version — where to see it on the fixture: **Fixture Information**. Per the manual, it shows firmware version, running mode, DMX address, temperature, running time, IP, subnet mask and MAC.
- Latest known version: **V1.240826** (latest found 2026-10-03), a "factory update – for internal use only". The last public fix is **V1.211005**. Both are on [github.com/Chauvet-Pro/MAVERICKFORCESSPOT](https://github.com/Chauvet-Pro/MAVERICKFORCESSPOT); the file is `A40715-FORCESSPOT-V1.240826-20250114-2.CHL`.
- What you need: a FAT32 USB stick (≤32 GB). Keep an UPLOAD 08 for recovery. The port type wasn't captured ⚠️.
- Update steps (USB stick, from the GitHub README and manual):
  1. Copy the .CHL file to the **root** of the stick.
  2. Power on and plug in the stick.
  3. **"USB UPDATE"** appears → **YES**.
  4. Pick the version with **UP / DOWN** → **ENTER**.
  5. **"USB UPDATE"** appears again → **YES**.
  6. **"USB Update Wait"** shows. **Don't cut power or pull the stick while the USB LED blinks.** It may show "DO NOT UNPLUG, UPDATING".
  7. It reboots by itself.
  8. Check Fixture Information, then restart.
- Updating a whole rig: **"It is possible to update multiple units with the USB if they are daisy chained via DMX"** (README and manual). Chain only Force S Spots and disconnect the console (general knowledge). No unit count is given ⚠️.
- Web server: the firmware has a web "Upgrade" page with an Upload File button (strings "POST /upgrade/get", "FILE UPLOAD SUCCESS, PLEASE WAIT FOR FIXTURE TO FINISH THE UPGRADE"). Not confirmed in this model's manual ⚠️ unverified.
- If it fails or bricks mid-update: partial or total firmware failure needs the **UPLOAD 08**. "Please contact Chauvet regarding this device" (manual). Force Upload steps are in `_chauvet-common.md`.
- Release notes worth knowing (GitHub README):
  - V1.240826: factory or internal update.
  - **V1.211005**: fixed the gobo fans.
  - **V1.210811**: new curve to reduce motor noise (good for theatre or quiet rooms).

## Road notes (community)
- None found.

## Sources
- [Maverick Force S Spot User Manual Rev 5 (Chauvet)](https://www.chauvetprofessional.com/wp-content/uploads/2021/03/Maverick-Force-s-Spot_UM_Rev5.pdf) and [parlights mirror](https://parlights.com/wp-content/uploads/2024/04/MAVERICK-FORCE-S-SPOT-MANUAL-2.pdf): power-link limits (2 @100/120 V, 5 @208/230/240 V)
- [Maverick Force S Spot QRG (Full Compass)](https://www.fullcompass.com/common/files/61565-MaverickForceSSpotQuickReferenceGuide.pdf) and [BMI Supply copy](https://shop.bmisupply.com/Resources/en/ItemDocuments/39D1025/BMI.Chauvet.Maverick.Force.S.Spot.QuickReferenceGuide.pdf): the search summary that gave 4 @208 V came from a set that included these
- [notice-facile manual](https://www.notice-facile.com/en/manual/539158/chauvet+maverick-force-s-spot), [manualslib](https://www.manualslib.com/manual/2409706/Chauvet-Professional-Maverick-Force-S-Spot.html): full manual (not read)
- [Force S Spot data sheet (parlights)](https://parlights.com/wp-content/uploads/2024/04/MAVERICK-FORCE-S-SPOT-DATASHEET-2.pdf): not read
- [github.com/Chauvet-Pro/MAVERICKFORCESSPOT](https://github.com/Chauvet-Pro/MAVERICKFORCESSPOT) — firmware versions, release notes, USB update procedure incl. multi-unit DMX chain, .CHL file name (checked 2026-10-03)
- [Maverick Force S Spot User Manual Rev 7](https://www.chauvetprofessional.com/wp-content/uploads/2021/03/Maverick-Force-S-Spot_UM_Rev7.pdf) — USB update, multi-unit via DMX, Fixture Information contents, UPLOAD 08 recovery (via search summary)
- [UPLOAD 08 Instructions Rev 4](https://www.chauvetprofessional.com/wp-content/uploads/2015/12/UPLOAD_08_Instructions_Rev4.pdf) — UPLOAD 08 PC setup, COM129, up to 10 same-product fixtures, Force Upload
