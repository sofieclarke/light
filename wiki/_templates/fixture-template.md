---
# ---- Machine-readable block (the future app indexes this). Leave a field as null if unknown. ----
title: "Manufacturer Model"
manufacturer: ""
model: ""
aliases: []            # every name crews / consoles / rental houses use, lowercase: ["outcast 2x", "r2x"]
type: ""               # spot | profile | beam | hybrid | wash | beam-wash | batten | pixel-bar | strobe | blinder | ellipsoidal | par | effect | atmospheric
light_source: ""       # e.g. "LED 7x 40W RGBW", "Osram Sirius HRI 470W"
ip_rating: null        # e.g. IP20, IP65
weight_lb: null
weight_kg: null
dimensions: ""         # L x W x H, inches and mm
power:
  input: ""            # e.g. "100–240 VAC, 50/60 Hz, auto-ranging"
  connector_in: ""     # e.g. "Neutrik powerCON TRUE1"
  connector_out: ""
  watts_max: null
  amps_120v: null      # from the manual's electrical table, not watts/volts
  amps_208v: null
  amps_230v: null
  link_max_120v: null  # manufacturer's power-link limit
  link_max_208v: null
  link_max_230v: null
  per_20a_120v: null   # min( floor(16 / amps_120v), link_max_120v as TOTAL on one feed, any maker cap e.g. Chauvet 12 A ) — see reference/power-math.md
  per_20a_208v: null
  fuse: ""
dmx:
  connectors: ""       # e.g. "5-pin XLR in/out, etherCON in/out"
  protocols: []        # DMX, RDM, Art-Net, sACN, W-DMX, CRMX
  modes: []            # - { name: "Standard", channels: 24 }
menu_password: null    # e.g. "2323" — also note HOW to enter it in the body
firmware:
  latest_known: null   # newest version found, e.g. "V1.260610"
  checked: null        # date that version was checked, e.g. "2026-10-03"
  check_on_fixture: "" # menu path that shows the installed version
  methods: []          # e.g. ["USB stick", "DMX cable + UPLOAD 08", "Ethernet (Robe Uploader)", "RDM"]
  interface: null      # hardware needed, e.g. "Chauvet UPLOAD 08", "Robe Universal Interface", null if a USB stick is enough
  software: null       # PC/app software, e.g. "Chauvet Firmware Uploader", "ROBE Uploader", "Martin Companion"
  file_type: null      # e.g. ".chl", ".dsu", ".pkg"
  download: null       # where the file lives
tools: []              # e.g. ["Torx T25", "Phillips #2", "M5 hex"]
verification: ""       # manual-verified | web-search | community | unverified
last_updated: ""
---

# Manufacturer Model

> **2AM CARD** — the stuff you need first
> - **Password / menu lock:** …
> - **Power:** … A @120 V / … A @208 V → **… per 20 A circuit @120 V, … @208 V** (link limit …)
> - **DMX:** modes … · address via …
> - **Won't move?** transport locks at …
> - **Tools:** …

## Identity
- What crews call it:
- Fixture library / profile names (MA3, GDTF, Hog, Eos):
- Variants and how to tell them apart:

## Passwords, menu locks & hidden menus
- Default passcode and how to enter it (button sequence)
- Service / factory menu access
- How to unlock a locked display

## Power
| | 120 V | 208 V | 230 V |
|---|---|---|---|
| Current (A) | | | |
| Power (W) | | | |
| Max power-link (manufacturer) | | | |
| **Max per 20 A circuit** (16 A continuous) | | | |

- Input range / auto-ranging:
- Connectors in / out:
- Fuse (type, rating, location):
- Inrush / power-up notes:

## Data & addressing
- Connectors:
- Protocols:
- DMX modes / footprints:
- Set the address (menu path, button by button):
- Battery / unpowered addressing:
- Factory reset:
- Wireless / Ethernet setup notes:

## Rigging & hardware
- Bracket / omega type and clamp spacing:
- Fasteners (quarter-turn camlocks etc.):
- Safety cable point:
- Mounting orientations allowed:
- Transport / pan-tilt locks (location):
- Weight / dimensions:

## Tools & screws
| Job | Fastener | Bit / tool |
|---|---|---|
| Top / head covers | | |
| Gobo / effects module access | | |
| Lens / front glass | | |
| Omega bracket | | |

## Optics & consumables
- Source / lamp, lamp life:
- Color system:
- Gobo wheels (rotating / static), gobo size (OD / image / thickness):
- Prism / frost / zoom / iris / shutters:
- Gobo / module change procedure:

## Error codes
| Code / message | Meaning | Fix |
|---|---|---|

## Symptom → fix
| Symptom | Likely cause | Fix |
|---|---|---|

## Maintenance
- Recalibrate / reset procedure:
- Fan / filter cleaning:

## Firmware
- Installed version — where to see it on the fixture:
- Latest known version (date checked) and where to download it:
- What you need: interface box / cable / software / USB stick format:
- Update steps (numbered, button by button):
- Updating a whole rig (how many at once, same model only?, over DMX/Ethernet):
- If it fails or bricks mid-update (recovery mode):
- Release notes worth knowing (show-relevant bug fixes, new modes — a mode change can break your console patch):

## Road notes (community)
- Real-world gotchas from forums / Reddit / techs. Always say where it came from.

## Sources
- [Manual name rev X](url) — what was taken from it
