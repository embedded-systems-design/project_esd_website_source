---
tags:
- cadence
title: Resetting Reference Designators in Cadence Design Entry CIS
---

## Introduction

When drawing a circuit, you will often move and delete components as part of the process, meaning that the reference designators (e.g., R1, C1, U1) may be out of order or scattered throughout your design. This tutorial walks through how to reset the reference designators so they are sequential.

***WARNING:** Do not reset the reference designators after you have moved a design to PCB Editor, or it may break links between the schematic and PCB layout.*

## How do you reset the reference designators in Cadence Design Entry CIS?

1.  Open your schematic in Design Entry CIS

2.  In Design Entry CIS, select the root folder for your schematic and click the Annotate button in the toolbar (see Figure 1). The Annotate window will appear (see Figure 2).

    ![Figure 1: Annotate tool](/larger/image0220.png)

    ![Figure 2: Annotate Window](/larger/image0221.png)

3.  In the Annotate window (see Figure 2), choose Action > Reset part references to "?". Click OK.

4.  Click the Annotate button again, and this time choose Action > Incremental reference update. Click OK. Your reference designators are now renumbered!

*Based on a tutorial written by Robert Goby and updated by Ryan Sparks*
