---
title: "Getrag GS7"
draft: true
---

## Shift Forks
There are four hydraulically operated selector rods and four sliding clutches, with one
selector rod and one sliding clutch for each gear pair 4/6, 2/R, 1/3 and 5/7. Gears 1, 2, 3
and Reverse are equipped with double taper synchronization and gears 4, 5, 6 and 7 with
single taper synchronization.

In the M DCT, driving force is transmitted in gears 1, 3, 5, 7 and R from clutch 1 to inner
input shaft 1 and sub-transmission 1.

In gears 2, 4 and 6 the driving force is transmitted from clutch 2 to inner input shaft 2
and sub-transmission 2.

![alt text](../../../img/getrag-gs7/gs7_mech1.png)

![alt text](../../../img/getrag-gs7/gs7_mech2.png)

![alt text](../../../img/getrag-gs7/gs7_mech3.png)

## M DCT Transmission Sensors
The following sensors are mounted in the transmission and their signals are sent directly
to the M DCT electronics:
• Input shaft 1 speed (Hall) sensor monitors rotation and direction of transmission
shaft 1.
• Input shaft 2 speed (Hall) sensor without rotation direction detection for the
transmission shaft 2.
• Clutch oil pressure (Piezo) sensors for clutch 1 and 2.
• 3 temperature sensors (NTC), one for the ejected clutch oil and two redundant
temperature sensors for the M DCT electronics.
• 4 linear (Hall) sensors monitor the selector rod position.
• 1 double (redundant) parking lock (Hall) sensor.
The oil sump temperature is measured using a complex temperature map and checked
against the temperature of the clutch oil by the M DCT electronics.
Torque Intervention
The M DCT mechatronics module sends a torque requirement to the engine control
module on the PT-CAN in order to achieve a torque intervention when shifting gear under
load or when coasting. This is negative when upshifting so that the engine speed is
reduced. When downshifting the torque intervention is positive, in order to increase the
engine speed. Gear shifting is supported by the engine control module through this
torque intervention strategy.

## Pressure
The operating pressure is determined by a regulated control valve depending on the load
and the function selected. The system is protected by a pressure relief valve in the pump.
The pressure is regulated according to the following priorities:
• Clutch engagement and disengagement
• Gear changes
• Cooling the clutch
• Lubrication cycle.
The transmission oil pressure should be high enough to:
• Be able to engage the clutches reliably.
• Allow the gear selector rod to reach the required control shift speed.
The normal operating pressure range is between 5 and 20 bar, although it can be
increased up to 30 bar if necessary to maintain proper transmission operation.
At maximum shifting force, the pressure required to operate the selector rods can be the
same as the operating pressure.
The pressure required for the clutches is limited to 18 bar. The clutch is regulated by an
integrated proportioning valve.
Overpressure protection is ensured by a pressure relief valve.
Clutch cooling is map-controlled using a proportional valve.


## Oil to Coolant Cooling
The M DCT transmission oil cooling circuit consists of an oil to coolant heat exchanger,
an oil to air heat exchanger, a transmission oil thermostat and the relevant cooler lines.
The oil to coolant heat exchanger is part of the engine cooling system of the vehicle.
Mounted on the transmission housing it allows the oil to flow directly from the M DCT
into the oil to coolant heat exchanger.
Engine coolant directly from the cylinder head is pumped to the oil to coolant heat
exchanger by the auxiliary coolant pump and then circulated back to the engine cooling
system. The M DCT electronics can switch on the auxiliary coolant pump as needed.
The auxiliary coolant pump, which is normally used to enhance the efficiency of the
heating system, is used here to warm up the M DCT transmission. This design shortens
the warm up time and maintains the transmission oil in the desired operating temperature
range.
After the oil to coolant heat exchanger has brought the temperature of the transmission
oil to above 95°C/203°F, an oil thermostat directs the transmission oil to the oil to air heat
exchanger located at the front of the vehicle.