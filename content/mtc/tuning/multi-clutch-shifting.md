---
title: "Multi-Clutch Shifting"
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

## Line Pressure
>[!IMPORTANT] DO NOT try to tune the shifting on a multi-clutch transmission by manipulating the Line Pressure.

Line Pressure should be sufficient to supply all the pressure the clutches need during a shift, but the clutches should control their own pressures. 

Clutch pressure can be considered a minimum value for the Line Pressure Target.

Some transmissions will require the Line Pressure to be set very high for the duration of a shift, giving maximum flow control to the clutch solenoids. 

> Depending on the transmission in question, setting the Line Pressure to "Downstream Pressure Offset" mode can simplify this process.

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

Pre-fill pressure does not usually exceed the touch point pressure.

**Typical Pressure:** 0.5 - 1.5 Bar
**Typical Time:** 0-100ms

> Setting the `Pre-Fill Time` to 0 will skip the Pre-fill phase.

### Fast Fill
![alt text](/assets/mtc/fast_fill.png)

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

### Up Shift & Overrun Down Shift
Torque is transferred to the oncoming clutch while the offgoing clutch is mostly released. By the end of the phase, the oncoming clutch will be carrying all the torque, but it will still be fully slipping at the offgoing gear speed.
It's the Inertial Sync phase's job to reduce the slip to zero.

![Up Shift Transfer Torque](/assets/mtc/transfer_torque.png)
> Note the engine speed is still matching Clutch A (offgoing) at the end of the transfer phase.

### Driven Down Shift
During a driven down shift, the offgoing clutch's torque capacity is reduced to deliberately introduce a controlled amount of slip that will bring the Input Shaft Speed up to the ongoing gear speed. 
As the clutch slip approaches zero, the oncoming clutch is ramped in to catch the input load, while the offgoing clutch is tapered out. 

By the end of the Transfer phase the oncoming clutch slip should be near zero. 

![Driven Down Shift](/assets/mtc/driven_down_shift.png)
> Driven Down Shift with ideal speed synchronization.

### Down Shift Rev Match
During a rev match, both the offgoing and oncoming clutch are reduced to zero torque capacity. They will both settle on their touch points, allowing the engine to freely rev.

As the oncoming slip approaches zero, the oncoming clutch is ramped in to catch the input torque load.

---

## Inertial Sync Phase
During this phase, clutch slip is reduced to near zero and the Input Shaft Speed is synced to the oncoming gear speed. Additional Torque capacity is applied to the oncoming clutch to achieve this.

The engine's inertia and torque is considered when calculating how much torque to apply to control the slip.

At high input torque, prolonged sync times will result in increased clutch heat and wear.

>[!INFO] The main "Gear" runtime will change to the next gear at the start of the Inertial Sync phase.

![Inertial Phase Torque](/assets/mtc/inertial_torque.png)
>The Engine Speed is now matching Clutch B (oncoming) at the end of the Inertial Sync phase.

### Torque Reductions
Any torque reduction that is enabled by the user is applied now to aid in syncing the Input Shaft Speed. Using torque reductions mean less clutch capacity is needed to achieve synchronization.

![Up Shift Torque Limit](/assets/mtc/up_shift_torque_limit.png)
> Up shift torque limit gets applied at the start of the Inertial Sync phase and is removed as slip approaches zero.

>[!TIP] If the engine continues to limit torque after the clutch is synced and locked, the shift will feel harsh.

---

## Lock Phase
The Lock phase is used to eliminate any remaining clutch slip. A user definable amount of additional torque capacity is applied to the clutch during the lock phase. 

---

## Shift Tuning
The torque modelled approach to shifting dramatically reduces the tuning complexity of gear shifts for the end user, provided the input torque is accurate and the Clutch Configuration is accurate.

The goal when tuning a shift is simply to achieve the slip target throughout the shift. If the slip is on target then the only thing left to do is dial in the feel by manipulating the shift target times.

The runtimes to watch are `Oncoming Clutch Slip Target` and `Oncoming Clutch Slip`. Ideally they should lay over each other.

If a shift feels harsh, check the slip curve. If the slip is on target, extend the shift times before looking for a way to alter the clutch pressure or clutch torque capacity.

![Ideal Shift Slip Example](/assets/mtc/shift_slip_ideal.png)
> Ideal clutch slip curve during an upshift.

### Touch Points
>[!IMPORTANT] It is critical that the Clutch Touch Points are setup at the outset. Poorly configured touch points will always lead to bad shifting and drivability.



