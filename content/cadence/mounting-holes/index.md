---
title: Cadence Mounting Hole/Post Tutorial
tags: [cadence]
---
# Cadence Mounting Hole/Post Tutorial

Some components have, in addition to their electrical pins, mechanical supports that must be accounted for in the PCB footprint. Otherwise, without mounting holes for these pins to go into, the component will not fit onto the board. This tutorial will demonstrate how to add the mounting holes to the footprint for a [THB001P] joystick.

1.  Open the product drawing. Look at the "PCB Installation Holes" figure. Note that this only shows the drill hole diameters and does not recommend pad sizes. Also, the units are in mm and will need to be converted to mils.

2.  Open PCB Editor and create a new package symbol.

3.  Add the electrical pins as shown in the drawing; the four un-numbered holes are the mounting ones. This is not the focus of the tutorial, but here are a couple hints:

    a.  You may need to create two new padstacks, one for the two axes and one for the pushbutton

    b.  For both padstacks, use the drill diameter specified in the drawing and select a pad size which will result in sufficient [annular ring].

> ![][1]

4.  Note the drill diameter of the four mounting holes given in the drawing.

5.  Use Padstack Editor to create an appropriately sized padstack. As with the electrical pins, this will need to have the drill diameter specified in the drawing along with a pad resulting in sufficient annular ring. Many mounting posts, despite not being electrically connected, will still need to be soldered to the board for mechanical stability.

6.  Prepare to place the four mounting pads. Set the type as "Mechanical" instead of "Connect" ![A screenshot of a computer Description automatically generated with medium confidence]

> Note: Placing electrical pins and then deleting the pin number will also result in the pins being considered mechanical. However, this action might not be reversible, and setting them as mechanical in the first place is easier when creating a new symbol.

7.  Use the dimensions on the drawing to determine where to place the four pins. Since they are arranged in a rectangle, by setting X and Y quantities of 2 and the spacing values as specified in the drawing, you can place all of them at once.

![Background pattern Description automatically generated]

8.  You now have a PCB footprint with mounting holes! Don't forget to add a reference designator before saving the file.

  [THB001P]: https://www.ckswitches.com/media/2873/thb.pdf
  [annular ring]: https://www.protoexpress.com/blog/dont-let-annular-rings-drive-you-crazy/
  [1]: image1.PNG
  [A screenshot of a computer Description automatically generated with medium confidence]: image2.PNG
  [Background pattern Description automatically generated]: image3.PNG 
