---
title: "Firmware Updates (all brands)"
aliases: ["firmware", "update", "software update", "upload", "uploader", "bricked", "bootloader", "flash", "version"]
type: reference
last_updated: "2026-10-03"
---

# Firmware Updates (all brands)

How firmware updates work in general, and what to bring. **Each fixture page has a Firmware section** with its own version and steps, and each maker's `_common` page has that brand's tools and procedure. The [firmware table](../firmware.md) lists every fixture's update method side by side.

> **2AM CARD**
> - **Don't update on show day** unless the update fixes the problem you have right now.
> - **Unplug the console** from the DMX line, and put **only the fixtures being updated** (usually one model) on it.
> - **Never cut power or pull the cable/USB stick mid-update.** That's how fixtures get bricked.
> - **After updating:** check the version on every unit, then check the DMX mode and address. New firmware can **add or renumber modes**, which breaks the console patch.
> - **Bricked?** Most fixtures have a recovery/bootloader mode that accepts the update again over the maker's interface. See the maker's `_common` page.

## By manufacturer — what you need

| Maker | Usual method | Hardware | Software | Details |
|---|---|---|---|---|
| Chauvet Professional | USB stick (newer) or DMX cable | UPLOAD 08 (USB-to-DMX) | Chauvet uploader | [Chauvet common](../fixtures/chauvet/_chauvet-common.md) |
| Robe | DMX/RDM via interface, or Ethernet (several at once) | Robe Universal Interface (RUNIT / WTX) | ROBE Uploader (DSU package from robe.cz); PC on 2.x.x.x for Ethernet | [Robe common](../fixtures/robe/_robe-common.md) |
| Martin | USB stick (.BANK in root → SERVICE → USB) on newer fixtures; DMX/RDM | Companion Cable P/N 91616091; older: USB Duo / DABS1 | Martin Companion Desktop (Windows); older: Martin Uploader; P3 controller for Aura PXL / Ultra | [Martin common](../fixtures/martin/_martin-common.md) |
| Claypaky | Fixture-to-fixture (Advanced → 1234 → Upload Firmware, same model), CloudIO box (USB stick, .img), web server, PC | CloudIO Box CA8001, or Claypaky USB/DMX uploader | Files from Claypaky Customer Care | [Claypaky common](../fixtures/claypaky/_claypaky-common.md) |
| GLP | DMX line, several at once; X5 also via app / web / fixture push | GLP D3Prog (battery handheld, 5- and 3-pin out) | Loaded from PC over USB; hex/BIN files | [GLP common](../fixtures/glp/_glp-common.md) |
| Elation | 3-pin DMX from a loader, or USB on some models | E-LOADER III (ELO601, micro SD) | Windows PC to load the SD card; no downgrades | [Elation common](../fixtures/elation/_elation-common.md) |
| ETC | DMX via Gadget, Net3, or USB drive (Series 3); ColorSource fixture-to-fixture | Gadget / Gadget II, or Net3 gateway | UpdaterAtor (Windows). Pull non-ETC opto-splitters off the line first | [ETC common](../fixtures/etc/_etc-common.md) |
| Astera, Solaris, SGM, hazers | Astera: app over Bluetooth · Flare: Upload menu, fixture to fixture · SGM: USB-XLR cable · MDG: service only | ART7 / phone; SGM uploader cable | AsteraApp; SGM Firmware Tool | [Misc common](../fixtures/misc/_misc-common.md) |

The maker pages are the source of truth; this table is a summary.

## Before you update
1. **Decide if you need it.** Good reasons: a known bug you're seeing, a fixture that won't patch because its firmware lacks a mode the rest of the rig uses, or the shop asked you to. "There's a newer version" is not a reason to do it mid-tour.
2. **Read the release notes.** Look for new or renumbered DMX modes, changed defaults, and "cannot downgrade" warnings.
3. **Write down** each fixture's current version, DMX mode, address and any custom settings (some updates reset to defaults).
4. **Match the rig.** Mixed firmware across one fixture type can mean different colour calibration, different mode lists, or different behaviour on the same DMX values. Update the whole set, not one unit.
5. **Kit:** laptop (most uploaders are Windows-only, so Mac users need a VM), the maker's interface box, firmware files saved locally, USB stick formatted as the maker requires (often FAT32, sometimes ≤ 32 GB), 5↔3-pin adaptors, a terminator, short DMX cables.

## During the update
- Console disconnected. Nothing else sending DMX/Art-Net/sACN on that line or network.
- Same model only on the line, unless the maker's tool says it can handle mixed models.
- Keep the line short and terminated. Batch limits exist (e.g. 10 units per pass for Chauvet's UPLOAD 08). Respect them.
- Stable power: no generator switchovers, no one else working on that distro.
- Don't touch the fixture until it has rebooted and finished homing.

## After the update
- Check the version on each fixture's display/info menu.
- Check mode and address, then **check the console's fixture profile matches** the new firmware's channel layout.
- Run a quick test: home, pan/tilt, colour, gobo, shutter, dimmer.

## When it goes wrong
| Symptom | What to do |
|---|---|
| Uploader can't find the fixture | Fixture not in update mode (many need a menu setting like "Software Update → On" first), wrong cable (3-pin vs 5-pin), console still connected, an opto-splitter in the line (blocks the return data some uploaders need), wrong COM port, driver missing for the interface box. |
| Update stops partway | Don't power-cycle yet. Retry from the uploader. If the fixture has rebooted dead, use its recovery/bootloader mode. |
| Fixture dead or stuck on boot logo after an update | Recovery mode via the maker's interface (Chauvet: UPLOAD 08; Robe: DSU mode / "fix broken device with RUNIT"; Martin Quantum/Encore: bootloader switch in the base; MDG: USB during "Testing BootLoad" at power-up). If that fails, it's a shop/service repair. |
| Works, but console control is wrong | Mode list changed. Re-patch with the updated profile, or check the mode number on the fixture. |

## Sources
- General practice: general knowledge. Maker-specific tools, versions and steps are cited on each maker's `_common` page and fixture page.
- Robe Universal Interface / ROBE Uploader: [ROBE Uploader manual TB54](https://www.robelighting.de/res/downloads/tech_bulletins/TB54_ROBE_Uploader_manual_EN.pdf), [Robe Universal Interface WTX manual](https://luxpro.ua/files/User_manual_Robe_Universal_Interface_WTX.pdf) (via web search).
