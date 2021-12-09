---
title: Merging Multiple Schematics into a Single Schematic
tags: [cadence,]
---

# Merging Multiple Schematics into a Single Schematic

1.  Take note of all the files involved in the schematics you are merging, and ensure you have all of them. These include .dsn (design), .opj (project) and .olb (library) files, in addition to .psm (Package symbol, a.k.a. PCB footprint) files.

2.  Create a new project in Capture CIS. Rename the default schematic so that you know it will contain your final combined schematic.

3.  Right click on "Referenced Projects" in the "File" menu, and click "Add File". Find all of the .opj project files which contain the schematics you're trying to merge and add them as referenced projects. This will allow you to more conveniently open them alongside your combined project and extract the schematics.

> ![Text Description automatically generated]

4.  Create a new schematic, separate from the default one in the project, to contain copies of each original schematic as separate pages.

5.  Open each of your newly referenced projects. One by one, find their schematics in the "File" navigation menu, right click the page(s) and hit Copy. Then go back to your combined project, right-click your "source" schematic, and click Paste.

![][1]![Text Description automatically generated with medium confidence]

6.  Note that as you do this, the components used in each added schematic become part of the design cache. When combining projects created on different computers, you may find that the library path for some components now points to an invalid location, which can be corrected by right clicking them, selecting "Replace Cache", and specifying a correct path for each.

![][2]

7.  Add all .olb library files referenced in the source schematics/projects by right-clicking "Library" under "Design Resources" and then selecting to add the respective files.

![Graphical user interface, text, application Description automatically generated]

8.  Place all .psm files for referenced footprints in the schematic in one of the correct directories to be recognized by Cadence. These will be under "Allegro Footprints" in Capture.ini and the "psmpath" setting in PCB Editor; if you use the provided Cadence folder hierarchy and configure Cadence accordingly, the "symbols" folder will work.

9.  Take a look at the individual schematics, and select a page size for the combined schematic which will have sufficient space to accommodate all of them.

10. In the referenced projects, open each individual schematic page. Use Control + A to select all and Control + C to copy, then Control + V to paste the contents into the combined schematic. Some items, such as the schematic information usually found in the bottom right corner, do not need to be copied over and so should be deleted in the new schematic.

11. You now have one schematic containing each original schematic on a single page.

12. Clean up your schematic, and be sure to fix any netlisting errors. If you are combining schematics in order to merge multiple subsystems into a full system, there is more work to do, such as standardizing power nets and merging components shared between subsystems (e.g. the microcontroller).

  [Text Description automatically generated]: image1.PNG 
  [1]: image2.PNG 
  [Text Description automatically generated with medium confidence]: image3.PNG 
  [2]: image4.PNG 
  [Graphical user interface, text, application Description automatically generated]: image5.PNG 
