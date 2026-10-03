---
title: "Connectors & Pinouts"
aliases: ["socapex", "soca", "true1", "powercon", "xlr", "ethercon", "pinout", "l6-20", "l21-30", "cam lok", "camlock", "edison"]
type: reference
last_updated: "2026-10-03"
---

# Connectors & Pinouts

> **2AM CARD**
> - **Socapex:** circuit *n* = hot pin (2n–1), neutral pin (2n), ground pin (12+n). Pin 19 unused.
> - **DMX XLR:** 1 = shield, 2 = Data –, 3 = Data +.
> - **TRUE1:** locking, OK to unplug under load. **Blue/grey powerCON: NOT** OK to unplug under load (it arcs).
> - **etherCON** = RJ45, T568B.

## Socapex 19-pin (6-circuit multicable)

| Circuit | Hot | Neutral | Ground |
|---|---|---|---|
| 1 | 1 | 2 | 13 |
| 2 | 3 | 4 | 14 |
| 3 | 5 | 6 | 15 |
| 4 | 7 | 8 | 16 |
| 5 | 9 | 10 | 17 |
| 6 | 11 | 12 | 18 |
| — | Pin 19: unused (rarely the cable screen) | | |

- Each circuit is normally a separate 20 A breaker on the distro (120 V).
- **208 V on soca:** some distros put 208 V on soca by feeding the "neutral" pin from a second phase. Those multis/breakouts must be clearly labelled. Plugging a 120 V breakout into a 208 V soca output puts 208 V on your Edison sockets. **Always check the distro labelling.**
- A breakout (fan-out) gives you 6 Edison / TRUE1 / L6-20 tails. Breakout tails are often labelled 1–6; match them to the distro breaker numbers on your paperwork.
- Some shops wire non-standard socas (pin 19, 208 V, or swapped grounds). If a breakout behaves strangely, meter it.

## powerCON family

| Type | Colour | Rating | Disconnect under load? | Notes |
|---|---|---|---|---|
| powerCON TRUE1 / TRUE1 TOP | Black | 16 A IEC / 20 A UL | **Yes** | The modern standard. TRUE1 TOP is IP65 (outdoor fixtures). |
| powerCON (NAC3) power-in | Blue | 20 A | **No** | Twist to lock, pull the latch. Unplugging under load arcs and pits the contacts. |
| powerCON (NAC3) power-out | Grey | 20 A | **No** | Thru to next fixture. |

- **Look-alikes:** some cheap fixtures/cables use TRUE1-compatible clones. Mostly fine, but they can be tighter/looser — if a fixture loses power when bumped, suspect the connector.
- Seetronic powerKON TRUE = TRUE1-compatible (Chauvet and others ship it).
- IP65 fixtures: unused outputs need their **sealing caps** on, or the IP rating is void.

## NEMA (US)

| Connector | Voltage | Amps | Pins |
|---|---|---|---|
| 5-15 (Edison) | 120 V | 15 A | Hot (short flat), neutral (tall flat), ground (round) |
| 5-20 | 120 V | 20 A | Neutral slot is T-shaped |
| L5-20 | 120 V | 20 A | Twist-lock |
| L6-20 | 208/240 V | 20 A | Twist-lock, 2 hots + ground, **no neutral** |
| L6-30 | 208/240 V | 30 A | Twist-lock |
| L21-30 | 120/208 V 3φ | 30 A | X, Y, Z, N, G |
| Stage pin (2P&G) | 120 V | 20 A | Theatre standard; middle pin is ground |

## Cam-lok (feeder)
- 5 single-pole connectors per feeder: **Green = ground, White = neutral, Black/Red/Blue = X/Y/Z** (US colour code).
- **Connect: Ground → Neutral → Hots. Disconnect: Hots → Neutral → Ground.** Only with the disconnect OFF. Feeder tie-in is a job for qualified people.
- Double neutrals are common on concert feeders (harmonics from LED loads).

## DMX

| Pin | 5-pin | 3-pin |
|---|---|---|
| 1 | Shield/common | Shield/common |
| 2 | Data – | Data – |
| 3 | Data + | Data + |
| 4 | Data 2 – (unused) | — |
| 5 | Data 2 + (unused) | — |

Terminator: 120 Ω, ¼ W across pins 2–3. More in [DMX troubleshooting](dmx-troubleshooting.md).

## etherCON / RJ45 (T568B)

| Pin | Colour |
|---|---|
| 1 | White/orange |
| 2 | Orange |
| 3 | White/green |
| 4 | Blue |
| 5 | White/blue |
| 6 | Green |
| 7 | White/brown |
| 8 | Brown |

Use shielded Cat5e/Cat6 for touring. Max 100 m copper run between switches.

## Sources
- Socapex pinout: [Wikipedia — Socapex](https://en.wikipedia.org/wiki/Socapex), [Entertaining Safety — Socapex](https://entertainingsafety.com/knowledge-base/multi-cable-19-pin-socapex-entertainment-lighting/), [Stagecraft Production Service socapex diagrams](https://www.stagecraftproductionservice.com/socapex/index.htm) (via web search).
- powerCON, NEMA, cam-lok, DMX and T568B details — general knowledge; confirm ratings on the connector/manufacturer datasheet.
