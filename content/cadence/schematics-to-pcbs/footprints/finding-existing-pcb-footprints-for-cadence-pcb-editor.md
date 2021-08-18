---
tags:
- cadence
- pcb
title: Finding existing PCB footprints for Cadence PCB Editor
---

## Where can I find a list of existing PCB footprints for Cadence PCB Editor?

While Cadence does have some built-in footprint libraries, they are limited due to the hundreds of thousands of different parts in existence. Additionally, most companies make their own footprints to match the specific manufacturing processes that they use.

In most cases, it is easier and faster to build your own custom footprints for all components. However, there are some built-in libraries that can be found in the following directory:

```
C:\Cadence\SPB_17.4-silent\share\pcb\pcb_lib\symbols
```

Within this folder, you can double-click on the .dra files to see footprints and the .pad files to see padstacks in PCB Editor.

Additionally, there is a [footprints document](https://drive.google.com/file/d/1zVosc_4U5ubucQU0fOhIIONPz780_0aY/view) that will show you most of the footprints that exist in the library.

## What are the most commonly used built-in padstacks?

There are a number of useful built-in through-hole padstacks located in:

```
C:\Cadence\SPB_17.4-silent\share\pcb\pcb_lib\symbols
```

that follow the naming convention:

pad(number1)(circle/square)(number2)d where

-   "number1" is the outer diameter of the copper ring outlining the pad (see Figure 1, blue ring),
-   "circle/square" is the shape of the pad (cir is most common for this class),
-   "number2" is the diameter of the hole in the center of the pad (see Figure 1, red circle)

![Figure 1: Example through-hole Padstack, where the blue ring is copper and the red is the hole](/larger/image0164.png)


For example, pad93cir56d.pad is a padstack with an outer copper ring diameter of 93 mils (not mm), and a center hole diameter of 56 mils.

For surface-mount padstacks, it is easiest to make your own using the Padstack Editor application.

## What are the most commonly used built-in footprints?

First, look in the manufacturer's datasheet for each component and identify the package type and footprint dimensions. Package type information is typically near the beginning or end of the datasheet. Footprint dimensions are typically near the end of the datasheet.

Once you have identified the package type and footprint dimensions, there are a number of useful built-in through-hole and surface mount footprints located in:

```
C:\Cadence\SPB_17.4-silent\share\pcb\pcb_lib\symbols
```

### Capacitors (through-hole)

-   cap196 - cylindrical vertical-mount capacitor (e.g., electrolytic, tantalum) with 100-mil center-to-center spacing between pins
-   cap300 - circular flat or rectangular vertical-mount capacitor (e.g., ceramic, film) with 300-mil center-to-center spacing between pins
-   cap400 - axial horizontal-mount capacitor with 400-mil center-to-center spacing between pins
-   cap600 - axial horizontal-mount capacitor with 600-mil center-to-center spacing between pins
-   cap1000 - axial horizontal-mount capacitor with 1000-mil center-to-center spacing between pins
-   cap1500 - axial horizontal-mount capacitor with 1500-mil center-to-center spacing between pins

### Capacitors (surface mount)

-   smc0805 - rectangular surface mount capacitor of size 0805 (0.08" x 0.05")
-   smc1206 - rectangular surface mount capacitor of size 1206 (0.12" x 0.06")
-   smc1210 - rectangular surface mount capacitor of size 1210 (0.12" x 0.10") 
-   smc1812 - rectangular surface mount capacitor of size 1812 (0.18" x 0.12")

### Diodes, inductors, resistors, and other axial-lead components (through-hole, horizontal mount)

-   res400 - resistor with a 400-mil center-to-center spacing between holes
-   res500 - resistor with a 500-mil center-to-center spacing between holes
-   res600 - resistor with a 600-mil center-to-center spacing between holes
-   res800 - resistor with a 800-mil center-to-center spacing between holes
-   res1000 - resistor with a 1000-mil center-to-center spacing between holes

### Headers and Jumpers (through hole)

-   jumper1 - 1-pin header
-   jumper2 - 2-pin header with 100-mil center-to-center spacing between pins
-   jumper3 - 3-pin single-row header with 100-mil center-to-center spacing between pins
-   jumper4 - 4-pin single-row header with 100-mil center-to-center spacing between pins
-   jumper5 - 5-pin single-row header with 100-mil center-to-center spacing between pins
-   jumper8 - 8-pin (4x2) double-row header with 100-mil center-to-center spacing between pins
-   jumper14 - 14-pin (7x2) double-row header with 100-mil center-to-center spacing between pins
-   jumper16 - 16-pin (8x2) double-row header with 100-mil center-to-center spacing between pins

### Resistors (surface mount)

-   smr0805 - rectangular surface mount resistor of size 0805 (0.08" x 0.05")
-   smr1206 - rectangular surface mount resistor of size 1206 (0.12" x 0.06")
-   smr1210 - rectangular surface mount resistor of size 1210 (0.12" x 0.10") 
-   smr2010 - rectangular surface mount resistor of size 2010 (0.20" x 0.10")
-   smr2512 - rectangular surface mount resistor of size 2512 (0.25" x 0.12")

### Test Points (used to provide easy access for a multimeter or oscilloscope probe) (through hole)

-   tp1 - square pad with round hole in the middle

### [Transistor Outline (TO) Package Types](http://eesemi.com/to-types.htm) (through hole)

-   to(number), where "number" is the number of the specific to case style from the component data sheet (e.g., a transistor with a to92 package type)

If your package type and footprint dimensions do not match one of those listed above, then you must [create your own custom footprint](/creating-custom-footprints/).
