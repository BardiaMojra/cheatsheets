# Open Items — Batteries and Chargers

Everything in these documents that is **not yet verified on the lab's own hardware**, or
still missing. Each item says where it shows up, so a fix can be pulled through.

Last reviewed: 2026-11-13.

!!! danger "T1 — ISDT 608PD procedure is NOT verified on the lab unit"
    **Where:** `main_guide.md` §5.7 · `cards/03_charging_card.md`  
    **What:** the button sequence (left / centre / right, hold-centre to edit) and the  
    profile behaviour come from a **published review of the model**, not from a test on the
    charger sitting on the table. Its error codes are not documented at all.
    **Why it matters:** this is the charger students are told to use for 6S packs. A wrong  
    keystroke here is a wrong cell count.
    **To close:** walk the procedure through once at the table, correct anything that  
    differs, photograph the error-code page of its printed manual, then delete this item
    and the caution in §5.7.
    **Owner:** Steve / TA.

!!! warning "T2 — How does the lab bring 6S packs to storage voltage?"
    **Where:** `main_guide.md` §5.4, §5.7  
    **What:** the ISDT 608PD has **no storage or discharge program**, and the TB6B  
    **cannot balance 6S** (failed balancer board). So there is currently no documented way  
    to storage-charge a 6S pack in this lab.
    **Why it matters:** packs left full puff on the shelf. This is the gap most likely to  
    cause a slow-burn safety problem.
    **To close:** decide the procedure (repair/replace the TB6B, a second charger, or a  
    documented manual method) and write it into §5.4.
    **Owner:** Steve.

!!! warning "T3 — Six connector photos need to be taken in the lab"
    **Where:** `main_guide.md` §4.2, §4.3 · `img/README.md`  
    **What:** `fetch_images.py` filled the slots Commons can cover (Anderson Powerpole,
    JST, JST-XH, USB-C, plus a Tamiya pack photo); XT90 uses the lab photo. **Commons has
    no usable photo of XT30, XT60, EC5, Deans/T-plug, RC bullet connectors or MX2.0** —
    its search matched the words, not the parts, and those downloads are parked in
    `img/rejected/` with an explanation.  
    **Why it matters:** **XT60 is the lab default connector and has no picture at all.**
    Students match what they are holding against the page, so lab photos of the actual
    parts beat stock images anyway.  
    **To close:** photograph the lab's parts into `img/xt30_01.jpg`, `img/xt60_01.jpg`,
    `img/ec5_01.jpg`, `img/deans_01.jpg`, `img/bullet_01.jpg`, `img/molex_01.jpg` (plain
    background, connector filling the frame), then `./build_pdfs.sh`. Also pick one
    candidate per filled slot, delete the rest, and trim `img/sources.md` to match.  
    **Owner:** whoever has the parts out.

!!! warning "T4 — Pack masses are examples, not measurements"
    **Where:** `main_guide.md` §3.4 · `cards/01_batteries_card.md`  
    **What:** the 6S 16000 vs 6S 7500 endurance comparison assumes ~2.0 kg and ~1.0 kg and  
    a 45 A hover current. The energy figures (355 Wh / 167 Wh) are correct; the mass and
    current figures are illustrative.
    **Why it matters:** this comparison is the evidence behind retiring the 6S 16000 packs.  
    It should rest on measurements.
    **To close:** weigh both packs and log the real hover current, then replace the table  
    in §3.4 and the summary line on the batteries card.
    **Owner:** whoever flies it next.

!!! warning "T5 — TB6B 6S fault: repair, replace, or retire?"
    **Where:** `main_guide.md` §5.6 · every card that names a charger  
    **What:** the TB6B's balancer board has failed for 6S. The documents currently say  
    "2S–4S only". Tenergy balancer boards have a history of this.
    **To close:** decide the disposition and update §5.6. If the unit is replaced, the  
    charger-selection box on `cards/00_safety_card.md` and `cards/03_charging_card.md`  
    changes too.
    **Owner:** Steve.

!!! note "T6 — Two overlapping document sets in this folder"
    **Where:** this folder  
    **What:** `main_guide.md` + `cards/` is the knowledge-base set. The earlier  
    `battery-cheat-sheets-markdown/` four-document set is still here; its lab photos and
    diagrams are referenced live by `main_guide.md`, so **it cannot simply be deleted.**  
    **To close:** move the images it owns into `img/`, repoint the references, then archive  
    the older markdown.

## Margin policy — do not quietly undo it

Every limit in these documents is **already derated** (`main_guide.md` §0). Connector
figures are 80% of the lowest published continuous rating; discharge is 70% of the printed
C; charging defaults to 0.5C; the cell floor is 3.30 V, not 3.00 V. If you update a number
from a datasheet, **apply the same margin** before it goes in the table.
