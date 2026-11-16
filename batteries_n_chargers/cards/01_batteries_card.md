# Battery Basics — Quick Card

## Read the label: `6S1P 22.2V 7500mAh 25C XT90`

| Field | Means |
|---|---|
| `6S1P` | 6 cells in **series** → **set the charger to 6S**. S adds voltage, P adds capacity |
| `22.2V` | Nominal (`6 × 3.7 V`). The pack is **full at 25.2 V**, not 22.2 V |
| `7500mAh` | 7.5 Ah. **Charge at 0.5C = 3.75 A** (lab default; `1C` is the ceiling) |
| `25C` | Claimed `25 × 7.5 = 187 A`. **Plan to 70% = 131 A** |
| `XT90` | Power plug. The small white one is the **balance lead** (JST-XH) |

An `nS` pack has an **`n+1` pin** balance plug — a 6S lead has 7 pins.

## Voltages

| | per cell | 3S | 4S | 6S |
|---|---|---|---|---|
| **Full** | 4.20 V | 12.6 V | 16.8 V | 25.2 V |
| **Nominal** | 3.70 V | 11.1 V | 14.8 V | 22.2 V |
| **Storage (shelf)** | 3.80–3.85 V | 11.4 V | 15.2 V | 22.8 V |
| **Land now** (~15%) | 3.50 V | 10.5 V | 14.0 V | 21.0 V |
| **Stop** — working floor *(3.00 V = damage)* | **3.30 V** | 9.9 V | 13.2 V | 19.8 V |

Per cell: **Li-ion** 3.6–3.7 / 4.20 · **LiFe** 3.2 / 3.65 · **NiMH** 1.2 / ~1.45. Measure **rested**.

## The four formulas

```
Power    P (W) = V × I          1C current (A) = capacity in mAh / 1000
Energy   Wh    = nominal V × Ah       6S 7500 → 167 Wh · 6S 16000 → 355 Wh
Run time min   = 60 × (0.8 × capacity in Ah) / average current
```

!!! example "Why 6S beats 4S for the same 1000 W"
    `4S: 1000 / 14.8 = 67.6 A` → `67.6² × 0.005 Ω = 22.9 W` lost as heat  
    `6S: 1000 / 22.2 = 45.0 A` → `45.0² × 0.005 Ω = 10.1 W` lost as heat  
    One third less current, **less than half the wiring loss** — heat goes as `I²R`.
    Lower current also means thinner wire, smaller plugs and less voltage sag.

!!! warning "Higher voltage is not free"
    Every part — ESC, BEC, motor — must be rated for **full-charge** voltage (6S = 25.2 V),
    not nominal, and `RPM ≈ KV × V`: **changing cell count is a powertrain redesign.**

*Limits already derated: connectors 80%, discharge 70%, charge 0.5C, floor 3.30 V. Pack masses are examples — **T4 in `todo.md`**.*
