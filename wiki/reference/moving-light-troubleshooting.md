---
title: "Moving Light Troubleshooting (any brand)"
aliases: ["won't move", "no pan", "no tilt", "lamp won't strike", "no light", "fixture resets", "error", "homing", "recalibrate", "overheating", "fan", "flicker on camera"]
type: reference
last_updated: "2026-10-03"
---

# Moving Light Troubleshooting (any brand)

Start here when you don't know the fixture well or its page doesn't cover the problem. Every fixture page has its own **Symptom → fix** table.

> **2AM CARD: the five checks that fix most problems**
> 1. **Transport / pan-tilt locks** engaged? (won't move, pan/tilt error)
> 2. **Address and mode** match the console patch? (does the wrong thing, or nothing)
> 3. **Shutter / dimmer / lamp** — is the shutter channel open and the lamp actually on? (moves but no light)
> 4. **Reset it** — reset from the menu or power-cycle and let it home with nothing touching it.
> 5. **Swap it** — swap address/cable with the next fixture. If the problem moves with the cable, it's the cable; if it stays with the fixture, it's the fixture.

## Won't move / pan or tilt error
| Check | Detail |
|---|---|
| Transport locks | Pan lock (base) and tilt lock (yoke arm). Engaged locks cause pan/tilt errors at homing. Unlock, then reset. |
| Something blocking movement | Safety cable through the yoke, cable ties, truss, a neighbour fixture, case foam left in. |
| Pan/tilt disabled or inverted in the menu | Many fixtures have "Pan/Tilt invert", "swap", "disable", or a movement-blackout setting. Check fixture settings. |
| Console | Position values parked, a position preset at home, wrong mode, pan/tilt on fine-only channels. |
| Mechanical | Slipping belt (moves but loses position), dead motor/encoder (error at reset). After a hard truck ride, recalibrate. |
| Feedback / position correction | If "position correction" or "feedback" is on, the fixture fights to return when bumped. Error messages after a knock are normal — reset. |

## Moves but no light
| Fixture type | Check |
|---|---|
| All | Dimmer channel up? **Shutter/strobe channel at "open"?** Many shutters are closed at 0. |
| All | Colour wheel at a dark/blackout slot? Iris closed? Framing shutters all the way in? |
| Discharge lamp | Lamp-on command sent? "Auto lamp on" setting? **Hot restrike**: most discharge lamps need 3–10 min to cool before they'll strike again. |
| Discharge lamp | Lamp hours past rated life, lamp door/cover microswitch open (fixture won't strike with a cover off), igniter/ballast fault message. |
| LED | Thermal derate / overtemp shutdown, "LED driver" error, dimmer curve or "max output" limit in the menu. |

## Fixture resets, douses, or homes by itself
1. **Control/reset channel** — a preset, effect or cue is sending a value on the fixture's control channel. Check the control channel in the programmer/sheet.
2. **Power** — loose powerCON, link chain over its limit, voltage sag on long runs. Watch the display: if it reboots, it lost power.
3. **Thermal** — fixture overheating (dirty filters, blocked vents, direct sun, hot truss position).
4. **DMX** — bad data can be read as random control values. Terminate and check cables.

## Overheating / fans
- Clean filters and fans (compressed air / blower, hold the fan still while blowing it).
- Check fan mode in the menu: "silent/studio" modes reduce cooling and the fixture dims itself to compensate.
- Fixtures in direct sun or in a hot grid derate output.
- IP65 fixtures in heat: some have temperature-based output limits — check the fixture page.

## Flicker on camera / video
- Most LED fixtures have a **PWM / refresh frequency** setting. Raise it (e.g. high-speed or 25 kHz modes) when a camera sees flicker or rolling bars.
- Discharge fixtures don't have this (but the dimmer/shutter mechanics can show stepping).
- Strobes: match strobe rate to camera frame rate if needed.

## After a truck ride / random weirdness
- Reset/recalibrate from the menu (usually "Reset", "Home", "Calibration" under a service or test menu).
- Check for loose gobos, colour wheel out of index (wrong colour shown), stuck flags.
- Look and listen during homing: grinding, a wheel not spinning, or a module that doesn't move points to the fault.

## Factory reset — use carefully
- Clears address, mode, and any user settings. Write down the address/mode/settings first.
- Usually in a "Service", "Default" or "Factory" menu, sometimes passcode-protected — see the fixture page.

## Swap-out decision (on a show day)
Swap the fixture if: it fails reset twice, has a repeating motor/encoder error, smells hot/burnt, has a cracked lens, or a lamp/ballast fault you can't clear. Tag it with the symptom and error code for the shop.

## Sources
- General moving-light service practice — general knowledge. Fixture-specific errors and menu paths are on each fixture page.
