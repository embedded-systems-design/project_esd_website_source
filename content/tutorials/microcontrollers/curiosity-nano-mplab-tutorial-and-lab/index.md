---
title: "**Curiosity Nano & MPLAB Tutorial**"
---

# **Objectives**

Getting familiar with the MPLAB X programming environment to program the PIC16F18446 Curiosity Nano development board. In this tutorial, you will learn to set up the general-purpose input/output pins (GPIO), external interrupts (ISR), pulse-width modulation (PWM), as well as the timer module for the PWM.

# **Resources**

* [*PIC16F18446 Curiosity Nano Hardware User Guide*]
* [*PIC16F18446 Datasheet*]
* [*Using GPIO in MPLAB® X with MCC*]
* [*What is an Interrupt?*]
* [*Implementing Interrupts using MPLAB® Code Configurator*]

# **1. Create Your First Project**

1.  After finish installing the MPLAB X IDE, you can plug the USB mini cable into the Curiosity USB debugging port. Once you plug the USB to your PC, a green LED will light up. This indicates the Curiosity board has been powered up.

2.  To create a new project, go to "**File**" - "**New Project**" - select "**Standalone Project**" - and click "**Next \    **"

    ![][1]

3.  Select **Device** as "**PIC16F18446**" and click "**Next \    **"

    ![][2]

4.  If you have your Curiosity Nano connected to your PC, the serial number of the device will show up.

    Select the serial number of your Curiosity board and click **"Next \    ."**
    
    ![][3]

5.  Now you will have to select a compiler for the MPLAB X. If you haven't installed **Microchip XC8 Compiler**, you can install it by clicking the **"Download Latest."**

    ![][4]

6.  Once the XC8 compiler has been installed, select the **"XC8"** as the compiler for this project.

    ![][5]

7.  The last step is to give a name to your first project as well as the location where you want to put your project.

# **2. Install MPLAB Code Configurator** 

*Once you have all MPLAB X IDE installed, you can install the MPLAB Code Configurator*

1.  Select **"Plugins"** under **"Tools"**

![][6]

2.  Select the **second tab ("Available Plugins")** and check the **"MPLAB Code Configurator."**

    Click **"Install"** to install this plugin.

![][7]

3.  Once the Code Configurator has been installed, you can open it by clicking **"Tools" - "Embedded".**

    ![][8]

# 3. Getting Familiar with Code Configurator

![The screenshot above is the layout of the main page of the Code Configurator][9]
    

-   **Pin Manager (Blue Area)**

    Configure the direction (Input/Output), external interrupt, and PWM of GPIO pins in this area.

-   **Available Device Resources (Red Area)**

    Peripherals (UART, PWM, I2C, SPI, etc) that available to the microcontroller.

-   **Used Resources (Yellow Area)**

    The peripherals have been added/used in the microcontroller.

-   **Resources Setups/ Register Setup (Blue Area)**

    The detailed register set up for the selected peripheral.

-   **Code Generate Button (Pink Button)**

# **4. Lab Tutorials**

## **4.1 Make an onboard LED blink**

***In this lab, you will turn on and off the onboard LED (LED0) by using a GPIO pin on the Curiosity.***

*Required Hardware: Curiosity Nano*

### **4.1.1 Code Configurator Setup**

1.  From [*Curiosity Nano Hardware User Guide*][*PIC16F18446 Curiosity Nano Hardware User Guide*], we know that the onboard LED has been routed to pin RA2.

2.  Double Click **Pin Module** under **Project Resources.**

3.  Lock the **Port A - Pin 2** to **GPIO - Output.**

4.  Click the **Generate button** to generate code for the GPIO module.

    The Code Configurator setup for Lab 4.1 should look like this:

![Setting up the RA2 as GPIO output pin][10]


### **4.1.2 MCC (Microchip Code Configurator) Generated Files and Main.c**

1.  Go back to **Projects**, you will see two subfolders called **MCC Generated Files** under both **Header Files** and **Source Files.** These folders contain the generated code, functions, and macros by **MCC (Microchip Code Configurator).**

2.  The list of MCC generated functions or macro could be found at the **header files**. *(A header file is a file with extension .h which contains C function declarations and macro definitions to be shared between several source files.)*

    ![][11]

3.  Since we only use GPIO as our peripheral, we can double click the "**pin_manager.h**" and see all the macros that MCC generated for us.

4.  To enable the onboard LED, we can use the following macros (also highlighted at the screenshot below):

![][12]

| **Macros**           | **Purpose of the Macro**                             |
|:---------------------|:-----------------------------------------------------|
| **IO_RA2_SetHigh()** | Set pin **RA2** as logic High                        |
| **IO_RA2_SetLow()**  | Set pin **RA2** as logic Low                         |
| **IO_RA2_Toggle()**  | Set pin **RA2** opposite to the previous logic state |

5.  Go back to the "**main.c**" and use the macros inside the main function.

    You can also add a delay function in order to see the on and off transition of the LED.

    ```
    IO_RA2_SetHigh(); //Set RA2 (LED0) to logic high, turn on
    __delay_ms(1000); //delay
    IO_RA2_SetLow();  //Set RA2 (LED0) to logic low, turn off
    ```

    Now your main function should look something like this:
    
    ![Main.c for Lab 4.1][13]
    
6.  Click the **Hammer button** (![][14]) to compile the project. If you see "**Build Successful**", then you can flash the program to the microcontroller by clicking the **Run** main project button (![][15].)

## **4.2 Make More LEDs Blink**

***In this lab, we will learn how to blink the external LEDs using pin RC1 and RC3 from the Curiosity Nano.***

*Required Hardware: Curiosity Nano, Breadboard, 220 Ohm resistors x2, Green LED x2*

### **4.2.1 Hardware Setup**

1.  Place headers on all ground (**GND**) pins of the Curiosity Nano. Connect the GND pin to the negative rail on the breadboard using a jumper cable.

2.  Place header on both pin **RC1** and **RC3.**

3.  Place the first 220 Ohm resistors to RC1 and then place the second 220 Ohm resistor to RC3. ([***What is a current limiting resistor?***])

4.  Connect the Anode of the LED to the resistor. Connect the Cathode to Ground.

    ![][16]
    
    *A simplified schematic for the Hardware Setup for this Lab.*
    
    The Hardware Setup for Lab 4.2 should look like this:

![][17]

*Lab 4.2 Hardware Setup*

### **4.2.2 Code Configurator Setup**

1.  Open **Pin Manager: Grid View,** lock both **Port C - Pin 1** and **Port C - Pin 3** to **GPIO - Output**.

![][18]

2.  Click the **Generate button** to generate code for GPIO module.

### **4.2.3 GPIO Setup**

1.  Go back to **Project**, open "**pin_manager.h**". You can see macros for **IO_RC1** and **IO_RC3** has been generated and ready for use.

    ![][19]

### **4.2.4 Lab Activity** 

Can you write a program in "**Main.c**" and make the external LEDs blink in sequence?

## **4.3 Setting Up PWM (Pulse-Width Modulation)**

***In this lab, we will set up PWM (Pulse-Width Modulation) on the Curiosity board and create a breathing LED effect.***

*Required Hardware: Curiosity Nano*

### **4.3.1 Code Configurator Setup**

1.  Under **Device Resources**, add **PWM6** module to **Project Resources.**

    ![][20]
    
    *PWM Setup Page*

2.  Under the **Notification \[MCC\]**, the warning tells us to configure **Timer2** for the PWM6 module.

3.  Find **TMR2 (**Timer 2) under the **Device Resources** and add **TMR2** as peripherals.

4.  Change the **Clock Source** to **FOSC/4**. Keep the **Prescaler** and **Postscaler** as **1:1.**

    ![][21]
    
    *Setting the TMR2 (Timer 2) Clock Source as "FOSC/4"*

5.  Go back to **Pin Manager: Grid View.** Now you will see two extra rows. One of them is the PWM6 module, and the other one is the TMR2 (Timer 2) module. Lock the **Port A - Pin 2** to **PWM6** row.

    ![Setting the PWM6 to Port A - Pin 2][22]
    

6.  Click **Generate button** to generate code for both PWM and Timer module.

### **4.3.2 PWM Duty Cycle Setup**

1.  Go back to **Project**, you should be able to see **pwm6.h**, **tmr2.h**, **pwm6.c,** and **tmr2.c** have been generated. Open "**pwm6.h**", scroll down and you can find there's a custom function named **PWM6_LoadDutyValue**.

    **PWM6_LoadDutyValue** allows you to change the PWM duty cycle.
    
    ![The Custom Function "PWM6_LoadDutyValue" at "pwm6.h"][23]
    

2.  According to the datasheet of the [*PIC16F18446*][*PIC16F18446 Datasheet*], we know that the resolution of the PWM can go up to 10-bit resolution. Therefore, the total number of PWM steps can be calculated as follows:

    ${2^{10}\  = \ 1024}^{}\text{steps}$
    
    In this case, we can calculate and get the PWM module outputting at 50% duty cycle.
    
    ${50\%\ Duty\ Cycle\  = \ 1024\  \times 50\% = \ 512}^{}$
    
    From the coding standpoint, we can use the following code to achieve a 50% PWM duty cycle to RA2 pin:

    ```c
    PWM6_LoadDutyValue(512); // 50% duty cycle for PWM
    ```

### **4.3.3 Make an LED Breathe**

1.  The idea of making LED breathing is to dim the LED with different PWM duty cycle.

    Try following code in your **Main.c** program:

    ```c
    for (int i = 0; i<1024; i++) // increase duty cycle to 100%
    {
        PWM6_LoadDutyValue(i);
        __delay_ms(1);
    }

    for (int i = 1023; i>= 0; i--)// decrease duty cycle to 0%
    {
        PWM6_LoadDutyValue(i);
        __delay_ms(1);
    }
    ```

2.  Click the **Hammer button** (![][14]) to compile the project. If you see "**Build Successful**", then you can flash the program to the microcontroller by clicking the **Run** main project button (![][15].)

## **4.4 Button Controlled LED**

***In this lab, we will learn about the ISR ([*Interrupt Service Routine*][*What is an Interrupt?*]) and use ISR to light up the onboard LED.***

*Required Hardware: Curiosity Nano x1*

### **4.4.1 Code Configurator Setup**

1.  Under **Device Resources**, find **Ext_Interrupt** under **Device Resources.**

2.  Add **EXT_INT** module to **Project Resources.**

3.  From [*Curiosity Nano Hardware User Guide*][*PIC16F18446 Curiosity Nano Hardware User Guide*], we know that the onboard **mechanical switch (SW0)** has been routed to **pin RC2.** When the mechanical switch (SW0) is pressed, it will drive the RC2 to the ground (GND).

4.  Under Project Resources, open **Pin Module** and **Pin Manager: Grid View**

5.  Lock **Port C - Pin 2** to **GPIO - Input and EXT_INT**.

6.  Check the **WPU** box for **Pin RC2**. This will configure a **Weak Pull-up (WPU)** to **Pin RC2**. The WPU will keep the Pin RC2 as logic High.

    ![][24]
    
    *A simplified schematic for WPU configuration with RC2 and SW0.*

7.  You can also rename the **IO_RC2** to **SW** under the **Custom Name** column.

    ![][25]
    
    *Giving a custom name (SW) to pin RC2*

8.  Now double click the **EXT_INT** under the **Project Resources.**

9.  Since the SW0 will drive the Pin RC2 to logic low (GND) when it's being pressed, we will need to Change **Edge Detection** to **falling edge**. In this case, an external interrupt will generate when the SW0 is pressed.

    ![Setting the Edge Detection to Falling Edge][26]
    
10. Click the **Generate button** to generate code for the External Interrupt module.

### **4.4.2 Push Button Interrupt Setup**

1.  Go back to **Project**, you should be able to see **ext_int.h**, **interrupt_manager.h**, **ext_int.c,** and **interrupt_manager.c** have been generated.

2.  Open "**pin_manager.h**", scroll down and you can find the macros for **SW (Pin RC2)**. The macro **SW_GetValues()** is the one that can get the input state (either logic High or logic Low). We will use this macro to get whether the button is pressed or not.

    ![][27]

    ```c
    SW_GetValues() // Macro for knowing the input state of SW0 (Pin RC2) 
    ```

3.  Open "**ext_int.c**". You can find a couple of predefined functions that related to interrupts that Inside the "ext_int.c."

4.  Include the "mcc.h" at the beginning of the "ext_int.c." In this case, we can utilize the Breathing LED code.

    ```c
    #include "mcc.h" //include “mcc.h” to “ext_int.c”
    ```

    ![][28]
    
    *Include header file "mcc.h" to "ext_int.c"*

5.  Scroll down the "**ext_int.c**", and you can find there's a custom function named **INT_DefaultInterruptHandler**.

    You can write the code for your interrupt inside this function.

6.  Now, we want to know the push button (SW0) whether it is being pressed or not. Once the SW0 is being pressed, the MCU will detect the input of the RC2 has been driven to logic Low. This will create an interrupt and will run the code inside the **INT_DefaultInterruptHandler**.

7.  **Copy** the following code and **paste** them inside the **INT_DefaultInterruptHandler.**

    ```c
                                          // check the SW0 is being pressed or not
        if (SW_GetValue() == 0)           // if the SW0 is in logic Low (pull to GND)
        {
            //Now Blink the LED
            for (int i = 0; i<1024; i++)  // increase duty cycle to 100%
            {
                PWM6_LoadDutyValue(i);
                __delay_ms(1);
            }

            for (int i = 1023; i>= 0; i--)  // decrease duty cycle to 0%
            {
                PWM6_LoadDutyValue(i);
                __delay_ms(1);
            }
        }
    ```

    ![][29]
    
    *ISR code for INT_DefaultInterruptHandler function.*

### **4.4.3 Enable Interrupt Services**

1.  The last step is to enable the interrupt services for the microcontroller.

    Go back to **Main.c**, uncomment following code that inside the main function:

    ```c
                                            //Enable the Global Interrupts
    INTERRUPT_GlobalInterruptEnable();      //Uncommented

                                            // Enable the Peripheral Interrupts
    INTERRUPT_PeripheralInterruptEnable();  //Uncommented
    ```

    ![][30]
    
    *Enable Interrupt Service at Main.c*

2.  Click the **Hammer button** (![][14]) to compile the project. If you see "**Build Successful**", then you can flash the program to the microcontroller by clicking the **Run** main project button (![][15].)

  [*PIC16F18446 Curiosity Nano Hardware User Guide*]: http://ww1.microchip.com/downloads/en/DeviceDoc/50002808B.pdf
  [*PIC16F18446 Datasheet*]: http://ww1.microchip.com/downloads/en/DeviceDoc/40001985B.pdf
  [*Using GPIO in MPLAB® X with MCC*]: https://microchipdeveloper.com/mcc:mccgpio
  [*What is an Interrupt?*]: https://learn.adafruit.com/multi-tasking-the-arduino-part-2/what-is-an-interrupt
  [*Implementing Interrupts using MPLAB® Code Configurator*]: https://microchipdeveloper.com/mcc:interrupts
  [Objectives]: #objectives
  [Resources]: #resources
  [1. Create Your First Project]: #create-your-first-project
  [2. Install MPLAB Code Configurator]: #install-mplab-code-configurator
  [3. Getting Familiar with Code Configurator]: #getting-familiar-with-code-configurator
  [4. Lab Tutorials]: #lab-tutorials
  [4.1 Make Onboard LED Blinks]: #make-an-onboard-led-blink
  [4.1.1 Code Configurator Setup]: #code-configurator-setup
  [4.1.2 MCC (Microchip Code Configurator) Generated Files and Main.c]: #section
  [4.2 Make More LED Blinks]: #make-more-leds-blink
  [4.2.1 Hardware Setup]: #hardware-setup
  [4.2.2 Code Configurator Setup]: #code-configurator-setup-1
  [4.2.3 GPIO Setup]: #gpio-setup
  [4.2.4 Lab Activity]: #lab-activity
  [4.3 Setting Up PWM]: #setting-up-pwm-pulse-width-modulation
  [4.3.1 Code Configurator Setup]: #code-configurator-setup-2
  [4.3.2 PWM Duty Cycle Setup]: #pwm-duty-cycle-setup
  [4.3.3 Make a LED Breathing]: #make-an-led-breathe
  [4.4 Button Controlled LED]: #button-controlled-led
  [4.4.1 Code Configurator Setup]: #code-configurator-setup-3
  [4.4.2 Push Button Interrupt Setup]: #push-button-interrupt-setup
  [4.4.3 Enable Interrupt Services]: #enable-interrupt-services
  [1]: image29.png 
  [2]: image25.png 
  [3]: image30.png 
  [4]: image10.png 
  [5]: image16.png 
  [6]: image24.png 
  [7]: image20.png 
  [8]: image6.png 
  [9]: image3.png 
  [10]: image27.png 
  [11]: image19.png 
  [12]: image9.png 
  [13]: image31.png 
  [14]: image1.png 
  [15]: image2.png 
  [***What is a current limiting resistor?***]: https://www.sparkfun.com/tutorials/219
  [16]: image17.png 
  [17]: image8.jpg 
  [18]: image28.png 
  [19]: image9.png 
  [20]: image22.png 
  [21]: image23.png 
  [22]: image26.png 
  [23]: image18.png 
  [24]: image4.png 
  [25]: image12.png 
  [26]: image15.png 
  [27]: image14.png 
  [28]: image11.png 
  [29]: image21.png 
  [30]: image13.png 
