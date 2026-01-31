---
title: "FAQ"
weight: 1
draft: true
params:
  menuPre: '<i class="far fa-question-circle"></i> '
---

## Supported Transmissions
The TCM has been designed to be as universally applicable as possible. In much the same way that an aftermarket engine management system doesn't really know what engine it's running, the TCM is never explicitly set to run a specific transmission. There's no "Select your transmission" option anywhere. Instead, each applicable input, output and sub system is configured on a case by case basis to build a full configuration. Different transmissions will use different combinations of sub systems. 

The TCM's firmware is fully configurable in every aspect, with almost nothing hidden behind presets or obfuscated away from the tuner. This means that it is theoretically possible to control most modern transmissions, once you have physical control of the hardware (in some cases this will involve removing and bypassing mechatronics units). 

Building a transmission config from scratch is a complex task that requires significant knowledge of all systems involved, but it is very much possible.

We are testing and building applications specific configurations in-house which will dramatically speed up the process of commissioning and tuning your transmission. Below is a list of the transmission that we're focussing on. If you transmission isn't in the list, that doesn't mean it cannot be supported, it just means you might have to attempt it yourself.

### Transmission Development Status
| Transmission   | Type         | Status       | Base Cal | Notes |
| -------------- | ------------ | ------------ | -------- | ----- |
| [ZF 8HP](./transmissions/zf-8hp.md) | Multi-clutch | Supported    | Included |       |
| [Nissan GR6](./transmissions/nissan-gr6.md) | DCT          | Supported    | Included |       |
| Getrag GS7     | DCT          | Testing      | Coming Soon      |       |
| Porsche PDK    | DCT          | Planned      | TBA      |       |
| VW DQ500       | DCT          | Planned      | TBA      |       |
| Tremec TR-9080 | DCT          | Planned      | TBA      |       |
| Audi DL800     | DCT          | Planned      | TBA      |       |
| GM 6L80E       | Multi-clutch | Planned      | TBA      |       |
| Ford 6R80      | Multi-clutch | Planned      | TBA      |       |
| Ford 10R80     | Multi-clutch | Planned      | TBA      |       |

## Supported ECU Platforms
We have worked very closely with [Emtron Australia](https://emtron.world) to create a seamless CAN integration that allows for fully torque modelled shifting and down shift rev-matching with minimal setup complexity. This is the best way to achieve an OEM quality driving experience.

Additionally, the TCM also has a two fully open and configurable CAN bus nodes, meaning that users can send and receive any data required in any format to integrate almost any third party ECU. The level of control available is ultimately up to the ECU in question and will vary from extremely crude to fully featured depending on the ECU in question.

Critical signals such as Engine Speed and Throttle Position can also be inputted via physically wired inputs.

For optimal results, it is strongly recommended that the engine ECU be capable of modelling and reporting accurate engine torque as well as abiding by torque reduction requests and meeting down shift rev match targets. If the ECU is incapable of modelling torque, the TCM has it's own torque model that can calculate accurate engine torque from as little as an injector duty cycle value.

## CAN Integrations

As well as a fully user definable CAN bus, the TCM does have some preset CAN data sets which are always being added to over time.

**Available CAN Presets**

| Preset                      | Direction | Note   |
| --------------------------- | --------- | ------ |
| Emtron Transmission Control | Rx & Tx | Used for Emtron torque modelled CAN integration |
| Emtron Predefined Tx Set 1  | Rx      |  |
| Emtron Predefined Tx Set 2  | Rx      |  |
| Emtron Predefined Tx Set 3  | Rx      |  |
| Link Generic Dash           | Rx      |  |
| Nissan R35 GTR TCM          | Rx & Tx | Free when used with an Emtron ECU. Unlock required for use with other ECU platforms. |

## Shifter Inputs
The TCM can use a wide variety of shifters including CAN bus, analog, digital switch arrays, individual switches, CAN keypads, or combinations of any of the aforementioned input types.

For more information on Shifter Inputs and Drive Modes, refer [here](./tuning/drive-modes.md).

## Drive Modes and Map Switching
Shift tables can be switched using inputs from CAN bus, rotary switches, fixed switches, sensor input and user logic.

Table axes can be set to any one of over 1500 channels allowing a virtually limitless amount of flexibility.

## Output Duty Cycle vs Amperage
The majority of transmission related output functions generate a target current setpoint in amps, rather than a fixed PWM duty cycle.

When a solenoid is commanded draw a certain current, it's physical position is extremely consistent, resulting in a stable and repeatable position regardless of system voltage and temperature variables. If a fixed duty cycle were used, the transmission may work well one day, and poorly the next.

Every output pin can be used in current control mode, including auxiliary outputs.

User Functions can configured to output either a traditional PWM waveform, or a current setpoint.

## Unused Solenoid Output Pins
Unused solenoid output pins can be used as auxiliary outputs for any purpose, including User Functions. 

Solenoid pins have a maximum PWM frequency of 20 KHz.

## Unused Input Pins
Unused analog and digital input pins can be used as general purpose inputs.

Analog input pin voltages are measured at all times.

Digital input pin voltage, frequency, duty cycle, pulse width, period, and level are measured at all times.

Pin channels are free to be transmitted via CAN, effectively turning the TCM input an input expander.