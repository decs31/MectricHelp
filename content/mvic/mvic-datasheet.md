---
title: "MVIC Datasheet"
params:
    menuPre: '<i class="fa-regular fa-file-lines"></i> '
---

The Mectric Vehicle Integration Controller (MVIC) is a fully featured, user definable, programmable CAN translation unit. It's 2x CAN 2.0B/FD interfaces can be configured to send and receive a virtually limitless combination of data. Powerful firmware and an intuitive user interface allows the generation of thousands of predefined and custom channels.

## Applications
 - Integration of aftermarket ECU's with OEM systems.
 - Integration of cross-brand aftermarket systems.
 - Complex custom logic control for extending existing system controls.
 - Reverse engineering.
 - CAN protocol prototyping.

---

## Wiring Pinout
![MVIC Connector Pinout](/assets/mvic_pinout.png)
> Mating Connector: Deutsch DT06-6S

| Pin | Function    |
|-----|-------------|
| 1	  | GND         |
| 2	  | CAN 1 Low   |
| 3	  | CAN 2 Low   |
| 4	  | CAN 2 High  |
| 5	  | CAN 1 High  |
| 6	  | +14V        |

---

## Features
### Processor
 - 96 MHz, 32bit Automotive Processor w/ FPU.
 - 2x Controller Area Network (CAN) interfaces, up to 5 Mbit/s
 - Compatible with CAN 2.0A/B and CAN-FD (ISO 11898-1:2015)
 - USB-C PC interface.
 - Configuration, live data, firmware updates over USB.

### CAN
 - 2x CAN FD Hardware Nodes.
 - Over voltage & ESD protected.
 - Fully user definable CAN streams.
 - Compound message frames and sequential ID frames supported.
 - User definable Rx/Tx parameters with custom bit lengths, factor, & offset.
 - Predefined standard transmit and receive data sets.

### Firmware
 - Multi-threaded Realtime Operating System.
 - User CAN Signal Objects w/ user defined bit positions, factor, offset, multiplexing.
 - Dynamic 4D Tables w/ freely configurable X,Y,Z axes.
 - Math Expression Parsers, 32 characters, including math, logic and bitwise operations.
 - Combinational Logic Blocks, 4 inputs per block, on/off delays.
 - CAN bus diagnostics and error detection.

### MecScript
 - C-Style syntax.
 - Statically typed.
 - Heap-less, memory safe design.
 - Non-interpreted, compiled to byte-code before upload to device.
 - 64kb of Compiled User Code Storage (ROM).
 - 64kb of User Code Stack Memory (RAM).
 - Edit in MectriCal or in external editors such as VS Code.

---

## Programming
All device configuration and firmware updates are done via USB-C connection with our free MectriCal PC Software.

---

## Device Specifications
| Parameter	                    | Value                         |
| ----------------------------- | ------------------------------|
| Processor	                    | 96 MHz, 32 Bit, Cortex M4F w/FPU |
| Script Memory Storage         | 64 Kb                         |
| CAN                           | 2x 2.0A/2.0B/FD               | 
| Connector	                    | 6 Pin Deutsch DT Series       |
| Nominal Supply Voltage Range  | 9 - 22 V                      |
| Minimum operating voltage	    | 6 V                           |
| Maximum operating voltage	    | 35 V 1                        |
| Supply Current                | 15 mA                         |
| Size                          | 84mm L, 53mm W, 32mm H        |
| Weight                        | 130g                          |
| Mounting                      | 2x M5 Mounting Holes          |
| Minimum operating temperature	| -40 °C                        |
| Maximum operating temperature	| 105 °C                        |
| Minimum component automotive qualification | AEC-Q100 Grade 2 |

