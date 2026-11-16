# Charging — Quick Card

!!! warning "Which charger for which pack"
    **TB6B — 2S–4S only** (6S balancing failed); 50 W caps it at **4.0 A on 3S, 3.0 A on
    4S.** · **ISDT 608PD — use for 6S.** · **NOCO Genius 2 — lead-acid only, never LiPo.**

## Get these four right, every time

| Setting | How to choose | If wrong |
|---|---|---|
| **Chemistry** | From the label: LiPo / Li-ion / LiFe / NiMH | Wrong target voltage per cell |
| **Cell count (S)** | From the label, confirmed on the charger | **The dangerous one.** 3S as 6S → fire |
| **Current** | **0.5C = half the Ah.** 7500 mAh → **3.75 A** (`1C` is the ceiling) | Too high: heat, swelling, fire |
| **Mode** | **Balance** to use it · **Storage** to shelve it | Unbalanced cells go over-voltage |

Say it out loud, then read the screen back: *"Six S, LiPo, 3.75 amps, balance."*

## Procedure

1. **Inspect** — swollen, punctured, wet or hot → stop, quarantine, tell Steve.
2. **Read the label** — chemistry, cell count, capacity.
3. **Check resting voltage.** Every cell **3.3**–4.2 V, within ~0.1 V of each other.
4. **Pack into the LiPo bag or metal bin** on the charging table.
5. **Balance lead in first** (white JST-XH), then the power connector.
6. **Set chemistry, cell count, current, mode**, then **read the detected count back** —
   mismatch → **stop, ask a TA. Never override.**
7. **Start, watch the first minute**, then **stay in the room.** Note the finish time.
8. **Power lead out first**, then the balance lead.

## How long will it take

```
set current (A) = 0.5 × capacity in Ah          (lab default; 1C is the ceiling)
charge time (h) ≈ 1.15 × capacity in Ah / charge current
max current (A) = charger or adapter watts / full pack voltage  ← usually the real limit
```

!!! danger "The supply sets your charge rate"
    **ISDT 608PD** only gets what the USB-C adapter gives — read the wattage printed on it:
    into 6S, **65 W → 2.6 A · 100 W → 4.0 A · 140 W → 5.6 A**. Above 100 W needs an
    **EPR-marked cable.** Power the charger **before** the battery.

!!! danger "Stop and fetch a TA — and two open items"
    **Stop:** wrong cell count · one cell far below the rest · `CELL LOW/HIGH VOL` · hot or
    puffing. **ISDT 608PD steps are NOT verified on this unit**, and 6S has no documented
    storage-charge route — **T1/T2 in `todo.md`**.
