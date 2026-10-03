---
title: "Chauvet Professional Rogue Outcast 3 Spot"
manufacturer: "Chauvet Professional"
model: "Rogue Outcast 3 Spot"
aliases: ["outcast 3", "outcast 3 spot", "rogue outcast 3", "outcast 3 spot-2", "rogueoutcast3spot", "rogueoutcast3spot-2"]
type: "spot"
light_source: "LED 1x 300W cool white, 7044 K"
ip_rating: IP65
weight_lb: 51
weight_kg: 23.2
dimensions: null
power:
  input: "100–240 VAC, 50/60 Hz, auto-ranging"
  connector_in: "Seetronic Powerkon IP65 (SAC3MPX)"
  connector_out: "Seetronic Powerkon IP65 (SAC3FPX)"
  watts_max: 510
  amps_120v: 4.24
  amps_208v: 2.43
  amps_230v: 2.19
  link_max_120v: 3
  link_max_208v: 5
  link_max_230v: 6
  per_20a_120v: 3
  per_20a_208v: 5
  fuse: "F8A (8 A) in FH15-22A holder, per Chauvet BOM"
dmx:
  connectors: "5-pin XLR IP65 in/out"
  protocols: ["DMX", "RDM"]
  modes:
    - { name: "20CH", channels: 20 }
    - { name: "25CH", channels: 25 }
menu_password: "2323"
firmware:
  latest_known: "V1.241025"
  checked: "2026-10-03"
  check_on_fixture: "MENU → Sys Info → Ver"
  methods: ["USB stick (USB-C)", "DMX cable + UPLOAD 08 (recovery)"]
  interface: null
  software: null
  file_type: ".chl"
  download: "https://github.com/Chauvet-Pro/ROGUEOUTCAST3SPOT"
tools: []
verification: "web-search"
last_updated: "2026-10-03"
---

# Chauvet Professional Rogue Outcast 3 Spot

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** **2323**. Hold the menu button on the main screen until the passcode screen appears (the R2X and Outcast manuals name MENU). **UP** raises the digit, **DOWN** goes to the next digit → **ENTER**. This opens Offset (Pan / Tilt / Zoom home trim).
> - **Power:** 4.24 A @120 V / 2.43 A @208 V → **3 per circuit @120 V, 5 @208 V** (Chauvet link limit, counted as the total on one feed; never over 12 A).
> - **DMX:** 20 or 25 ch. Address: MENU → Address → 001–512.
> - **Won't move?** It has **pan AND tilt transport locks** (BOM lists pan lock and tilt lock parts). Release both before power-up.
> - **Tools:** TBD – check on next show. At 51 lb, use two people to hang it.

## Identity
- What crews call it: "Outcast 3", "O3 spot".
- Model IDs: ROGUEOUTCAST3SPOT. A newer SKU is **ROGUEOUTCAST3SPOT-2 ("Outcast 3 Spot-2")**. Retailers show the same core specs; what changed was not documented ⚠️.
- Not the same as the **Outcast 3X Wash** or the indoor **Rogue R3 Spot**.

## Passwords, menu locks & hidden menus
- **2323** → Offset mode. From the main level, press and hold (MENU) until the passcode screen appears, enter with UP (raise value) and DOWN (next digit), then ENTER. Offset adjusts the home position of pan, tilt and zoom.
- The firmware contains the strings "Password" and "Zero Adjust".
- Firmware V1.241025 added a standalone menu.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | 4.24 | 2.43 | 2.19 |
| Power (W) | 506 (510 @100 V) | 493 | 494 |
| Max power-link (manufacturer) | 3 (12 A max) | 5 (12 A max) | 6 (12 A max; also 6 @240 V, 2 @100 V) |
| **Max per 20 A circuit** (16 A continuous) | link limit **3** total (12.7 A) → **3** | link limit **5** total (12.2 A) → **5** | link limit **6** total (13.1 A) → **6** |

Chauvet link limits are read as the **total** on one feed. Every Chauvet limit works out to about 12 A total, which matches the manual's 12 A cap; see [power math](../../reference/power-math.md).

- The manual says "3 units @120 V… never exceed 12 A on a single circuit when power linking". 3 × 4.24 A = 12.7 A and 5 × 2.43 A = 12.2 A, both right at the 12 A cap, so this wiki reads the limit as **3 total @120 V, 5 total @208 V**.
- Connectors: Seetronic Powerkon IP65 in and out. The US kit ships an Edison to Powerkon cable.
- Fuse: F8A in an FH15-22A holder with an IP fuse cap (BOM).

## Data & addressing
- Connectors: 5-pin XLR IP65 (J5F2C / K5F2C).
- Modes: 20CH and 25CH, confirmed by the firmware strings too.
- Address: MENU → Address → 001–512 → ENTER.
- Pan/Tilt ranges: 540° / 270°, with selectable ranges 180/360/540 pan and 90/180/270 tilt.

## Rigging & hardware
- 2 Omega brackets are included. Clamp spacing: Not found.
- **Transport locks:** pan lock and tilt lock (BOM: "pan lock block", "pan lock pick", "tilt lock block", "tilt lock pick"). Exact location: TBD – check on next show.
- IP65 with a pressure-equalising M12 GORE valve.
- Weight: 51 lb (23.2 kg). Dimensions: Not found.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | Head cover with gasket (BOM). Screw not listed | TBD – check on next show |
| Gobo / effects module access | Head cover off (sealed IP head) | TBD – check on next show |
| Lens / front glass | Not found | TBD – check on next show |
| Omega bracket | Quarter-turn | TBD – check on next show |

The BOM also lists "screw M5×6" and "screw 304 CM6×12" but doesn't say where they go.

## Optics & consumables
- Source: 300 W cool-white LED, 7044 K, rated 50,000 h. 20,000 lm at the source, 14,989 lm output.
- Zoom: 4.9°–38.7°.
- Color: two color wheels, each with 7 splittable colors + white.
- Gobos: two wheels, one rotating and one static (BOM). Sources disagree on the counts:
  - One retailer: "Gobo 1: 7 metal, interchangeable; Gobo 2: 8 metal, fixed".
  - Another: "7 metal fixed scrolling and 8 metal rotating".
  - The manual says the gobos in **gobo wheel 1** come out of their holders.
- Gobo sizes (retailer spec): wheel 1 OD 25.5 mm, max image 14.8 mm, max thickness 0.6 mm; wheel 2 OD 24 mm, max image 16 mm, max thickness 0.6 mm ⚠️ (one source, check before ordering custom gobos).
- Iris, prism, frost.
- Gobo change: disconnect power first. Glass gobos go shiny (glass base) side toward the LED.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Thermistor Hot / Thermistor Open / Short | Firmware strings. Probably over-temperature or a sensor fault ⚠️ | Check fans, then service |
| Light Block | Firmware string only. Meaning unknown ⚠️ | Not found — fill in from the fixture |
| USB Error / File Not Found / USB Disconnected | USB update messages | FAT32 drive, .chl file in root |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Fixture grinds or errors on power-up | Pan/tilt locks engaged | Release both locks and reset |
| RDM discovery problems | Early firmware | V1.221014 fixed RDM issues. Update |

## Maintenance
- Cleaning intervals: Not found.

## Firmware
- Installed version — where to see it on the fixture: **MENU → Sys Info → Ver** (GitHub README; the firmware has "Sys Info" / "System Information" screens).
- Latest known version: **V1.241025** (latest found 2026-10-03). Download from [github.com/Chauvet-Pro/ROGUEOUTCAST3SPOT](https://github.com/Chauvet-Pro/ROGUEOUTCAST3SPOT) as `V1.241025.zip`, which holds `A4079D-Rogue Outcast 3 Spot-V1.241025-1025-2.CHL`.
- What you need: a FAT32 USB stick (≤32 GB) with a USB-C plug or an adapter. Keep an **UPLOAD 08** for recovery.
- Update steps (USB stick, from Chauvet's GitHub README for this model):
  1. Unzip the download. Copy only the **.CHL** file to the **root** of a **FAT32** stick, **32 GB or smaller**.
  2. Power on the fixture and plug the stick into the **USB-C** port. You need a USB-C stick or a USB-A→C adapter. Chauvet's own Firmware USB stick has both plugs.
  3. **"USB Update"** appears → **YES**.
  4. If the stick holds several versions, pick one with **UP / DOWN** → **ENTER**.
  5. **"USB Update"** appears again → **YES**.
  6. **"USB Update Wait"** shows. It can take several minutes. **Don't cut power or pull the stick while the USB LED blinks.**
  7. When the LED stops, the motors power down and the display goes blank. **Still don't cut power.** The fixture reboots by itself.
  8. Check **Sys Info** for the new version, then restart the fixture.
- Updating a whole rig: one fixture at a time with the stick. For batches, the UPLOAD 08 does up to 10 of the same model over DMX (see `_chauvet-common.md`). USB-over-DMX linking is not described for this model ⚠️ unverified.
- If it fails or bricks mid-update: pulling power or the stick while the USB LED blinks causes "partial or total firmware failure". Chauvet's fix is the **UPLOAD 08** (GitHub README). In the UPLOAD 08 app, use **Force Upload**:
  1. Power the fixture off, but leave it connected to the UPLOAD 08.
  2. Make sure the LED on the UPLOAD 08 is flashing.
  3. Select the .CHL file.
  4. Click **Force Upload** and follow the prompts.
  - Source: UPLOAD 08 Instructions Rev 4. Full setup is in `_chauvet-common.md`.
- Release notes worth knowing (GitHub README):
  - **V1.241025**: added a standalone menu.
  - V1.221227: listed as the "initial software version".
  - **V1.221014**: fixed RDM issues. Update if RDM discovery misbehaves.
  - No mode changes are listed in the notes.

## Road notes (community)
- No specific forum notes found.

## Sources
- [Rogue Outcast 3 Spot UM Rev 3](https://www.chauvetprofessional.com/wp-content/uploads/2025/08/Rogue_Outcast_3_Spot_UM_Rev3.pdf), [Rev 1 (Hibino mirror)](https://www.hibinolighting.co.jp/hibino_wp/wp-content/uploads/2023/01/Rogue_Outcast_3_Spot_UM_Rev1.pdf) — current draw, link limits, passcode/offset, gobo replacement, Omega brackets
- [Chauvet product page](https://chauvetprofessional.com/product/rogue-outcast-3-spot/), [idjnow](https://www.idjnow.com/chauvet-professional-rogue-outcast-3-spot-moving-head.html), [GoKnight](https://goknight.com/chauvet-pro-rogue-outcast-3-spot-outdoor-ready-ip65-moving-head/) — LED, lumens, zoom, modes, wattage per voltage, connectors, GORE valve, gobo sizes, weight
- [Sweetwater Outcast 3 Spot-2](https://www.sweetwater.com/store/detail/RogueO3Spt2--chauvet-pro-rogue-outcast-3-spot-2-moving-head) — Spot-2 SKU
- [github.com/Chauvet-Pro/ROGUEOUTCAST3SPOT](https://github.com/Chauvet-Pro/ROGUEOUTCAST3SPOT) — firmware history, BOM (pan/tilt lock parts, fuse, connectors, wheels), firmware strings
- [github.com/Chauvet-Pro/ROGUEOUTCAST3SPOT](https://github.com/Chauvet-Pro/ROGUEOUTCAST3SPOT) — firmware versions, release notes, USB update procedure, .CHL file name (checked 2026-10-03)
- [UPLOAD 08 Instructions Rev 4](https://www.chauvetprofessional.com/wp-content/uploads/2015/12/UPLOAD_08_Instructions_Rev4.pdf) — UPLOAD 08 PC setup, COM129, up to 10 same-product fixtures, Force Upload
