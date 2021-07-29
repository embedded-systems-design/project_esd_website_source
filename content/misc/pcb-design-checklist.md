---
tags:
- checklist
- pcb
title: PCB design checklist
---

Before exporting your PCB design for fabrication, you **must **verify the design and fix any errors. Time invested verifying your design before manufacturing will make the assembly and testing process significantly easier.

### What are best practices for the design of PCBs?

-   [Designing PCBs for Debugging - (First Board Spins) video](https://www.youtube.com/watch?v=wQcuQSO1sls) from Casey Petersen
-   [Fundamentals of Layout Out PC Boards](https://drive.google.com/a/asu.edu/file/d/0ByRWb7dgVD-rQ1d4MUJlZEVDQ1k/edit) from Jack Ardizzoni of Analog Devices
-   [Printed Circuit Board (PCB) Design Issues](https://drive.google.com/a/asu.edu/file/d/0ByRWb7dgVD-ranVQcmJoS3B2Tjg/edit) from Analog Devices
-   [PCB Design of Switch Mode Power Supplies (SMPS or Switchers)](https://www.youtube.com/watch?v=kZDnnmrQx9g) video from Casey Petersen
-   [A Practical Guide to High-Speed Printed Circuit Board Layout](https://drive.google.com/a/asu.edu/file/d/0ByRWb7dgVD-rd0w5MmE2SWo1Rk0/edit) from Jack Ardizzoni of Analog Devices
-   [High Speed System Applications: PC Board Layout and Design Tools](https://drive.google.com/a/asu.edu/file/d/0ByRWb7dgVD-rZUNvNHl1NmRma0U/edit) from Analog Devices

### General

-   All components have footprints
-   Bypass/decoupling capacitors for voltage regulators are placed as physically close as possible to the regulators
-   Bypass/decoupling capacitors for ICs are placed as physically close as possible to each IC's power and ground pins (see example of good layout, Figure 1)
-   Power and ground traces are at least 40 mil wide and were sized using a [trace width calculator](http://www.4pcb.com/trace-width-calculator.html)
-   Board space is allocated for mechanical constraints (e.g., PCB mounting holes, heat sinks, connectors)
-   The top and bottom copper layers are labeled in text "top", "bottom", and "group name"

![Figure 1: Example of good bypass capacitor placement](/larger/image0193.jpeg)
  
### Vias

-   Minimize the number of vias in your design. Vias reduce the reliability of your system.
-   No vias under components (particularly ICs)

### Additional Considerations

-   Consider how your components will be mounted when routing traces. For example, if you have a through-hole connector on the top of your board, it's better to route the traces for it on the bottom layer.
-   Make the board outline in copper
-   Make sure that the size of your board will fit inside your product enclosure
-   Do NOT use the autorouter. Use manual routing to simplify the board design. Simple design = easier debugging.
-   When using surface mount components, size 0805 resistors and capacitors (or larger) are easier to work with
-   Through-hole connectors are mechanically stronger than surface-mount connectors
-   Avoid right angles (90 degrees) in traces. Instead, "curve" the trace with a 45 degree angle around a corner
-   Fill some extra space on your board with several 0.1" spaced test points to allow for easier modifications
-   If your system uses in-system programming (ISP), place the ISP connector as physically close to the microcontroller as possible
