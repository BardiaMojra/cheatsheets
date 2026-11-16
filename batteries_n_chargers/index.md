# Batteries and Chargers — Document Set

Teaching material for students handling UAV/UGV lithium packs and the chargers on the lab
charging table. Written against the brief in `readme.md`.

## What is here

| File | What it is | Print as |
|---|---|---|
| `todo.md` | **Open items** — everything not yet verified on the lab's own hardware, with where each one shows up | Read before editing |
| `main_guide.md` | **The central document.** Full reference: safety, battery theory, sizing, connectors, chargers, troubleshooting, glossary, sources | Multi-page, stapled or in the knowledge base |
| `cards/00_safety_card.md` | Emergency steps, the five rules, quarantine triggers, voltage limits | **1 side — laminate, post at the charging table** |
| `cards/01_batteries_card.md` | Label reading, voltage table, the four formulas, the 6S-vs-4S case | **1 side — laminate** |
| `cards/02_connectors_card.md` | Power and signal/balance connector tables, pitch, wiring rules | **1 side — laminate** |
| `cards/03_charging_card.md` | Which charger, the four settings, the procedure, charge time | **1 side — laminate** |
| `build_pdfs.sh` | Builds every PDF into `pdf/` | — |
| `fetch_images.py` | Downloads connector photo candidates from Wikimedia Commons into `img/`, with licences, and writes `img/sources.md` | — |
| `md2html.py` | markdown → styled HTML, used by the build script | — |
| `style/cheatsheet.css` | Page size, colors, type, callouts, photo plates | — |
| `img/` | Connector photos, plus `img/README.md` listing which slots are still empty | — |

The cards are condensed from `main_guide.md`. **The guide is the authority** where the two
disagree; edit the guide first, then pull the change through to the card.

`readme.md` is Steve's original brief and is left untouched.

`battery-cheat-sheets-markdown/` is the earlier four-document set (Battery Fundamentals,
Charger Guides, Battery Guides, Connector Cheat Sheet) with the lab photos and diagrams.
`main_guide.md` and the cards **reference its images directly** rather than copying them,
and its confirmed charger facts (TB6B 50 W / 0.1-5.0 A, ISDT 608PD, NOCO Genius 2) are
folded in. The two sets still overlap and should be consolidated - see "Still open".

## Building the PDFs

```bash
./build_pdfs.sh              # everything into pdf/
./build_pdfs.sh cards        # only the laminate cards
./build_pdfs.sh guide        # only the main guide
./build_pdfs.sh --keep-html  # leave the intermediate HTML in build/ for debugging
```

**Toolchain** — nothing to install on the dgx, no sudo:

| Tool | Role | Check |
|---|---|---|
| `python3` + `markdown` module | markdown → HTML | `python3 -c "import markdown; print(markdown.__version__)"` |
| `google-chrome` headless | HTML + CSS → PDF | `command -v google-chrome` |

If the `markdown` module is missing: `pip3 install --user markdown`.

Page size and margins live in the `@page` rule in `style/cheatsheet.css`. The build gives
each source file a body class — `guide` or `card` — which selects the type scale.

## House rules for editing

- **Every card is one single side.** They are laminated and read at arm's length, so if
  an edit pushes a card onto a second page, **cut content rather than shrink the type** —
  and ask before letting a card go double-sided. Check the fit with:

  ```bash
  pdftotext -bbox pdf/03_charging_card.pdf - | grep -c "<page"
  ```

  The printable column is 265 mm tall; the build is at its limit on the safety card.
- **Callout line breaks.** Markdown collapses consecutive lines into one paragraph, which
  runs worked calculations together. Lines inside a `!!!` callout that must stand alone
  end with **two trailing spaces**. Keep them when editing.
- **Cite anything numeric.** Connector current ratings and wire ampacity figures conflict
  wildly between vendors; `main_guide.md` §8 explains which numbers are trustworthy and
  which are not. Keep the caveats when you edit.
- **Never quietly remove margin.** Every limit in these documents is already derated, and
  the policy is stated in the box at the top of `main_guide.md`:

  | Thing | Rule |
  |---|---|
  | Connectors | **80%** of the lowest published continuous rating |
  | Pack discharge | **70%** of the printed C rating |
  | Charge current | **0.5C** default, `1C` absolute maximum |
  | Cell floor | **3.30 V/cell** working floor (3.00 V is damage, not a target) |
  | Wire | one gauge **thicker** than the connector's minimum |

  If you refresh a number from a datasheet, **apply the same margin before it goes in a
  table**, and update the figure in every place it appears (guide and card).
- **Photos stay local.** Nothing in these documents may depend on fetching a URL at build
  time. See `img/README.md`.
- Callouts use Python-Markdown admonition syntax, styled in the CSS:
  `!!! danger`, `!!! warning`, `!!! tip`, `!!! example`.
- An `<img>` whose file is missing renders as a labelled placeholder box, so the layout is
  final before the photos land. Drop the file into `img/` under the expected name and
  rebuild; no markdown edit is needed.

## Still open

Full detail, with owners, is in **`todo.md`**. Summary:

1. **TB6B charge power / max charge current / max discharge power** — could not be
   confirmed from a clean source. Read off the unit's label, fill into `main_guide.md` §5.6.
2. **USB-C charger make and model** — §5.7 is written generically against the USB-PD
   standard. Add the real keystrokes and error codes once the unit is identified.
3. **Connector photos** — see `img/README.md`.
4. **Pack masses** for the 6S 16000 and 6S 7500 — the endurance comparison in §3.4 uses
   example figures. Weigh the real packs and replace them.
5. **Consolidation.** `main_guide.md` and `battery-cheat-sheets-markdown/` cover
   overlapping ground and disagree on some connector ratings (XT90, Deans, Tamiya).
   Decide which is the knowledge-base document and retire or fold in the other.
