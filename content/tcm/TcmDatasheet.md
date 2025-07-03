---
title: "Praetor TCM Datasheet"
weight: 2
---

The Mectric Praetor TC24 is a fully programmable Transmission Control Module aimed at controlling the most complex driveline and transmission components. Designed with an over abundant amount of processing power to allow for the implementation of extremely complex, no compromise control strategies.

## Overview
 - 2x 650 MHz Automotive Processors
 - Tightly Coupled FPGA
 - 512 MB DDR3 RAM
 - 8 GB Data Logging Memory
 - Built-In PDM-Like power supplies
 - 8x Half-Bridge Auxiliary Outputs
 - 16x Low Side Proportional Current Solenoid Outputs
 - 4x Analogue Outputs
 - 16x Analogue Inputs
 - 16x Digital Inputs
 - 4x 2 Wire Hall Effect Wheel Speed Inputs
 - IMU (3 Axis Accelerometer & Gyroscope)
 - Onboard Barometric Pressure Sensor
 - 2x CAN 2.0A/B Busses
 - 1x RS232 Interface
 - 2x 5V Sensor Supplies
 - 1x 8V Sensor Supply
 - Ethernet PC Tuning

## Applications
 - DSG/DCT Transmissions

---

## Wiring Pinout
![Praetor TC24 Pinout](/assets/tcm/tcm_pinout.png)
> Looking into TCM

### Connector A
{{% badge style="info" %}}**Mating Connector**: TE 4-1437290-0{{% /badge %}}

| Pin     | Function    |
|---------|-------------|
| A1	  | ANV 1  |
| A2	  | ANV 2  |
| A3	  | ANV 3  |
| A4	  | ANV 4  |
| A5	  | ANV 5  |
| A6	  | ANV 6  |
| A7	  | ANV 7  |
| A8	  | ANV 8  |
| A9	  | Sensor GND |
| A10	  | ANV 9  |
| A11	  | ANV 10  |
| A12	  | ANV 11  |
| A13	  | ANV 12  |
| A14	  | ANV 13  |
| A15	  | ANV 14  |
| A16	  | ANV 15  |
| A17	  | ANV 16  |
| A18	  | DI 1  |
| A19	  | DI 2  |
| A20	  | DI 3  |
| A21	  | DI 4  |
| A22	  | DI 5  |
| A23	  | DI 6  |
| A24	  | DI 7  |
| A25	  | DI 8  |
| A26	  | DI 9  |
| A27	  | DI 10 |
| A28	  | DI 11 |
| A29	  | DI 12 |
| A30	  | DI 13 |
| A31	  | DI 14 |
| A32	  | DI 15 |
| A33	  | DI 16 |
| A34	  | Sensor GND |

### Connector B
{{% badge style="info" %}}**Mating Connector**: TE 4-1437290-1{{% /badge %}}

| Pin     | Function    |
|---------|-------------|
| B1	  | Aux 1  |
| B2	  | Aux 2  |
| B3	  | Aux 3  |
| B4	  | Aux 4  |
| B5	  | Aux 5  |
| B6	  | Aux 6  |
| B7	  | Aux 7  |
| B8	  | Aux 8  |
| B9	  | GND    |
| B10	  | Solenoid 1  |
| B11	  | Solenoid 2 |
| B12	  | Solenoid 3 |
| B13	  | Solenoid 4 |
| B14	  | Solenoid 5 |
| B15	  | Solenoid 6 |
| B16	  | Solenoid 7 |
| B17	  | Solenoid 8 |
| B18	  | Solenoid 9 |
| B19	  | Solenoid 10 |
| B20	  | Solenoid 11 |
| B21	  | Solenoid 12 |
| B22	  | Solenoid 13 |
| B23	  | Solenoid 14 |
| B24	  | Solenoid 15 |
| B25	  | Solenoid 16 |
| B26	  | Analog Out 1 |
| B27	  | Analog Out 2 |
| B28	  | Analog Out 3 |
| B29	  | Analog Out 4 |
| B30	  | Solenoid 1-4 Supply Output |
| B31	  | Solenoid 5-8 Supply Output |
| B32	  | Solenoid 9-12 Supply Output |
| B33	  | Solenoid 3-16 Supply Output |
| B34	  | GND |

### Connector C
{{% badge style="info" %}}**Mating Connector**: TE 3-1437290-7{{% /badge %}}

| Pin     | Function    |
|---------|-------------|
| C1	  | Battery Hot Supply  |
| C2	  | Aux 1-4 Supply  |
| C3	  | Aux 5-8 Supply  |
| C4	  | Solenoid 1-8 Supply  |
| C5	  | Solenoid 9-16 Supply  |
| C6	  | Ignition Switch  |
| C7	  | GND  |
| C8	  | CAN 1 Hi  |
| C9	  | CAN 2 Hi  |
| C10	  | Hall 1  |
| C11	  | Hall 2  |
| C12	  | Hall 3  |
| C13	  | Hall 4  |
| C14	  | CAN 1 Lo  |
| C15	  | CAN 2 Lo  |
| C16	  | 5V0 Ref Output 1  |
| C17	  | 5V0 Ref Output 2  |
| C18	  | 8V0 Ref Output  |
| C19	  | Sensor GND  |
| C20	  | Ethernet Rx+  |
| C21	  | Ethernet Rx-  |
| C22	  | Ethernet Tx+  |
| C23	  | Ethernet Tx-  |
| C24	  | RS232 Rx  |
| C25	  | RS232 Tx  |
| C26	  | GND  |

---

## Features

### Power Supply
 - Reverse polarity protection
 - Over temperature protection
 - Over current protection
 - Current & voltage diagnostic monitoring
 - 1x Battery constant supply
 - 2x Auxiliary output driver supplies
 - 2x Solenoid supplies
 - 1x Ignition switch input

### Processor
 - Duel 650 MHz, 32bit Automotive Processors
 - 512MB DDR3 RAM
 - Tightly coupled FPGA

### Analog Inputs
> 16x Analog Inputs
 - 0-5V
 - 12 bit, 1.22mV resolution
 - Switchable 1K pullups to 5V Out 1 on pins 1-8
 - Switchable 1K pullups to 5V Out 2 on pins 9-16
 - ~10K samples per second
 - 100K Ohms to ground
 - 24V tollerant

### Digital Inputs
> 16x Digital Inputs
 - 0.5 – 20KHz
 - 0-39V Analog Input on all pins
 - 12 bit, 9.52mV resolution
 - Hall effect & Reluctor sensor compatible
 - Switchable 4K7 pullups to 8.0V on all pins
 - Digital Input 1-8:
 - Programmable 0-5V low trigger thresholds
 - Programmable 0-5V high trigger thresholds
 -  Digital Input 9-16:
 -  Fixed low trigger threshold: 0.42V
 -  Fixed high trigger threshold: 2.40V


### Auxiliary Outputs
> 8x Auxiliary Outputs 
 - Half-Bridge Drivers
 - 0.1 – 20 KHz PWM
 - High Side / Low Side 35A peak, 15A continuous
 - Bi-directional current monitoring on all pins

### Solenoid Outputs
> 16x Proportional Current Solenoid Drivers
 - 0.1 – 20 KHz PWM
 - Low side only
 - 1.8A continuous
 - Current monitoring and control on all pins
 - Flywheel diodes connected to solenoid power supply outputs (see below)
 - Unused solenoid outputs can be used as low side auxiliary outputs


### Solenoid Power Supply Outputs x4
> 4x Protected Solenoid Supply Outputs
 - Protected and monitored solenoid supply pins
 - Over current protected
 - Current & voltage diagnostic monitoring

### Analog Outputs
> 4x Analog Outputs

---

## Programming
All device configuration and firmware updates are done via ethernet connection with our free MectriCal PC Software.
