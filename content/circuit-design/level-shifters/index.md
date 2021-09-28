---
title: Level shifters
tags: 
  - circuit-design
  - level-shifters
---

What is a level shifter?

A level shifter either shifts the voltage of a data line up or down depending on what your circuit entails.

Why?

The most common type of level shifter is one that shifts 5v logic down to 3.3v logic. If a level shifter is not used the receiver of the logic will be irreparably damaged. If you do not know if you need this, check your data sheet! Look for a phrase such as "3.3v tolerant"

Shift down level shifter

For the example above, you would need a shift down level shifter. There are many ways to do this, but the easiest way is to create a voltage divider as seen in Figure 1. This is the easiest and cheapest way to construct a low power level shifter and will be adequate for most projects. A good way to calculate this is use V=IR. In this case first solve for current with 5v which is 5/3000 = 1.6ma then use that to solve for 3 = R2 \* 1.6e-3 = approximately 2k. then just subtract r2 from rtot for r1.

![][1]

Figure 1

Shift up level shifter.

This level shifter does the exact opposite of the shift down, it boosts the signal voltage. A nice easy way to do this would be to use a transistor as seen in Figure 2. Keep in mind that the transiter will be able to give decent amount off current so it will be a good idea to put a current limiting resistor if your situation calls for it. This one is a little nicer than the shift down as you need to make the DesiredSignalLevel as seen in Figure 2 the correct voltage and the circuit does the rest.

![][2]

Figure 2

Level sifting ICs

Level shifting ICs address the main problem with the above circuits. The above circuits are one way only. Bidirectionality is extremely important for 2-way connections like UART. For a level shifting IC you need to look at the data sheet to make sure it is acceptable for your usage. Make sure it can handle both voltages before you commit to it. A good example is the LSF0102-Q1. This was chosen as one of its primary bidirectional functions is 3v-5v which is extremely common. link to data sheet: <https://www.ti.com/lit/ds/symlink/lsf0102-q1.pdf?HQS=dis-dk-null-digikeymode-dsf-pf-null-wwe&ts=1618807473804>

This specific IC has 2 lanes of level shifters. You may want more so check your project before purchase. It is recommended to find an IC with a typical application section as the usage of the pins of some ICs are not immediately clear. This specific IC needs its EN pulled to GND to enable the input, and since all data pins are inputs, it essentially turns off the chip. You then have your A and B lanes, do not mix them up. A1 and A2 are both inputs and outputs on the same line. This is where you put your data lines. Then to change how the IC shifts the voltage you will need to calculate the voltages that need to be on the vref pins for that specific ic. A good way to get those voltages is using the voltage divider seen in Figure 1.

  [1]: image1.png
  [2]: image2.png
