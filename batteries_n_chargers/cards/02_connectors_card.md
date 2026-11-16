# Connectors — Quick Card

!!! danger "The number in the name is not the rating"
    **XT60 is not a 60 A connector.** Vendor figures vary by 2× and mix continuous with
    burst. The **Lab limit** column below is **80% of the lowest credible continuous
    rating** — design to that number, never to the vendor's headline.

## Power connectors

| Connector | Conservative cont. | **Lab limit (80%)** | Wire | Notes |
|---|---|---|---|---|
| **XT30** | 15 A | **12 A** | 18–20 AWG | Micro UAV |
| **XT60** (yellow) | 30 A | **24 A** | 14–16 AWG | **Lab default, 3S–4S** |
| **XT90** (blue) | 40 A | **32 A** | 10–12 AWG | **Lab 6S packs.** `-S` = anti-spark |
| **Deans / T-plug** | 15 A | **12 A** | 12–14 AWG | Older. Avoid above 3S |
| **EC3 / EC5** | 60 / 120 A | **48 / 96 A** | 12–14 / 10–12 | Horizon / E-flite |
| **Anderson PP15/30/45** | 15 / 30 / 45 A (UL) | **12 / 24 / 36 A** | 16–20 / 12–16 / 10–14 | Genderless. Bench supplies |
| **Tamiya** (white) | 10 A | **8 A** | 16–18 AWG | Legacy. Not for LiPo |
| **Bullet 3.5/4/5.5** | 40 / 60 / 120 A | **32 / 48 / 96 A** | varies | **No keying.** Motor–ESC only |

## Signal and balance connectors — no propulsion current

| Connector | Pitch | Rated | **Lab limit** | Where |
|---|---|---|---|---|
| **JST SH** | 1.0 mm | ~1 A, 50 V | **0.8 A** | Tiny sensors, cameras, GPS |
| **JST ZH** | 1.5 mm | ~1 A, 50 V | **0.8 A** | Small sensor breakouts |
| **JST PH** | 2.0 mm | 2 A (24 AWG), 100 V | **1.6 A** | 1S packs, dev boards |
| **JST XH** | 2.5 mm | 3 A (22 AWG), 250 V | **2.4 A** | **Balance leads — every pack** |
| **MX2.0** (Molex 51005/6) | 2.0 mm | 2.0 A @24 AWG · 1.5 @26 · 1.0 @28 | **1.6 A** | Micro / whoop 1S packs |

!!! warning "Pitch is how you tell JST apart — and they will not mate"
    "JST 1.0 / 1.5 / 2.0 / 2.5" is the **pin pitch in mm** → SH / ZH / PH / XH.
    An N-pin XH shell is about `N × 2.5 mm` wide.

!!! tip "Wire, joint and plug — the weakest one sets the rating"
    Use the gauge the connector is built for. Solder XT/Deans **while mated**, heat-shrink
    every joint. **One adapter, never two** (Tamiya caps the path at 8 A). Check for
    cracked shells, pushed-back pins, blackened contacts. Warm plug = undersized or cold joint.
