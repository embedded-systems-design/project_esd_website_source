---
tags:
- cadence
- pcb
title: Creating Custom Footprints
---

You can try to [find existing footprints](/finding-existing-pcb-footprints-for-cadence-pcb-editor/) for components, but most components will require custom footprints.

If you are not able to find an existing footprint for a component, then you will need to make a custom footprint. In order to make a custom footprint, you will need a datasheet for the component that includes mechanical dimensions of the component and footprint.

The process for creating a footprint is as follows:

[Create a custom padstack](/creating-a-custom-padstack-in-cadence/) for the component. A [padstack](https://www.speedingedge.com/PDF-Files/anatomy%20of%20a%20plated%20hole.pdf) is a design for the exposed copper surface area for each hole or pad on the board where the component is mounted and soldered.

Create a custom footprint for the component. There are two ways to do this:

1.  [Creating a custom footprint using Package Designer](/creating-a-custom-pcb-footprint-using-package-designer-in-cadence/) - useful for symmetric ICs (e.g., microcontrollers). Does not work well for parts that have mechanical or thermal pads or non-symmetric packages (e.g., voltage regulators or MOSFETs)
2.  [Creating a custom footprint manually](/creating-a-custom-pcb-footprint-manually-in-cadence/) / [creating a custom SMD footprint manually](/creating-a-custom-smd-footprint-manually-in-cadence/)

[Update the library search path in Design Entry CIS](/changing-the-default-via-padstack-in-cadence-pcb-editor_4/)

[Update the library search path in PCB Editor](/changing-the-default-via-padstack-in-cadence-pcb-editor/)

<iframe width="560" height="315" src="https://www.youtube.com/embed/UFB1-EyFxco" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Figure 1: Video walkthrough of creating a custom footprint (by Ryan Sparks, 2020)
