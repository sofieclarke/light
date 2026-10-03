---
title: "Chauvet Professional Maverick MK3 Spot"
manufacturer: "Chauvet Professional"
model: "Maverick MK3 Spot"
aliases: ["mk3 spot", "maverick mk3", "mav mk3 spot", "maverick mk 3 spot", "maverickmk3spot", "mk3"]
type: "spot"
light_source: "LED 820W cool white"
ip_rating: null
weight_lb: 72.9
weight_kg: 33
dimensions: "16.10 x 11.92 x 29.76 in (409 x 303 x 756 mm)"
power:
  input: "100–240 VAC, 50/60 Hz, auto-ranging"
  connector_in: "powerCON TRUE1-compatible"
  connector_out: null
  watts_max: 1180
  amps_120v: 9.90
  amps_208v: 5.60
  amps_230v: 5.04
  link_max_120v: null
  link_max_208v: null
  link_max_230v: null
  per_20a_120v: 1
  per_20a_208v: 2
  fuse: null
dmx:
  connectors: null
  protocols: ["DMX", "RDM", "W-DMX", "Art-Net", "sACN"]
  modes:
    - { name: "31CH", channels: 31 }
    - { name: "39CH", channels: 39 }
menu_password: "2323"
tools: []
verification: "web-search"
last_updated: "2026-10-03"
---

# Chauvet Professional Maverick MK3 Spot

> **2AM CARD** — the stuff you need first
> - **Power:** 9.90 A @120 V / 5.60 A @208 V / 5.04 A @230 V → **1 per 20 A circuit @120 V, 2 @208 V** (manufacturer link limit not found)
> - **Passcodes:** **2323** = Offset Mode (Zero Adjust). **0920** shows up in the manual as either the service-menu code or the touchscreen/button unlock code; search summaries disagree (⚠️ try it if the panel is locked). Web server **admin / admin**.
> - **DMX:** 31 or 39 channels. Also W-DMX, Art-Net, sACN, RDM.
> - **Gobos:** 2 rotating wheels, 30 mm OD, 1.1 mm max thickness (image 23 mm on wheel 1, 21 mm on wheel 2), plus 1 static wheel.
> - **Tools:** TBD – check on next show.

## Identity
- What crews call it: "MK3 Spot", "Mav MK3".
- Fixture library / profile names: Chauvet Professional "Maverick MK3 Spot", 31ch / 39ch.
- Variants and how to tell them apart: **MK3 Profile** (same family, adds framing shutters), **MK3 Profile CX** (different color system), **MK3 Wash** ([page](maverick-mk3-wash.md)). **MK2 / MK1 Spot** are older generations and their passcodes and menus differ. **Maverick Force S Spot** is a newer, smaller spot ([page](maverick-force-s-spot.md)).

## Passwords, menu locks & hidden menus
- **Offset Mode / Zero Adjust: 2323** (Chauvet's usual offset code).
- **0920.** One search summary of the MK3 Spot manual called it "the passcode to enter the service menu". Another said it "is used to unlock the touchscreen and menu buttons". ⚠️ The same code also appears in the MK2 Spot manual. Try 0920 for both purposes.
- **Sibling MK3 Profile:** when asked for the passcode, press **UP, DOWN, UP, DOWN, ENTER**. Settings → **Touchscreen Lock** (YES/NO) and Settings → **Lock Screen** (locks buttons + touchscreen). ⚠️ That's from the MK3 **Profile** manual. The Spot likely shares it but this isn't confirmed.
- **Web server:** default user name **admin**, password **admin**.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | 9.90 | 5.60 | 5.04 |
| Power (W) | 1180 | 1160 | 1150 |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | floor(16/9.90)=1 → **1** | floor(16/5.60)=2 → **2** | floor(16/5.04)=3 → **3** |

- If Chauvet's usual 12 A rule applies (as in other Chauvet manuals): floor(12/9.90)=1 and floor(12/5.60)=2, which gives the same answer.
- Input range / auto-ranging: 100–240 VAC, 50/60 Hz, auto-ranging.
- Connectors in / out: TRUE1-compatible power input. Output: Not found.
- Fuse: Not found.
- Inrush: none found. These are big switch-mode supplies, so power up a rig of them in stages (general knowledge).

## Data & addressing
- Connectors: Not found — fill in from the fixture.
- Protocols: DMX, RDM, W-DMX (built-in wireless), Art-Net, sACN.
- DMX modes / footprints: 31 ch, 39 ch.
- Set the address: Not found — has a touchscreen plus menu buttons.
- Battery / unpowered addressing: Not found.
- Factory reset: Not found.
- Wireless / Ethernet setup notes: W-DMX built in. Web server login admin/admin.

## Rigging & hardware
- Bracket / omega: Not found.
- Fasteners: Not found.
- Safety cable point: Not found.
- Orientations: Not found.
- Transport / pan-tilt locks: Not found — TBD check on next show.
- Weight / dimensions: 72.9 lb (33 kg). 16.10 x 11.92 x 29.76 in (409 x 303 x 756 mm).

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD – check on next show |
| Gobo / effects module access | TBD – check on next show | TBD – check on next show |
| Lens / front glass | TBD – check on next show | TBD – check on next show |
| Omega bracket | TBD – check on next show | TBD – check on next show |

## Optics & consumables
- Source: 820 W cool-white LED. 58,200 lux at 16.4 ft (manufacturer spec).
- Color system: CMY mixing plus a color wheel (general knowledge for CMY; color wheel ⚠️ unverified).
- Gobo wheels:

| Wheel | Type | OD | Image | Max thickness |
|---|---|---|---|---|
| 1 | Rotating | 30 mm | 23 mm | 1.1 mm |
| 2 | Rotating | 30 mm | 21 mm | 1.1 mm |
| 3 | Static | "160 mm" as given by the source (⚠️ almost certainly not a slot size; measure it) | 22 mm | 0.8 mm |

- Prism / frost / zoom / iris: Not found in excerpts.
- Gobo change procedure: Not found.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| (menu) Error Information | Shows current errors or "No Error" | Check here first |
| X_op | Pan optocoupler error | ⚠️ From the **MK1** Spot manual. Likely the same convention on the MK3 |
| Y_op | Tilt optocoupler error | ⚠️ From the MK1 Spot manual, as above |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Two on a 120 V circuit trip the breaker | 2 × 9.9 A = 19.8 A | 1 per 120 V circuit. Use 208 V (2 per circuit) |
| Panel locked / asks for a code | Lock Screen / Touchscreen Lock enabled | Try 0920, or UP-DOWN-UP-DOWN-ENTER (MK3 Profile method) ⚠️ |

## Maintenance
- Recalibrate: Offset/Zero Adjust (2323).
- Fan info: the menu shows head fan speed settings (Fan Information).
- Firmware update method: Not found in the excerpts — fill in.

## Road notes (community)
- PLSN did a road test of this fixture (see Sources). No troubleshooting threads turned up in search. Add notes here.

## Sources
- [Maverick MK3 Spot User Manual Rev 6 (Chauvet)](https://www.chauvetprofessional.com/wp-content/uploads/2019/02/Maverick_MK3_Spot_UM_Rev6.pdf): power/current at 120/208/230 V, auto-ranging, passcodes 2323 and 0920, web server admin/admin, Error Information menu
- [Maverick MK3 Spot User Manual Rev 1](https://www.chauvetprofessional.com/wp-content/uploads/2019/02/Maverick_MK3_Spot_UM_Rev1.pdf): TRUE1-compatible input
- [Maverick MK3 Profile User Manual (Full Compass)](https://www.fullcompass.com/common/files/37895-MaverickMK3ProfileUserManual.pdf): UP-DOWN-UP-DOWN-ENTER, Touchscreen Lock, Lock Screen (sibling model)
- [Maverick MK1 Spot User Manual](https://www.chauvetprofessional.com/wp-content/uploads/2017/03/Maverick_MK1_Spot_UM_Rev4_WO.pdf): X_op / Y_op (older model)
- [Maverick MKII Spot User Manual Rev 4](https://www.chauvetprofessional.com/wp-content/uploads/2016/05/Maverick_MKII_Spot_UM_Rev4_WO.pdf): 0920 also appears (older model)
- [B&H listing](https://www.bhphotovideo.com/c/product/1531658-REG/chauvet_professional_maverickmk3spot_maverick_mk_3_spot_ip.html), [Chauvet product page](https://www.chauvetprofessional.com/products/maverick-mk3-spot/), [Musson data sheet](https://media.musson.com/mti/docs/m/a/maverick_mk3_spot.pdf): DMX modes, weight, dimensions, gobo sizes, lux, protocols
- [PLSN road test](https://plsn.com/articles/road-tests/chauvet-maverick-mk3-spot/)
