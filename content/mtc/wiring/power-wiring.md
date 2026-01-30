---
title: "Power Supply"
---

This document outlines the correct wiring of the TCM's power supplies and power outputs.

## Power Supplies
The TCM can be used in 12V or 24V systems with a nominal supply voltage of 9-32V.

All power supply pins are protected against reverse battery, over current, over voltage, over temperature, transients and load dumps.

Voltages are clamped internally to 35V.

### Battery Hot Supply
| Pin | Voltage | Current |
| --- | ------- | ------- |
| C1  | 9-32V   | < 1A   |

>[!WARNING] 
>This pin must be powered at all times to allow the TCM to control it's own power supply. Failure to do so may result in data logging memory being corrupted.

When more than ~3.5V is present on the [Ignition Switch](#ignition-switch) pin (C6), the internal circuitry will turn on the circuits connected to pin C1 and the TCM will power up.

Once the TCM is booted, the CPU will latch the internal power switch ON. In this state, if the voltage on the [Ignition Switch](#ignition-switch) pin drops to 0, the TCM will remain on until the CPU disables the internal power latch.

>When the TCM is off, this pin does NOT draw any current.

### Ignition Switch
| Pin | Voltage | Current |
| --- | ------- | ------- |
| C6  | 9-32V   | < 3mA   |
>[!INFO] 
>This pin must does NOT supply any power to the device. Without connecting the [Battery Hot Supply](#battery-hot-supply) pin (C1), the TCM will not power up.

The ignitions switch serves only to enable the internal power switch connected to pin C1. It's voltage is monitored by the TCM at all times and the data is available to the user.

### Auxiliary Supplies
| Pin | Voltage | Current |
| --- | ------- | ------- |
| C2  | 9-32V   | 15A max, *Application Specific* |
| C3  | 9-32V   | 15A max, *Application Specific* |

Pins C2 and C3 supply the half bridge drivers on Aux Output 1-8. The current draw of these inputs is determined by the total high side current of the Auxiliary outputs.

The auxiliary outputs are split into 2 banks of 4: 1-4 and 5-8. The total high side current of a single bank should not exceed 15A for an extended period of time.

> Auxiliary Supply pins can be supplied with constant or switched power. The TCM will only turn them on when the Ignition switch is on.

### Solenoid Supplies
| Pin | Voltage | Current |
| --- | ------- | ------- |
| C4  | 9-32V   | 15A max, *Application Specific* |
| C5  | 9-32V   | 15A max, *Application Specific* |

Pins C4 and C5 supply the Solenoid power output pins (B30-B33) as well as the flywheel diodes and voltage monitors of the solenoid drivers.

> Solenoid Supply pins can be supplied with constant or switched power. The TCM will only turn them on when the Ignition switch is on.

---

## Solenoid Power Outputs
| Pin | Solenoids | Continuous Current |
| --- | --------- | --------- |
| B30 | 1-4       | 7.5A      |
| B31 | 5-8       | 7.5A      |
| B32 | 9-12      | 7.5A      |
| B33 | 13-16     | 7.5A      |

The 4 Solenoid Power Supply Output pins are intended to supply the high side of the solenoids driven by any of the 16 Solenoid Output pins. 

All supply outputs are protected against reverse battery, short to ground, over current, over voltage, over temperature.

Ideally, you should supply the solenoids with their respective linked output. This means that in the event of a critical fault, the TCM can shut down the supply to the problem solenoid bank. 

Many applications will not be flexible enough to allow this. Best judgement should be used to make the system as robust as possible.

> **Example:** ZF 8HP: There is only 1 solenoid supply pin for 9 solenoids. You can join two or more output pins to increase to total current capacity of the supply.

> **Note:** During normal operation in a typical transmission, not all solenoids are on at the same time and not all solenoids will be commanding maximum current.