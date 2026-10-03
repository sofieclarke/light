---
title: "ETC Source Four"
manufacturer: "ETC"
model: "Source Four (tungsten ellipsoidal)"
aliases: ["source four", "source 4", "s4", "leko", "ellipsoidal", "ers", "s4 leko", "source four ellipsoidal", "hpl leko"]
type: "ellipsoidal"
light_source: "HPL tungsten-halogen lamp, 575 W or 750 W (120 V, 115 V or 230 V versions)"
ip_rating: null
weight_lb: 14
weight_kg: 6.4
dimensions: null
power:
  input: "Set by the lamp installed: 115 V / 120 V HPL on US rigs, 230 V HPL in EU. Fed from a dimmer, not a constant feed"
  connector_in: "Pigtail — varies by rental house (stage pin / Edison / twist-lock / powerCON). Check the plug"
  connector_out: ""
  watts_max: 750
  amps_120v: null
  amps_208v: null
  amps_230v: null
  link_max_120v: null
  link_max_208v: null
  link_max_230v: null
  per_20a_120v: 3
  per_20a_208v: null
  fuse: ""
dmx:
  connectors: "None — conventional fixture, controlled through a dimmer"
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
verification: "web-search"
last_updated: "2026-10-03"
---

# ETC Source Four

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** None. No electronics in the fixture, it runs off a dimmer.
> - **Power:** Tungsten is a resistive load, so amps = watts ÷ volts. 575 W ÷ 120 V = 4.8 A → **3 per 20 A circuit**. 750 W ÷ 120 V = 6.25 A → **2 per 20 A circuit**. **Never put 208 V on a 115 V or 120 V HPL lamp.** The lamp dies, and it can burst.
> - **Lamps:** HPL 575/115 and 575/120: 16,520 lm, 3250 K, 300 h. HPL 575/115X: 12,360 lm, 3050 K, 2,000 h. HPL 750/120: 21,900 lm, 300 h. The 750 long-life version: 16,400 lm, 1,500 h.
> - **Gobos:** **A size** (100 mm OD, 75 mm max image) or **B size** (86 mm OD, 64.5 mm image) in the pattern holder. **M size** (66 mm) is for the Source Four **Jr**, not the full Source Four.
> - **Lens tubes:** 5°, 10°, 14°, 19°, 26°, 36°, 50°, 70°, 90°.
> - **Tools:** TBD – check on next show. Usually a crescent/C-wrench for the yoke and clamp (general knowledge).

## Identity
- What crews call it: Source Four, S4, "leko" (US slang for any ellipsoidal), ERS.
- Fixture library / profile names (MA3, GDTF, Hog, Eos): it's patched as a dimmer channel, not a fixture profile. Eos/MA use the generic "Dimmer" or "Source Four" conventional type (general knowledge).
- Variants and how to tell them apart:
  - **Source Four** (full size): accepts A/B pattern holders and a drop-in iris (general knowledge).
  - **Source Four Jr**: smaller body, uses **M-size** gobos. Search result: "Size M, 66 mm OD, found in Source Four Jr" ⚠️ don't put A/B holders in a Jr.
  - **Source Four Zoom** (15–30°, 25–50°). These are separate fixtures (general knowledge).
  - **Source Four LED** (Series 2/3 Lustr etc.): separate pages. Same lens tubes, different body.
  - **Lamp is the variant that matters for power**: read the lamp label (HPL 575/115, 575/120, 750/120, or /230 in EU).

## Passwords, menu locks & hidden menus
- None. It's a conventional fixture with no electronics.

## Power
Tungsten lamps are resistive (PF = 1), so watts ÷ volts is a legitimate way to get current here. The manuals quoted for the LED fixtures don't apply. ETC doesn't publish an electrical table for the fixture body, so the numbers below are **computed from lamp wattage**.

| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | 575 W: 4.8 A · 750 W: 6.25 A (computed) | **DO NOT** with 115/120 V lamps | 575 W/230 V lamp: 2.5 A · 750 W/230 V lamp: 3.3 A (computed) |
| Power (W) | 575 or 750 (lamp) | — | 575 or 750 (lamp) |
| Max power-link (manufacturer) | n/a, no thru connector | n/a | n/a |
| **Max per 20 A circuit** (16 A continuous) | 575 W: floor(16/4.79)=**3** · 750 W: floor(16/6.25)=**2** | — | n/a (EU circuits are 16 A, so compute there) |

- Input range / auto-ranging: **none**. The voltage is set by the lamp. A 115 V lamp on 120 V runs slightly over-voltage and has a shorter life ⚠️ unverified (general knowledge of tungsten behavior).
- Connectors in / out: pigtail only, no thru. The plug type depends on the rental house (general knowledge).
- Fuse: none in the fixture. Protection comes from the dimmer or breaker.
- Inrush / power-up notes: a cold tungsten filament has a high inrush current (general knowledge). On a non-dim or relay circuit, many units snapping on at once can trip a marginal breaker. Preheat them to a low level if you can (general knowledge).
- **Dimmer channel loading (general knowledge):** a 2.4 kW dimmer carries 3 × 575 W (1,725 W) or 2 × 750 W (1,500 W) with room to spare. 4 × 575 W (2,300 W) fits 2.4 kW on paper but is more than 16 A continuous at 120 V (19.2 A). Don't do it.

## Data & addressing
- Connectors: none.
- Protocols: none. Patch the **dimmer** channel.
- DMX modes / footprints: n/a (1 dimmer channel).
- Set the address: on the dimmer rack/pack, not on the fixture.
- Factory reset: n/a.

## Rigging & hardware
- Bracket / omega type and clamp spacing: standard yoke with a C-clamp (general knowledge).
- Fasteners: yoke knob and clamp bolt (general knowledge).
- Safety cable point: around the yoke and pipe (general knowledge).
- Mounting orientations allowed: any. ETC states lamp-orientation limits for HPL in its manual. Not found, so fill in from the fixture.
- Transport / pan-tilt locks: none.
- Weight / dimensions: **14 lb (6.4 kg) for the 36°**, from the ETC 36° spec sheet search result. Other lens tubes differ. EDLT lens tube alone is 4.5 lb (2.1 kg) per ETC EDLT spec sheet search result. Dimensions: not found, fill in from the fixture.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Lamp cap / lamp change | TBD – check on next show | TBD – check on next show |
| Shutter barrel rotate | Barrel rotation knob/lock (general knowledge) | Hand |
| Lens tube swap | Lens tube lock knob (general knowledge) | Hand |
| Yoke / C-clamp | Bolt | TBD – check on next show (usually a C-wrench) |

## Optics & consumables
- Source / lamp, lamp life (from search results quoting lamp retailers and ETC lamp listings):

| Lamp | Watts | Volts | Lumens | CCT | Life |
|---|---|---|---|---|---|
| HPL 575/115 | 575 | 115 | 16,520 | 3250 K | 300 h |
| HPL 575/120 | 575 | 120 | 16,520 | 3250 K | 300 h |
| HPL 575/115X (extended life) | 575 | 115 | 12,360 | 3050 K | 2,000 h |
| HPL 750/120 | 750 | 120 | 21,900 | 3250 K | 300 h |
| HPL 750/120 long life | 750 | 120 | 16,400 | 3050 K | 1,500 h |
| HPL 750/230 (EU) | 750 | 230 | not found | 3050 K | not found |

  - **115 vs 120 V lamps:** use 120 V lamps on 120 V service. A 115 V lamp on 120 V is brighter but has a shorter life ⚠️ unverified (general knowledge).
  - **750 W**: check that your dimmer and circuit loading still work (2 per 20 A, not 3). A ControlBooth thread compares 575 vs 750 use: [HPL 575 or 750 in your Source4?](https://www.controlbooth.com/threads/hpl-575-or-750-in-your-source4.5345/). Only the title was seen in search, so read the thread itself for its content.
  - Never touch the quartz envelope with bare fingers (general knowledge).
- Color system: gel frame in the front color slot (general knowledge). Size: not found, fill in from the fixture.
- Gobo / pattern sizes (search results quoting gobo makers):

| Size | OD | Max image | Pattern holder (X × Y) | Fits |
|---|---|---|---|---|
| **A** | 100 mm | 75 mm | 3.25" × 3.75" | Source Four |
| **B** | 86 mm | 64.5 mm | 2.75" × 3.75" | Source Four |
| **M** | 66 mm | — | 2.12" × 2.75" | Source Four **Jr** |

  - B size gives a sharper, more even image for logos and text. A size is fine for breakups (gobo-maker guidance).
  - A glass pattern holder is also available for the Source Four.
- Prism / frost / zoom / iris / shutters: 4 shutters on a **rotating shutter assembly**. ETC literature commonly quotes **±25°** rotation ⚠️ unverified, not confirmed in this research. Drop-in iris goes in the pattern slot (general knowledge).
- Lens tubes / field angles: **5°, 10°, 14°, 19°, 26°, 36°, 50°, 70°, 90°**, from ETC Source Four documentation via search. EDLT (enhanced definition) tubes come in 19/26/36/50°.
- Gobo / module change procedure: slide the pattern holder into the gate slot with the gobo's emulsion/printed side facing the lamp ⚠️ unverified (general practice). Watch for heat: the gate is hot.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| — | No electronics, no codes | — |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| No light | Lamp blown, dimmer not patched or no level, pigtail or two-fer fault | Check the lamp, check dimmer output with a tester, swap cable |
| Hot spot / uneven field | Lamp alignment out | Adjust the lamp-cap alignment knob for a flat or peak field (general knowledge) ⚠️ |
| Soft gobo / can't sharpen | Lens barrel not run in or out far enough, or wrong gobo size | Run the barrel; check A vs B vs M |
| Lamps keep dying | Over-voltage (115 V lamp on high line), hand-touched quartz, or rough handling hot | Use 120 V lamps; handle with gloves or cloth; let it cool before striking |
| Breaker trips on a non-dim circuit | Too many lamps × inrush | Stay at ≤3 × 575 W or ≤2 × 750 W per 20 A |

## Maintenance
- Recalibrate / reset procedure: n/a. Re-peak the lamp after every lamp change (general knowledge).
- Fan / filter cleaning: no fan. Clean the reflector and lens with the lamp cold (general knowledge).

## Firmware
- **None.** The tungsten Source Four is a lamp, a reflector and a lens with no electronics, so there's nothing to update. The dimmer or the console does the dimming. (Source Four LED models do have firmware. See their pages.)

## Road notes (community)
- ControlBooth has a thread on 575 vs 750 W lamp choice. Only the title appeared in search, so read the thread: [HPL 575 or 750 in your Source4?](https://www.controlbooth.com/threads/hpl-575-or-750-in-your-source4.5345/).
- ControlBooth on gobo size: [Source Four Gobo Size?](https://www.controlbooth.com/threads/source-four-gobo-size.15059/). Content not seen.
- ⚠️ Fill in from the road: lamp-cap screw type, pattern holder slot behavior when hot.

## Sources
- Search summary citing lamp retailers: [EiKO HPL575/115 at B&H](https://www.bhphotovideo.com/c/product/1141798-REG/eiko_hpl575_115v_hpl_source_four_lamp.html), [GoKnight HPL575/120](https://goknight.com/etc-hpl575-120-hpl-575w-120v-300hr-lamp-for-source-four-ellipsoidal-series/), [GoKnight HPL575/115X](https://goknight.com/etc-hpl575-115x-hpl-575w-115v-2000hr-lamp-for-source-four-ellipsoidal-series/), [HPL 750 standard](https://www.filmandvideolighting.com/hpl-750-watt-120-volt-120v-750w-hpl-bulb-lamp-arri-etc-source-four.html), [HPL 750 long life](https://www.filmandvideolighting.com/hpl-750-watt-120-volt-120v-750w-hpl-bulb-lamp-arri-etc-source-four-long-life.html), [Ushio HPL 750/230](https://www.filmandvideolighting.com/ushio-hpl-ceramic-base-750w-hpl-source-4-bulb-lamp-long-life-220v-240v-230v-3050k.html): lamp lumens, CCT, life.
- [Machine Artist: Gobo sizes](https://www.machineartist.com/blog/gobo-sizes/), [Goboman: What size gobo holder fits a Source Four](https://goboman.com/what-size-gobo-holder-fits-a-etc-source-four/), [ETC Size A pattern holder at B&H](https://www.bhphotovideo.com/c/product/435139-REG/ETC_7060A1013_Size_A_Pattern_Holder.html): A/B/M sizes and pattern holder dimensions.
- [ETC Source Four documentation](https://www.etcconnect.com/Products/Entertainment-Fixtures/Source-Four/Source-Four/Documentation.aspx) and [Source Four 36° spec sheet](https://www.etcconnect.com/workarea/DownloadAsset.aspx?id=10737460423), via search summary: nine field angles, 36° weight of 14 lb / 6.4 kg. [EDLT spec sheet (BMI mirror)](https://shop.bmisupply.com/Resources/en/ItemDocuments/38110032/BMI.ETC.S4%2026%C2%B0%20ED%20Lens%20Tube.pdf): EDLT tube weight of 4.5 lb / 2.1 kg.
- Note: the ETC site couldn't be fetched directly (egress blocked). The spec sheets weren't read in full.
