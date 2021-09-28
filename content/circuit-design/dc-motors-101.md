---
title: DC Motors 101
tags:
  - circuit-design
  - motors
---

#### [Watch the video mini-lecture on DC motor control from Dr. Jordan](https://youtu.be/nMhxy2hxcKs)

<iframe width="560" height="315" src="https://www.youtube.com/embed/nMhxy2hxcKs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## What types of DC motors are most common?

-   Brushed DC motors. Current flowing in one direction makes the motor turn one direction, and current flowing in the opposite direction makes the motor turn the opposite direction.
-   Stepper motors - provide absolute position control but require a special controller IC
-   Servo motors - PWM signal controls the position of the motor

## How do I connect a brushed DC motor to a microcontroller?

DC motors are inductive loads and therefore cannot be directly connected to a microcontroller without damaging the microcontroller. There are two protection mechanisms that go into a successful motor interface:

1.  [Back EMF / flyback diode](https://www.electronicshub.org/flyback-diode-or-freewheeling-diode/) - protects against current spikes that can damage a microcontroller. Use "rectifier" diodes (e.g., 1N400x series)
2.  [H-bridge](http://modularcircuits.tantosonline.com/blog/articles/h-bridge-secrets/h-bridges-the-basics/) - switches current on or off to the motor, and changes the direction of the motor

The [LMD18200](http://www.superdroidrobots.com/product_info/LMD18200.pdf) is a common off-the-shelf H-Bridge IC.

## How do I change the speed of the motor?

Generate a [Pulse Width Modulation (PWM)](https://learn.sparkfun.com/tutorials/pulse-width-modulation) signal from your microcontroller and use it to control the H-bridge.

## How does a stepper motor work?

See the excellent animated GIFs in the [Stepper motor entry on Wikipedia](https://en.wikipedia.org/wiki/Stepper_motor)

## How do I connect a stepper motor to a microcontroller?

Use an off-the-shelf driver IC instead of trying to build your own driver. The [DRV8825](https://www.pololu.com/file/0J590/drv8825.pdf) is a common stepper motor control chip.
