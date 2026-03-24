---
title: "Multi-Clutch Shifting"
draft: true
---

Shifting on multi-clutch transmissions happens over 4 phase:
 1. Fill
 2. Torque Transfer
 3. Inertial Sync
 4. Lock

![Shift Pressure Phases](</assets/mtc/shift_pressure_phases.png>)
> A simplified representation of the clutch pressures during the 4 shift phases.

The TCM will calculate all required clutch pressures based on supplied and available engine torque. As long as the clutch geometry is configured reasonably and the torque data from the engine is accurate, there's very little tuning required.

>[!WARNING] It is absolutely critical that the engine torque data is accurate.

---

## Fill Phase
Any clutch that is disengaged will have it's pressure fully bled off. The job of the fill phase is simply to ensure that the oncoming clutch pressure chamber is filled with fluid so that it can operate as fast as possible once the shift actually starts.

Generally, the clutch pressure at the end of the Fill phase will be the clutch's touch point pressure. The Fill phase is not intended to apply any meaningful clutch pressure.

>[!INFO] Unlike the rest of the shift phases, the fill phase doesn't use torque, it is purely pressure based.

The Fill phase is broken into 3 sub phases:
 1. Pre-Fill
 2. Fast Fill
 3. Stable Fill

The amount of time spent in each phase is limited by the `Total Fill Time` table and the phase order.
```
Stable Fill time = Total Fill Time - (Pre-fill + Fast Fill)
```
**Example:**
 - Pre-fill = 20ms
 - Fast fill = 40ms
 - Total fill time = 100ms

Stable fill = 100 - (20 + 40) = 40ms

Setting a fill phase time to zero will result in that phase being skipped. It's perfectly valid in many cases to skip the Pre-fill or the Fast Fill phase.
It's also common for high torque, high speed shifts to consist of only the Fast-Fill phase. In this case, the Pre-fill Time would be 0 and the Fast Fill Time would take up the entire Total Fill Time. 

> [!INFO] Regardless of the Pre-fill and Fast Fill times, the Fill phase will always exit once the Total Fill Time has elapsed.


### Pre-Fill
The Pre-fill phase simply opens the clutch pressure solenoid at the very start of the shift. The specified pressure is absolute and disregards the touch point.

Pre-fill pressure doesn't not usually exceed the touch point pressure.

**Typical Pressure:** 0.5 - 1.5 Bar
**Typical Time:** 0-100ms

> Setting the `Pre-Fill Time` to 0 will skip the Pre-fill phase.

### Fast Fill
During Fast Fill, the clutch pressure solenoid is driven very high for a short period. The intention is to allow a fast in-rush of fluid to fill the clutch chamber as fast as possible.

>[!CAUTION] A correctly configured combination of Fast Fill Pressure and Fast Fill Time should result in the actual pressure ramping up very quickly to, but never in excess of the touch point.

**Typical Pressure:** 3.0 - 5.0 Bar
**Typical Time:** 20-50ms

### Stable Fill
After the Pre-fill and Fast Fill phases are complete, any remaining Fill Time will be spent in the Stable Fill phase.

The pressure specified during Stable Fill is an **offset** of the clutch's touch point pressure. 

**Example:**
 - Touch Point = 1.3 Bar.
 - Stable Fill Pressure Offset = -0.1 Bar.

Stable Fill Pressure = 1.3 + -0.1 = 1.2 Bar.

**Typical Pressure Offset:** 0.0 Bar (Settle on the Touch Point)

---

## Torque Transfer Phase
The Torque transfer phase begins the process of transferring supplied engine torque over to the oncoming clutch. In most cases, the oncoming clutch will still be fully slipping by the end of the phase, but it will be holding most of if not all the torque.


---

## Inertial Sync Phase


---

## Upshift Phases

| Phase       | Time       | Oncoming Clutch | Offgoing Clutch |
| ----------- | ---------- | --------------- | --------------- |
| Prefill     | 0-100 ms   | Filling to a low pressure under the touch point. | Full torque capacity | 
| Fast fill   | 0-60 ms   | A high pressure is temporarily targeted to rapidly fill the clutch to it's touch point pressure. The pressure should not actually reach the high target, rather the increased solenoid opening speeds up the filling time. | Full torque capacity |
| Stable fill | 20-60 ms   | Clutch pressure is stablised to it's touch point. | Full torque capacity |  
| Transfer    | 50-200 ms  | Pressure is ramped up to torque transfer pressure over the desired time. At the end of the transfer phase, the oncoming clutch is holding the torque capacity, but is still fully slipping as the rest of the rotating components need to catch up.  | Bleeding off to touch point pressure |
| Inertial        | 50-300 ms  | Torque limits are now requested. Pressure is ramped up until slip is zero. The pressure should ramp just enough to linearly reduce slip to zero over the course of the target slip time. | Slowly bleeding off under touch point pressure |
| Hold        | 20-100 ms  | Ramping up to full torque capacity to ensure zero slip. Torque limits are lifted. | Fully bled off |   