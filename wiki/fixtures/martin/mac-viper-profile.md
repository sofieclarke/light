---
title: "Martin MAC Viper Profile"
manufacturer: "Martin"
model: "MAC Viper Profile"
aliases: ["viper", "viper profile", "mac viper", "viper performance", "viper airfx", "viper air fx", "viper wash", "viper wash dx"]
type: "profile"
light_source: "1000 W short-arc discharge lamp (exact lamp part number not confirmed)"
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
  connectors: "5-pin XLR (per community fixture libraries)"
  protocols: ["DMX"]
  modes: []
menu_password: null
tools: []
verification: "community"
last_updated: "2026-10-03"
---

# Martin MAC Viper Profile

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** No passcode found in any source. ⚠️ unverified
> - **Power:** amps **not found**. Community libraries list the Viper family at about 1200–1225 W. A rough guess (⚠️ unverified, not from a manual) is **1 per 20 A circuit @120 V, 2 @208 V** until you read the label.
> - **Lamp won't strike / strike it from the desk:** on the Viper Performance, AirFX and Wash, the control channel does **lamp ON at DMX 40–44** and **lamp OFF at 45–49 (hold 5 s)**. **Reset all is 10–14 (hold 5 s).** ⚠️ The Profile probably uses the same values but this is unverified.
> - **Shutter closed (DMX 0–19) for 10 s drops the lamp to 800 W mode** (Performance, AirFX and Wash libraries).
> - **DMX:** Viper Profile modes not found. Viper Performance is 32 / 40 ch, AirFX 20 / 28 (33 with Quadray), Wash DX 18 / 24 (community libraries).
> - **Won't move?** Pan and tilt transport locks are not confirmed by any source. TBD – check on next show.
> - **Tools:** TBD – check on next show

## Identity
- What crews call it: "Viper", "Viper Profile" (general knowledge).
- Fixture library / profile names: Open Fixture Library and QLC+ have **Viper Performance, Viper AirFX and Viper Wash (DX)** but not the Viper Profile. Use the console library.
- **Viper family: how to tell them apart** (all 1000 W discharge, sharing the same base and yoke size):

| Model | What it is | Community data (Open Fixture Library / QLC+) |
|---|---|---|
| **Viper Profile** | Profile spot: CMY, gobos, animation wheel, iris (general knowledge) | Modes not found |
| **Viper Performance** | Profile with **4-blade framing shutters** and a framing-rotation channel, plus CMY, CTO, color wheel, rotating gobo wheel (5 gobos), animation wheel ("Ripple Waves"), frost, prism, iris. 10–44° zoom. | Basic 32 ch, Extended 40 ch (5 reserved). About 37.9–38 kg. Listed 26,000 lm. |
| **Viper AirFX** | Beam/wash hybrid with a **160 mm PC front lens**, 1:5 zoom, an aerial-effects wheel and a static gobo wheel. Takes the optional **Quadray** module, which splits the beam into 4 rays. | Basic 20, Extended 28, Quadray FX 33. About 35.7 kg. Listed 34,500–35,000 lm. |
| **Viper Wash / Wash DX** | Wash. The **DX adds the color wheel, iris and internal barndoors.** 13.5–59° zoom. | Basic 18, Extended 24. About 33 kg. Open Fixture Library note: focus and zoom are 8-bit, "the manual is wrong". |

## Passwords, menu locks & hidden menus
- Default passcode: none found. Not found — fill in from the fixture.
- Service / factory menu: Not found. The control channel gives remote access to calibration (see Data). See also [Martin common](./_martin-common.md).
- Turn the display back on from the desk (Performance library): DMX **155–159 display ON**, **160–164 display OFF**.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found | Not found | Not found |
| Power (W) | about 1200–1225 W (community libraries, not manual) | same | same |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | Not found. Rough guess 1225/120 ≈ 10.2 A → **1** ⚠️ unverified | Not found. Rough guess 1225/208 ≈ 5.9 A → floor(16/5.9)=**2** ⚠️ unverified | — |

- Those guesses use unity power factor and community wattage. **Read the rating label** before loading more onto a circuit.
- Input range, connectors, fuse: Not found — fill in from the fixture.
- Ballast output can be reduced from the desk (Performance library): DMX 125–126 = 100% (default). 127–128 = 90%, 129–130 = 80%, 131–132 = 70%, 133–134 = 60%.

## Data & addressing
- Connectors: 5-pin XLR DMX (community libraries).
- Protocols: DMX. The Viper Performance library lists an RDM model ID, which suggests RDM support on that model. ⚠️ unverified
- DMX modes: Viper Profile, Not found — fill in from the fixture. See the family table for the others.
- **Fixture control channel** (Viper Performance, from the Open Fixture Library transcription of manual rev C. AirFX and Wash match for the values shown):
  - 10–14 reset entire fixture (5 s). 15–19 reset dimmer/shutter. 20–24 reset color. 25–29 reset effects/beam. 30–34 reset pan/tilt. 35–39 reset framing (Performance only).
  - **40–44 lamp ON. 45–49 lamp OFF (hold 5 s).**
  - 55–59 enable calibration. 60–79 dimming curves (linear, square, inverse square, S).
  - 80–94 pan/tilt speed normal, fast, slow. 105–124 zoom/focus linking off, or near / medium / far.
  - 145–154 auto blackout on/off. 155–164 display on/off.
  - 165–244 store calibrations (pan/tilt, dimmer, CMY, CTC, gobo index, prism, iris, focus, zoom, pan, tilt). **245–249 reset all calibration to factory defaults.**
- Strobe/shutter channel: 0–19 closed (lamp goes to 800 W after 10 s), 20–49 open, 50–200 strobe, 201–210 open, 211–255 strobe.
- Set the address: Not found — fill in from the fixture.

## Rigging & hardware
- Bracket / omega type: Not found.
- Transport / pan-tilt locks: Not found — TBD – check on next show.
- Weight / dimensions: Profile not found. Performance is about 472 x 748 x 566 mm, 37.9 kg (Open Fixture Library).

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD |
| Gobo / effects module access | TBD – check on next show | TBD |
| Lens / front glass | TBD – check on next show | TBD |
| Omega bracket | TBD – check on next show | TBD |
| Lamp access | TBD – check on next show | TBD |

## Optics & consumables
- Lamp: 1000 W short-arc discharge, 6000 K (community libraries list "HTI 1000W" / "MSR 1000W"). The lamp part number and lamp life are not confirmed. ⚠️ unverified
- Gobo size: Not found.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Not found | — | See [Martin common](./_martin-common.md) for the general Martin error display |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Dimmer up but no light, display fine | Lamp off (auto blackout, or switched off from the desk) | Send lamp ON (40–44 on the control channel) |
| Output looks dimmer than the others | Shutter was closed long enough for 800 W mode, or ballast reduced to 60–90% | Check control-channel ballast output. Set 125–126 for 100%. |
| Zoom and focus fight each other | Zoom/focus linking setting | 105–109 turns linking off. 110–124 sets near / medium / far. |
| Display dark | Display turned off by DMX | 155–159 display ON |

## Maintenance
- Recalibrate: enable calibration (55–59), adjust, then store (165–244). Factory calibration reset is 245–249 (Performance library).
- Firmware update: Not found for this model. See [Martin common](./_martin-common.md).

## Road notes (community)
- Open Fixture Library maintainers note that on the Viper Wash, **focus and zoom are 8-bit, and the manual is wrong** about that.

## Sources
- [Open Fixture Library: mac-viper-performance.json](https://github.com/OpenLightingProject/open-fixture-library/blob/master/fixtures/martin/mac-viper-performance.json): Performance modes, control-channel values, shutter 800 W mode, ballast output, weight/dims, wheels. Cites [UM_MACViperPerf_EN_C](https://www.martin.com/files/files/productdocuments/11_MANUALS/999/35000275c%20UM_MACViperPerf_EN_C.pdf).
- [Open Fixture Library: mac-viper-airfx.json](https://github.com/OpenLightingProject/open-fixture-library/blob/master/fixtures/martin/mac-viper-airfx.json): AirFX modes, Quadray, 160 mm lens, control channel. Cites [UM_MACViperAirFX_EN_B](https://www.martin.com/files/files/productdocuments/11_MANUALS/999/UM_MACViperAirFX_EN_B.pdf).
- [Open Fixture Library: mac-viper-wash.json](https://github.com/OpenLightingProject/open-fixture-library/blob/master/fixtures/martin/mac-viper-wash.json): Wash / DX differences, 8-bit focus/zoom note. Cites [UM_MACViperWash_EN_B](https://www.martin.com/files/files/productdocuments/11_MANUALS/999/UM_MACViperWash_EN_B.pdf).
- [QLC+ Martin fixtures](https://github.com/mcallegari/qlcplus/tree/master/resources/fixtures/Martin) (Martin-MAC-Viper-Performance.qxf, Martin-Viper-AirFX.qxf, Martin-MAC-Viper-Wash-DX.qxf): modes, wattage (1200 W), weights, lamp type.
- Web searches for this model returned no usable manual content. The session's search budget ran out before the Viper Profile could be researched.
