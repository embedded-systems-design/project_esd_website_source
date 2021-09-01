---
tags:
- cadence
- pcb
title: Packaging Cadence Files for Submission
---

## Introduction

This tutorial goes through how to package Cadence schematic and PCB files for submission to Canvas.

## First, configure Microsoft Print to PDF to print to a file

1.  In Windows, go to Settings > Devices > Printers & scanners and click on Microsoft Print to PDF. Click Manage and then Printer properties to open the "Microsoft Print to PDF Properties" window.

2.  In the "Microsoft Print to PDF Properties" window, click the Change Properties button and then click on the Ports tab (see Figure 1). Select the checkbox next to FILE: Print to File and click OK.

    ![Figure 1: Microsoft Print to PDF Properties, Ports tab](/larger/image0186.png)

## Packaging a Cadence schematic project for submission to Canvas

1.  Open your schematic project in Capture CIS

    First, you will convert your schematic to PDF form.

2.  Choose File > Print Setup... and change the printer setup to "Microsoft Print to PDF" (or your other preferred method of printing to PDF).

3.  Choose File > Print and click OK, saving your PDF to the desktop. If you are trying to expand the printout to fill a C-sized sheet, make sure to indicate that when you submit the PDF for printing to the plotter.

    Next, you will ZIP the folder with your schematic project files.

5.  In Windows, find the project folder in which you created and saved your Cadence schematic design (see Figure 2).

    ![Figure 2: Example of finding the schematic project folder](/larger/image0187.png)

6.  Verify that the most important files are in your project folder: (see Figure 3)

    -   .DSN - Cadence schematic design file
    -   .OPJ - Cadence schematic project file
    -   .OLB - Cadence schematic library file (only exists if you have a custom library)

    ![Figure 3: Example of Cadence DSN and OPJ files](/larger/image0188.png)

    **Note:** You may have additional files in this folder, depending on the steps you took during the creation of your schematic. It is OK to leave additional files in the folder.

7.  In Windows, right-click on the project folder and choose Send to > Compressed (zipped) folder (see Figure 4).

    ![Figure 4: Creating a .zip file in Windows](/larger/image0189.png)
                    
  
8.  Move the .zip file to the desktop with the .pdf you created in steps 1 - 4.

9.  Submit **both** the .pdf and the .zip file to the appropriate assignment on Canvas.

## Packaging a Cadence schematic and PCB project for submission to Canvas

1.  In Windows, open your PCB in PCB Editor

    First, you will convert your PCB layout to .jpg form.

2.  Choose File > Plot... Click "Setup..." and change the printer to "Microsoft Print to PDF". Save the PDF file to the desktop.

    Next, you will ZIP the folder with your PCB project files.

3.  In Windows, find the project folder in which you created and saved your Cadence PCB design (see Figure 6).

    ![Figure 6: Example of finding the PCB project folder](/larger/image0190.png)
               
  
4.  Verify that the most important files are in your project folder: (see Figure 7)
    -   .DSN - Cadence schematic design file
    -   .OPJ - Cadence schematic project file
    -   .OLB - Cadence schematic library file (only exists if you have a custom library)
    -   .ART - Gerber files used for manufacturing
    -   .DRL - Drill files used for manufacturing (only exists if you have through-hole components)
    -   .BRD - Cadence PCB editor design file

    ![Figure 7: Example of Cadence PCB files](/larger/image0191.png)
                      
    **Note:** If you are missing any of the above files then recheck your Gerber file export process or seek additional assistance from course staff. You may have additional files in this folder, depending on the steps you took during the creation of your schematic and PCB. It is OK to leave additional files in the folder.

5.  In Windows, right-click on the project folder and choose Send to > Compressed (zipped) folder (see Figure 8).

     ![Figure 8: Creating a .zip file in Windows](/larger/image0192.png)

6.  Move the .zip file to the desktop with the .jpg you created in steps 1 - 2.

7.  Submit **both** the .jpg and the .zip file to the appropriate assignment on Canvas.

The following video shows an older version of the process described in this tutorial.

<iframe width="560" height="315" src="https://www.youtube.com/embed/qsP4t-bZf8I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

*Based on a video and tutorial created by Robert Goby*
