---
tags:
- cadence
title: Using VCC and GND Symbols
---

You can use VCC (power) and GND (ground) symbols to connect power and ground instead of manually routing wires across your schematic. This is a common technique used by professional engineers to improve the readability of schematics.

1.  With a schematic open Design Entry CIS, click on the Vxx or GND buttons in the toolbar at the top or right side of the screen (see Figure 1)

    ![Figure 1: Place power and ground symbol buttons in the toolbar](/larger/image0258.png)

2.  Select the symbol you would like to use for your design and place it in your design (see Figure 2). You can rename power and ground symbols to assign them to a particular electrical net (e.g., +5V or +12V).

    ![Figure 2: +5V and GND symbols connected to a connector](/larger/image0259.png)

3.  In order to connect multiple components to the same power rail, place the same power or ground symbol with the same net name on your schematic (see Figure 3). Symbols that have different net names will **not** be connected.

    ![Figure 3: Example of +5V and GND symbols connected to multiple components. In this example, pin 1 of J1 is electrically connected to Pin 6 of U2, and Pin 2 of CON2 is electrically connected to pin 21 of U2.](/larger/image0260.png)

*Based on a tutorial written by Robert Goby and updated by Ryan Sparks (2020)*
