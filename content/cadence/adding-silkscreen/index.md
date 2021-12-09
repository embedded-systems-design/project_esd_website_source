---
title: How to Create a Silkscreen in Cadence and Manually Add Text to it
tags: [cadence,silkscreen]
---
# How to Create a Silkscreen in Cadence and Manually Add Text to it

1.  Create a (finalized) PCB layout. Note that the amount of additional work required for a good silkscreen layer will depend on how your PCB footprints were designed. This example will use the board shown below:

![][1]

2.  Go to Manufacture \> Silkscreen. Clicking the "Silkscreen" button generates a manufacturing-specific silkscreen film for either the top, bottom, or both, by combining several related classes into a single film for each selected layer.

![][2]

3.  Open the Artwork Control Form at Manufacture \> Artwork. Similarly to adding soldermask layers, right click an existing film and select "Add Manual" from the drop-down menu. Create a layer called "SilkscreenTop" using the film located at MANUFACTURING/AUTOSILK_TOP and a bottom layer using AUTOSILK_BOTTOM.

![Graphical user interface, text, application Description automatically generated]

![A screenshot of a computer Description automatically generated with medium confidence]

Your list of films should now resemble this image.

4.  View the silkscreen film(s) you've generated. This can be done within Cadence by switching to the "Visibility" tab on the far right and selecting a film from the "View" drop-down menu. To go back to displaying your regular PCB layout, click "On" next to "Global visibility".

![A screenshot of a computer Description automatically generated]

![A screenshot of a computer Description automatically generated with medium confidence][3]

5.  You may find that design outlines and/or reference designators for specific components are missing from your silkscreen. In this case, try the following:

    a.  Select "Any" instead of "Silk" for the menus under "Classes and Subclasses" in step 2. This was necessary for the reference designators to appear in this example. Alternatively, when designing a PCB footprint, you can place a refdes on Silkscreen_Top as well as Assembly_Top\-- the package symbol wizard does this.

    b.  Edit your custom PCB footprints to ensure they include component outlines. The green rectangles drawn around symbols' pins by default if they lack an actual outline are not transferred to the silkscreen, as can be seen with the example PCB.

6.  To manually add text to a silkscreen layer, first, select the text tool from the toolbar, then select Board Geometry and Silkscreen_Top for Active Class and Subclass. Click where you want the text, type it in, and press Enter, the same way you would add text to an etch layer.

![A green circuit board Description automatically generated with low confidence]

7.  Re-create the Manufacturing AutoSilk film(s) as described in Step 2. Switch your visibility to the corresponding silkscreen film and you will see your text has been added.

![A screenshot of a computer Description automatically generated][4]

References:

[Cadence PCB Interactive Automatic Silkscreen] (Youtube) by parsysEDA.

  [1]: image1.PNG 
  [2]: image2.PNG 
  [Graphical user interface, text, application Description automatically generated]: image3.PNG 
  [A screenshot of a computer Description automatically generated with medium confidence]: image4.PNG 
  [A screenshot of a computer Description automatically generated]: image5.PNG 
  [3]: image6.PNG 
  [A green circuit board Description automatically generated with low confidence]: image7.PNG 
  [4]: image8.PNG 
  [Cadence PCB Interactive Automatic Silkscreen]: https://www.youtube.com/watch?v=ODumzQwb4Pc
