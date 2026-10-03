---
title: "Generic 2-lite / 4-lite DWE Blinder (Molefay type)"
manufacturer: "Generic (Mole-Richardson Molefay and clones)"
model: "2-lite / 4-lite DWE blinder"
aliases: ["blinder", "2-lite", "4-lite", "2 lite", "4 lite", "molefay", "mole fay", "dwe blinder", "audience blinder", "2-cell", "4-cell", "8-lite"]
type: "blinder"
light_source: "Tungsten PAR36 DWE lamps, 650 W 120 V each (2 or 4 per fixture)"
ip_rating: null
weight_lb: null
weight_kg: null
dimensions: null
power:
  input: "120 V lamps. Wired EITHER in parallel for 120 V OR in series pairs for 208/240 V. READ THE FIXTURE LABEL"
  connector_in: "Varies by rental house"
  connector_out: ""
  watts_max: 2600
  amps_120v: 10.83     # 2-lite wired for 120 V (2 x 5.42 A per lamp). A 4-lite on 120 V is 21.7 A: 2 circuits.
  amps_208v: null
  amps_230v: null
  link_max_120v: null
  link_max_208v: null
  link_max_230v: null
  per_20a_120v: 1      # 2-lite. A 4-lite on 120 V does NOT fit one 20 A circuit.
  per_20a_208v: null
  fuse: ""
dmx:
  connectors: "None — fed from a dimmer"
  protocols: []
  modes: []
menu_password: null
firmware:
  latest_known: null
  checked: null
  check_on_fixture: null
  methods: []
  interface: null
  software: null
  file_type: null
  download: null
tools: []
verification: "community"
last_updated: "2026-10-03"
---

# Generic 2-lite / 4-lite DWE Blinder (Molefay type)

> **2AM CARD** — the stuff you need first
> - **FIRST: read the label or wiring.** Each DWE lamp is **650 W at 120 V**. A blinder is wired **either** with lamps in **parallel for 120 V** **or** in **series pairs for 208/240 V**.
>   - **A parallel (120 V) blinder on 208 V gives each lamp 208 V. Lamps flash out and can burst.**
>   - A series (240 V) blinder on 120 V just runs dim (each lamp gets 60 V). Safe, but wrong.
> - **Amps per lamp at 120 V:** 650 ÷ 120 = **5.42 A**. Tungsten is resistive, so W ÷ V is exact enough.
> - **Per 20 A circuit (16 A continuous):**
>   - 2-lite, 120 V parallel: 10.8 A → **1 per circuit**.
>   - **4-lite on 120 V is 21.7 A. It does NOT fit one 20 A circuit.** It needs 2 circuits or 2 dimmer channels.
>   - 2-lite, series pair on 240 V: 5.42 A. On 208 V: **≤5.42 A** (lamps are under-voltage) → **2 per circuit** at 208 V.
>   - 4-lite, series pairs on 208/240 V: ≤10.8 A → **1 per circuit**.
> - **Dimmer:** a 2.4 kW channel takes a 2-lite (1,300 W) but **not** a 4-lite (2,600 W).

## Identity
- What crews call it: 2-lite, 4-lite, molefay, DWE blinder, audience blinder.
- Fixture library / profile names: generic dimmer channel(s). GDTF "Generic@2-lite_Blinder" and "Generic@4-lite_Blinder" (community; "2x/4x DWE 650W 120V", 1ch or 2ch modes).
- **Variants and how to tell them apart (the part that matters):**
  - **120 V parallel wiring:** every lamp across 120 V. Common on US rigs fed from 120 V dimmers ⚠️ general knowledge.
  - **Series-pair wiring for 208/240 V:** two 120 V lamps in series per circuit. The EU community GDTF models the 4-lite this way: two Schuko feeds at 220–240 V, **1,300 W each** (= 2 × 650 W lamps in series per feed).
  - **Number of cables:** a 4-lite commonly has 2 feeds (2 lamps each) so it can be split across 2 circuits or dimmer channels ⚠️ general knowledge. Count the tails.
  - Lamp type: **DWE** = 650 W 120 V PAR36, about 3200 K (general knowledge). **FAY** = the 5000 K dichroic version (general knowledge). Check the lamp code.

## Passwords, menu locks & hidden menus
- None. Conventional fixture.

## Power
All figures computed from lamp ratings with Ohm's law (resistive load, PF = 1). No manufacturer electrical table was found.

| | 120 V | 208 V | 230/240 V |
|---|---|---|---|
| Current per lamp, parallel 120 V wiring | **5.42 A** (650/120) | **DO NOT** | **DO NOT** |
| Current per series pair (2 lamps) | Runs at half voltage, dim | **≤5.42 A** (each lamp sees about 104 V, so it draws less than rated) | **5.42 A** (1300/240) |
| 2-lite total | 10.83 A (parallel) | ≤5.42 A (series) | 5.42 A (series) |
| 4-lite total | **21.7 A** (parallel), needs 2 circuits | ≤10.83 A (2 series pairs) | 10.83 A (2 series pairs) |
| **Max per 20 A circuit** (16 A) | 2-lite: floor(16/10.83)=**1** · 4-lite: **0** (split across 2 circuits, 1 feed each) | 2-lite: floor(16/5.42)=**2** · 4-lite: floor(16/10.83)=**1** | — |

- At 208 V a series pair of 120 V lamps is under-voltage (about 104 V each). Output is lower and warmer than on 240 V. That's expected, not a fault ⚠️ general tungsten behavior.
- Inrush: cold tungsten inrush is high. Many blinders snapping to full together on non-dim circuits can trip breakers. Preheat a few percent if they're on dimmers (general knowledge).
- Dimmer loading: 2.4 kW dimmer = one 2-lite (1,300 W). A 4-lite (2,600 W) needs 2 dimmer channels or a 5 kW+ dimmer (general knowledge).

## Data & addressing
- None on the fixture. Patch the dimmer channel(s). GDTF 4-lite offers 1ch (all lamps) or 2ch (lamp pairs).

## Rigging & hardware
- Yoke with C-clamp or truss clamp (general knowledge). Molefays often have per-lamp tilt or swivel (general knowledge).
- Weight: community GDTF lists 6.4 kg for its generic 2-lite/4-lite model ⚠️ placeholder, not a real product weight. Not found, fill in from the fixture.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Lamp change | TBD – check on next show | TBD – check on next show |
| Lamp terminals | TBD – check on next show | TBD – check on next show |
| Yoke / clamp | TBD – check on next show | TBD – check on next show |
| Omega bracket | n/a | n/a |

## Optics & consumables
- Lamp: DWE 650 W 120 V PAR36 (general knowledge, confirmed by the community GDTF description). Beam: wide flood, set by the lamp (general knowledge).
- **Never mix a 240 V lamp into a series pair** or mix lamp types in a series string. The voltage splits unevenly and one lamp overdrives (general electrical knowledge).

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| — | No electronics | — |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| **Two lamps out together** on a series-wired unit | One lamp in the series pair failed, which opens the circuit for both | Replace the dead lamp. Test each lamp for continuity |
| All lamps very dim | Series-wired (240 V) unit plugged into 120 V | Move to 208/240 V, or swap for a parallel-wired unit |
| Lamps flash and die on power-up | Parallel (120 V) unit plugged into 208 V | **Stop.** Swap the lamps, check the wiring, move to 120 V |
| Breaker trips | 4-lite on one 120 V circuit (21.7 A) | Split onto 2 circuits or dimmers |
| One lamp much brighter than its pair | Mismatched lamps in a series pair | Use identical lamps |

## Maintenance
- Check the lamp terminal connections and the high-temp wiring for heat damage (general knowledge).

## Firmware
- **None.** Lamps and wiring only. No electronics to update.

## Road notes (community)
- Nothing forum-confirmed found (search budget ran out). The series-wiring trap is standard industry knowledge, also flagged in [reference/power-math.md](../../reference/power-math.md).

## Sources
- [GDTF Generic@4-lite_Blinder and Generic@2-lite_Blinder (community, Lampy-Paperwork mirror)](https://github.com/Ai-Lampy/Lampy-Paperwork/tree/main/gdtf/fixtures/generic): "4x DWE 650W 120V", two 220–240 V feeds at 1,300 W each (series pairs), 1ch/2ch modes.
- All amp figures: Ohm's law from the 650 W / 120 V lamp rating (resistive load). Not a manufacturer table.
