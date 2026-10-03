---
title: "MDG theONE"
manufacturer: "MDG Fog Generators"
model: "theONE Atmospheric Generator (Model 1.30 / 1.31)"
aliases: ["theone", "the one", "mdg", "mdg the one", "mdg hazer", "mdg theone", "the one hazer"]
type: "atmospheric"
light_source: null
ip_rating: null
weight_lb: 50
weight_kg: 23
dimensions: "Standalone 24 in H x 10 in W x 12 in D (61 x 25 x 30 cm). Touring rack 42 x 30 x 24 in (106 x 76 x 61 cm), 265 lb / 120 kg loaded"
power:
  input: "100–250 VAC, 50/60 Hz, single phase"
  connector_in: "IEC C19-type inlet (OFL community data) — fill in from the fixture"
  connector_out: ""
  watts_max: 1480
  amps_120v: null
  amps_208v: null
  amps_230v: null
  link_max_120v: null
  link_max_208v: null
  link_max_230v: null
  per_20a_120v: 1
  per_20a_208v: null
  fuse: ""
dmx:
  connectors: "5-pin XLR in/out, RJ45 Ethernet, USB-B (diagnostic/bootload)"
  protocols: ["DMX", "RDM", "Art-Net", "sACN", "Pathport", "ETC Net2", "ETC Net3", "Strand ShowNet"]
  modes:
    - { name: "Standard", channels: 5 }
menu_password: null
tools: []
verification: "manual-verified"
last_updated: "2026-10-03"
---

# MDG theONE

> **2AM CARD** — the stuff you need first
> - **Warm-up:** about **7 min heat**, then a 30–60 s purge, then READY. The troubleshooting table says to allow **about 8 min**. Spec: "under 10 minutes".
> - **Needs GAS:** industrial **CO2 or N2**, bottles open, gauge **> 100 psi**. **Never use siphon (liquid) CO2 bottles.** That causes P. LOW or P. HIGH faults.
> - **Fluid:** **MDG Neutral Fog Fluid ONLY**. 20 L jug. Open the vent on the jug.
> - **DMX, 5 ch:** 1 Unit off/on (≥128 = ON) · 2 Haze/Fog (≥128 = FOG) · 3 Output 0–255 · 4 Fog off/on (≥128 = ON) · 5 External fan. Address 1–508.
> - **Power:** 100–250 V, **1100 W at 100 V, 1480 W at 250 V**. Amps aren't published. Worst case 1480/120 = 12.3 A → **1 per 20 A circuit, dedicated.**
> - **SHUTDOWN:** Fog OFF → wait 1 min purge + 30 s depressurize → Unit OFF → mains off → close gas. **Never kill power while fogging.**
> - **"DMX" mode vs "AUTO":** in DMX mode, **losing DMX triggers an automatic shutdown**. In AUTO it holds the last values.

## Identity
- What crews call it: theONE, MDG.
- Fixture library / profile names: GDTF "MDG@theONE" Release 1.0 (5 ch: Control, OutputMode, OutputLevel, Output, Fan). OFL "theONE Atmospheric Generator" (RDM model ID 1).
- Variants: **theONE Touring** (in a rolling aluminum rack with 2 gas bottles, a 20 L fluid jug, a 10" external fan and a tool drawer) vs **theONE Standalone** (generator only). Model 1.30 / 1.31.
- Dual mode: **Haze** and **Fog**, switchable by DMX channel 2.

## Passwords, menu locks & hidden menus
- No passcode mentioned in the manual.
- Menu: 4×20 LCD, 5 buttons (down, up, back/escape, into sub-menu, enter). Four main menus: **STATUS** (read-only), **CONTROL**, **INTERFACE**, **SETTINGS**.
- LCD saver: 30 s, 2 min or OFF (SETTINGS → LCD SAVER). Press any key to wake it.
- In **AUTO** with a valid DMX signal, menus are partly disabled. **Unplug DMX to control locally.**
- USB terminal / diagnostics: needs the MDG Terminal package from MDG Service.

## Power
Manual quote: "Operating voltage: 100-250 VAC, single phase, 50/60 Hz, 1100-1480 W." "Power consumption: 1100 W @ 100 VAC, 1480 W @ 250 VAC." **No amp figure is published.** The values below are upper-bound estimates from the 1480 W maximum.

| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not published. ≤ 1480/120 = **12.3 A** (upper-bound estimate) | ≤ 1480/208 = 7.1 A (estimate) | ≤ 1480/230 = 6.4 A (estimate) |
| Power (W) | between 1100 and 1480 | ≤1480 | ≤1480 |
| Max power-link (manufacturer) | No thru power | — | — |
| **Max per 20 A circuit** (16 A continuous) | floor(16/12.3)=**1** (give it its own circuit) | floor(16/7.1)=2 (estimate). **Plan 1** with lights on the same circuit | — |

- Input range / auto-ranging: 100–250 VAC, single phase. **Ground required.**
- Power cable spec in the manual: 1.5 mm² (14 AWG), 3-wire, 90 °C copper.
- Connectors: IEC C19 inlet per OFL ⚠️ (fill in from the fixture). Fuse: not stated in the manual.
- **Heater trick from the manual:** if one heater cartridge has failed (HEATER error), running it on **100–130 VAC** gets you through temporarily.

## Data & addressing
- Connectors: 5-pin XLR DMX in/out, RJ45, USB-B.
- Protocols: DMX512-A, RDM (E1.20). Ethernet node built by Pathway: Art-Net, Pathport, Strand ShowNet, ETC Net2/Net3, sACN.
- DMX map (5 ch):

| Ch | Function | Values |
|---|---|---|
| 1 | Unit | 0–127 OFF · 128–255 ON (starts the heat cycle) |
| 2 | Mode | 0–127 HAZE · 128–255 FOG |
| 3 | Output | 0–255 = minimum to maximum pressure |
| 4 | Haze/Fog on | 0–127 OFF · 128–255 ON |
| 5 | External fan | 0–255 speed |

- Set the address: **INTERFACE → DMX ADDR** (1–508).
- Comm mode: **INTERFACE → COMM.** = AUTO / LOCAL / DMX / ETHERNET.
  - AUTO: DMX if a signal is present, otherwise local. Loss of DMX = holds the last values.
  - DMX: DMX only. **Loss of DMX = automatic shutdown.**
  - ETHERNET: set the universe with **INTERFACE → UNIV No** (1–128). Configure with Pathport Manager 5.2+. Pathport nodes default to 10.x.x.x / 255.0.0.0.
- RDM: start address, device label, identify (LCD flashes), comm mode, LCD saver, plus MDG custom PIDs.
- Saved to EEPROM: comm mode, DMX address, device label, universe name, units, LCD saver.
- Haze pressure range 3–30 psi, fog 5–40 psi (CONTROL → PRES HAZE / PRES FOG).

## Rigging & hardware
- **Never install overhead** (standalone). Keep **2 m from people** and from open flame. Clearance 1 m on the sides, 2 m in front.
- Touring rack: hangs under truss with **3 Doughty T57100-series cheeseborough clamps** (manual quotes a safety factor of about 8). **Never above the audience.** Stack max **2 high** with 3 half-couplers (T57000).
- Rack: 4 casters (2 braked), gas bottles 150–200 mm (6–8") diameter, max 915 mm (36") tall.
- Weight: standalone 23 kg (50 lb). Touring loaded about 120 kg (265 lb).
- **Lock the tool drawer with its quick-release pin** for transport or rigging.
- Gas inlet (standalone): 1/4" male JIC 37° flare. Fluid: 3/8" OD plastic tube. Max gas input 2500 psi (17.2 MPa).

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Regulator to CO2 bottle | Regulator nut with **nylon or Teflon washer** (required) | TBD – check on next show (wrench size) |
| Gas line to generator | 1/4" JIC 37° flare | TBD – check on next show |
| Fan mount | Quick-release pins + handwheels | Hand |
| Covers | TBD – check on next show | TBD – check on next show |

- **CO2 and N2 regulators use different bottle threads.** Use the right one.

## Optics & consumables
- **Fluid: MDG Neutral Fog Fluid only.** Other fluid voids the warranty and can damage the unit. 20 L jug.
- Fluid use: Haze 55 mL/h at 30 psi, 12 mL/h at 10 psi. Fog 1 L/h at 40 psi, 0.5 L/h at 10 psi.
- Gas use: Haze 0.35 kg/h at 30 psi, 0.15 kg/h at 10 psi. Fog 1.16 kg/h at 40 psi, 0.44 kg/h at 10 psi.
- Run time on 2 × 9 kg bottles + 20 L: Haze **50 h** at 30 psi / **120 h** at 10 psi. Fog 15 h at 40 psi / 41 h at 10 psi.
- Particle size 0.5–0.7 µm. Fog output 85 m³/min (3000 ft³/min) in fog mode at full pressure.
- **Swap a gas bottle while running:** close the bottle → close the rack ball valve → swap → open the bottle → open the ball valve.

## Error codes
STATUS → STATE = FAIL, then STATUS → ERROR. The last 5 errors are in STATUS → LAST ERR. The LCD flashes in a FAIL state.

| Code / message | Meaning | Fix |
|---|---|---|
| REFILL (code C) | Couldn't fill the internal reservoir in time | Jug empty? Filtered end of the line submerged? Line connected and not leaking? Jug vent open? |
| P. LOW (code 7) | Couldn't reach operating pressure | Open the bottles **and** the rack 1/4-turn ball valves. Check the gauge. Look for a leaking or frozen line. **Siphon CO2 bottle?** Check STATUS → PRESSURE |
| P. HIGH (code 8) | Pressure too high with the gas inlet closed | Solenoid fault, transducer fault, partly clogged heater, or **liquid (siphon) CO2**. Restart and test both modes for several minutes |
| HEATER (code 6) | Heater not ramping (timeout) | Restart and watch STATUS → STATE "xx% HEAT". If % doesn't rise, a cartridge has failed. **Run on 100–130 VAC as a temporary fix** if one cartridge is out. Call service |
| T. HIGH (code 4) | Heating module overtemp | Usually electronic. Restart, then call service |
| T. SAF (code 5) | The two heater sensors disagree | Sensor or electronics fault. Restart, then call service |
| PCB HIGH (code D) | Internal electronics too hot | Clear the vents, move it to shade or a cooler spot, restart |
| WD RESET (code E) | Software watchdog reset | Restart. Call service if it repeats |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Won't switch on | Power cord or breaker | Check the cord at both ends and the breaker (1480 W load) |
| No haze but no FAIL | Not READY yet (about 8 min), Unit not ON, or wrong comm mode | Check STATUS → STATE. Send Ch1 ≥128 **and** Ch4 ≥128. Check COMM mode and address |
| Can't control from the buttons | In DMX or AUTO with a signal present | Unplug DMX or set COMM → LOCAL |
| Shuts down when the DMX cable is pulled | COMM = DMX (by design) | Use AUTO if you want it to hold the last values |
| Pathport shows "OFFLINE" | Not in ETHERNET mode, or the Embedded RDM ID doesn't match the DEV ID | Set COMM → ETHERNET. Match the IDs |
| LCD shows garbage | RF or static scrambled the LCD | Wait 30 s for the LCD saver, then press a key. If it doesn't clear, restart |
| Takes up to 2 min at power-up before anything happens | Refilling the internal reservoir | Normal |
| 10 s pause switching FOG → HAZE | Purge between modes | Normal (HAZE → FOG is instant) |

## Maintenance
- Daily: check fluid and gas for the day.
- Weekly: inspect the rack for bends or cracks.
- Monthly: clean the exterior with a damp sponge and mild soap. Inspect all fluid and gas lines and fittings for leaks.
- "Requires no preventive maintenance" beyond that, per the manual. APS (Automatic Purging System) cleans the heater after every fog-off.
- Firmware: USB A-to-B cable to a Windows PC during the 4-second "Testing BootLoad" window at power-up. Get the package from MDG Service.

## Road notes (community)
- No forum notes gathered (search budget ran out).

## Sources
- [MDG theONE User Guide Rev A/f, Nov 2016](https://mdgfog.s3.amazonaws.com/uploads/docs/theONE-User-Guide-Rev-Af.pdf). Read in full. Source for everything above unless noted: power, DMX map, menus, warm-up, errors, gas, fluid, rigging, specs, maintenance.
- [Open Fixture Library: mdg/theone-atmospheric-generator.json](https://github.com/OpenLightingProject/open-fixture-library/blob/master/fixtures/mdg/theone-atmospheric-generator.json): IEC C19 power inlet (community), RDM model ID.
- [GDTF MDG@theONE Release 1.0 (Lampy-Paperwork mirror)](https://github.com/Ai-Lampy/Lampy-Paperwork/tree/main/gdtf/fixtures/mdg): 5-ch mode confirmation.
