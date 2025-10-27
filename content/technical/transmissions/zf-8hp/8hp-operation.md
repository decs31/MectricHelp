---
title: "ZF 8HP Operation"
draft: true
---

## Solenoids
The ZF 8HP contains nine solenoids. All but the park-release/hold solenoids are Variable‐Force Solenoids (VSF). The park‐release and park‐hold are on/off.

### Shift Elements
The 8HP uses the following "shift elements":
 - Two fixed multidisc brakes (brake A and B)
 - Three rotary multidisc clutches (clutch C, D and E).

The multidisc clutches (C, D and E) feed the drive torque to the planetary gear. The multidisc brakes (A and B) support the torque against the transmission housing.

| Solenoid             | Shift Element | Note                                            |
| -------------------- | ------------- | ----------------------------------------------- |
| **Shift Solenoid A** | Brake A       | VFS, normally vented (no pressure when off).    |
| **Shift Solenoid B** | Brake B       | VFS, normally vented (no pressure when off).    |
| **Shift Solenoid C** | Clutch C      | VFS, normally applied (high pressure when off). |
| **Shift Solenoid D** | Clutch D      | VFS, normally applied (high pressure when off). | 
| **Shift Solenoid E** | Clutch E      | VFS, normally applied (high pressure when off). | 

### Line Pressure Solenoid
VFS, normally applied. Modulates the valve-body pressure regulator to maintain the transmission’s main hydraulic (line) pressure under all operating conditions. 

### Torque Converter Clutch (TCC) Solenoid
VFS, normally vented. Controls apply pressure to the lock-up piston in the torque converter for smooth lock/unlock transitions. 

### Park Release Solenoid
On/Off, normally open. When energized, it directs line pressure to the park-release valve to retract the parking pawl, allowing selection of Drive or Reverse. 

### Park Hold Solenoid
Mechanical. Clips onto and holds the park-release piston in its disengaged position after the pawl is withdrawn. Does not flow hydraulic oil. 

--- 

## Gear Sequencing
 By engaging different combinations of the five shift elements listed above, the transmission obtains each of its eight forward ratios (plus reverse). 

| Gear | Brake A | Brake B | Clutch C | Clutch D | Clutch E |
| ---- | :-----: | :-----: | :------: | :------: | :------: |
| P    |    ✓    |    -    |     –    |     -    |     –    |
| R    |    ✓    |    ✓    |     –    |     ✓    |     –    |
| N    |    ✓    |    -    |     –    |     -    |     –    |
| 1    |    ✓    |    ✓    |     ✓    |     –    |     –    |
| 2    |    ✓    |    ✓    |     –    |     –    |     ✓    |
| 3    |    –    |    ✓    |     ✓    |     –    |     ✓    |
| 4    |    –    |    ✓    |     –    |     ✓    |     ✓    |
| 5    |    –    |    ✓    |     ✓    |     ✓    |     –    |
| 6    |    –    |    –    |     ✓    |     ✓    |     ✓    |
| 7    |    ✓    |    –    |     ✓    |     ✓    |     –    |
| 8    |    ✓    |    –    |     –    |     ✓    |     ✓    |
