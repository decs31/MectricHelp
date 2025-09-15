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

## Selector Forks
| Fork | Gear Low | Gear High |
| ---- | -------- | --------- |
| A    | 1        | R         |
| B    | 2        | 4         |
| C    | 3        | 5         |
| D    | N        | 6         |

### Gear to Fork Mapping
| Gear | Fork  | Position | Volts (Nominal) |
| ---- | ----- | -------- | ----- |
| R*   | A     | L        | 1.300 / 3.800 |
| N    | *ALL* | *ALL*    | 2.500 |
| 1*   | A     | H        | 3.800 / 1.300 |
| 2    | B     | L        | 1.300 |
| 3    | C     | L        | 1.300 |
| 4    | B     | H        | 3.800 |
| 5    | C     | H        | 3.800 |
| 6    | D     | L        | 1.300 |
> \* Fork A has two position sensors.

--- 

## Shift Solenoids
| Solenoid | Function         |
| -------- | ---------------- |
| 1        | 4 / N            |
| 2        | 2 / 6            |
| 3        | R / 5            |
| 4        | 1 / 3            |
| 5        | Sequence         |

### Fork Solenoids Command Table
| Fork        | Pos  | Sol 1 | Sol 2 | Sol 3 | Sol 4 | Seq |
| ----------- | ---- |:-----:|:-----:|:-----:|:-----:|:---:|
| **A (1/R)** | R << |       |       | X     |       |     |
| **A (1/R)** | >> 1 |       |       |       | X     |     |
| **B (2/4)** | 2 << |       | X     |       |       |     |
| **B (2/4)** | >> 4 | X     |       |       |       |     |
| **C (3/5)** | 3 << |       |       |       | X     | X   |
| **C (3/5)** | >> 5 |       |       | X     |       | X   |
| **D (6/N)** | 6 << |       | X     |       |       | X   |
| **D (6/N)** | >> N | X     |       |       |       | X   |

---

## Axis Feed Pressure Solenoids
### Active Clutch Behaviour
Maintains about 3.5 bar above the active clutch pressure target.

### Inactive Clutch Behaviour
Holds 10 bar at most times.
During a fork movement, it ramps up a few bar to star the fork moving, then drops to slow it down. Once the fork is in position it returns to 10 bar.

---

## Lubricating Flow Solenoid
Remains inactive by default, allowing fully lubrication and cooling flow.
During a shift or high torque demand it will close off, to reduce pressure drop and allow maximum line pressure availability.