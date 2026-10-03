---
title: "ETC Source Four LED Series 3 Lustr X8"
manufacturer: "ETC"
model: "Source Four LED Series 3 Lustr X8"
aliases: ["lustr x8", "series 3 lustr", "s4 led series 3", "source four led series 3", "s4 lustr x8", "lustr 3", "s4 led"]
type: "ellipsoidal"
light_source: "LED, 90 Lumileds LUXEON C and CZ emitters, 8-color (Lustr X8)"
ip_rating: null
weight_lb: 19.6
weight_kg: 8.9
dimensions: "216 x 298 x 700 mm (OFL community data, lens tube not stated)"
power:
  input: null
  connector_in: null
  connector_out: null
  watts_max: 340
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
    - { name: "Direct", channels: 12 }
    - { name: "Expanded", channels: 11 }
    - { name: "Studio", channels: 7 }
    - { name: "HSIC", channels: 8 }
    - { name: "3ch RGB", channels: 3 }
    - { name: "1ch (Intensity)", channels: 1 }
menu_password: null
firmware:
  latest_known: "v1.3.0"
  checked: "2026-10-03"
  check_on_fixture: null
  methods: ["USB drive (Local Settings > USB > Update Firmware)", "UpdaterAtor + ETC USB/DMX Gadget or Net3 gateway"]
  interface: null
  software: "ETC UpdaterAtor (optional; Windows only)"
  file_type: null
  download: "etcconnect.com (Source Four LED Series 3 Fixture Software release notes) or UpdaterAtor"
tools: []
verification: "community"
last_updated: "2026-10-03"
---

# ETC Source Four LED Series 3 Lustr X8

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** Not found. Fill in from the fixture.
> - **Power:** amps not found, no manufacturer electrical table seen. Community data lists **340 W** max (OFL) ⚠️. Read the label for amps and the link limit before linking.
> - **DMX modes (ETC official GDTF v1.3.0):** Direct 12 · Expanded 11 · Studio 7 · HSIC 8 · 3ch RGB 3 · 1ch 1.
> - **Lens tubes:** same Source Four lens tubes, 5–90° (ETC GDTFs exist for 5/10/14/19/26/36/50/70°).
> - **Tools:** TBD – check on next show.

## Identity
- What crews call it: Lustr X8, Series 3, S4 LED Series 3.
- Fixture library / profile names: GDTF "ETC@S4_Series_3_Lustr_X8_<deg>Deg" (official ETC file v1.3.0, one per lens tube). OFL "Source Four LED Series 3 Lustr X8" (RDM model ID 1281).
- Variants and how to tell them apart: the Series 3 range also includes Daylight HDR and others. **Series 2 Lustr** (7-color, 60 emitters) is older and has a different mode list. See [source-four-led-series-2-lustr.md](source-four-led-series-2-lustr.md). Check the label on the back of the body.

## Passwords, menu locks & hidden menus
- Default passcode and how to enter it: not found. Fill in from the fixture.
- Service / factory menu access: not found.
- How to unlock a locked display: not found.

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found | Not found | Not found |
| Power (W) | 340 max (OFL community data) ⚠️ | 340 max ⚠️ | 340 max ⚠️ |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | Not found — read the label | Not found | — |

- Input range / auto-ranging: not found. Fill in from the fixture.
- Connectors in / out: not found.
- Fuse: not found.
- ⚠️ Rough sanity check only, not a manufacturer figure: 340 W ÷ 120 V ≈ 2.8 A before power factor. Use the label amps.

## Data & addressing
- Connectors: 5-pin XLR (OFL).
- Protocols: DMX, RDM (OFL lists an RDM model ID).
- DMX modes / footprints (ETC official GDTF v1.3.0, cross-checked against OFL; OFL lists "Intensity" for 1ch and doesn't list HSIC):

| Mode | Ch | Layout |
|---|---|---|
| Direct | 12 | Int, Deep Red, Red, Amber, Lime, Green, Cyan, Blue, Indigo, Strobe, Dimmer Curve, Fan |
| Expanded | 11 | Int, CCT, Tint, Tuning, Mix, R, G, B, Strobe, Dimmer Curve, Fan |
| Studio | 7 | Int, CCT, Tint, Tuning, Strobe, Dimmer Curve, Fan |
| HSIC | 8 | Hue (16-bit, 2 ch), Sat, Int, CCT, Strobe, Dimmer Curve, Fan |
| 3ch RGB | 3 | R, G, B |
| 1ch | 1 | Intensity |

- Set the address (menu path, button by button): not found. Fill in from the fixture.
- Battery / unpowered addressing: not found.
- Factory reset: not found.

## Rigging & hardware
- Bracket / omega type: yoke and C-clamp (general knowledge).
- Safety cable point: around the yoke and pipe.
- Weight: **8.87 kg** (ETC official GDTF, 26° tube), 8.9 kg (OFL).

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD – check on next show |
| Gobo / effects module access | TBD – check on next show | TBD – check on next show |
| Lens / front glass | TBD – check on next show | TBD – check on next show |
| Yoke / clamp | TBD – check on next show | TBD – check on next show |

## Optics & consumables
- Source: 90 LUXEON C and CZ LEDs (OFL), 14,214 lm (OFL, conditions not stated) ⚠️.
- Color system: 8-color additive mix (Deep Red, Red, Amber, Lime, Green, Cyan, Blue, Indigo), per the Direct mode channel list.
- Gobos: uses the Source Four pattern slot, A/B size (general knowledge, same optical train as the tungsten Source Four ⚠️ unverified).
- Lens tubes: 5–90° (OFL), the same as the tungsten Source Four.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| Not found | — | Fill in from the fixture |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| Fixture looks different from its neighbors in the same color | Different mode or dimmer curve, or Series 2 mixed with Series 3 | Match the mode and dimmer curve channel. Check the label for Series 2 vs 3 |
| Fan noise | Fan channel at default | Use the Fan channel (last channel in most modes) to set a quiet fan mode ⚠️ check the values in the ETC manual |

## Maintenance

## Firmware
- Installed version — where to see it on the fixture: menu path not found in the sources read.
- Latest known version (date checked) and where to download it: **v1.3.0** ("Source Four LED Series 3 Fixture Software v1.3.0 Release Note" on etcconnect.com, latest found, checked 2026-10-03). Get the file from etcconnect.com or through UpdaterAtor.
- What you need: a **USB drive** with the firmware file on it. The USB port is on the rear of the fixture. Or use UpdaterAtor with a Gadget or Net3 gateway (ETC's general method) ⚠️ not confirmed in the Series 3 manual.
- Update steps (USB, from the Series 3 user manual via search summary):
  1. Download the firmware from etcconnect.com (or export it from UpdaterAtor) and save it to a USB drive.
  2. Insert the drive in the **USB port on the rear** of the fixture.
  3. Press **Menu** and turn the **Intensity encoder** to **Local Settings > USB > Update Firmware**.
  4. Turn the encoder to the firmware file and **press the encoder** to start.
  5. The fixture copies the files (progress meter), verifies them (ETC logo shown), then installs. Don't cut power during any of this.
- Updating a whole rig: USB is one fixture at a time. For many fixtures, use UpdaterAtor over DMX or Net3 ⚠️ batch limit not found.
- If it fails or bricks mid-update: no recovery mode found. Contact ETC.
- Release notes worth knowing: not read. The official GDTF file is also v1.3.0. Check the release note for mode changes before updating a patched rig.

## Road notes (community)
- Nothing confirmed found. Search budget ran out before forum queries could run.

## Sources
- [ETC official GDTF "S4 Series 3 Lustr X8 26Deg" v1.3.0 (mirror in Ai-Lampy/Lampy-Paperwork)](https://github.com/Ai-Lampy/Lampy-Paperwork/tree/main/gdtf/fixtures/etc): mode list and footprints, 8.87 kg weight.
- [Open Fixture Library: source-four-led-series-3-lustr-x8.json](https://github.com/OpenLightingProject/open-fixture-library/blob/master/fixtures/etc/source-four-led-series-3-lustr-x8.json): 340 W, 8.9 kg, dimensions, LED count, lumens, RDM model ID. OFL links the ETC manuals at etcconnect.com DownloadAsset id=10737510600 and 10737506242, which couldn't be fetched.
- [Source Four LED Series 3 User Manual v1.0.0 (Grand Stage mirror)](https://www.grandstage.com/assets/images/S4_LED_Series3_v100_UserManual_revB.pdf): found in search but not readable (egress blocked). Get the electrical table and menu paths from here.
- [ETC Source Four LED Series 3 user manual, Update Firmware page (ManualsLib p.30)](https://www.manualslib.com/manual/2296552/Etc-Source-Four-Led-3-Series.html?page=30): USB update menu path and steps (search summary)
- [Source Four LED Series 3 Fixture Software v1.3.0 Release Note](https://www.etcconnect.com/workarea/DownloadAsset.aspx?id=10737515440): latest version found (title only)
- [ETC support: Updating ColorSource Par to v1.3.0](https://support.etcconnect.com/ETC/Fixtures/ColorSource/PAR/Updating_ColorSource_Par_to_v1.3.0): UpdaterAtor, interface list, opto-splitter warning, bootloader step (search summary)
