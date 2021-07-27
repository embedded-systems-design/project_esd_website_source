---
tags:
- cadence
- pcb
title: Manual Routing in Cadence PCB Editor
---

## How do I manually route a design in PCB Editor?

Your design should have a board outline and components placed, and blue lines (the "rats nest") between the components (see example, Figure 1). These blue lines are not traces, but rather points that are connected on your schematic and should be converted to traces in your design.

  ------------------------------------------------------------------------------
   [![](/figures/figure_207.png)](/larger/image0178.png)
                Figure 1: Board outline, components, and rats nest
  ------------------------------------------------------------------------------

1.  Click the "Add Connect" button in the toolbar (see Figure 2)

[![](/figures/figure_206.png)](/larger/image0179.png)

Figure 2: Add Connect button

2.  Go to the "Options" tab on the right side of the screen and change the settings for the trace as necessary (e.g., whether it will be on the top or bottom layer, which via will be used, and the line width) (see Figure 3).

*Note: *Make sure that your power and ground traces meet the recommended minimums

  ------------------------------------------------------------------------------
   [![](/figures/figure_208.png)](/larger/image0180.png)
                      Figure 3: Options tab for Add Connect
  ------------------------------------------------------------------------------

3.  Left click on a starting pin to start the trace, and left click on the ending pin to end the trace (see Figures 4 and 5).

*Note:* Avoid 90 degree angles when routing traces. They create electro-magnetic radiation that interferes with other circuits.

  ------------------------------------------------------------------------------
   [![](/figures/figure_209.png)](/larger/image0181.png)
                      Figure 4: Left click to start a trace
  ------------------------------------------------------------------------------

  ------------------------------------------------------------------------------
   [![](/figures/figure_210.png)](/larger/image0182.png)
                       Figure 5: Left click to end a trace
  ------------------------------------------------------------------------------

4.  If you need to add a via (a conductive hole from one layer to another, allowing traces to cross on different layers), you can double-left click while you are placing the trace in order to change layers (see Figure 6).

*Note:* Vias reduce the reliability of a trace. It is recommended that you minimize the number of vias used in your design.

  ------------------------------------------------------------------------------
   [![](/figures/figure_211.png)](/larger/image0183.png)
                     Figure 6: Double-left click to add a via
  ------------------------------------------------------------------------------

5.  Continue the above process until all of the rats nest lines are routed (see example, Figure 7). Note that the power and ground traces are larger than the signal traces. This is important for having a fully-functioning design.

  ------------------------------------------------------------------------------
   [![](/figures/figure_212.png)](/larger/image0184.png)
                      Figure 7: Example completed PCB design
  ------------------------------------------------------------------------------

*Note:* Manual routing of traces will almost always result in the best possible design. Auto-routing algorithms are notoriously poor and create board designs that are more complex and more difficult to debug.

## Additional Resources

-   [How to Route Multiple Traces Simultaneously video](https://www.youtube.com/watch?v=IKCEs5HOpZE) from EMA Design Automation

*Based on a tutorial by Seana O'Reilly*
