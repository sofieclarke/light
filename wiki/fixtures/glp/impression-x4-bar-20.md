---
title: "GLP impression X4 Bar 20"
manufacturer: "GLP (German Light Products)"
model: "impression X4 Bar 20"
aliases: ["x4 bar 20", "x4 bar", "x4bar20", "impression x4 bar", "glp x4 bar", "x4 bar 10", "impr x4 bar 20"]
type: "pixel-bar"
light_source: "LED 20x 15W RGBW"
ip_rating: null
weight_lb: 32
weight_kg: 14.5
dimensions: "1000 x 100 x 240 mm (39.4 x 3.9 x 9.4 in), L x W x H per manual summary"
power:
  input: "100–240 VAC, 50–60 Hz, auto-sensing"
  connector_in: "Neutrik powerCON (exact type not confirmed)"
  connector_out: "Neutrik powerCON thru (exact type not confirmed)"
  watts_max: 550
  amps_120v: 4.6
  amps_208v: null
  amps_230v: null
  link_max_120v: null
  link_max_208v: null
  link_max_230v: null
  per_20a_120v: 3
  per_20a_208v: null
  fuse: "Micro-fuse 5x20 mm, T5A"
dmx:
  connectors: "5-pin XLR in/thru"
  protocols: ["DMX"]
  modes:
    - { name: "Compressed (comp)", channels: 20 }
    - { name: "Normal (norm)", channels: 34 }
    - { name: "High Resolution (hires)", channels: 35 }
    - { name: "Dual Pixel (dpix)", channels: 48 }
    - { name: "Dual Pixel High Res (dpixh)", channels: 49 }
    - { name: "Single Pixel (spix)", channels: 88 }
menu_password: null
tools: []
verification: "web-search"
last_updated: "2026-10-03"
---

# GLP impression X4 Bar 20

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** No passcode found. Keys locked? Press **Mode + Enter + Up at the same time** to lock/unlock the menu keys (manual).
> - **Power:** 4.6 A @120 V (rental-house spec, 550 W max) / 208 V not published → **3 per 20 A circuit @120 V** (floor(16/4.6)=3). Manual: never put more than **20 A total** on a powerCON thru chain (connector limit). No manufacturer link count found.
> - **DMX:** 6 modes found (manual says 7): comp 20 · **norm 34** · hires 35 · dpix 48 · dpixh 49 · spix 88. Address: **Mode → DMX Address (Level 1) → Up/Down → Enter**. Default address 001.
> - **Won't move?** **Tilt lock on the yoke.** Release it before power-up. Also check Special → Tilt current / Tilt reset aren't set to Off.
> - **Tools:** Omega brackets go on with quarter-turn camlocks (no tool needed to fit them). Screw sizes: TBD – check on next show.

## Identity
- What crews call it: "X4 Bar", "X4 Bar 20", "the 1 m X4 bar". The half-length one is the **X4 Bar 10**.
- Fixture library / profile names: in grandMA it shows as "Impr X4 Bar 20" (MA forum thread). A user on that forum said MA's 3D model of the fixture isn't very good. Roughly 7 profiles exist across consoles (search summary). GDTF / Hog / Eos names: Not found — fill in from the fixture.
- Variants and how to tell them apart:
  - **X4 Bar 20**: 1 m long, 20 x 15 W RGBW cells, 14.5 kg.
  - **X4 Bar 10**: 0.5 m long (500 x 240 x 100 mm / 19.7 x 9.4 x 3.9 in), 10 x 15 W RGBW cells, 8 kg / 17.6 lb, 200 VA. It has 7 DMX modes: Normal is 33 ch, Compressed is 19 ch. **The Bar 10 footprints are different from the Bar 20's, so don't copy a Bar 20 patch onto a Bar 10.** Its other mode sizes: Not found — fill in from the fixture.
  - Both bars share the same feature set: zoom, tilt and variable CTO from 2500 K to 10,000 K (spec sheet that covers both).

## Passwords, menu locks & hidden menus
- Default passcode: **none found** in any source. Not found — fill in from the fixture.
- Key lock: **Mode + Enter + Up pressed together** locks and unlocks the menu keys (manual summary).
- Service / factory menu access: Not found.
- Menu navigation (manual): press **Mode** to enter the main menu. Use **Up/Down** to scroll and **Enter** to go one level down or to confirm.
- Where the controls are: PLSN says the LCD sits in the **middle of the base**. One manual excerpt says the control board is "on the side part of the arm". ⚠️ Check on the unit.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | 4.6 A (rental-house spec sheet, not manual table) ⚠️ | Not found | Not found |
| Power (W) | 550 W max (rental listing) | — | Manual: 450 VA power consumption. Some listings say 400 W typical / 550 W max at 230 V |
| Max power-link (manufacturer) | No count given. Manual: "never connect more than a total load of 20A" (connector limit) | same | same |
| **Max per 20 A circuit** (16 A continuous) | floor(16/4.6)=3 → **3** | Not found. Estimate only: 450 VA÷208 ≈ 2.2 A, floor(16/2.2)=7. ⚠️ Not a manufacturer figure; confirm with a meter | — |

- Input range / auto-ranging: auto-sensing 100–240 V AC, 50–60 Hz (manual).
- Connectors in / out: powerCON in and thru. Sources don't confirm whether it's blue/grey or TRUE1. Rental houses ship it with powerCON-to-L6-20 or other tails. Check the unit.
- Fuse: **5x20 mm micro-fuse, T5A** (manual). Fuse location: Not found — fill in from the fixture.
- Inrush / power-up notes: Not found. The fixture runs a tilt reset at power-up, so give it clearance.
- The numbers conflict: the manual says 450 VA and a rental listing says 550 W / 4.6 A at 120 V. Plan circuits on the higher **4.6 A** figure.

## Data & addressing
- Connectors: 5-pin XLR DMX in/thru (spec sheet).
- Protocols: DMX512. RDM / Art-Net: Not found.
- DMX modes / footprints (manual v1.8, SW v0.60). The manual says **seven** modes, but the search summaries only list six:
  - Compressed (comp): 20 ch
  - Normal (norm): 34 ch. The manual calls this "the most common mode with all basic functions."
  - High Resolution (hires): 35 ch
  - Dual Pixel (dpix): 48 ch
  - Dual Pixel High Res (dpixh): 49 ch
  - Single Pixel (spix): 88 ch
  - 7th mode: Not found — fill in from the fixture.
- Pixels are numbered **1–20 from left to right** (manual). **Reverse pixel** in the menu flips the count.
- Set the address: **Mode** → Level 1 **DMX Address** [001] → **Enter** → Up/Down → **Enter**.
- Set the mode: Mode → **Set DMX Mode** (Level 2) → pick NORM / SPIX / DPIXH / etc. → Enter.
- Battery / unpowered addressing: Not found. No source mentions battery addressing for this fixture.
- Factory reset: Not found. The **Reset** menu item recalibrates; it doesn't restore defaults. See Maintenance.
- Wireless / Ethernet: none found.

## Rigging & hardware
- Bracket / omega type: it ships with **two omega brackets**, each with a quick-trigger clamp (rental listing). The brackets fit into **quarter-turn camlock** slots on the base: insert and turn 90° to lock. The clamp can slide along the bracket (about a foot long) to find clear truss (PLSN). GLP sells separate X4 Bar brackets and accessories.
- Safety cable point: run the safety wire through the **two attachment points** to the primary structure (PLSN / manual summary).
- Mounting orientations allowed: Not found in sources.
- Transport / tilt lock: there's a **tilt lock on the yoke** (PLSN). The yoke and tilt motors sit under the outer LED cells.
- Weight / dimensions: the manual summary says **14.5 kg / 32 lb net, 16 kg / 35 lb with 2 brackets**, 1000 x 100 x 240 mm. ⚠️ PLSN's road test says "about 17 lbs", which conflicts. Trust the manual figure for rigging loads.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD |
| Gobo / effects module access | n/a (LED wash, no gobos) | — |
| Lens / front glass | TBD – check on next show | TBD |
| Omega bracket | Quarter-turn camlocks (PLSN) | Tool-free / flat blade ⚠️ unverified |

## Optics & consumables
- Source: 20 x 15 W RGBW LEDs. LED life: Not found.
- Color system: RGBW mixing, variable CTO 2500–10,000 K (spec sheet).
- Zoom: **7°–50°**.
- Tilt: **210°**, about 1.5 s end to end, with position feedback (spec). PLSN says the motors are very quiet and there's no lag on reversal.
- Filters: GLP sells X4 Bar filter accessories. Some rental kits include a **clear lens and a frost lens**.
- Gobos / prism / iris: none (wash bar).

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Not found | The manual excerpts found don't list error messages | Check the full manual (link below) and fill in |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Buttons do nothing | Key lock engaged | Press **Mode + Enter + Up** together (manual) |
| Bar won't tilt | Yoke tilt lock engaged, or Special → Tilt current = Off | Release the tilt lock and set Tilt current to On |
| Tilt drifts or loses position | Needs recalibration | Menu **Reset** (manual says this needs Tilt firmware V.20 or later) |
| Tilt moves the wrong way vs. the other bars | Reverse tilt set on some units | Menu: **Reverse tilt** On/Off |
| Pixel chase runs backwards | Reverse pixel set, or fixture hung flipped | Menu: **Reverse pixel** |
| Display upside-down | Display flip | Menu: **Display flip**. It can also be set over DMX: the control channel at 144–147 = off and 148–151 = on (manual summary; which channel isn't confirmed) |
| Dimming curve looks different from the other bars | Dimming mode mismatch | Special → dimmer mode **ESOFT / LIN / SOFT**. Set all bars the same |
| Breaker trips on a long chain | Too many on one 20 A circuit | Max 3 per 20 A @120 V. Never more than 20 A through the thru |

## Maintenance
- Recalibrate / reset: menu **Reset** runs a reset and recalibrates all functions. The manual notes this needs Tilt firmware V.20 or later.
- The Special menu also has: **Tilt reset** (whether tilt moves during reset), **Tilt current** (tilt motor on/off) and **Tilt slow** (slow tilt speed) (manual).
- Fan / filter cleaning: Not found.
- Firmware update method: Not found in the manual excerpts. See [_glp-common.md](_glp-common.md).

## Road notes (community)
- PLSN road test: very quiet tilt with no lag on reversal. The tilt lock is on the yoke. The power supply is in the base and the LCD is in the middle of the base.
- MA Lighting forum: a user said MA's built-in 3D model of the "Impr X4 Bar 20" is poor for visualization.
- No Reddit, ControlBooth or Blue Room threads were found in searches.

## Sources
- [impression X4 Bar 20 User Manual v1.8 EN (SW v0.60) — glp.de](https://glp.de/files/products/impression-x4-bar-20-product-data/impression_X4_Bar_20_User_Manual_v1.8_EN.pdf) — 450 VA, 100–240 V auto-sensing, T5A 5x20 fuse, 20 A connector-load warning, DMX modes, menu lock, Special menu, Reset
- [Same manual, Full Compass mirror](https://www.fullcompass.com/common/files/45327-impressionX4Bar20UserManual.pdf) — as above
- [Manual v1.9 EN](https://www.germanlightproducts.com/wp-content/uploads/2019/02/impression_X4Bar20_manual_v1.9_EN.pdf) — weight 14.5/16 kg, dimensions
- [Manual v1.4 EN](https://www.germanlightproducts.com/wp-content/uploads/2014/11/impression-X4-Bar-20-User-Manual-v1.4-EN.pdf)
- [ManualsLib X4 Bar 20 (menu page 9–10)](https://www.manualslib.com/manual/1568587/Glp-Impression-X4-Bar-20.html) — menu navigation, Display flip, Reset
- [DMX Channel Index v1.7](https://www.germanlightproducts.com/wp-content/uploads/2019/02/Impression_X4Bar20_DMX_v1.7_EN.pdf)
- [Christie Lites X4 Bar 20 listing](https://www.christielites.com/glp-impression-x4-bar-20/228w2w10w161w324) and [4Wall rental page](https://www.4wall.com/rentals/9758238/glp-impression-x4-bar-20) — 4.6 A @120 V / 550 W (search summary attributed to rental listings), package contents
- [PLSN road test](https://plsn.com/articles/road-tests/glp-impression-x4-bar-20/) — tilt lock on yoke, camlock omega, safety points, 210° tilt speed, "about 17 lbs" (conflicts with manual)
- [X4 Bar spec sheet (Bar 10 & 20)](https://www.germanlightproducts.com/wp-content/uploads/2016/01/PDF-Spec-Sheet-impression-X4-Bar.pdf) — CTO range, powerCON thru, Bar 10 specs
- [X4 Bar 10 User Manual (Full Compass)](https://www.fullcompass.com/common/files/45323-impressionX4Bar10UserManual.pdf) — Bar 10: 200 VA, 8 kg, 7 modes, Normal 33 / Compressed 19
- [MA Lighting forum thread](https://forum.malighting.com/forum/thread/62384-impr-x4-bar-20-model/) — 3D model complaint
- [GLP X4 Bar Brackets](https://glp.de/en/products/miscellaneous/accessories/x4-bar-brackets-en) — accessory brackets exist
