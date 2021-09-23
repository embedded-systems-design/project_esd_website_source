---
tags:
- cadence
title: Cadence schematic tutorials
---

There are a number of tutorials available for creating schematics in Cadence. The best tutorials are in videos, as the manuals and online help are poor.

## What is a schematic?

A schematic is an electronic CAD diagram that shows the components used in a circuit and the interconnections among the components. A schematic includes a symbology described in the [table of Electrical Symbols & Electronic Symbols](http://www.rapidtables.com/electric/electrical_symbols.htm). An [example schematic created by Dr. Jordan is available here](https://drive.google.com/file/d/0ByRWb7dgVD-remI0MW9HaWJlamc/edit?usp=sharing).

## What is Cadence Schematic Capture?

Cadence Schematic Capture is an electronic CAD (ECAD) program that captures the components that go into a circuit and the interconnections between the component. This information will later be passed to the PCB Editor by way of a netlist in order to create a PCB. Read the short [Cadence Schematic Capture Datasheet](https://www.cadence.com/content/cadence-www/global/en_US/home/tools/pcb-design-and-analysis/design-authoring/allegro-design-entry-capture-cis.html) for an overview of the software and its features.

## How do I launch Cadence to create a schematic?

In Windows, launch "Design Entry CIS".

This program is also called "Allegro Design Entry CIS" and "OrCAD Capture CIS". These programs are all equivalent.

## How do I create a schematic?

<iframe width="560" height="315" src="https://www.youtube.com/embed/Rim7BOzS-jk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

** WARNING:** Do NOT use spaces in naming your projects. Spaces will prevent Cadence from working correctly.

-   [Quick Guide: Creating a New Project in Cadence](/creating-a-new-project-in-cadence/)
-   [Cadence Schematics Settings and Setup](https://www.youtube.com/watch?v=VjxWnRx8WZQ&list=PLfPEKfeM1ZYMa7phcDzKXsb0zQN60Vv3Q&index=2) video from Casey Petersen
-   [Starting a Schematic](https://youtu.be/HU0upM9UCF4) video from Andrew Crouch
-   [Part 1: Getting Started](https://www.youtube.com/watch?v=NU8i39HZTik) video from iEngineered
-   [OrCAD Basic Tutorial](https://www.youtube.com/watch?v=LhSo14DUFVQ) video from Lauren Spradlin

If you plan to import any schematic symbols from the web (see below) or create custom schematic symbols (see below), you must create a custom symbol library in which to store them.

-   [Quick Guide: Creating a Custom Library in Cadence](/creating-a-custom-library-in-cadence/)
-   [Part 7: Working with Part Libraries](https://www.youtube.com/watch?v=sWKBbRqe5qQ) video from iEngineered.

## How do I place parts on a schematic?

-   [Placing parts, editing schematics, editing parts, and connecting parts](https://www.youtube.com/watch?v=h_H2ncFaD2s&list=PLfPEKfeM1ZYMa7phcDzKXsb0zQN60Vv3Q&index=3) video from Casey Petersen
-   [Part 2: Drawing Schematics](https://www.youtube.com/watch?v=rTbFK6jepv8) video from iEngineered

## How do I edit parts and annotations on a schematic?

-   [Part 3: Editing the Schematic Design](https://www.youtube.com/watch?v=WDfBSvLCy64) video from iEngineered
-   [Part 4: Editing Text and Graphics](https://www.youtube.com/watch?v=0ICr74NMrJY) video from iEngineered

## Where do I find parts?

The first place to look for parts is in the built-in libraries, which have hundreds of thousands of parts but will likely not have every part that you need.

-   [Searching the built-in Cadence libraries](https://www.youtube.com/watch?v=GjHgwmbvyo0) video from parsysEDA

You can also search for parts that others have made using the ActiveParts Internet Component Assistant tool. Any parts that you add using ActiveParts will need to be stored in a custom parts library (see **How do I create a schematic?** above).

-   [Using the ActiveParts Internet Component Assistant](http://www.activeparts.com/walk-through.asp#) tutorial from Cadence

## How do I create a custom part (schematic symbol)?

If a part is not available through one of the sources above, then you must create both a custom schematic symbol and a custom PCB footprint (the physical layout of copper on a printed circuit board to which the component is soldered). Creating a custom PCB footprint is covered in another blog entry on creating PCB layouts.

-   [Quick Guide: Creating a Custom Schematic Symbol](/creating-a-custom-schematic-symbol-in-cadence/)
-   [Creating new parts and preparing for footprints](https://www.youtube.com/watch?v=8EgTsjVaZS8&index=5&list=PLfPEKfeM1ZYMa7phcDzKXsb0zQN60Vv3Q) video from Casey Petersen
-   [Creating a custom schematic symbol](https://youtu.be/jBOrCeYZxdM) video from Andrew Crouch
-   [Creating custom schematic symbols](https://www.youtube.com/watch?v=JBrpZbYMN4c) video from parsysEDA
-   [Making and Editing Capture Parts - Chapter 7 in the *Complete PCB Design Using OrCAD Capture and PCB Editor*](http://search.ebscohost.com.ezproxy1.lib.asu.edu/login.aspx?direct=true&db=nlebk&AN=249296&site=ehost-live&ebv=EB&ppid=pp_v) book by Kraig Mitzner

## How do I show the power and ground pins on a schematic component?

Cadence sometimes hides the power and ground pins on components (particularly ICs and custom components). Components don't automatically have power and ground connected to them. In order to show the power and ground pins, do the following:

1.  Open your project in Allegro Design Entry CIS
2.  Open the schematic page
3.  Right-click on the component and choose "Edit Properties..."
4.  Make sure the "Power Pins Visible" property checkbox is checked
5.  Repeat for each component that has power and ground pins

## How do I prepare my schematic for transfer to a PCB layout?

**STEP 1:** Assign footprints to all components.

-   [Quick Guide: Transferring a Schematic to PCB Editor](/transferring-a-cadence-schematic-to-pcb-editor/)
-   [OrCAD Tutorial - Section 8.3](https://drive.google.com/a/asu.edu/file/d/0ByRWb7dgVD-rX3VWTWxLNjdsRWs/edit) *(older version of software)*

**STEP 2:** Check the schematic for errors. Schematic capture programs have a design rules check (DRC) option that checks for inconsistencies in schematics. DRCs will not find all errors (for instance, choosing the wrong part or function).

-   [Quick Guide: Transferring a Schematic to PCB Editor](/transferring-a-cadence-schematic-to-pcb-editor/)
-   [Design Rules Check example](https://youtu.be/ktMlFAqgS08) video by Andrew Crouch
-   [OrCAD Tutorial - Section 2.4](https://drive.google.com/a/asu.edu/file/d/0ByRWb7dgVD-rX3VWTWxLNjdsRWs/edit) *(older version of software)*
-   [Part 10: Design Validation and Processing](https://www.youtube.com/watch?v=WCCgKwLbV6o) video from iEngineered

**STEP 3:** Convert the schematic into a netlist (a file that lists all of the interconnections in a schematic) that will then be loaded into the PCB layout program. Loading a netlist into a PCB layout program is covered on the [Transferring a Schematic to PCB Editor](/transferring-a-cadence-schematic-to-pcb-editor/) page.

-   [Part 11: Intercommunication tools, Netlist Creation and Back Annotation](https://www.youtube.com/watch?v=3u1eGx95vLk) video from iEngineered
-   [OrCAD Tutorial - Section 2.6](https://drive.google.com/a/asu.edu/file/d/0ByRWb7dgVD-rX3VWTWxLNjdsRWs/edit) *(older version of software)*

## How do I configure Capture to find my custom footprints?

A common error message is that Cadence cannot find your custom footprints. The footprint search path must be updated in order to correct this error.

-   [Changing the Library Search Path in Cadence Design Entry CIS](/changing-the-library-search-path-in-cadence-design-entry-cis/) tutorial

## How do I configure project and program settings?

-   [Part 5: Using Project Manager](https://www.youtube.com/watch?v=U3AwiOS7FBk) video from iEngineered
-   [Part 6: Setting Preferences and Backup](https://www.youtube.com/watch?v=pHfd47WWNNM) video from iEngineered

## How do I organize a large design?

Cadence supports two major ways to organize large designs: splitting them over multiple pages and using hierarchical blocks. Either method is appropriate for use in projects, and often companies will specify the way that official schematics should be organized.

A design can span over multiple pages as long as the necessary signal nets are connected. Nets can be connected across pages using off-page connectors with the same name on each page.

-   [Part 8: Off-Page Connectors and Net Connectivity](https://www.youtube.com/watch?v=AwUmqxsdweQ) from iEngineered

Designs can also be organized to use hierarchical blocks, which are similar to blocks on a block diagram. Descending into a hierarchical block will open a sub-schematic with the circuitry that is part of the block (e.g., the power supply).

-   [Part 9: Creating Hierarchical Blocks](https://www.youtube.com/watch?v=Szi9mB9V5rM) from iEngineered

## Working With Part Libraries

-   How to create and add a new custom library to your project: <working-with-libraries.html>
-   How to update your design cache if you update a part in your library: <updating-part-in-your-library.html>
