---
title: "Claypaky Sharpy"
manufacturer: "Claypaky"
model: "Sharpy"
aliases: ["sharpy", "clay paky sharpy", "claypaky sharpy", "c61375", "original sharpy", "sharpy 189"]
type: "beam"
light_source: "Discharge 189W short-arc (manual: Osram Sirius HRI 190W+; Christie Lites lists Philips 5R)"
ip_rating: null
weight_lb: 41.8
weight_kg: 19
dimensions: "H 475 mm (18.70 in) x W 330 mm (12.99 in) x D 280 mm (11.02 in) (datasheet)"
power:
  input: "Manual/datasheet: power supplies 100-120 V 50/60 Hz and 200-240 V 50/60 Hz (datasheet header: 115/230 V). Auto-switching not confirmed."
  connector_in: "Christie Lites lists Neutrik TRUE1 (may be rental retrofit; unverified for factory units)"
  connector_out: null
  watts_max: 350
  amps_120v: 2.59
  amps_208v: 1.44
  amps_230v: null
  link_max_120v: null
  link_max_208v: null
  link_max_230v: null
  per_20a_120v: 6
  per_20a_208v: 11
  fuse: ""
dmx:
  connectors: "XLR 3-pin and XLR 5-pin in/thru (Christie Lites spec)"
  protocols: ["DMX"]
  modes:
    - { name: "Standard", channels: 16 }
    - { name: "Vector", channels: 20 }
menu_password: "1234"
tools: []
verification: "web-search"
last_updated: "2026-10-03"
---

# Claypaky Sharpy

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** Advanced menu access code **1234** (entered with UP / DOWN / RIGHT, confirm with F). If someone set a "Menu Locking" password, the default unlock code is also **1234** (from the manual).
> - **Power:** 2.59 A @120 V / 1.44 A @208 V (Christie Lites rental spec; the manual only gives 350 VA @230 V) → **6 per 20 A circuit @120 V, 11 @208 V** (no manufacturer link limit found). ⚠️ Check the rating label: the manual lists separate 100-120 V and 200-240 V power supplies, and I could not confirm that it auto-switches.
> - **DMX:** Standard 16 ch / Vector 20 ch. Press **F** to show the address, set it with UP / DOWN / RIGHT, then press F to confirm. The display runs on its buffer battery with **mains unplugged**: press F to wake it.
> - **Lamp won't strike from the desk?** Menu option **Lamp DMX** has to be On (it's On by default). Ch 16 Lamp Control: **101-255 = ON, 26-100 = OFF; hold for about 5 s**.
> - **Won't move?** Pan/tilt transport locks are on the fixture (exact location not sourced). Release them before you power up.
> - **Tools:** TBD – check on next show

## Identity
- What crews call it: "Sharpy", "original Sharpy", "189 Sharpy" (to tell it apart from the Sharpy Plus / Sharpy X Frame / Ultimo Sharpy).
- Fixture library / profile names: Standard (16 ch) and Vector (20 ch). On consoles there are separate "Sharpy" and "Sharpy LC / Lamp On" style profiles. ETC forum advice is to patch the LC (lamp control) version to get lamp on/off (community).
- Variants and how to tell them apart: Sharpy Wash 330 is a different fixture with a different lamp (550 W max, per PLSN). The Sharpy Plus is bigger (23 kg), has CMY and a 3-36° zoom, and puts "SHARPY PLUS" on the head. The Sharpy X Frame has framing shutters. Code C61375 = Sharpy (manual title).

## Passwords, menu locks & hidden menus
- **Advanced menu:** enter the Access code **1234** with UP, DOWN and RIGHT, then press F and "Menu advanced" appears on the display (manual). The Advanced menu contains Access code, Upload Firmware, Setup Model, Calibration, Factory Default and Menu Locking.
- **Menu Locking:** puts a 4-digit password on the user menu. The default unlock code is **1234** (manual). If a rental house changed it, the code isn't recoverable from here.
- Service / factory menu: Factory Default lives in the Advanced menu.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | 2.59 (Christie Lites) | 1.44 (Christie Lites) | Not given as amps. Manual: 350 VA → ≈1.52 A derived, not manufacturer |
| Power (W) | 301 W (Christie Lites) | — | 350 VA (manual/datasheet) |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | floor(16/2.59)=6 → **6** | floor(16/1.44)=11 → **11** | — |

- Input range / auto-ranging: the datasheet and manual list power supplies for 100-120 V 50/60 Hz and 200-240 V 50/60 Hz. ⚠️ unverified whether a given unit auto-switches. Read the rating plate before patching to 208 V.
- Connectors in / out: Christie Lites lists TRUE1 and can supply TRUE1-to-Edison, L5-20, L6-15, L6-20 or powerCON adapters. Whether there's a factory power-thru: Not found — fill in from the fixture.
- Fuse (type, rating, location): Not found — fill in from the fixture.
- Inrush / power-up notes: discharge lamp. Fast lamp ON-OFF cycles shorten lamp life (manual).

## Data & addressing
- Connectors: XLR3 and XLR5 in/thru (Christie Lites).
- Protocols: DMX512.
- DMX modes / footprints (manual):
  - **Standard 16 ch**: colour wheel, stop/strobe, dimmer, gobo, prism, effects (prism rotation), frost, focus, pan, pan fine, tilt, tilt fine, function, reset, lamp control (ch 16, only when Lamp DMX is On).
  - **Vector 20 ch**: Standard plus ch 17-20: pan/tilt time, colour time, beam time, gobo time.
  - Christie Lites' default profile is Standard 16.
- Control channel values (QLC+ community profile, consistent with the manual's lamp values):
  - Reset: 26-76 effects reset, 77-127 pan/tilt reset, 128-255 complete reset.
  - Lamp: 26-100 OFF, 101-255 ON (manual: hold about 5 s).
  - Function: 12-24 pan/tilt fast (default), 25-37 pan/tilt normal, 38-50 conventional dimmer curve, 51-62 linear (default).
- Set the address: press **F** and the current DMX address appears. Set it with UP (B), DOWN (C) and RIGHT (E), then press F to confirm. Without confirmation the display switches off after 30 s (manual).
- Battery / unpowered addressing: **yes**. The display has a long-life self-charging buffer battery. Press F to wake it with the fixture unplugged (manual).
- Without a DMX signal the address field **flashes**. That's normal, not a fault (manual).
- Factory reset: Advanced menu (code 1234) → Factory Default.
- Wireless / Ethernet setup notes: the Information menu has a "Network Parameters" entry (manual). Whether this model has an Ethernet port: Not found.

## Rigging & hardware
- Bracket / omega type and clamp spacing: Not found — fill in from the fixture.
- Fasteners: Not found.
- Safety cable point: Not found — fill in from the fixture.
- Mounting orientations allowed: "capable of functioning in any position" (manual).
- Transport / pan-tilt locks: the manual says there is a device that locks the PAN and TILT mechanisms for transport and maintenance. Exact location: TBD – check on next show. Two side handles.
- Weight / dimensions: 19 kg / 41.8 lb. H 475 x W 330 x D 280 mm (datasheet).
- Pan 540°, tilt 252°. Max speed: pan 2.45 s, tilt 1.30 s (manual).

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD – check on next show |
| Gobo / effects module access | TBD – check on next show | TBD – check on next show |
| Lens / front glass | TBD – check on next show | TBD – check on next show |
| Omega bracket | TBD – check on next show | TBD – check on next show |

## Optics & consumables
- Source / lamp: the manual says Osram Sirius HRI 190W+ (8200 K, 8100 lm). Christie Lites says "189W Arc, Philips 5R, 7,950 lumens". Both are 189-190 W short-arc 5R-class lamps, so confirm against what's in the fixture. Lamp life: 3000 h average per a lamp vendor listing ⚠️ unverified.
- Color system: one interchangeable colour wheel, 14 colours + open.
- Gobo wheels: interchangeable wheel with 17 fixed gobos + open. No rotating gobos. Gobo size: Not found — fill in from the fixture.
- Prism / frost / zoom / iris / shutters: 8-facet rotating prism, soft frost, focus. Beam 0-3.8°. Mechanical dimmer and strobe (Christie Lites).
- Gobo / module change procedure: Not found.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Address flashing on display | No DMX signal present | Check the data cable, terminator and console output (manual) |
| System Errors list (Information menu) | Warnings and messages logged since power-on | Read the list, fix, then reset the list from the same menu (manual) |
| Shutter closes by itself after the head is bumped | "Shutter on error" option: stop/strobe closes automatically on a pan/tilt position error, and pan/tilt reposition themselves after uncommanded movement | Normal protection. Let it re-home or send a pan/tilt reset (manual) |
| Specific error code strings | Not found — fill in from the fixture | |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Won't switch on | No mains | Check supply voltage (manual) |
| Electronics work, no light | Lamp exhausted or defective | Replace lamp (manual) |
| Lamp won't strike from desk | Lamp DMX option Off, or the profile has no lamp control | Turn Lamp DMX On, patch an LC / lamp-control profile, hold ch 16 at 101-255 for about 5 s (manual + ETC forum) |
| Still won't strike, lamp is good | Ignitor/ballast, or a failed thermal sensor near the lamp housing | Swap ignitor and ballast with known-good ones. Wiggle and test sensor wiring for continuity. Meter at the ballast output on the ignitor (ControlBooth/ETC community) |
| Fixture doesn't follow desk / defective projection | Faulty or disconnected data cable | Replace cables (manual) |
| Reduced output | Incorrect addressing / dirty optics / broken lens | Check address. Clean the optics or call a technician (manual) |
| Fan error | Fan failure | See the Fans Monitor in the Information menu. YouTube repair video "Fan Errors on Clay Paky Sharpy" exists (title only) |

## Maintenance
- Recalibrate / reset procedure: Advanced → Calibration. Reset from the desk with ch 15 Reset (128-255 = complete).
- Information menu (manual): System Errors, Fixture Hours (total and partial), Lamp Hours (total and partial), Lamp Strikes, System Version, Board Diagnostic, DMX Monitor, Fans Monitor, Sensor Status, Network Parameters.
- Test menu: Pan-Tilt, Colour, Beam, Gobo tests. Manual Control menu: drive each effect by hand (manual).
- Fan / filter cleaning: Not found.
- Firmware update method: Advanced → Upload Firmware (manual). The tool and connector aren't confirmed. See [_claypaky-common.md](_claypaky-common.md).

## Road notes (community)
- ETC Community "Clay Paky Sharpy strike issue": patch the Sharpy LC profile to get lamp control, **and** set "DMX Lamp" On at the fixture. On MA, use "Clay Paky Sharpy Vector Lamp On" (ETC / MA Lighting forums).
- ControlBooth (Stage Color thread, same Claypaky lamp-start logic): standard procedure is to swap the ignitor and ballast with known-working ones. Thermal sensors near the lamp housing fail, sometimes the wiring and sometimes the sensor. An open sensor at normal temperature is your fault.
- Quora/rental chatter about how many fit on a 20 A circuit: use the 2.59 A figure above, not watts divided by volts.

## Sources
- [Sharpy C61375 Instruction Manual (4wall mirror)](https://cdn01.4wall.com/cms/rentals/files/f60ef02cea55e4.pdf) — access code 1234, Advanced menu contents, channel functions, lamp DMX, address procedure (via search summary)
- [Sharpy manual (Christie Lites mirror)](https://www.christielites.com/file_uploads/manual_643_Sharpy_Manual.pdf) — battery display / address without mains, Information menu
- [Sharpy manual (richardmartinlighting mirror)](https://richardmartinlighting.co.uk/wp-content/uploads/Sharpy-Manual.pdf) and [prolight.com.pl mirror Rev.0 06.11](https://prolight.com.pl/images/content/Image/instrukcje/Sharpy_Manual_Rev.0_(06.11)_EN.pdf) — modes, troubleshooting table
- [ManualsLib Sharpy p.20 Information Menu](https://www.manualslib.com/manual/963250/Clay-Paky-Sharpy.html?page=20), [p.31 cause/solution](https://www.manualslib.com/manual/963250/Clay-Paky-Sharpy.html?page=31), [p.32 channel functions](https://www.manualslib.com/manual/963250/Clay-Paky-Sharpy.html?page=32)
- [Sharpy Datasheet (Christie Lites)](https://www.christielites.com/file_uploads/spec_643_Sharpy%20Datasheet.pdf) — 350 VA @230 V, supply options, weight, dimensions
- [Christie Lites Sharpy rental page](https://www.christielites.com/clay-paky-sharpy/228w2w10w167w318) — 2.59 A @120 V (301 W), 1.44 A @208 V, lamp, connectors, default profile
- [Claypaky Sharpy legacy product page](https://www.claypaky.it/products/sharpy-legacy/) — lamp type, pan/tilt range, colours/gobos
- [ETC Community: Sharpy strike issue](https://community.etcconnect.com/control_consoles/eos-family-consoles/f/eos-family/9608/clay-paky-sharpy-strike-issue), [MA forum: Lamp On Sharpy](https://forum.malighting.com/forum/thread/48267-lamp-on-sharpy/), [ControlBooth: Stage Color lamp won't strike](https://www.controlbooth.com/threads/clay-paky-stage-color-lamp-wont-strike.12789/) — road notes
- QLC+ fixture definition Clay-Paky-Sharpy.qxf (github.com/mcallegari/qlcplus, commit 1ccdab8) — reset/function/lamp DMX value ranges (community)
