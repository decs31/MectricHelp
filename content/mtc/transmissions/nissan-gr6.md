---
title: "Nissan GR6"
---

{{% children sort="title" %}}

## Wiring

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
| 1    | R        | 1         |
| 2    | 2        | 4         |
| 3    | 3        | 5         |
| 4    | 6        | -         |

### Gear to Fork Mapping
| Gear | Fork  | Position | Volts |
| ---- | ----- | -------- | -------------- |
| R    | 1-L   | -9.0mm   | 1.300 / 3.800* |
| N    | *ALL* | 0.0mm    | 2.500 |
| 1    | 1-H   | 9.0mm    | 3.800 / 1.300* |
| 2    | 2-L   | 9.0mm    | 1.300 |
| 3    | 3-L   | 9.0mm    | 1.300 |
| 4    | 2-H   | -9.0mm   | 3.800 |
| 5    | 3-H   | -9.0mm   | 3.800 |
| 6    | 4-L   | 9.0mm    | 1.300 |
> \* Fork 1 has two position sensors.

--- 

## Shift Solenoids
| Solenoid | Function         |
| -------- | ---------------- |
| 1        | 4 / N            |
| 2        | 2 / 6            |
| 3        | R / 5            |
| 4        | 1 / 3            |
| Sequence | Fork 3 & 4       |

### Shift Solenoid Truth Table
| Fork        | Gear | Sol 1 | Sol 2 | Sol 3 | Sol 4 | Seq |
| ----------- | ---- |:-----:|:-----:|:-----:|:-----:|:---:|
| **1 (1/R)** | R << |       |       | X     |       |     |
| **1 (1/R)** | >> 1 |       |       |       | X     |     |
| **2 (2/4)** | 2 << |       | X     |       |       |     |
| **2 (2/4)** | >> 4 | X     |       |       |       |     |
| **3 (3/5)** | 3 << |       |       |       | X     | X   |
| **3 (3/5)** | >> 5 |       |       | X     |       | X   |
| **4 (6/N)** | 6 << |       | X     |       |       | X   |
| **4 (6/N)** | >> N | X     |       |       |       | X   |

---

## Axis Feed Pressure Solenoids
### Active Clutch Behavior
Maintains about 3.5 bar above the active clutch pressure target.

### Inactive Clutch Behavior
Holds 10 bar at most times.
During a fork movement, it ramps up a few bar to star the fork moving, then drops to slow it down. Once the fork is in position it returns to 10 bar.

---

## Lubricating Flow Solenoid
Remains inactive by default, allowing fully lubrication and cooling flow.
During a shift or high torque demand it will close off, to reduce pressure drop and allow maximum line pressure availability.