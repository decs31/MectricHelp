---
title: "Drive Modes"
draft: true
---

`Drive Modes` refer to the main transmission states such as Park, Reverse, Neutral, and Drive (Auto, Sport, Manual). Selection of the desired drive mode can be achieved a variety of ways including:
 - CAN bus shifter (preset or custom)
 - Analog shifter position
 - Digital shifter position matrix
 - Switches or buttons
 - Up Shift & Down Shift switches
 - Combinations of the above

## Drive Mode Input Priorities
Drive mode input sources have fixed priorities. This allows them to be used in conjunction with one-another with predictable results. Inputs with higher priority will override inputs with lower priority.

| Priority    | Input Source                                |
| ----------- | ------------------------------------------- |
| 1 (Highest) | Park Request Switch                         |  
| 2           | Neutral Request Switch                      |
| 3           | Shifter Position (Park / Reverse / Neutral) |
| 4           | Reverse Request Switch                      |
| 5           | Manual Switch                               |
| 6           | Sport Switch                                |
| 7           | Drive Switch                                |
| 8           | Shifter Position (Drive / Sport / Manual)   |
| 9           | Up Shift Switch                             |
| 10 (Lowest) | Down Shift Switch                           |

> **Example:** If the shifter is in the Neutral position, but the Park Request Switch is enabled and in the active (ON) state, the transmission will remain in Park until the Park Request Switch becomes inactive (OFF) because the Park Switch has higher priority than the Shifter Position input.