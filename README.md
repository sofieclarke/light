# Light — Offline Lighting Tech Wiki

A searchable, offline troubleshooting wiki for concert lighting fixtures. It's built for finding one fact fast, in bad cell service: a menu passcode, how many fixtures fit on a 208 V circuit, an error code, or which Torx bit the gobo cover takes.

**Start here:** [`wiki/index.md`](wiki/index.md)

## Using it offline today
The wiki is plain Markdown, so any Markdown app can search it with no signal.

- **Obsidian (recommended, free, iOS/Android/desktop):** download this repo (GitHub → Code → Download ZIP), unzip, and open the folder as a vault. Search (`🔍`) covers every page, and links between pages work.
- **Any Markdown/notes app** that opens folders (e.g. Markor on Android, 1Writer/iA Writer on iOS) works too.
- Re-download after updates. (The app planned below will handle syncing.)

### Search tips
- Search the **nickname** crews use: `outcast 2x`, `pxl bar`, `mega`, `aura`. Every page lists its aliases.
- Search **topic + model**: `208 pxl`, `password outcast`, `error megapointe`.
- Each fixture page opens with a **2AM CARD**: passcode, power-per-circuit, DMX modes, transport locks and tools.

## What's in here

| Path | What |
|---|---|
| `wiki/index.md` | Every fixture, grouped by manufacturer (generated) |
| `wiki/passwords.md` | Every known menu passcode on one page (generated) |
| `wiki/comparison.md` | Power, link limits, DMX modes and tools side by side (generated) |
| `wiki/research-status.md` | What is solid, what is a stub, and known conflicts |
| `wiki/reference/` | Power math, DMX/network troubleshooting, moving-light troubleshooting, connectors & pinouts, tool kit |
| `wiki/fixtures/<maker>/` | One page per fixture, plus a `_<maker>-common.md` page for shared menus, firmware and error codes |
| `wiki/_templates/fixture-template.md` | Template for new fixture pages |
| `data/fixtures.json` | All fixture data in machine-readable form, for the app (generated) |
| `tools/build_index.py` | Regenerates the generated pages and JSON from fixture front matter |

## How trustworthy is each page?
Each fixture page's `verification` field says where its facts came from:

| Value | Meaning |
|---|---|
| `manual-verified` | Checked against the manufacturer PDF |
| `web-search` | Numbers came from search results quoting the manual; spot-check the important ones against the real manual when you can |
| `community` | Mostly forum/Reddit knowledge |
| `unverified` | Needs checking |

Anything uncertain inside a page is marked **⚠️ unverified**. Screw and bit sizes are rarely in manuals, so most of those are `TBD – check on next show`. Fill them in from real fixtures; that's the information nobody else has.

> The first research pass ran in an environment that blocked downloading manufacturer PDFs directly, so most pages are `web-search` level. Upgrading pages to `manual-verified` is the main follow-up task.

## Adding or editing a fixture
1. Copy `wiki/_templates/fixture-template.md` to `wiki/fixtures/<maker>/<model-slug>.md`.
2. Fill in the YAML block at the top (the app reads it) and the sections below it.
3. Run `python3 tools/build_index.py` to regenerate the index, comparison, passwords and JSON (`--check` validates only).
4. Photos: put them in `wiki/fixtures/<maker>/img/` and link them, e.g. `![Rear panel](img/outcast-2x-rear.jpg)`. Your own photos of rear panels, omega brackets, transport locks and packed cases are the most useful.

## Roadmap
1. **Now:** research and documents (this repo).
2. **Next:** verify the high-traffic pages against the real manuals; add photos.
3. **Then:** an offline-first app (PWA or native) that bundles `data/fixtures.json` and the Markdown, with instant search, a power calculator, and filters like "which fixtures use T25".
