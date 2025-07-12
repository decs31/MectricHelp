---
title: "Nissan GR6 Operation"
---

## Gear Ratios
| Gear | Ratio  |
| ---- | ------ |
| R	   | -3.383 |
| 1st  | 4.056  |
| 2nd  | 2.301  |
| 3rd  | 1.595  |
| 4th  | 1.248  |
| 5th  | 1.001  |
| 6th  | 0.796  |
| FD   | 3.700  |

--- 

## Gear Mapping
| Gear | Fork | Position | Volts |
| ---- | ---- | -------- | ----- |
| R    | A    | L        |       |
| N    | -    | -        | -     |
| 1    | A    | H        | 3.800 |
| 2    | B    | L        | 1.300 |
| 3    | C    | L        | 1.400 |
| 4    | B    | H        | 3.740 |
| 5    | C    | H        | 3.820 |
| 6    | D    |          |       |

---

## Selector Forks
| Fork | Gear Low | Gear High |
| ---- | -------- | --------- |
| A    | 1        | R         |
| B    | 2        | 4         |
| C    | 3        | 5         |
| D    | 6        | -         |

The high-level rule for selecting the direction of any fork:

**Upshift (low → high):**
 - E = On (apply feed)
 - Target fork’s shift-solenoid = On (bleed closed → high-side pressurized)
 - All other shift-solenoids = Off (their bleeds open → those circuits stay unpressurized)

**Downshift (high → low):**
 - E = On
 - Target fork’s shift-solenoid = Off (bleed open → low-side pressurized)
 - All other shift-solenoids = On (their bleeds closed → those circuits stay at equal pressure)

After the fork moves you drop E = Off to vent the feed gallery and let all spools return to neutral under spring/detent, leaving the dog-rings locked in their new positions.

| Fork (gear-pair) |  Target | A (1–R) | B (2–4) | C (3–5) | D (6–N) | E (Seq) | What happens                                                                                          |
| :--------------: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :---------------------------------------------------------------------------------------------------- |
|      **1–R**     | Neutral |  **On** |    –    |    –    |    –    |    –    | Bleed closed → equal pressure → no move                                                               |
|      **2–4**     |   2nd   |    –    | **Off** |    –    |    –    |    –    | Bleed open → differential when E pulses → moves to 2nd                                                |
|      **3–5**     |   3rd   |    –    |    –    |  **On** |    –    |    –    | Bleed closed → equal pressure → no move (dogged by odd clutch)                                        |
|      **6–N**     | Neutral |    –    |    –    |    –    |  **On** |    –    | Bleed closed → equal pressure → no move                                                               |
|   **All forks**  |    –    |    –    |    –    |    –    |    –    |  **On** | Feed applied to all galleries, but only the B-circuit (bleed-open) sees differential → only 2–4 moves |
