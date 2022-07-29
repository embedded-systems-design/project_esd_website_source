---
title: Symbol Creation
weight: 40
author: Dan Aukes
menu:
  main:
    weight: 40
    parent: KiCad
---

## Introduction

## Resources

* LM3178 ([On Digikey](https://www.digikey.com/en/products/detail/stmicroelectronics/LM317BT/5308099) | [datasheet](https://www.st.com/content/ccc/resource/technical/document/datasheet/group1/a0/db/e6/9b/6f/9c/45/7b/CD00000455/files/CD00000455.pdf/jcr:content/translations/en.CD00000455.pdf))
* [KiCad.org](https://www.kicad.org/)
* [KiCad Documentation](https://docs.kicad.org/)
* [Common Pin Types and their Meanings](/kicad-common-pin-types)

## Steps



1. Open up KiCad (start --> KiCad) and select the Symbol Editor

    ![Open Symbol Editor](VirtualBox_Windows_10_2_29_07_2022_08_18_23.png)

1. If this is the first time running the symbol editor, you will be asked to configure the global symbol library table.  Select the default option.

    ![Configure Global Symbol Library Table](VirtualBox_Windows_10_2_29_07_2022_08_18_28.png)

1. Select File-->New Library

    ![Step 2](VirtualBox_Windows_10_2_29_07_2022_08_19_03.png)

1. Give the library a name unique to yourself

    ![Name your library](Untitled.png)
    
1. In the main editor, create a new symbol

    ![Create new symbol](VirtualBox_Windows_10_2_29_07_2022_08_19_29.png)

1. Fill in Symbol information

    ![Fill in Symbol Info](VirtualBox_Windows_10_2_29_07_2022_08_24_29.png)

1. Create a rectangle
    
    ![Create a Rectangle](VirtualBox_Windows_10_2_29_07_2022_08_24_47.png)
    
1. Place the rectangle in the working area.  It doesn't have to be precise yet.

    ![Place Rectangle](VirtualBox_Windows_10_2_29_07_2022_08_26_38.png)

1. Create a Pin to go along the bottom of the part (similar to its package)

    ![Create a Pin](VirtualBox_Windows_10_2_29_07_2022_08_26_48.png)

1. Fill in Pin information, including pin name, number, type, and orientation.  Refer to the datasheet.

  
    1. For example, pin one should be an "input" pin
    
        ![Pin 1](VirtualBox_Windows_10_2_29_07_2022_13_37_51.png)
    
    1. Pin 2 is a voltage out pin type
    
        ![Pin 2](VirtualBox_Windows_10_2_29_07_2022_13_37_59.png)
    
    1. Pin 3 is a voltage input type
    
        ![Pin 3](VirtualBox_Windows_10_2_29_07_2022_13_38_03.png)

1. Finally, adjust pins and boxes to get the final look and feel of the device.  Select the parts you wish to move, right click and select "move" (or type "m") 


    ![Adjust Pins and Box ](VirtualBox_Windows_10_2_29_07_2022_14_21_15.png)
    
1. Save and Close.

![]()

![]()

![]()