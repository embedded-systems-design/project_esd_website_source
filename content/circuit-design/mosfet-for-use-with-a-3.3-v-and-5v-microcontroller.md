---
title: MOSFET for use with a 3.3V and 5V Microcontroller
tags: 
  - circuit-design
  - transistors
  - mosfet
---

## Selecting the MOSFET

When selecting a MOSFET for either 3.3V or 5V applications there are three parameters to consider.

-   Continuous drain Current (Id)
    -   Amount of current the MOSFET can handle.
-   Drain Source Voltage (Vds)
    -   Voltage rating of the MOSFET (Do not exceed this value)
-   Threshold Voltage (Vgs(th) )
    -   Gate that will switch MOSFET on. (This value should be in the midrange of your microcontroller\'s power value. 1.7V(3.3V) or 2.4V (5V) min)

A load must always be on the drain side of the MOSFET due to the gate and source being hard connected inside of the MOSFET itself.
