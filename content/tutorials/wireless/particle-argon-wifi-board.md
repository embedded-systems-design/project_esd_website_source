---
tags:
- tutorial
- uart
- design
- argon
- wireless
- particle
title: Particle Argon Wifi Board
---

## What is the Particle Argon? What does it do?

The [Particle Argon](https://docs.particle.io/argon/) is a "wi-fi for everything" development kit that includes a microcontroller, wi-fi hardware, and easy-to-use web-based IDE (Integrated Development Environment). It is typically used to add wi-fi functionality into products without spending a huge amount of development time on the wi-fi hardware and software. A more detailed introduction is available [here](https://docs.particle.io/quickstart/argon/).

*Note:* The Particle Argon was previously known as the Photon and the Spark Core, so you may see documentation referring to Spark Core or Photon instead. The software API is basically the same for all of them.

## Where can I get an Argon board?

-   Each team can check out one (1) Argon board in PRLTA 109. If you need additional Argon boards, please see Dr. Jordan
-   If you want to buy your own Argons, you can [purchase them from Particle](https://store.particle.io/collections/wifi)

## Where can I find the hardware specifications for the Argon?

-   [Argon Datasheet](https://docs.particle.io/datasheets/wi-fi/argon-datasheet/) from Particle

## Where can I find the firmware/software for the Argon?

*Notes: Firmware is a term used to describe software that directly interfaces with hardware. An API (Application Programming Interface) is a guide to the software/firmware functions you can use in your code.*

-   [Particle Device OS Firmware API](https://docs.particle.io/reference/device-os/firmware/photon/) API from Particle
-   [Firmware Upgrades](https://support.particle.io/hc/en-us/articles/360039251774) from Particle

## How do I configure the Argon to run on my computer?

-   [Getting Started](https://docs.particle.io/quickstart/argon/) guide from Particle

## How do I communicate between the Argon and my microcontroller?

There are two major ways to communicate between the devices:

1.  Using a UART (Universal Asynchronous Receiver Transmitter). UART connections transmit ASCII text, meaning that if you are trying to send numbers you will first need to convert them into strings (see FAQ question below). This strategy allows you to send data either to or from the Argon by either reading from or writing to the UART. An older example of how to do this is available [here](https://docs.google.com/document/d/1ArfviVWar79W0KfDVcT3e13jerVyXOeRsWhZUyI3jHg/edit?usp=sharing) (note that it is for the older version of the Argon called the Spark Core, so some of the code may not work).
2.  Using the I/O pins on the Argon *(Note: This is **not** a form of serial communication)*. If you only need to turn something on and off, or read a simple bit or analog value, then this is a simpler solution than using the UART. See the [Pins and button definitions](https://docs.particle.io/datasheets/wi-fi/argon-datasheet/#pins-and-button-definitions) section of the datasheet and the [Input/Output API](https://docs.particle.io/reference/device-os/firmware/photon/#input-output) pages on the Argon for more information.
3.  Here is a [UART PIC to Argon Tutorial](/uart-pic-to-argon-tutorial/) written by Mykol Reklaitis

## How do I send numeric or formatted data over a UART connection?

-   Use the sprintf() function for your microcontroller. sprintf() prints formatted data to a string that can be sent over a UART connection. See [this tutorial](http://www.tutorialspoint.com/c_standard_library/c_function_sprintf.htm) from tutorialspoint for more information.

## Where can I find examples of Argon projects?

-   [Particle Community](https://community.particle.io/)
-   [SPO Learning Lab](http://spolearninglab.com/curriculum/lessonPlans/hacking/hardware/sparkcore/intro.html)

## How do I communicate between a Argon and a phone app?

### Option 1: Tinker Mobile App

One option is use the [Tinker mobile app](https://docs.particle.io/tutorials/developer-tools/tinker/photon/) from Particle. This off-the-shelf app is a good option if your project only needs to send simple information between Argon and the microcontroller.

*Advantages of Tinker app*

-   Off-the-shelf multi-platform option to control individual analog and digital I/O pins through a standard interface
-   Easy to use
-   Useful to test whether a problem is in software or hardware (because since it's provided by the manufacturer, it will hopefully work correctly)
-   You can modify the callback functions to include your own code

*Disadvantages of Tinker app*

-   App can not be modified, so you don't have control over the user interface on the phone. (This may be OK for a proof of concept)
-   Does not support entering text into the app directly (though you can send ASCII text over the UART in the firmware code)

### Option 2: UbiDots App Framework

The [UbiDots app framework](http://ubidots.com/) is designed to capture and display sensor data using an off-the-shelf app provided by the company. This is a good option if your project primarily needs to display and/or log sensor data (e.g., body temperature).

*Advantages of UbiDots*

-   You have some control over the user interface in the app
-   [Connect your Particle device to Ubidots](https://help.ubidots.com/en/articles/513304-connect-your-particle-device-to-ubidots-using-particle-webhooks) tutorial from UbiDots

*Disadvantages of UbiDots*

-   UbiDots is primarily for gathering and displaying information (microcontroller --> Argon --> UbiDots --> UbiDots app), and may not be able to send information back to your microcontroller easily.

### Option 3: Write your own phone app

You will need to create functions in the Argon firmware and call those functions via the [Particle Cloud REST API](https://docs.particle.io/reference/api/). This is a good option if someone in your group has prior coding experience and/or time to figure out how to write an app.

*Advantages of custom apps*

-   Full access to send and receive data between the Particle and the microcontroller
-   Full access to modify the user interface (within Android/iOS limitations)

*Disadvantages of custom apps*

-   Apps are usually platform-specific, meaning that if you write an app for Android it will likely not be compatible with iOS and vice-versa

More information on custom app development is provided below.

### Option 4: Run a web server on the Argon

You can run a web server (based on [Webduino](https://github.com/m-mcgowan/webduino), documentation [here](http://ten-fingers-and-a-brain.com/arduino-projects/webduino/webserver/)) on the Argon and then log into it from a phone or computer. This is a good option if you want to have full control via HTML over what is displayed.

*Advantages of a web server*

-   Platform-independent
-   Allows use of JavaScript and HTML to sculpt your "app"

*Disadvantages of a web server*

-   Programming is time consuming and somewhat unintuitive

### Option 5: Use Particle.publish() to post data to a web page on your computer

*Advantages of Particle.publish()*

-   Platform-independent
-   Tutorial available [here](https://community.particle.io/t/tutorial-getting-started-with-spark-publish/3422?redirected=true)

*Disadvantages of Particle.publish()*

-   Requires the use of HTML and JavaScript

## How do I create an Android app?

-   [Particle Android Cloud SDK](https://docs.particle.io/reference/android/) (Software Development Kit) from Particle

You will need an app development environment. Suggested environments include:

-   [MIT App Inventor](http://appinventor.mit.edu/)
-   [Xamarin](https://dotnet.microsoft.com/apps/xamarin) (cross-platform, free for academic use)
-   [Phonegap](http://phonegap.com/) (cross-platform)

## Where can I find examples of custom Android apps that work with Argon?

-   [MIT App Inventor example](https://community.particle.io/t/connect-spark-core-with-android-app-made-in-appinventor/7378/2)

## How do I create an iOS app?

-   [Particle iOS Cloud SDK](https://docs.particle.io/reference/ios/) (Software Development Kit) from Particle

You will need an app development environment. Suggested environments include:

-   [Start Developing iOS Apps (Swift)](https://developer.apple.com/library/ios/referencelibrary/GettingStarted/DevelopiOSAppsSwift/) from Apple
-   [Xamarin](https://dotnet.microsoft.com/apps/xamarin) (cross-platform, free for academic use)
-   [Phonegap](http://phonegap.com/) (cross-platform)

## Where can I find examples of custom iOS apps that work with Argon?

-   Coming soon

## How do I communicate between a Argon and a computer?

-   Coming soon

## How do I communicate between a Argon and another Argon?

-   [Connecting Two Photons Together](https://community.particle.io/t/connecting-two-photons-together/17617)
-   [TCP Server and Client between two Photons](https://community.particle.io/t/tcp-server-and-client-between-two-photons/16865)
-   [The Buddy System: Publish and Subscribe](https://docs.particle.io/guide/getting-started/examples/photon/#the-buddy-system-publish-and-subscribe)
