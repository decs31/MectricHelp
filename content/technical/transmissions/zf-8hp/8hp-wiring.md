---
title: "ZF 8HP Wiring"
draft: true
weight: 1
---

| Pin | Function                                  | Note                   |
| --- | ----------------------------------------- | ---------------------- |
| 1   | Sensor 0V Ref                             | For temperature sensor |
| 2   | Line Pressure Solenoid                    |                        |
| 3   | Speed Sensor 8V Supply                    |                        |
| 4   | Accumulator Solenoid                      |                        |
| 5   | Park Hold Solenoid                        |                        |
| 6   | Park Release Solenoid                     |                        |
| 7   | Clutch C Solenoid                         |                        |
| 8   | Input Shaft Speed Signal                  | DI 1-8, Pulldown On    |
| 9   | Clutch E Solenoid                         |                        |
| 10  | Output Shaft Speed Signal                 | DI 1-8, Pulldown On    |
| 11  | Brake A Solenoid                          |                        |
| 12  | TC Lockup Solenoid                        |                        |
| 13  | Trans Fluid Temp Sensor                   |                        |
| 14  | Solenoid Power Supply                     | From B30 *(1)*         |
| 15  | Brake B *(G1)* / Clutch D *(G2)* Solenoid |                        |
| 16  | Clutch D *(G1)* / Brake B *(G2)* Solenoid |                        |

> 1. Ideally each 4 solenoids would have a seperate supply bank, but this isn't possible using the OEM connector. Connecting to a single solenoid supply will suffice.

