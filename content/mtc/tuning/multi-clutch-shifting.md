---
title: "Multi-Clutch Shifting"
draft: true
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