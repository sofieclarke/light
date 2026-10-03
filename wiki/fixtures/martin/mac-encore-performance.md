---
title: "Martin MAC Encore Performance"
manufacturer: "Martin"
model: "MAC Encore Performance (CLD / WRM)"
aliases: ["encore", "encore performance", "mac encore", "encore cld", "encore wrm", "encore performance cld", "encore performance wrm"]
type: "profile"
light_source: "White LED engine. CLD = cool-white version, WRM = warm-white version (wattage not confirmed)"
ip_rating: null
weight_lb: null
weight_kg: 31
dimensions: "480 x 740 x 452 mm (community libraries, W x H x D)"
power:
  input: null
  connector_in: "Neutrik powerCON TRUE1 (input only, per Open Fixture Library)"
  connector_out: "none listed (no power thru per Open Fixture Library)"
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
  connectors: "5-pin XLR (community libraries)"
  protocols: ["DMX"]
  modes:
    - { name: "CLD (single mode)", channels: 38 }
    - { name: "WRM (single mode)", channels: 38 }
menu_password: null
tools: []
verification: "community"
last_updated: "2026-10-03"
---

# Martin MAC Encore Performance (CLD / WRM)

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** No passcode found in any source. ⚠️ unverified
> - **Power:** amps **not found**. Community libraries list **585 W**. A rough guess (⚠️ unverified, not from a manual) is 585/120 ≈ 4.9 A → 3 per circuit @120 V, 585/208 ≈ 2.8 A → 5 @208 V. **powerCON TRUE1 is input only, with no thru**, so each fixture needs its own feed (Open Fixture Library).
> - **DMX:** **38 ch** in both versions. The only difference: **CLD has a CTO channel, WRM has a CTB channel** (channel 7).
> - **Theatre-quiet fan modes from the desk** (control channel): 54 regulated fan / fixed output, 55 full fan, 56 medium, 57 low, **58 ultra-low** (fixed fan speed, output regulated). **Reset all = 10–14 (5 s).**
> - **Won't move?** Transport locks: Not found — TBD – check on next show
> - **Tools:** TBD – check on next show

## Identity
- What crews call it: "Encore", "Encore CLD" / "Encore WRM" (general knowledge).
- Fixture library / profile names: Open Fixture Library and QLC+ "MAC Encore Performance", with modes **CLD** and **WRM** (38 ch each). Pick the mode that matches the fixture version, or CTO/CTB will be wrong.
- Variants:
  - **CLD (cold):** cool-white engine, warms with a **CTO** channel.
  - **WRM (warm):** warm-white engine (about 3000 K per QLC+), cools with a **CTB** channel.
  - **MAC Encore Wash CLD / WRM** is a separate wash fixture with its own user guide.
  - How to tell CLD from WRM on the truss: the label on the fixture, or the model name the display shows at boot. Not confirmed. ⚠️ unverified

## Passwords, menu locks & hidden menus
- Default passcode: none found. Not found — fill in from the fixture.
- Display back on from the desk: control channel **52 = display ON, 53 = display OFF** (1 s).
- **Hibernation:** control channel **61 = ON, 62 = OFF** (5 s). If a fixture seems dead but is powered, try 62.
- Service menu access: Not found.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found | Not found | Not found |
| Power (W) | 585 W (community libraries, not manual) | 585 W | 585 W |
| Max power-link (manufacturer) | **No power thru** (TRUE1 input only, per Open Fixture Library) | same | same |
| **Max per 20 A circuit** (16 A continuous) | Not found. Rough guess 585/120 ≈ 4.9 A → floor(16/4.9)=**3** ⚠️ unverified | Not found. Rough guess 585/208 ≈ 2.8 A → floor(16/2.8)=**5** ⚠️ unverified | — |

- Since there is no thru, those counts mean fixtures on **separate feeds** off one 20 A breaker, for example through a power strip or a TRUE1 splitter. Read the rating label for real amps.
- Fuse, input range: Not found — fill in from the fixture.

## Data & addressing
- Connectors: 5-pin XLR DMX (community libraries).
- Protocols: DMX. RDM is not confirmed.
- **38-channel layout** (Open Fixture Library, from manual rev A):
  1 shutter/strobe · 2–3 dimmer + fine · 4–6 C / M / Y · 7 **CTO (CLD) or CTB (WRM)** · 8 color wheel · 9 rotating gobo wheel · 10–11 gobo index/rotation + fine · 12–13 animation wheel function + index/rotation · 14 frost · 15 iris · 16–17 zoom + fine · 18–19 focus + fine · 20–27 framing blades 1–4 (insertion + rotation) · 28 framing system rotation · 29–32 pan, pan fine, tilt, tilt fine · 33 fixture control · 34–37 FX1/FX2 select + speed · 38 FX sync.
- **Control channel (ch 33) highlights:**
  - 10–14 reset all (5 s). 16 reset color, 17 reset beam, 18 reset pan/tilt.
  - 23–26 dimming curves. 28 fast / 29 smooth pan-tilt.
  - 32–35 focus tracking off, or close / medium / long range. 36/37 video tracking on/off. 41/42 beam smoothing on/off.
  - 52/53 display on/off. **54–58 fan modes.** 61/62 hibernation on/off.
  - **65–71 pan/tilt limits** (enable, store lower/upper pan and tilt, reset). Useful when the head hits set pieces.
  - 72/73 tungsten emulation on/off. 74/75 alternative light source (color-temperature shift) on/off.
  - 100 enable calibration. 101–116 store calibrations. **199 reset all calibrations to factory default.**
- Strobe channel: 0–19 closed, 20–49 open, 50–200 strobe, 201–210 open, 211–255 strobe.
- Set the address: Not found — fill in from the fixture. (Newer Martin fixtures have a battery-powered display for setting the address with no mains. This is not confirmed for the Encore. ⚠️ unverified)

## Rigging & hardware
- Bracket / omega type: Not found.
- Transport / pan-tilt locks: Not found — TBD – check on next show.
- Weight / dimensions: 31 kg. About 480 x 740 x 452 mm. Pan 540°, tilt 268° (QLC+ / Open Fixture Library).

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD |
| Gobo / effects module access | TBD – check on next show | TBD |
| Lens / front glass | TBD – check on next show | TBD |
| Omega bracket | TBD – check on next show | TBD |

## Optics & consumables
- Source: white LED. QLC+ lists about 11,600 lm and 3000 K for the WRM. ⚠️ community
- Color: CMY + CTO (CLD) or CTB (WRM). Color wheel (Open Fixture Library slot names): Open, Blue 101, Green 203, Orange 311, Magenta 522, Congo Blue 108, Red 310.
- Gobos: one rotating gobo wheel (5 gobos + open) and an animation wheel ("Radial Breakup"). Gobo size: Not found.
- Frost, iris, 4-blade framing with rotation. Zoom 12–48° (community).

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Not found | — | See [Martin common](./_martin-common.md) |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| CTO fader makes the light bluer (or the reverse) | Patched as CLD on a WRM fixture, or WRM on a CLD | Repatch the correct mode |
| Fixture won't move or light but has power | Hibernation on | Control channel 62 (hibernation OFF, 5 s) |
| Too loud for a quiet scene | Fan mode | 57 low or 58 ultra-low (output is regulated down instead) |
| Pan/tilt stops short | Pan/tilt limits enabled | 71 resets and disables the limits |
| Output warmer or cooler than the rest of the rig | Tungsten emulation or alternative light source is on | 73 / 75 turn them off |

## Maintenance
- Recalibrate: 100 enable calibration, adjust, 101–116 store. **199 restores factory calibration.**
- Fan / filter cleaning: Not found.
- Firmware update method: Not found. See [Martin common](./_martin-common.md).

## Road notes (community)
- None found in searches (search budget ran out before this model).

## Sources
- [Open Fixture Library: mac-encore-performance.json](https://github.com/OpenLightingProject/open-fixture-library/blob/master/fixtures/martin/mac-encore-performance.json) (Felix Edelmann, Ryan Goodwin, 2023): 38-ch layout for CLD/WRM, control-channel values, TRUE1 input only, weight, dims, 585 W, color and gobo wheels. Cites [UM_MACEncorePerformance_EN_A](https://adn.harmanpro.com/site_elements/executables/7477_1526701894/UM_MACEncorePerformance_EN_A_original.pdf), [CLD product page](https://www.martin.com/en/products/mac-encore-performance-cld), [WRM product page](https://www.martin.com/en/products/mac-encore-performance-wrm).
- [QLC+ Martin-MAC-Encore-Performance.qxf](https://github.com/mcallegari/qlcplus/tree/master/resources/fixtures/Martin): lumens, CCT, pan/tilt range.
- [MAC Encore Wash user guide](https://www.martin.com/en-US/site_elements/mac-encore-wash-user-guide): confirms the separate Encore Wash CLD/WRM product (title only).
