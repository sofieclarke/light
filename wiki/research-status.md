---
title: "Research Status & To-Do"
type: reference
last_updated: "2026-10-03"
---

# Research Status & To-Do

First pass: 2026-10-03. Manufacturer sites and manual mirrors were blocked from the research environment, and web searches were capped at 200 for the session. Figures came from search results quoting the manuals, the manufacturers' own GitHub repositories (Chauvet firmware and parts lists, ETC's GDTF files), and community fixture libraries (Open Fixture Library, QLC+). Treat pages marked `community` or `unverified` as starting points.

## Solid pages (manual figures for power, passcode and DMX)
Chauvet Rogue Outcast 2X Wash, Outcast 1 BeamWash, Outcast 3 Spot, COLORado PXL Bar 16, PXL Bar 8, PXL Curve 12, Maverick MK3 Spot/Wash (no link limit) · Martin MAC Aura XB · GLP impression X4 Bar 20, JDC1 · MDG theONE (read in full) · Claypaky Sharpy (amps from a rental house) · Robe MegaPointe, Spiider (watts only, no amps)

## Biggest gaps
1. **Amps and link limits** are missing for most non-Chauvet fixtures. Robe, Claypaky and Elation manuals list watts or VA at 230 V. The service manuals or tech support have the full tables.
2. **Not started yet:** Ayrton (Perseo, Khamsin, Diablo, MagicDot-R, Cobra), Elation Fuze, Chorus Line 16 and an Elation blinder, SGM Q-7.
3. **Stubs / thin pages:** Chauvet Color STRIKE M, Strike Array 4, Maverick Force S Spot, Rogue R2X/R3 (no power data) · Robe BMFL Spot, Esprite, Forte, LEDBeam 150, Pointe, iFORTE · GLP X4/X4 S/X4 L, X5, FR10 Bar, JDC Line 1000, S350 · Martin Ultra Performance, Quantum Wash, Viper Profile modes · Claypaky B-EYE K20, Scenius Unico, Sharpy X Frame.
4. **Screw and bit sizes:** almost all TBD. Measure on real fixtures; nobody else has this.
5. **Error-code tables:** missing for most fixtures (manuals have them; search didn't surface them).
6. **Photos:** none yet (rear panels, omega brackets, transport locks, safety points, packed cases).
7. **Firmware:** every page has a Firmware section. Chauvet versions and release notes come straight from Chauvet's GitHub (solid). Martin, GLP, ETC, Elation and Astera versions come from search summaries. No version numbers found for Robe or Claypaky. Recovery steps are missing for most non-Chauvet fixtures.
8. **Road notes:** few forum or Reddit notes found. Add your own.

## Known conflicts to settle
- Chauvet link limits: this wiki reads them as the total on one feed (matches the 12 A cap). Confirm with Chauvet tech support.
- Maverick MK3 Spot: is 0920 the service code or the panel unlock? Sources disagree.
- Maverick Force S Spot link limit at 208 V: 4 or 5.
- Elation passcodes 050/011 come from other Proteus manuals; confirm on the Maximus and Hybrid.
- Robe 7623 is stated as line-wide but only seen in the Forte, T2, MegaPointe and Pointe manuals.
- Claypaky Sharpy lamp: Osram Sirius 190W+ (manual) vs Philips 5R (rental house).
- GLP X4 Bar 20 weight: 14.5 kg (manual) vs ~17 lb (press).

## To finish the job
Either raise the web-search limit or allow these domains in the environment's network settings, then rerun a verification pass: `chauvetprofessional.com`, `robe.cz`, `martin.com`, `help.harmanpro.com`, `claypaky.it`, `glp.de`, `elationlighting.com`, `ayrton.eu`, `etcconnect.com`, `manualslib.com`, `reddit.com`, `controlbooth.com`.
