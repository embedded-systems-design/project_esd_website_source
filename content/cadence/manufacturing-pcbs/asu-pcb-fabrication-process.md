---
tags:
- asu
- cadence
- pcb
title: ASU PCB Fabrication Process
---

## How are PCBs fabricated at ASU?

The following video shows our PCB manufacturing process.

<iframe width="560" height="315" src="https://www.youtube.com/embed/DJPIYXGpPVo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

*Video by Peralta Engineering Studios*

## How do you prepare and submit Cadence PCB design for fabrication?

[Label the PCB design](/adding-text-to-a-layout-in-cadence-pcb-editor/) with your name, course, and team number *(required for manufacturing)*

[Run a Design Rules Check in Cadence PCB Editor](/running-design-rules-check-in-cadence-pcb-editor/) and fix any errors identified

[Export Gerber files from Cadence PCB Editor](/exporting-gerber-files-from-cadence-pcb-editor/)

[Export solder mask layers from Cadence PCB Editor](/exporting-solder-mask-layers-from-cadence-pcb-editor/) *(optional, final design only)*

Run a [Design for Manufacturing check](https://peraltastudios.engineering.asu.edu/wp-content/uploads/2021/08/dfmchecker.html) and fix any errors identified

[Print a 1:1 (100%)-sized copy of your PCB design](/printing-a-pcb-layout-in-cadence-pcb-editor/) and physically place all components on the printout to confirm that the footprints are correct. This is particularly important for ICs, connectors, and daughterboards.

Show your successful DFM check results to a TA or professor so that they can document approval of your PCB design for fabrication. **You must receive approval from a TA or the professor before your PCB will be fabricated.**

Zip all of your PCB files together in one ZIP folder with filename YourName###.zip, where ### is your team number.

1.  Top.art
2.  Bottom.art
3.  Outline.art
4.  Drill.drl
5.  SolderMaskTop.art
6.  SolderMaskBottom.art

Submit your files at [fultonapps.asu.edu/polylab](http://fultonapps.asu.edu/polylab). Include the following information in the request details:

1.  Professor and class
2.  Quantity of boards *(only 1 allowed per design; exceptions allowed with professor approval)*
3.  Solder mask needed? *(only allowed for final board designs)*
4.  Rub out area needed? If yes, specify location. (*Pro tip:* Rub out copper underneath antennas)
5.  Copper thickness (0.5, 1, or 2 oz/ft^2)

You must also attach the following files to your request:

1. ZIP of your Gerber files created above
2. PDF of the results of the [Design for Manufacturing check](https://peraltastudios.engineering.asu.edu/wp-content/uploads/2021/08/dfmchecker.html)

You will receive an emails from the Poly Lab Request Notification System indicating the acceptance of the job and when your PCB is ready to be picked up. If you are interested in learning about and being a part of the fabrication process with the LPKF mill, please see one of the staff members in PRLTA 109. If you have any questions, please contact <Peralta.Labs@asu.edu>

After receiving your PCB, make sure to do a continuity test on all traces and vias before adding parts and soldering.
