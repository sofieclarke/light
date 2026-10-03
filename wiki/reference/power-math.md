---
title: "Power Math Cheat Sheet"
aliases: ["power", "amps", "how many per circuit", "208v", "120v", "link", "jump power", "power linking", "breaker"]
type: reference
last_updated: "2026-10-03"
---

# Power Math Cheat Sheet

> **2AM CARD**
> - **Plan on 16 A per 20 A circuit** (80% continuous rule). Same at 120 V and 208 V.
> - **Fixtures per circuit = floor(16 ÷ amps per fixture)**, then **cap it at the manufacturer's link limit**. Treat the link limit as the **total** on one feed.
> - **Chauvet:** the PXL Bar manuals say **never exceed 12 A on a single circuit**. Plan Chauvet gear at 12 A, not 16, unless its fixture page says otherwise.
> - Use the **amps from the manual's electrical table**, not watts ÷ volts.
> - **Never put a 120 V-only device on 208 V** (tungsten blinders/PARs with 120 V lamps, many hazer heaters, Edison-only stuff). It has to say **100–240 V** or **auto-ranging**.
> - Lots of LED fixtures that **can't be linked at 120 V** (link limit 0) **can be linked at 208 V**.

## 1. The rules

| Rule | Why |
|---|---|
| 20 A breaker → plan **16 A** continuous | NEC treats show loads as continuous (3 h+). Breakers run at 100% get hot and nuisance-trip. |
| Use the manual's **current (A)** figure at *your* voltage | LED/switch-mode supplies have a power factor below 1, so watts ÷ volts underestimates amps. |
| Obey the **manufacturer's link limit** even if the math allows more | Limit comes from internal wiring and the thru connector rating, not the breaker. |
| Obey the **connector rating** | powerCON TRUE1 is rated 16 A (IEC) / 20 A (UL). Edison 5-15 = 15 A. |
| Obey any **manufacturer per-circuit cap** | Chauvet manuals: "never exceed 12 A on a single circuit". |
| The lowest of breaker ÷ 16 A, manufacturer cap, link limit and connector rating wins | — |

## 2. The formulas

```
Single-phase amps:    I = W ÷ (V × PF)        (PF ≈ 0.95–0.99 for modern LED, use the manual's A if given)
Per circuit:          N = floor(16 ÷ I)
With a link limit L:  N = min(floor(16 ÷ I), L)        ← L = total units on one feed (the safe reading)
Chauvet:              N = min(floor(12 ÷ I), L)        ← Chauvet's 12 A per-circuit rule
Three-phase amps:     I_line = W_total ÷ (√3 × V_LL × PF)     (V_LL = 208 on a 120/208 wye)
```

**How manuals count links:** read the link limit as the **total number of fixtures on one feed**, not "extra fixtures after the first". Chauvet's numbers only make sense that way: with "never exceed 12 A on a single circuit", the PXL Bar 16 at 208 V is 3 × 3.821 A = 11.5 A ✓, but 4 would be 15.3 A ✗. Each fixture page says how its manual words the limit.

## 3. Worked examples

| Fixture (from manual) | 120 V | 208 V |
|---|---|---|
| **Chauvet COLORado PXL Bar 16**: 6.60 A @120 V, 3.821 A @208 V, link 0 @120 V / 3 @208 V, 12 A cap | floor(16÷6.6)=2, but link limit is **0** → **1 per feed (no linking)** | floor(12÷3.821)=3, link limit 3 → **3 per circuit** (a 20 A breaker would hold 4 — don't) |
| **Chauvet COLORado PXL Bar 8**: 3.497 A @120 V, 2.013 A @208 V, link 3 / 5, 12 A cap | floor(12÷3.497)=3, link 3 → **3** | floor(12÷2.013)=5, link 5 → **5** |
| Hypothetical 3.0 A @120 / 1.8 A @208, no stated limit | floor(16÷3.0)=**5** | floor(16÷1.8)=**8** (then check TRUE1 = 16 A ✓) |

See each fixture page's **Power** table for its number, and [the comparison table](../comparison.md) for everything side by side.

## 4. 120 V vs 208 V — what's actually happening

- A US show service is usually **120/208 V 3-phase wye**. Hot-to-neutral = 120 V. Hot-to-hot (two different phases) = **208 V**.
- A 208 V "circuit" uses **two hots** (2-pole breaker), and a ground. No neutral is needed by the fixture.
- Same wattage at 208 V draws about **58%** of the current it draws at 120 V (120 ÷ 208), so you fit roughly 1.7× more fixtures per 20 A circuit.
- **208 V is not 240 V.** A fixture rated "200–240 V" works on 208; a fixture rated "220–240 V only" (some EU-spec gear) may brown out. Most modern movers are 100–240 V auto-ranging.
- Distros: most concert distros give you 120 V on Edison/socapex and 208 V on TRUE1 / L6-20 / dedicated 208 socapex. **Know which outputs are which on the distro you're handed** — label check before plugging in.

### Things that must NOT go on 208 V
- Tungsten fixtures with 120 V lamps (Source Four with HPL 575/115 or /120, PAR 64 with 120 V lamps, molefay/DWE blinders wired for 120 V) — instant lamp death, possible fire.
- Hazers/foggers rated 120 V only (heater block).
- Anything with only an Edison plug unless its label says 100–240 V.
- 2-lite/4-lite blinders: some are wired **in series** for 208/240 V. Read the fixture label, never assume. See the blinder page.

## 5. Inrush and power-up

- Switch-mode supplies pull a big current spike for a few milliseconds at power-on. One fixture is fine; **8+ on one breaker switched at once can trip it** even if running current is well under 16 A.
- Symptoms: breaker trips **only at power-up**, never during the show.
- Fixes: power up circuit by circuit (distro breakers one at a time), use distros with staggered/sequenced power-up, or reduce fixtures per circuit. Some breakers (thermal-magnetic "B curve") trip on inrush more easily than "C/D curve" ones.

## 6. Neutral & harmonics (why 3-phase LED rigs get weird)
- LED and switch-mode loads create harmonic currents that **add up on the shared neutral** instead of cancelling. On a big 120 V LED rig the neutral can carry more current than any phase.
- Concert feeders and distros are built for this (oversized neutral) but improvised house power often isn't. Hot neutral or warm cam-loks = call the house electrician.
- Running fixtures at 208 V (hot-to-hot) avoids the neutral entirely, which is one reason touring rigs prefer it.

## 7. Phase balancing
- Spread fixtures evenly across X/Y/Z (A/B/C). Add up amps per leg on the distro meter or by math.
- Rule of thumb: keep the legs within ~10–20% of each other.
- A 208 V fixture loads **two legs** at once (its full current shows up on both).

## 8. Quick reference: circuits & connectors

| Connector | Voltage | Rating | Notes |
|---|---|---|---|
| NEMA 5-15 (Edison) | 120 V | 15 A | Household. Don't load a 15 A plug to 16 A. |
| NEMA 5-20 | 120 V | 20 A | T-slot neutral. |
| NEMA L5-20 | 120 V | 20 A | Twist-lock. |
| NEMA L6-20 | 208/240 V | 20 A | Twist-lock, 2 hots + ground. Common 208 V fixture circuit. |
| NEMA L21-30 | 120/208 V 3φ | 30 A | 3 hots + neutral + ground. Feeds small distros. |
| powerCON TRUE1 / TRUE1 TOP | 100–250 V | 16 A IEC / 20 A UL | Locking, can be (dis)connected under load. Fixture in/out. |
| powerCON (blue in / grey out) | 100–250 V | 20 A | **Not** rated to disconnect under load. Older fixtures. |
| Socapex 19-pin | 120 V (or 208 V on some multis) | 6 × 20 A circuits | See [connectors & pinouts](connectors-and-pinouts.md). |
| Cam-lok (16 series) | feeder | 400 A typical | Connect **ground → neutral → hots**, disconnect in reverse. Qualified people only. |

## 9. Sanity checks before you plug in
1. Is the fixture rated for the voltage on this circuit? (label on the fixture)
2. Amps per fixture at this voltage × fixtures ≤ 16 A (≤ 12 A for Chauvet)?
3. Fixtures on this feed ≤ manufacturer's link limit (counted as the total on the feed)?
4. Is the circuit really 20 A? (some house circuits are 15 A → plan on 12 A)
5. Power up in stages.

## Sources
- General electrical practice (NEC 80% continuous-load rule, 120/208 V wye relationships) — general knowledge; confirm local code with the venue electrician.
- COLORado PXL Bar 16 / Bar 8 electrical figures and the 12 A rule: Chauvet user manuals, via web search (see [Bar 16](../fixtures/chauvet/colorado-pxl-bar-16.md), [Bar 8](../fixtures/chauvet/colorado-pxl-bar-8.md)).
