---
title: "FAQ"
weight: 1
draft: true
---

## Supported Transmissions
The MTC16 has been designed to be as universally applicable as possible. In much the same way that an aftermarket engine management system doesn't specifically what engine it's running, the MTC16 is never explicitly set to run a specific transmission. Instead each applicable input, output and sub system is configured on a case by case basis. 

The MTC16's firmware is fully configurable in every aspect, with almost nothing hidden behind presets or obfuscated away from the tuner. This means that in practice it's theoretically possible to control most common modern transmissions, once you have physical control of the hardware (in some cases this will involve removing and bypassing mechatronics units). 

Building a transmission config from scratch is a complex task that requires significant knowledge of all systems involved, but it is very much possible.

We are testing and building applications specific configurations in-house which will dramatically speed up the process of commissioning and tuning your transmission. Below is a list of the transmission that we're focussing on. If you transmission isn't in the list, that doesn't mean it cannot be supported, it just means you might have to attempt it yourself.

### Transmission Development Status
| Transmission   | Type         | Status       | Base Cal | Notes |
| -------------- | ------------ | ------------ | -------- | ----- |
| [ZF 8HP](./transmissions/zf-8hp.md) | Multi-clutch | Supported    | Included |       |
| [Nissan GR6](./transmissions/nissan-gr6.md) | DCT          | Supported    | Included |       |
| Getrag GS7     | DCT          | Testing      | TBA      |       |
| Porsche PDK    | DCT          | Planned      | TBA      |       |
| VW DQ500       | DCT          | Planned      | TBA      |       |
| Tremec TR-9080 | DCT          | Planned      | TBA      |       |
| Audi DL800     | DCT          | Planned      | TBA      |       |
| GM 6L80E       | Multi-clutch | Planned      | TBA      |       |
| Ford 6R80      | Multi-clutch | Planned      | TBA      |       |
| Ford 10R80     | Multi-clutch | Planned      | TBA      |       |