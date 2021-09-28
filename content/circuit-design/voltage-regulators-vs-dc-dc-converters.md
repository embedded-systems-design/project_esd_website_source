---
title: Voltage Regulators VS DC-DC converters
tags: 
  - circuit-design
  - power-supplies
---

## How do I choose a voltage regulator?

There are three major types of voltage regulators that you will encounter in this program:

-  Linear voltage regulator - burns off extra power in the form of heat
    -  Advantage: High current capacity
    -  Advantage: Low cost
    -  Disadvantage: Low precision
    -  Disadvantage: High dropout voltage (the voltage difference between the input and output)
-  Low dropout voltage regulator - burns off extra power in the form of heat, but continues to regulate even when the input voltage is near the output voltage
    -  Advantage: Excellent for battery-powered applications
    -  Advantage: Higher precision
    -  Disadvantage: Lower current capacity
    -  Disadvantage: Higher cost
-  Switching voltage regulator - generates as much power as is needed by the circuit, up to the maximum allowed by the regulator. Similar to Switching Power Supplies above
    -  Advantage: Highly energy efficient
    -  Disadvantage: High cost
    -  Disadvantage: External components (some difficult to find) may be necessary
    -  Disadvantage: Printed circuit board layout can be difficult
-  DC-DC Converter - An Isolated power converter. (No electrical connection between input and output) 
    -  Advantage: Can be used on sensitive equipment that need an isolated power supply
    -  Disadvantage: Requires more testing to guarantee isolation. 
    -  Disadvantage: External components (some difficult to find) may be necessary
    -  Disadvantage: Noise due to PWM signal switching 

A highly detailed guide to linear and switching regulators is available here: <http://www.ti.com/lit/an/snva558/snva558.pdf>

## When should I use a DC-DC Converter? 

A DC-DC converter should be used when the following is needed: 

-  Higher efficiency (95% when compared to linear voltage regulator of 65%)
-  Power that can be stepped up or stepped down 
-  A moderate - high max voltage output. 

