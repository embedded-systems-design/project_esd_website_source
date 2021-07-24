---
tags:
- components
- circuits
title: Strategies for using 0 Ohm Resistors
---

 

## Why use 0 ohm Resistors in a design? {#docs-internal-guid-639e596e-7fff-eb58-e2cc-d56e9d7f3db7 dir="ltr" style="background-color: white; line-height: 2.016; margin-bottom: 0pt; margin-top: 15pt; padding: 0pt 0pt 8pt;"}

0 ohm resistors act as a through hole jumper wire on manufactured PCBs. Also known as "jumper chips'' or"jumper leads", 0 ohm resistors can be substituted for vias to cross over line traces. This is useful for PCBs that have many vias already and PCBs that want to avoid vias altogether. In the PCB industry, using 0 ohm resistors over jumper wires in the design process allows one less specialized tool when assembling the PCB. It is cheaper and more practical to install a jump lead using readily available resistor placing machines over having a separate machine for just placing jumper wires. 

## Should you use this when manufacturing PCBs?  {#should-you-use-this-when-manufacturing-pcbs dir="ltr" style="background-color: white; line-height: 2.016; margin-bottom: 0pt; margin-top: 15pt; padding: 0pt 0pt 8pt;"}

Using 0 ohm resistors is practical in the course due to milling limitations of Peralta labs and use in some complex designs. Peralta labs ( the lab that prints PCB's for EGR 304 and 314) has specific instructions and limitations when it comes to manufacturing a PCB. A complex PCBs made in peralta with many vias and line traces has a higher chance of having a manufacturing error. Also, when many vias are already in place, a new trace might have multiple vias to reach its destination on the board. Depending on the design it could be more beneficial to use a 0 ohm resistor to avoid high line trace areas.

-   Note: Through hole components may not fit EGR 314's project requirements. Please check with teaching team if 0 ohm jumper resistor is applicable for EGR 314.

Based on a post written by Zachary Conley
