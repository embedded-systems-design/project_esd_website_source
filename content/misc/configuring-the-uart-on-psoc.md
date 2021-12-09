---
tags:
- cypress
- uart
- microcontroller
- debugging
- software
title: Configuring the UART on PSoC
---

## What is a UART (Universal Asynchronous Receiver/Transmitter)?

UART is one serial protocol used for communicating data between two digital devices (e.g., between the Pioneer Kit and the computer).

## When is a UART useful?

Some sensors (e.g., GPS and RFID units) have a UART interface. Additionally, it is very helpful for debugging programs by using it to send messages back to the computer indicating the current status of the program.

## How does a UART work?

More information on UARTs is available in the [Microcontroller UART Tutorial](http://www.societyofrobots.com/microcontroller_uart.shtml) from Society of Robots.

## How many PSoC® chips does the PSoC® 4 Pioneer Kit have?

See the [PSoC® Hardware Development Kits](/psoc-hardware-development-kits/) page. This is important to understand the answer to the next question.

## How do I connect and configure the PSoC® 4 Pioneer Kit to send information to the computer over the UART?

1.  On the Pioneer Kit, connect a jumper wire from UART RX (P0[4](/figures/figure_260.png)) of the PSoC® 4 to J8_10 (P12[7]) of the PSoC® 5LP

2.  On the Pioneer Kit, connect a second jumper wire from UART TX (P0[5]) of the PSoC® 4 to J8_9 (P12[6]) of the PSoC® 5LP

3.  Connect the Pioneer Kit to your computer with a USB cable.

    Next, you will need to determine which COM port the Pioneer Kit is connected to, install a terminal program, and configure it to read data from the serial port on your computer. This will allow you to see the output from your program.

4.  Determine which COM port the Pioneer Kit is connected to by opening the Bridge Control Panel application in the Cypress folder in the Start menu, and looking for the COM port listed with the highest number (see Figure 2, below). Write down this port name and close the Bridge Control Panel.

    ![Figure 2: Bride Control Panel](/figures/figure_259.png)

5.  Download, install, and open the terminal program [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/)

6.  Click on the Terminal tab and configure it with the settings shown in Figure 3 (below)

    ![Figure 3: PuTTY terminal configuration tab](/larger/image0073.png)

7.  Click on the Session tab and configure it with the settings shown in Figure 4. Use the COM port for your computer determined earlier in this tutorial. Save the session as PSoC and click "Open".

    ![Figure 4: PuTTY Session configuration tab](/figures/figure_260.png)
    
8.  Finished! Now, you can see text sent between your computer and PSoC® 4 Pioneer Kit via the UART.
