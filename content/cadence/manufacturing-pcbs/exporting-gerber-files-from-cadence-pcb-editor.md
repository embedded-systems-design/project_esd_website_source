---
tags:
- tutorial
- footprint
- cadence
- pcb
title: Exporting Gerber files from Cadence PCB Editor
---

## What is a Gerber file? {#what-is-a-gerber-file style="text-align: left;"}

A [Gerber file](https://en.wikipedia.org/wiki/Gerber_format) (also known as *artwork*) is a 2-D graphical representation of a single layer of a PCB. A typical design will have individual Gerber files for each layer (e.g., top copper, bottom copper, top silkscreen, bottom silkscreen, top soldermask, bottom soldermask) of a PCB.

## What is a drill file? {#what-is-a-drill-file style="text-align: left;"}

A drill file (also known as a NC Drill file) stores both the specific sizes and types of drill bits that will be used in manufacturing a PCB in addition to the specific coordinate locations where each hole must be drilled. Our equipment uses files that are in [Excellon format](https://en.wikipedia.org/wiki/Excellon_format).

You need **both** Gerber files for each layer **and** a single drill file in order to successfully submit your design for manufacturing.

## How do I export Gerber files from Cadence? {#how-do-i-export-gerber-files-from-cadence style="text-align: left;"}

1.  Open your PCB layout in Allegro PCB Designer

2.  Choose "Manufacture > Artwork..." The Artwork Control Form window (see Figure 1) appears.

  -------------------------------------------------------------------
  [![](/exporting_gerber_files/2.png)](/exporting_gerber_files/2.png)
  Figure 1: Artwork window
  -------------------------------------------------------------------

3.  Next, a board outline must be added. Right-click on the TOP folder and choose "Add Manual" (see Figure 2).

  -------------------------------------------------------------------
  [![](/exporting_gerber_files/3.png)](/exporting_gerber_files/3.png)
  Figure 2: Right-click on TOP and choose "Add Manual"
  -------------------------------------------------------------------

4.  Enter a film name of OUTLINE and click "OK" (see Figure 3).

  -------------------------------------------------------------------
  [![](/exporting_gerber_files/4.png)](/exporting_gerber_files/4.png)
  Figure 3: Film Name window
  -------------------------------------------------------------------

4.5. Expand OUTLINE folder and right click on "BOARD GEOMETRY/DESIGN_OUTLINE" and select add.

  -------------------------------------------------------------------
  [![](/exporting_gerber_files/5.png)](/exporting_gerber_files/5.png)
  Figure 3.5: Subclass Selection window
  -------------------------------------------------------------------

5.  In the Subclass Selection window (see Figure 4), expand the BOARD GEOMETRY folder and check the box next to DESIGN_OUTLINE. Click "OK".

  -------------------------------------------------------------------
  [![](/exporting_gerber_files/6.png)](/exporting_gerber_files/6.png)
  Figure 4: Subclass Selection window
  -------------------------------------------------------------------

6.  Select the OUTLINE checkbox (see Figure 5). Make sure in Film options that "Film name: DESIGN_OUTLINE" appears (if it does not, select the OUTLINE checkbox again). Set the Undefined line width to 0.1.

  -------------------------------------------------------------------
  [![](/exporting_gerber_files/7.png)](/exporting_gerber_files/7.png)
  Figure 5: Artwork Control Form
  -------------------------------------------------------------------

7.  If you have an anti-etch (rubout), you will need to add it to the layer that you put it on. Click on the down arrow under the layer folder(s) that you added it too. Then, right-click on the items in the folder and select Add (see Figure 6).

![](/figures/figure_267.png)

Figure 6: Add anti-etch layer

8.  Then, expand the anti-etch subclass folder and select the box next to the layer you are adding it to (see Figure 7). Repeat this process for each layer that you have an anti-etch on.

![](/figures/figure_268.png)

Figure 7: Adding the anti-etch layer to the top

9.  Click the "Select all" button to output all of the layers

10. Click "Create Artwork" to export the Gerber files

11. Click "OK" to return to the layout

## How do I export solder mask files from Cadence? {#how-do-i-export-solder-mask-files-from-cadence style="text-align: left;"}

See the [Exporting Solder Mask Layers from Cadence PCB Editor](exporting-solder-mask-layers-from-cadence-pcb-editor.html) tutorial

## How do I export drill files from Cadence? {#how-do-i-export-drill-files-from-cadence style="text-align: left;"}

1.  Open your PCB layout in Allegro PCB Designer

2.  Choose "Manufacture > NC > NC Drill..." The NC Drill window (see Figure 6) appears.

      ---------------------------------------------------------------------------------------------
      [![](/exporting_gerber_files/8.png)](/exporting_gerber_files/8.png)
      ---------------------------------------------------------------------------------------------
      Figure 6: NC Drill window

      ---------------------------------------------------------------------------------------------

3.  Click "Parameters..." The Parameters window (see Figure 7) appears.

      ---------------------------------------------------------------------------------------------
      [![](/exporting_gerber_files/1.png)](/exporting_gerber_files/1.png)
      Figure 7: NC Parameters window
      ---------------------------------------------------------------------------------------------

4.  Select "Enhanced Excellon format" and click "Close"

5.  Name the drill file and save it in the same directory as your project

6.  Select "Auto tool select" and "Repeat codes"

7.  Click "Drill" to export the drill file

8.  Click "Close" to return to the layout
