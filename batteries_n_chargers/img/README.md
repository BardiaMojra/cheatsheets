# Connector photos

Photos are referenced by fixed filenames from `main_guide.md` §4 and
`cards/02_connectors_card.md`. **A missing file renders as a labelled placeholder box**,
so the documents build and lay out correctly before the photos land. Drop a file in under
the expected name and rebuild — no markdown edit needed.

## Slots

| Filename | Subject | Used in |
|---|---|---|
| `xt60_01.jpg` | XT60, yellow | guide §4.2, connectors card |
| `xt90_01.jpg` | XT90, blue (ideally one XT90-S anti-spark) | guide §4.2, connectors card |
| `xt30_01.jpg` | XT30 | guide §4.2 |
| `deans_01.jpg` | Deans / T-plug | guide §4.2, connectors card |
| `ec5_01.jpg` | EC5 | guide §4.2 |
| `anderson_01.jpg` | Anderson Powerpole pair | guide §4.2, connectors card |
| `tamiya_01.jpg` | Tamiya, white | guide §4.2 |
| `bullet_01.jpg` | 4 mm bullet | guide §4.2 |
| `jst_xh_01.jpg` | JST-XH balance plug, ideally a 7-pin 6S lead | guide §4.3, connectors card |
| `jst_01.jpg` | JST family side by side, showing pitch difference | guide §4.3 |
| `molex_01.jpg` | MX2.0 / Molex 51005-51006 | guide §4.3, connectors card |
| `usbc_01.jpg` | USB-C plug | guide §4.3 |

## Status (2026-11-13)

`fetch_images.py` ran; `img/sources.md` is the attribution record. **Commons covers
general electronics well and RC hobby parts not at all.**

| Slot | Status |
|---|---|
| `anderson_01` · `jst_01` · `jst_xh_01` · `usbc_01` | **good** — correct subject, in use |
| `tamiya_01` | in use, but it is a photo of a **Tamiya battery pack**, not a connector close-up. Check `tamiya_02` and pick |
| `xt90_01` | filled from the lab photo in `battery-cheat-sheets-markdown/markdown/images/` |
| `xt30_01` · `xt60_01` · `ec5_01` · `deans_01` · `bullet_01` · `molex_01` | **empty — need lab photos.** Commons has nothing usable |

**XT60 matters most** — it is the lab default connector and has no picture at all.

Wrong-subject downloads are parked in `rejected/` with an explanation; they are not in the
documents. Two duplicate pairs to watch when picking: `anderson_01`/`anderson_03` and
`jst_01`/`jst_xh_01` are the same Commons image.

## Rules

- **Everything stays local.** No document may fetch a URL at build time.
- Plain background, connector filling the frame, both halves visible where it helps.
- A lab photo of the actual part beats a stock image — students match what they are
  holding against the page.
- Record every downloaded image in `sources.md` below: filename, source URL, author,
  licence. Wikimedia Commons is the preferred source because the licence is explicit.

## sources.md

Not yet written — no images downloaded. It must list, per file:

```
| file | source URL | author | licence |
```
