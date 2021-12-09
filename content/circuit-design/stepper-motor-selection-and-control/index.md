---
title: Stepper Motor Selection and Control
tags: 
  - circuit-design
  - motors
---

## Stepper Motor Selection 

There are four variables to consider when selecting a stepper motor

-   Load requirements for the project
-   Voltage and current needs
-   Right size
-   Polarity Type

Stepper motors should be used over DC motors when torque is needed at low speeds or precise motor input is needed. Stepper motors use 40 or more poles in its rotation of 360 degrees. This means each pole can relate to 9 degrees (example of 40 pole stepper) and using code the stepper motor can be called to rotate to an exact position. Project load for the stepper should not exceed the steppers max torque specs. A safety margin should be included in this evaluation.

Stepper motors have specific power requirements. Supplying a voltage that is too low for a stepper will impact its performance. Supplying a voltage that is too high will damage the stepper and even the microcontroller. Current should be supplied within the steppers specified rating. Stepper motors are rated per phase, so the current per phase needs to be multiplied by 2 to meet the current demands.

## Wiring a Stepper Motor

4 Wire Stepper

![][1]

6 Wire Stepper

Similar to 4 wire stepper. Add tap placed between either end of each phase. (Only some motors) Motors that do not require center taps can be wired like a 4 wire stepper.

![][2]

## What to do when Stepper has no Torque 

If a stepper motor keeps stalling or has lower torque than expected there could be a problem with the initial setup of the motor. Below lists a few things toi check if a stepper isnt working as intended.

-   Wiring Issue
-   Wrong voltage supplied
-   Profile of motion defined wrong (pole calculations

  [1]: image2.png 
  [2]: image1.png 
