---
title: "ETC Source Four LED Series 2 Lustr"
manufacturer: "ETC"
model: "Source Four LED Series 2 Lustr"
aliases: ["lustr 2", "series 2 lustr", "s4 led series 2", "source four led series 2", "lustr+", "s4 lustr"]
type: "ellipsoidal"
light_source: "LED, 60 7-color Lumileds LUXEON Rebel emitters"
ip_rating: null
weight_lb: 18.3
weight_kg: 8.3
dimensions: "338 x 615 x 631 mm (OFL community data)"
power:
  input: null
  connector_in: null
  connector_out: null
  watts_max: 171
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
  connectors: "5-pin XLR (OFL community data)"
  protocols: ["DMX", "RDM"]
  modes:
    - { name: "Direct", channels: 10 }
    - { name: "HSI", channels: 6 }
    - { name: "HSIC", channels: 7 }
    - { name: "RGB", channels: 6 }
    - { name: "Studio", channels: 6 }
    - { name: "HSI Plus 7", channels: 15 }
    - { name: "HSIC Plus 7", channels: 16 }
    - { name: "RGB Plus 7", channels: 15 }
menu_password: null
firmware:
  latest_known: "v1.8.2"
  checked: "2026-10-03"
  check_on_fixture: "Shown on the display at power-up"
  methods: ["UpdaterAtor + ETC USB/DMX Gadget or Gadget II", "UpdaterAtor + ETC Net3 gateway (One, Two or Four Port)"]
  interface: "ETC USB/DMX Gadget or Gadget II (4267A1001 / 4267A1004), or a Net3 gateway"
  software: "ETC UpdaterAtor (Windows only)"
  file_type: null
  download: "Inside UpdaterAtor, or the Source Four LED Series 2 documentation page on etcconnect.com"
tools: []
verification: "community"
last_updated: "2026-10-03"
---

# ETC Source Four LED Series 2 Lustr

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** Not found. Fill in from the fixture.
> - **Power:** amps not found. Community data lists **171 W** max (OFL) ⚠️. Read the label.
> - **DMX modes (OFL community data):** Direct 10 · HSI 6 · HSIC 7 · RGB 6 · Studio 6 · HSI+7 15 · HSIC+7 16 · RGB+7 15.
> - **Not the same as Series 3 Lustr X8.** The mode lists differ, so check the label before patching.
> - **Tools:** TBD – check on next show.

## Identity
- What crews call it: Lustr 2, Series 2, S4 LED.
- Fixture library / profile names: OFL "Source Four LED Series 2 Lustr" (short name EtcSF2Lustr).
- Variants: Series 2 Daylight HD and Tungsten HD use the same body with different arrays. Series 3 Lustr X8 has its own page: [source-four-led-series-3-lustr-x8.md](source-four-led-series-3-lustr-x8.md).

## Passwords, menu locks & hidden menus
- Not found. Fill in from the fixture.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found | Not found | Not found |
| Power (W) | 171 max (OFL) ⚠️ | 171 max ⚠️ | 171 max ⚠️ |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | Not found — read the label | Not found | — |

- Input range, connectors, fuse: not found. Fill in from the fixture.

## Data & addressing
- Connectors: 5-pin XLR (OFL).
- DMX modes (OFL; "?" marks a channel OFL lists without a usable name):

| Mode | Ch | Layout |
|---|---|---|
| Direct | 10 | Red, Lime, Amber, Green, Cyan, Blue, Indigo, Intensity, Strobe, Fan |
| HSI | 6 | Hue, Hue fine, Sat, Int, Strobe, Fan |
| HSIC | 7 | Hue, Hue fine, Sat, Int, Strobe, Fan, Color Point |
| RGB | 6 | R, G, B (emulated), ?, Strobe, Fan |
| Studio | 6 | Int, Color Point, Tint, ?, Strobe, Fan |
| HSI Plus 7 | 15 | HSI block + Plus 7 control + 7 direct colors |
| HSIC Plus 7 | 16 | HSIC block + Plus 7 control + 7 direct colors |
| RGB Plus 7 | 15 | RGB block + Plus 7 control + 7 direct colors |

- Set the address, factory reset: not found.

## Rigging & hardware
- Yoke and C-clamp (general knowledge). Weight 8.3 kg (OFL).

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD – check on next show |
| Gobo / effects module access | TBD – check on next show | TBD – check on next show |
| Lens / front glass | TBD – check on next show | TBD – check on next show |
| Yoke / clamp | TBD – check on next show | TBD – check on next show |

## Optics & consumables
- 60 × 7-color LUXEON Rebel emitters, 8,667 lm (OFL) ⚠️. Lens tubes 5–90° (OFL).

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Not found | — | Fill in from the fixture |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Patched as X8 but colors are wrong | It's a Series 2, so the channel layout differs | Repatch with the Series 2 profile |

## Maintenance
- Not found.

## Firmware
- Installed version — where to see it on the fixture: shown on the display at power-up (search summary).
- Latest known version (date checked) and where to download it: **v1.8.2**, "Source Four LED & Selador Desire Fixtures v1.8.2" release note dated 02-2022 (latest found, checked 2026-10-03). It's listed on ETC's [Source Four LED Series 2 documentation page](https://www.etcconnect.com/Products/Entertainment-Fixtures/Source-Four-LED-Series-2/Documentation.aspx). UpdaterAtor downloads it for you.
- What you need: a **Windows** PC with **UpdaterAtor**, plus an ETC USB/DMX **Gadget or Gadget II**, or an ETC **Net3 One, Two or Four Port Gateway**. No USB port was found on this model.
- Update steps:
  1. Install UpdaterAtor and let it download the latest Source Four LED software (Setup Versions → Download All Latest Software).
  2. Connect the Gadget or gateway to the fixtures' DMX line.
  3. **Take every non-ETC opto-splitter, isolator and repeater out of the line** (ETC's warning for its fixture updates).
  4. Find the fixtures in UpdaterAtor and run the update. Full steps are in the UpdaterAtor Quick Guide (v4.4.0 found).
- Updating a whole rig: UpdaterAtor updates over the DMX line through a Gadget, or over the network through Net3 gateways. A batch limit wasn't found.
- If it fails or bricks mid-update: no field recovery mode found. ETC warns that a failed load through a non-ETC splitter can leave a fixture needing repair at ETC.
- Release notes worth knowing: **v1.8.1** (12-2019) added a **calibrated Direct mode** so Series 2 fixtures color-match each other in Direct mode. Older and newer units on different versions **won't match in Direct mode**, so put the whole rig on the same version (ETC support article).

## Road notes (community)
- Nothing confirmed found. Search budget ran out.

## Sources
- [Open Fixture Library: source-four-led-series-2-lustr.json](https://github.com/OpenLightingProject/open-fixture-library/blob/master/fixtures/etc/source-four-led-series-2-lustr.json): modes, 171 W, 8.3 kg, dimensions, LED count. OFL links the ETC manuals at etcconnect.com DownloadAsset id=10737483869 and 10737501163, which couldn't be fetched.
- [ETC Source Four LED Series 2 documentation](https://www.etcconnect.com/Products/Entertainment-Fixtures/Source-Four-LED-Series-2/Documentation.aspx): v1.8.2 (02-2022) and v1.8.1 (12-2019) release notes (search summary)
- [ETC support: New Series 2 fixtures don't match existing ones in Direct mode](https://support.etcconnect.com/ETC/Fixtures/Source_Four_LED/Series_2/My_New_Source_Four_LED_Series_2_Fixtures_Dont_Exactly_Match_My_Existing_Fixtures_in_Direct_Mode): calibrated Direct mode (search summary)
- [UpdaterAtor Quick Guide v4.4.0 (ControlBooth attachment)](https://www.controlbooth.com/attachments/updaterator_quickguide_v4-4-0_reva-pdf.15829/): Gadget and Net3 gateway update paths, version at power-up (search summary)
- [ETC Community: Source 4 series 2 Firmware](https://community.etcconnect.com/luminaires_fixtures/led-fixtures/f/source-four-led/53833/source-4-series-2-firmware): UpdaterAtor handles Source Four LED (search summary)
- [ETC support: Updating ColorSource Par to v1.3.0](https://support.etcconnect.com/ETC/Fixtures/ColorSource/PAR/Updating_ColorSource_Par_to_v1.3.0): UpdaterAtor, interface list, opto-splitter warning, bootloader step (search summary)
