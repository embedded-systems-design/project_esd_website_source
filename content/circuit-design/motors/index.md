---
title: Motors
tags: 
  - circuit-design
  - motors
---

There are many types of motors out there each with their own pros and cons. There are two main types of motors, brushed and brushless, each with many subcategories within them. In this we will only be going over the most common types and their control. These include DC brushed, stepper, and 3-phase brushless.

**DC motors**

This is the simplest and most often the cheapest motor to use for a project. these have excellent torque and speed and are good enough for most projects. This motor is a good jack of all trades option. The down sides of this motor are its mediocre efficiency compared to other motors, its electronically noisy, and has a shorter life span due to its brushes.

![][1]

Control

There are many ways to control this type of motor depending on your use case. If you just need it turn on or off, you could simply use a single transistor/MOSFET. If you want to control the direction of the motor, you will need to make an H-bridge or use a dedicated chip such as the L293d. to control the speed of the motor you can use PWM on your transistor switch or H-bridge. Remember to use a flyback diode as these motors create nasty voltage spikes on startup and braking. Those flyback diodes ensure those spikes are absorbed back into the system as opposed to the control transistors/MOSFETS. Below is a typical application circuit from the L293d chip link: <https://www.ti.com/lit/ds/symlink/l293d.pdf?ts=1618773924301&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FL293D>

![][2]

Extra

A good addition to these motors is a rotary encoder. These use magnetic sensors that are attached to the output of the motor to allow you to know how fast the motor is spinning. This is especially useful with PID control.

It is also a good idea to pick a gearbox for your motor to either increase the torque or speed of the output shaft. DC motor gearboxes are extremely cheap and reliable.

Stepper

These motors are extremely efficient and have good torque but are mainly used for their excellent positioning. The shaft of these motors have special magnetic "teeth" on their shaft that allow them to make single "steps" at a time. This is useful for high precision applications such as 3d printers, CNC machines, and other precision machinery.

![][3]

Control

These motors are most easily controlled using a dedicated chip and to accurately use that chip refer to its datasheet. The good thing is many dual h-bridge chips have support for stepper motor driving. The basic principle behind its control is that there are two separate coils in the steeper motor. You need to power one coil after the other to get it to move from step to step. If you turn on one coil, but do not advance, this locks the motor in place, in this state it will not move unless a sufficient force is applied to overcome its magnetic field. This is different for each motor and can be solved with a gearbox.

![][4]

Extra

While stepper motors are accurate, remember to add a limit switch to determine where the motor is if your application requires that. Another thing to keep in mind is that once a stepper is over torqued your microcontroller will get confused where the motor is and this could potentially lead to the project breaking itself.

3-phase brushless.

These motors are top of the line in efficiency and torque. These motors are often referred to as Brushless DC motors. The main downside of these motors is their low start torque and their high price. Their high price is mainly due to their better-quality construction and their expensive control circuits. For most of your projects, most of these types of motors will take up your entire budget. There is one breed of 3-phase brushless that is cheap and easy to use for projects, PC fans. These fans use a 3-phase motor paired with a low power control circuit.

![][5]

![][6]

Control.

A PC fan only should be turned on or off unless there is a dedicated PWM pin as seen in the picture above or you use a more analog approach by changing the voltage of the power source. Do NOT try to use an H-bridge or anything else to reverse the polarity as this may damage the internal circuitry of the PC fan. Note: pc fans cannot be used as a generator as their control circuits will most likely block whatever power they generate, or the output voltage will be 3-phase dc.

The control circuits used for 3 phase brushless motors are well timed 3-half bridges. The motor needs to be timed correctly for each of its phases. Think of it like the timing of cylinders firing in a car. Here is a great video explaining this in detail.

<https://www.youtube.com/watch?v=W9IHEqlGG1s>

It is recommended to NOT try to design a brushless driver from the ground up as they are extremely complex to build. Either use a motor with built in circuitry like a pc fan or use a dedicated 3-phase motor driver chip.

  [1]: image1.png 
  [2]: image2.png 
  [3]: image3.png 
  [4]: image4.png 
  [5]: image5.png 
  [6]: image6.png 
