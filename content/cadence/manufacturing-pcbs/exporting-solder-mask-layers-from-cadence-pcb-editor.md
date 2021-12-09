---
tags:
- cadence
- pcb
title: Exporting Solder Mask Layers from Cadence PCB Editor
---

## What is a solder mask?

[Solder mask](https://en.wikipedia.org/wiki/Solder_mask) is the thin polymer layer that is applied to a printed circuit board to insulate copper traces from unwanted connections. It is often green, red, or blue, and is put over all parts of a PCB except where components are to be soldered.

## How do you create a solder mask layer in PCB Editor?

1.  Export TOP, BOTTOM, and OUTLINE Gerber files for your design (see [Exporting Gerber Files from Cadence](/exporting-gerber-files-from-cadence-pcb-editor/)).

2.  In PCB Editor, open your completed design and choose Manufacture > Artwork... (see Figure 1). The "Artwork Control Form" will open (see Figure 2).

    ![Figure 1: Manufacture > Artwork... menu option](/solder_mask_figures/figure-01.png)

    ![Figure 2: Artwork Control Form](/solder_mask_figures/figure-02.png)

3.  Right-click on any of the folders in the "Available films" section and select "Add Manual" (see Figure 3). The film naming dialog box will appear (see Figure 4).

    ![Figure 3: Add Manual contextual menu option](/solder_mask_figures/figure-03.png)
                                
  
4.  In the film naming dialog box, name the new film name SoldermaskTop (or something similar, see Figure 4) and click OK. The "Subclass Selection" dialog box will appear (see Figures 5, 6, and 7).

    ![Figure 4: Film naming dialog box](/solder_mask_figures/figure-04.png)

5.  In the "Subclass Selection" dialog box, expand the DRC ERROR CLASS, PIN, and VIA CLASS folders and check the box next to SOLDERMASK_TOP in each folder (See Figures 5, 6, and 7). Click OK.

    ![Figure 5: DRC ERROR CLASS](/solder_mask_figures/figure-05.png)

    ![Figure 6: PIN](/solder_mask_figures/figure-06.png)

    ![Figure 7: VIA CLASS](/solder_mask_figures/figure-07.png)

6.  In "Artwork Control Form", ensure that "Film name" is SoldermaskTop and "Undefined line width" is 0.01 (see Figure 8).

    ![Figure 8: Film name and undefined line width options](/solder_mask_figures/figure-08.png)
                          
  
7.  Repeat steps 3 - 6 to create a solder mask for the bottom layer, if desired.

8.  Under "Available films", select both the SoldermaskTop and SoldermaskBottom and click "Create Artwork".

9.  If successful, you will see the message in Figure 9.

    ![Figure 9: Success!](/solder_mask_figures/figure-09.png)
                                            
  
*Based on a tutorial by Seana O'Reilly*
