---
title: "Martin MAC Quantum Wash"
manufacturer: "Martin"
model: "MAC Quantum Wash"
aliases: ["quantum", "quantum wash", "mac quantum", "mac quantum wash"]
type: "wash"
light_source: "LED (configuration not confirmed)"
ip_rating: null
weight_lb: null
weight_kg: null
dimensions: null
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
  fuse: null
dmx:
  connectors: null
  protocols: []
  modes: []
menu_password: null
firmware:
  latest_known: "2.2.0"
  checked: "2026-10-03"
  check_on_fixture: "INFORMATION menu"
  methods: ["USB stick", "DMX + Martin Uploader (legacy)", "DMX + Martin Companion Cable"]
  interface: "None for USB stick; Martin Companion Cable P/N 91616091 for DMX"
  software: "Martin Companion (older: Martin Uploader)"
  file_type: ".BANK"
  download: "martin.com/en-US/firmware or Martin Companion"
tools: []
verification: "unverified"
last_updated: "2026-10-03"
---

# Martin MAC Quantum Wash

> ⚠️ **Thin page.** The session's web-search budget ran out before this fixture was researched. HARMAN lists the MAC Quantum range under **discontinued Martin products**.

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** Not found — fill in from the fixture
> - **Power:** Not found. **Read the rating label.**
> - **DMX:** Quantum Wash modes not found. (The sister **Quantum Profile** is Basic 19 / Extended 27 ch in QLC+. Not the Wash.)
> - **Display shows "MMER"?** HARMAN has a help article titled "MMER Code on MAC Quantum". What the code means was not captured. Look it up when you have signal, or check the Quantum troubleshooting sheet (Sources).
> - **Won't move?** Transport locks: Not found — TBD – check on next show
> - **Tools:** TBD – check on next show

## Identity
- What crews call it: "Quantum", "Quantum Wash" (general knowledge).
- Fixture library / profile names: Quantum Wash is not in Open Fixture Library or QLC+. QLC+ only has the **MAC Quantum Profile** (Basic 19, Extended 27; 23.2 kg; 750 W listed).
- Variants: MAC Quantum Profile and Quantum Wash (general knowledge).

## Passwords, menu locks & hidden menus
- Not found — fill in from the fixture. See [Martin common](./_martin-common.md).

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | Not found | Not found | Not found |
| Power (W) | Not found | Not found | Not found |
| Max power-link (manufacturer) | Not found | Not found | Not found |
| **Max per 20 A circuit** (16 A continuous) | Not found | Not found | — |

## Data & addressing
- Not found — fill in from the fixture.

## Rigging & hardware
- Not found — fill in from the fixture.

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | TBD – check on next show | TBD |
| Gobo / effects module access | n/a (wash) | — |
| Lens / front glass | TBD – check on next show | TBD |
| Omega bracket | TBD – check on next show | TBD |

## Optics & consumables
- Not found.

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|
| MMER | HARMAN help article exists ("MMER Code on MAC Quantum"). Meaning not captured. | Not found — see the HARMAN article / Quantum troubleshooting PDF |

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|
| — | — | — |

## Maintenance
- Recalibrate / fan / filter cleaning: Not found.

## Firmware
- Installed version — where to see it on the fixture: **INFORMATION** menu (user guide: the new version shows there after an update).
- Latest known version (date checked) and where to download it: **2.2.0** latest found (2026-10-03, martin.com firmware listing via search summary). martin.com/en-US/firmware or downloaded inside Martin Companion.
- What you need: USB stick (easiest), **or** a Windows PC with Martin Uploader (the manual's method) / Martin Companion + Companion Cable (P/N 91616091) on the DMX line. Companion support for this model is not confirmed for this fixture ⚠️ unverified.
- Update steps (USB stick, from the MAC Quantum Wash user guide):
  1. Get the **.BANK** file (martin.com product support page, or export it from Martin Companion). Read the release notes.
  2. Copy it to the **root directory** of a USB stick (format not stated in the manual; FAT32 is the safe guess ⚠️ unverified).
  3. **Disconnect the data link** (console) from the fixture.
  4. Insert the stick in the fixture's USB socket. If nothing happens, go to **SERVICE → USB**.
  5. **AVAILABLE FIRMWARE** appears — scroll to the version, press Enter, confirm with Enter (Menu exits without installing).
  6. Let it install and reboot. Don't power off and don't pull the stick while it is updating.
  7. Remove the stick, check the version in the **INFORMATION** menu, reconnect the data link.
- Updating a whole rig: USB = one fixture at a time. Over DMX with Uploader/Companion: limit not found. Keep one model per line (⚠️ unverified, general practice).
- If it fails or bricks mid-update: MAC Quantum and Encore have a **bootloader switch** inside the base on the main display PCB. **Hold it while powering on** to force bootloader mode, then reinstall firmware by USB or DMX (HARMAN help center). Exact switch position on the board: ⚠️ unverified.
- Release notes worth knowing: Not captured. Firmware can add or renumber DMX modes — re-check your console patch/profile after updating.

## Road notes (community)
- None found.

## Sources
- [HARMAN help: MMER Code on MAC Quantum](https://help.harmanpro.com/discontinued-products-martin/mmer-code-on-mac-quantum): shows the MMER code exists, and that the range sits under discontinued Martin products (title and URL only).
- [MAC Quantum Series Troubleshooting Display Messages and Symptoms (PDF)](https://adn.harmanpro.com/site_elements/executables/3910_1526136285/MAC_Quantum_Series_Trouble_Shooting_original.pdf): the official troubleshooting sheet. Contents not captured. **Download it when you have signal.**
- [QLC+ Martin-MAC-Quantum-Profile.qxf](https://github.com/mcallegari/qlcplus/tree/master/resources/fixtures/Martin): sister Profile modes, weight and wattage only.
- [Martin firmware page](https://www.martin.com/en-US/firmware) — latest firmware versions and update methods (via web-search summary, checked 2026-10-03)
- [MAC Quantum Wash user guide, firmware installation (manualslib p.16)](https://www.manualslib.com/manual/1053770/Martin-Mac-Quantum-Wash.html?page=16) — USB .BANK procedure, INFORMATION menu, Uploader alternative
- [HARMAN help: Bootloader button on MAC Quantum and MAC Encore series](https://help.harmanpro.com/en_US/general-mac-encore-inquiries/bootloader-button-on-mac-quantum-and-mac-encore-series) — bootloader switch location and use
