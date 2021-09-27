---
title: Cadence Forward Annotation Tutorial
tags: [cadence,]
---
# Cadence Forward Annotation Tutorial

After having started working on a PCB layout, sooner or later you will likely find changes need to be made to your original schematic. Fortunately, you do not need to start the PCB design over as a result! Forward annotation allows you to essentially export changes made in your schematic into an existing layout, and here is how to do this in Cadence.

1.  Create a schematic in Capture CIS. For this tutorial, two intentional connection errors have been made in the example schematic shown below.

![Diagram, schematic Description automatically generated]

2.  Transfer your schematic to a PCB layout using PCB \> New Layout. When placing your parts, pay attention to whether the net connections illustrated by the blue lines between pins make sense. For example, connectivity between both leads of a two-pin component, as is the case for R1 and D1 shown below, often indicates an error in your schematic.

![][1]

In this case, power and ground are shorted together, resulting in no GND net on the PCB. Also, there is a wire shorting together the leads of R1, as shown in the schematic by the line running through the symbol with pink dots on either end.

3.  Modify your schematic as needed in Capture. Here we delete the two unneeded wires, resulting in the following schematic:

![Diagram, schematic Description automatically generated][2]

4.  Update your PCB layout. There are two ways to do this:

    a.  Old method: Save and close your PCB design, then use PCB \> New Layout, with your current board file as the input, to import your updated netlist into the existing layout.

> ![][3]

b.  New method: Go to PCB \> Design Sync. This feature allows you to update the netlist in your PCB without closing Allegro. You can review the list of changes to be made, then press Sync to transfer them over to your PCB.

> ![][4]

![A screenshot of a computer Description automatically generated with low confidence]

We now see separate 3.3V and GND nets and a path for the current in this circuit to travel. Forward annotation has been achieved!

  [Diagram, schematic Description automatically generated]: image1.PNG
  [1]: image2.PNG
  [2]: image3.PNG
  [3]: image4.PNG
  [4]: image5.PNG 
  [A screenshot of a computer Description automatically generated with low confidence]: image6.PNG 
