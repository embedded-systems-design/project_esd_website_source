---
tags:
- cadence
- pcb
title: Creating a Board Outline in Cadence PCB Editor
---

## What is a board outline?

A board outline is the outermost boundary of a printed circuit board design. It is used by the PCB manufacturer to cut the printed circuit board to the specified size and shape.

## How do you create a board outline in Cadence PCB Editor?

1.  In PCB Editor, select the rectangle tool in the toolbar (see Figure 1).

[![](/figures/figure_213.png){width="320"}](/larger/image0074.png)

Figure 1: Rectangle tool

2.  In the "Options" tab on the right side of the screen, make sure "Active Class and Subclass" is set to Board Geometry and Design_Outline (see Figure 2).

[![](/figures/figure_214.png)](/larger/image0075.png)

Figure 2: Active Class and Subclass options

3.  If you would like to change the type of corners on the board, you can change them in the Corners section of the Options tab (see Figure 3). Options include *orthogonal* (90 degree), *chamfer* (sloping edge), and *round* (curved).

[![](/figures/figure_215.png)](/larger/image0076.png)

Figure 3: Corners options

4.  In the Shape Creation section of the Options tab, choose "Place Rectangle" and enter the width and height for the board outline in *mils* (1 mil = 0.001"; 2000 mil = 2") (see Figure 4).

[![](/figures/figure_216.png)](/larger/image0077.png)

Figure 4: Shape Creation options

5.  Place the rectangle on the board design (see Figure 5).

[![](/figures/figure_217.png)](/larger/image0078.png)

Figure 5: Board Outline Placed

6.  Choose Setup > Change Drawing Origin and click in the lower left-most point of the board outline. Your board outline is now complete!

*Based on a tutorial by Seana O'Reilly*
