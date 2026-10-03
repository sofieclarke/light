---
title: "ETC ColorSource PAR"
manufacturer: "ETC"
model: "ColorSource PAR"
aliases: ["colorsource par", "cs par", "colorsource", "etc par", "color source par"]
type: "par"
light_source: "LED, 40 Lumileds LUXEON Z, RGB-L (red, green, blue, lime)"
ip_rating: null
weight_lb: 8.3
weight_kg: 3.77
dimensions: "203 x 310 x 240 mm (OFL / QLC+ community data)"
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
  fuse: ""
dmx:
  connectors: "5-pin XLR (community data)"
  protocols: ["DMX", "RDM"]
  modes:
    - { name: "5ch (default)", channels: 5 }
    - { name: "6ch Direct", channels: 6 }
    - { name: "3ch RGB", channels: 3 }
    - { name: "1ch", channels: 1 }
menu_password: null
firmware:
  latest_known: "v4.0.2 (CPU3) / v3.0.0 (CPU2)"
  checked: "2026-10-03"
  check_on_fixture: "Shown on the display while the fixture boots"
  methods: ["UpdaterAtor + ETC USB/DMX Gadget or Gadget II", "UpdaterAtor + ETC USB/DMX Service Cable", "UpdaterAtor + ETC Net3 / DMX-RDM gateway", "Fixture-to-fixture push (same CPU type only)"]
  interface: "ETC USB/DMX Gadget or Gadget II (4267A1001 / 4267A1004)"
  software: "ETC UpdaterAtor (Windows only)"
  file_type: null
  download: "Inside UpdaterAtor (Setup Versions → Download All Latest Software), or etcconnect.com"
tools: []
verification: "community"
last_updated: "2026-10-03"
---

# ETC ColorSource PAR

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** Not found. Fill in from the fixture.
> - **Power:** amps not found. **Community sources disagree on watts: OFL says 90 W, QLC+ says 120 W** ⚠️. Read the label.
> - **DMX modes:** **5ch default** (Int, R, G, B, Strobe) · 6ch Direct (Int, R, G, B, Lime, Strobe) · 3ch RGB · 1ch Intensity.
> - **Tools:** TBD – check on next show.

## Identity
- What crews call it: ColorSource PAR, CS PAR.
- Fixture library / profile names: GDTF "ETC@ColorSource_Par" (community file). OFL "ColorSource PAR" (RDM model ID 513). QLC+ "ETC ColorSource PAR".
- Variants: **ColorSource PAR Deep Blue** (different emitter mix, its own OFL profile). ColorSource PAR V Zoom and ColorSource Spot are separate fixtures.

## Passwords, menu locks & hidden menus
- Not found. Fill in from the fixture.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found | Not found | Not found |
| Power (W) | 90 (OFL) / 120 (QLC+) ⚠️ | — | — |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | Not found — read the label | Not found | — |

- Input range / connectors / fuse: not found. Fill in from the fixture.

## Data & addressing
- Connectors: 5-pin XLR (OFL, QLC+).
- Protocols: DMX, RDM (OFL lists an RDM model ID).
- DMX modes (OFL, QLC+ and GDTF all agree):

| Mode | Ch | Layout |
|---|---|---|
| 5ch (default) | 5 | Intensity, Red, Green, Blue, Strobe |
| 6ch Direct | 6 | Intensity, Red, Green, Blue, Lime, Strobe |
| 3ch RGB | 3 | Red, Green, Blue |
| 1ch | 1 | Intensity (of a preset color) |

- Set the address: not found. Fill in from the fixture.

## Rigging & hardware
- Yoke with C-clamp (general knowledge). Weight 3.77 kg (OFL/QLC+), 3.8 kg (GDTF).

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Yoke / clamp | TBD – check on next show | TBD – check on next show |
| Lens / front glass | TBD – check on next show | TBD – check on next show |
| Top / head covers | TBD – check on next show | TBD – check on next show |
| Omega bracket | TBD – check on next show | TBD – check on next show |

## Optics & consumables
- 40 LUXEON Z LEDs, 3,039 lm (OFL) ⚠️. Beam listed as 14.5° in OFL ⚠️ unverified. ETC sells diffusion/lens accessories (general knowledge).

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Not found | — | Fill in from the fixture |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| No lime / colors look thin | Fixture is in 5ch mode (no Lime channel) | Use 6ch Direct if you want Lime control |
| Units in 1ch mode show the wrong color | 1ch drives a preset color | Set the preset on the fixture, or use 5ch |

## Maintenance
- Not found.

## Firmware
- Installed version — where to see it on the fixture: the display shows the software version while the fixture boots (search summary of ETC material). Early units showed 1.0.0, 1.0.1 or 1.1.0.
- Latest known version (date checked) and where to download it (checked 2026-10-03). **It depends on the CPU board inside**, and each board only accepts its own software line:
  - **CPU3** fixtures: **v4.x**. Latest found **v4.0.2** (released 11 Dec 2023). It fixes the loud fan noise on CPU3 units running v4.0.1.
  - **CPU2** fixtures: **v3.x** only. Latest found **v3.0.0** (release note Dec 2021).
  - Original CPU: v1.x. ETC's install guide is titled "v1.7/v3.0/v4.0", which suggests **v1.7** for the original board ⚠️ unverified.
  - To tell them apart, see ETC's ["Identify a CPU2 ColorSource PAR"](https://support.etcconnect.com/ETC/Fixtures/ColorSource/PAR/Identify_a_CPU2_ColorSource_PAR) article. Files come through UpdaterAtor or etcconnect.com.
- What you need: a **Windows** PC (7/8/10 listed; Mac not supported) running **UpdaterAtor**, plus one of these: the ETC USB/DMX Service Cable, the ETC USB/DMX **Gadget or Gadget II** (part numbers 4267A1001 / 4267A1004), or an ETC Networked DMX/RDM Gateway.
- Update steps (ETC support article, via search summary):
  1. Read the release note for the version you're loading.
  2. Install UpdaterAtor and connect the PC to the Gadget, service cable or gateway, then connect that to the fixture's DMX line.
  3. **Remove every non-ETC opto-splitter, opto-isolator and DMX repeater from the line.** ETC warns that sending firmware through one can leave the fixture with no firmware, needing repair at ETC.
  4. In UpdaterAtor press **Setup Versions** and check you have the ColorSource Bootloader and ColorSource software you need. If not, press **Download All Latest Software**.
  5. Run the update from UpdaterAtor.
  - Coming from **below v1.3.0**: update the **bootloader first** (ColorSource Family Bootloader 1.3.0.9.0.17 or higher), then the firmware.
- Updating a whole rig: UpdaterAtor works over the DMX line or the network. A fixture can also **push its software to other fixtures**, but only to fixtures with the **same CPU type**. A wrong-CPU fixture just won't accept the code. Don't mix CPU types on a line you're pushing to.
- If it fails or bricks mid-update: if the fixture is left without firmware (e.g. after updating through a non-ETC splitter), ETC says it may need to go back to ETC. No field recovery mode found.
- Release notes worth knowing: v4.0.2 fan-noise fix for CPU3 (above). Check the release note for mode changes before updating fixtures that are already patched.

## Road notes (community)
- Nothing confirmed found. Search budget ran out.

## Sources
- [Open Fixture Library: colorsource-par.json](https://github.com/OpenLightingProject/open-fixture-library/blob/master/fixtures/etc/colorsource-par.json): modes, 90 W, 3.77 kg, dimensions, LED type, RDM ID. OFL links ETC manuals at etcconnect.com DownloadAsset id=10737484145 and 10737494638, which couldn't be fetched.
- [QLC+ ETC-ColorSource-PAR.qxf](https://github.com/mcallegari/qlcplus/blob/master/resources/fixtures/ETC/ETC-ColorSource-PAR.qxf): modes, **120 W** (disagrees with OFL), 3.77 kg.
- [GDTF ETC@ColorSource_Par (community, Lampy-Paperwork mirror)](https://github.com/Ai-Lampy/Lampy-Paperwork/tree/main/gdtf/fixtures/etc): modes, 3.8 kg.
- [ETC support: Updating ColorSource Par to v1.3.0](https://support.etcconnect.com/ETC/Fixtures/ColorSource/PAR/Updating_ColorSource_Par_to_v1.3.0): UpdaterAtor, interface list, opto-splitter warning, bootloader step (search summary)
- [ETC support: CPU Variants in ColorSource and S4WRD Color Fixtures](https://support.etcconnect.com/ETC/Fixtures/ColorSource/Software_and_Programming/CPU_Variants_in_ColorSource_and_S4WRD_Color_Fixtures), [CPU2 Alternate Processor](https://support.etcconnect.com/ETC/Fixtures/ColorSource/PAR/CPU2_Alternate_Processor_for_ColorSource_Par), [Identify a CPU2 ColorSource PAR](https://support.etcconnect.com/ETC/Fixtures/ColorSource/PAR/Identify_a_CPU2_ColorSource_PAR): CPU-to-software mapping, same-CPU push rule (search summary)
- [ETC support: ColorSource PAR CPU3 loud fan noise](https://support.etcconnect.com/ETC/Fixtures/ColorSource/PAR/ColorSource_PAR_CPU3_loud_fan_noise): v4.0.2, 11 Dec 2023 (search summary)
- [ETC ColorSource PAR Installation Guide v1.7/v3.0/v4.0 (voxel.org mirror)](https://voxel.org/pdf/technical-manual/cspar.pdf), [ColorSource PAR documentation](https://www.etcconnect.com/Products/Entertainment-Fixtures/ColorSource-PAR/Documentation.aspx): software lines, v3.0.0 release note date (search summary)
- [ControlBooth: Updating ETC ColorSource PAR Firmware](https://www.controlbooth.com/threads/updating-etc-colorsource-par-firmware.51468/): version shown at boot (community, search summary)
