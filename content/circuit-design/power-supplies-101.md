---
title: Power Supplies 101
tags:
  - circuit-design
  - noise
  - power-supplies
---

## What are the components of a basic power supply subsystem?

1.  Source of power - battery, AC adapter, solar
2.  Input electronic noise filtering circuit
3.  Voltage regulator to provide a constant supply voltage
4.  Output electronic noise filtering circuit

## What are the design considerations for a battery-operated circuit?

How many Amp-Hours of capacity are needed?

-   Create a power budget to determine

What type of batteries?

-   See [Battery University](http://batteryuniversity.com/) for more information

Are the batteries rechargeable?

-   NiCd, NiMH, LIB, LiPoly? Different tradeoffs of cost, memory, lifetime, weight
-   Need a charging circuit. See [Maxim Integrated Circuits](https://www.maximintegrated.com/en/products/power.html)

Discharge Rate

-   Batteries can only discharge up to a certain limit to remain safe.  Different chemistries have different limitations.

## What are the design considerations for an AC-powered circuit?

The language "AC adapter" and "AC power supply" is used inconsistently. Sometimes it refers to regulated power supplies with a fixed voltage output, and sometimes it refers to unregulated power supplies with a promised voltage output that is inaccurate when measured with a DMM. More information on AC power adapters is available here: <http://www.dxing.info/equipment/wall_warts_bryant.dx>

### Linear Power Supplies

Linear power supplies are made up of a transformer, diodes, and sometimes a filter capacitor. They provide clean power, but waste lots of energy in the form of heat. See <http://www.allaboutcircuits.com/textbook/semiconductors/chpt-3/rectifier-circuits/> for more information on how a linear power supply works.

### Switching Power Supplies

Switching power supplies are most commonly used in PCs and other digital applications. They have a "noisy" power output because of the switching frequency, and are not ideal for inductive loads. They also tend to be more expensive, but are much more energy-efficient and generate less heat.

## How do I choose a voltage regulator?

There are three major types of voltage regulators that you will encounter in this program:

Linear voltage regulator - burns off extra power in the form of heat

-   Advantage: High current capacity
-   Advantage: Low cost
-   Disadvantage: Low precision
-   Disadvantage: High dropout voltage (the voltage difference between the input and output)

Low dropout voltage regulator - burns off extra power in the form of heat, but continues to regulate even when the input voltage is near the output voltage

-   Advantage: Excellent for battery-powered applications
-   Advantage: Higher precision
-   Disadvantage: Lower current capacity
-   Disadvantage: Higher cost

Switching voltage regulator - generates as much power as is needed by the circuit, up to the maximum allowed by the regulator. Similar to Switching Power Supplies above

-   Advantage: Highly energy efficient
-   Disadvantage: High cost
-   Disadvantage: External components (some difficult to find) may be necessary
-   Disadvantage: Printed circuit board layout can be difficult

A highly detailed guide to linear and switching regulators is available here: <http://www.ti.com/lit/an/snva558/snva558.pdf>

## What capacitor values should I use for input and output noise filtering?

First, check the data sheet for the voltage regulator and see if it specifies values for the input and output filtering capacitors. If it does not, the rule of thumb is to use 0.33 ÂµF ceramic non-polarized capacitors for input filtering and 0.1 ÂµF ceramic non-polarized capacitors for output filtering.

## What capacitor values should I use for bypass filtering near each integrated circuit?

Digital integrated circuits (ICs) need "bypass capacitors" to both filter the power going into the IC and provide a nearby reservoir of energy that the IC can draw from instantaneously. The rule of thumb is to put one 0.1 ÂµF ceramic non-polarized capacitor between each power pin on an integrated circuit and ground. This means a microcontroller might have 2 - 8 or more capacitors, one for each power pin on the IC.

## Where can I find additional information about power supplies?

-   [Wikipedia](https://en.wikipedia.org/wiki/Power_supply)

## Where can I find companies that manufacture power supply components?

-   [Sources for Electrical and Electromechanical Components](/sources-for-electrical-and-electromechanical-components/)
