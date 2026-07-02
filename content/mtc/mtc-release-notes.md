---
title: "MTC Release Notes"
weight: 2
---

## MTC v0.29.1
*03/07/2026*

 - Added solenoid output pairing for > 1.5A current targets.
 - Added solenoid fault status detection.
 - **BREAKING CHANGE:** Converter lockup now torque based with lock/unlock request tables. *Import the included module file as a starting point.*
 - Refactored takeup system and added clutch by wire cooldown timer.
 - Fixed R35 Shifter D to R logic bug.
 - Made DI 1-8 pulldown control accessible from switch and analog input functions.
 - Clutch learned capacity scaler tables can now use Gear on the Y axis.
 - Rewrote shift fork management to allow a fork to control gears on both clutch axes (Required for GS7 DCT).
 - Clutch capacity calculation now differentiates between single sided and double sided clutch disc counts.
 - R35 GTR Build tested and working with OEM R35 ECU *(Requires Emtron build package)*.
 - Added supply voltage lockout to solenoid driver banks to avoid damage caused by incorrect wiring back-feeding voltage through flywheel diodes.
 - Fixed takeup up/down shift lockout not working.
 - Updated 8HP base cal file.
 - Updated GR6 base cal file.

---

## MTC v0.26.0
*10/06/2026*

 - Added 16x General Purpose User Inputs
 - Device Label now stays with the device and is not changed when a cal file is uploaded.
 - Renamed "Clutch Input Torque" to "Input Shaft Torque".
 - Updated torque converter torque model.
 - Added Takeup bleed off enable table.
 - Internal Torque Model Enabled *(Experimental)*.

---

## MTC v0.25.1
*19/05/2026*

 - Added Clutch Gear Load Factor Table
 - Updated 8HP Base calibration

---

## MTC v0.24.0
*07/05/2026*

**Public Beta Release**
Includes:
 - Nissan GR6 Base calibration
 - ZF 8HP Base Calibration