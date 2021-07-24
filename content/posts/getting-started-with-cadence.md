---
tags:
- tutorial
- cadence
title: Getting Started with Cadence
---

## Introduction

A number of [basic Cadence tutorial videos](https://www.youtube.com/watch?v=QyfyskwCqGA&list=PLL5qFpazhNPkiMll-tzyYYOK3y9xvoLk6) are available on YouTube.

## Getting Started

1.  In Windows, find and open the application Capture CIS (see [Cadence Schematic Tutorials](cadence-schematic-tutorials.html))

2.  Create and name a new project and add existing part libraries (see [Creating a New Project in Cadence](creating-a-new-project-in-cadence.html))

3.  Add parts to your schematic. First, check to see if the parts you need already exist in a library. For example, schematic symbols for header pins (which are useful for connecting to components external to your custom printed circuit board, like batteries, PSoC® boards, and sensors, see Figure 1) can be found by searching for "Header" in the Place Part dialog box (see Figure 2)

  ----------------------------------------------------
   [![](/figures/figure_229.png){class="img-fluid"}](/larger/image0165.png)
                    Figure 1: Header
  ----------------------------------------------------

  -------------------------------------------------------
   [![](/figures/Place_Part.png){class="img-fluid"}](/figures/Place_Part.png)
              Figure 2: Place Part dialog box
  -------------------------------------------------------

4.  Create a custom library to store custom schematic symbols for your design that are not included in the built-in libraries (very common), and add it to your project (see [Creating a Custom Library in Cadence](creating-a-custom-library-in-cadence.html))

5.  Create and save custom schematic symbols in your custom library. If you later need to edit a custom schematic symbol, make sure to replace the edited symbol in the cache (see [Creating a Custom Schematic Symbol in Cadence](creating-a-custom-schematic-symbol-in-cadence.html))

6.  Create printed circuit board footprints for all components on your printed circuit board

7.  For electronic devices with DIP/SOIC/PLCC/QFP/PGA/SIP/ZIP packages (which are typically integrated circuits and plug-in modules with evenly-spaced pins), it is easiest to use the "Package Symbol Wizard" (See [Creating a Custom PCB Footprint using Package Designer in Cadence](creating-a-custom-pcb-footprint-using-package-designer-in-cadence.html))

8.  For all other components, create custom footprints manually (see [Creating a Custom PCB Footprint Manually in Cadence](creating-a-custom-pcb-footprint-manually-in-cadence.html))

9.  Create custom padstacks for the pads of each custom footprint (See [Creating a Custom Padstack in Cadence](creating-a-custom-padstack-in-cadence.html))

10. Link all footprints to schematic symbols in Design Entry CIS by updating the library search path (see [Changing the Library Search Path in Cadence Design Entry CIS](changing-the-default-via-padstack-in-cadence-pcb-editor_4.html))

11. Link all footprints to schematic symbols in PCB Editor by updating the library search path (see [Changing the Library Search Path in Cadence PCB Editor](changing-the-default-via-padstack-in-cadence-pcb-editor.html))

12. Transfer the schematic to PCB Editor for the PCB layout and design (see [Transferring a Cadence Schematic to PCB Editor](transferring-a-cadence-schematic-to-pcb-editor.html))

13. [Prepare and submit your PCB Layout for fabrication](asu-pcb-fabrication-process.html)

*Based on a tutorial by Cody Van Cleve*
