---
title: Schematic checklist
---

Before exporting your schematic to create a PCB, you **must** verify the design and fix errors in the schematic first. It is significantly more difficult to fix errors later (either during the PCB layout stage or after manufacturing) than to spend the time double-checking the schematic first.

### Design for Function and Performance

1.  Check symbol pinouts against the data sheet, paying special attention to the part package (e.g., chips often come in multiple physical packages with different pin numbers)
2.  Check connector pinouts and orientation (top or bottom of board, inversion of pins)
3.  Check the data sheet for each part to ensure all support circuitry (e.g., external resistors for configuration) is present
4.  If an external oscillator or crystal is used, check that all support circuitry is present (e.g., low-ESR X7R capacitors)
5.  Check that crossing wires that should be connected have a dot at the intersection, and those that should not be connected do not have a dot
6.  For ICs, check that all power and ground pins are connected
7.  Run the schematic design rules check and resolve all errors

### Design for Reliability

1.  When using an analog to digital converter, it's a good idea to filter the signal in hardware first with a [band pass filter](http://www.electronics-tutorials.ws/filter/filter_4.html). This helps eliminate spurious noise that can corrupt your readings
2.  De-bounce all mechanical switches in hardware
3.  Check that all resistors have a wattage listed, and that wattage has at least a 50% margin
4.  Check that all capacitors have a working voltage listed, and that working voltage has at least a 25% margin
5.  Add a fuse to each power rail to help protect the circuit against accidental damage (e.g., shorting power and ground). Buy extra fuses.
6.  Power supply has a 25% current safety margin over the maximum calculated operating current

### For ICs, make sure:

1.  Bypass/decoupling capacitors are present for each chip. (0.1 uF ceramic for every power pin AND 1 uF, 10 uF, or 100 uF tantalum for every 10 to 20 ICs) (see [Bypass Capacitor Basics page](/bypass-capacitor-basics/))
2.  Pull up or pull down resistors are used, rather than hardwiring signal pins to power planes
3.  Pull up or pull down resistors are used on all unused IC inputs. One exception is microcontrollers, which should have unused I/O pins tied to test points

### Design for Testing

1.  Critical signals are connected to headers and/or test points to facilitate easy testing and debugging
2.  Test points are attached to key signals or unused pins that may be useful in the future (e.g., extra microcontroller I/O pins)
3.  Zero-ohm resistors are used in series on critical nets (e.g., power nets) to allow easy troubleshooting of circuit subsystems

### Design for Manufacturability/Service/Accessibility/Assembly

1.  Group components into labeled modules matching with the labels on the block diagram
2.  There is a way to connect power to each board (e.g., a connector)
3.  Connectors are used for off-board connections. Always include at least one ground wire/signal return path in connections between boards
4.  Check that in-system programming headers exist and include any required support circuitry (e.g., pull-up resistors). This information can be found in the microcontroller data sheet.
5.  Check that all components have a real part number (meaning you could copy and paste the part number into a distributor's search engine and return one part). Resistors, capacitors, and inductors can be labeled with their values (e.g., 0.1uF) instead of the full part number.
6.  Add a surface-mount LED and current-limiting resistor to each power rail to provide a visual indication that the power supplies are on
