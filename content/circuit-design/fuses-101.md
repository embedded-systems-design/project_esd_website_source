---
tags:
  - components
  - circuit-design
  - fuses
title: Fuses 101
---

## What are fuses and when do I need them?

A fuse is an electronic component that protects a circuit by creating an open circuit if it draws too much *current*. **Fuses do not protect against voltages that are too high. **

Fuses are most useful around power supplies, both when power comes into a system and on individual power rails. For example, if you have a 12V rail that should only draw 750 mA and a 5V rail that should only draw 400 mA, you might put a 750 mA fuse in series with the 12V supply output and a 500 mA fuse in series with the 5V supply output.

A common mistake that fuses protect against is accidentally shorting the power rail to ground (e.g., with a DMM probe as you are trying to touch the correct pins). This causes an infinite amount of power to be drawn from the power supply, and can sometimes damage or destroy voltage regulators or power supplies.

## What are the most common types of fuses?

**Standard fuses** contain a small piece of wire made of an alloy that melts readily. If the current gets too high, it burns out and opens the circuit. Standard fuses come in many different shapes and sizes.

-   **Advantages:** Inexpensive, replaceable
-   **Disadvantages:** Must be replaced when blown, sometimes no visual indication that they are blown
-   [Examples from Littelfuse](http://www.littelfuse.com/products/fuses.aspx)

**Resettable PTC fuses** are tripped by heat caused by current above the rating of the fuse. If the current flowing through the fuse goes above its rating, the fuse changes from having very low resistance to having a high resistance (thereby stopping the flow of current through the circuit). It is self-resetting after power is removed and the fuse cools.

-   **Advantages:** Reusable, useful when cause of overcurrent is a user failure (e.g., plugging a connector into the wrong pins on a PCB)
-   **Disadvantages:** More expensive than standard fuses, small leakage current after breaking, significantly lower voltage ratings (60V) compared with non-resettable fuses (600V)
-   [Examples from Littelfuse](http://www.littelfuse.com/products/resettable-ptcs.aspx)

**Circuit breakers** are typically used in AC power applications like homes.

-   **Advantages:** Reusable and easy to reset by hand. This reduces downtime and repair costs. Easy-to-see indication of whether the circuit breaker is tripped. Useable as an on-off switch.
-   **Disadvantages:** Very expensive, not well suited for low-voltage DC applications
