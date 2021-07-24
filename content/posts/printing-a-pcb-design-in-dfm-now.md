---
tags:
- cadence
- pcb
title: Printing a PCB Design in DFM Now
---

*Note*: This tutorial shows how to print a PCB design on paper. Please see the [ASU PCB Fabrication Process](asu-pcb-fabrication-process.html) for instructions on how to manufacture / "print" a PCB design in copper.

## Why would you want to print a PCB design on paper?

Before sending a PCB to be manufactured, it is imperative to separate the layers and print it at 1:1 (100%) scale on paper to physically verify that your parts will fit through the holes and that pad spacing is correct.

*Note:* You can also [Print a PCB Layout in Cadence PCB Editor](printing-a-pcb-layout-in-cadence-pcb-editor.html).

## How do you print a PCB design on paper?

1.  [Run a Design for Manufacturing Check](running-a-design-for-manufacturing-check-in-dfm-now.html) in DFM Now

2.  In the Layer Display window, right-click on a layer and choose All Layers Off.

3.  Pick a layer and click the light bulb icon next to the layer name to enable it.

4.  Highlight the enabled layer in the workspace. Right-click on the enabled layer and choose Move from the contextual menu. Left-click anywhere in the workspace and then move the layer somewhere off to the side so that it won't overlap with the other layers. Left click again. Right click anywhere in the workspace to exit the "Move" mode.

5.  Repeat steps 3 - 5 for the remaining layers in your design (see example, Figure 1)

  ------------------------------------------------------------------------------
   [![](/figures/figure_102.png)](/larger/image0205.png)
                      Figure 1: Example of separated layers
  ------------------------------------------------------------------------------

6.  Choose File > Print... and select Plot Scale : User Scale of 1.0. Click Next and PLOT! to print your design.

*Based on a tutorial by Robert Goby*
