---
tags:
- tutorial
- programming
- design
- software
- software design
title: Software design
---

## What is a finite state machine?

A finite state machine (FSM) is a way of modeling a system such that there are a limited number of finite "states" that a system can be in, and that it can only be in one of those states at a time. Events (e.g., pushing a button) cause the system to change from one state to the next. Unexpected events do not cause the system to change states, which is useful for ignoring spurious inputs. Rather than coding for every possible input, you can instead code only for inputs that matter at the given time. The following resources provide a solid conceptual framing and implementation examples:

-   [Understanding State Machines, Part 1: What are they? from Mathworks](https://www.mathworks.com/videos/understanding-state-machines-what-are-they-1-of-4-90488.html)
-   [Understanding State Machines, Part 2: Why Use Them? from Mathworks](https://www.mathworks.com/videos/understanding-state-machines-why-use-them-2-of-4-90489.html)
-   [Understanding State Machines, Part 3: Mealy and Moore Machines from Mathworks](https://www.mathworks.com/videos/understanding-state-machines-mealy-and-moore-machines-3-of-4-90490.html)
-   [Understanding State Machines, Part 4: Harel State Machines from Mathworks](https://www.mathworks.com/videos/understanding-state-machines-harel-state-machines-4-of-4-90491.html)
-   [Implementing FSMs in Embedded Systems](https://www.embedded.com/implementing-finite-state-machines-in-embedded-systems/)

## What is Unified Modeling Languageâ„¢ (UML®)?

UML is an industry-standard specification for representing software designs. It is equivalent to schematics for hardware designs. More information on UML can be found at [uml.org](http://uml.org/). Official documentation on UML is available at:

-   [25 UML Diagrams](https://www.uml-diagrams.org/uml-25-diagrams.html)
-   [Official UML Examples](https://www.uml-diagrams.org/index-examples.html)
-   [UML Diagram Types Guide: Learn About All Types of UML Diagrams with Examples](https://creately.com/blog/diagrams/uml-diagram-types-examples/) from creately
-   [All You Need to Know About UML Diagrams: Types and 5+ Examples](https://tallyfy.com/uml-diagram/) from Tallyfy
-   [State Machine Diagram vs. Activity Diagram](https://www.visual-paradigm.com/guide/uml-unified-modeling-language/state-machine-diagram-vs-activity-diagram/) from Visual Paradigm
-   [What is the difference between an activity and a state chart diagram?](https://www.quora.com/What-is-the-difference-between-an-activity-and-a-statechart-diagram) from Quora
-   [Difference between StateChart and Activity Diagram](https://stackoverflow.com/questions/5559171/difference-between-statechart-and-activity-diagram) from stackoverflow

Common UML diagrams that you may use include:

**Activity Diagram.** An [Activity Diagram](https://en.wikipedia.org/wiki/Activity_diagram) (similar to a flowchart) captures the overall behavior of a program from start to finish.

-   [Official Documentation on Activity Diagrams](https://www.uml-diagrams.org/activity-diagrams.html)
-   [Activity Diagram in UML: Symbol, Components, & Example](https://www.guru99.com/uml-activity-diagram.html)
-   [UML - Activity Diagrams](https://www.tutorialspoint.com/uml/uml_activity_diagram.htm) from tutorialspoint
-   [What is an Activity Diagram](https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-uml/#activity-diagram) from Visual Paradigm
-   [UML 2 Activity Diagrams: An Agile Introduction](http://www.agilemodeling.com/artifacts/activityDiagram.htm) tutorial
-   *Example:* [Activity diagram for online shopping](http://www.uml-diagrams.org/activity-diagrams-examples.html)

**Statechart Diagram.** A [Statechart Diagram](https://en.wikipedia.org/wiki/State_diagram) is a UML representation for a finite state machine. A *[finite state machine](https://en.wikipedia.org/wiki/Finite-state_machine)* (also called a *state machine*) is a type of software design where your program is only in a single state at a time. The program changes state when a particular event happens, and remains in the same state if no event (or an unknown event) happens. This makes your program less likely to have unpredictable behavior, and is commonly used for copy machines, stoplight controllers, etc.

-   [Official Documentation on State Machine Diagrams](https://www.uml-diagrams.org/state-machine-diagrams.html)
-   [Statechart UML Tutorial with Example](https://www.guru99.com/state-machine-transition-diagram.html)
-   [UML - Statechart Diagrams](https://www.tutorialspoint.com/uml/uml_statechart_diagram.htm) from tutorialspoint
-   [What is a State Machine Diagram?](https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-uml/#state-machine-diagram) from Visual Paradigm
-   [UML Tutorial: Finite State Machines](http://is.ifmo.ru/automata_en/_UMLFSM.pdf)
-   [UML 2 State Machine Diagrams: An Agile Introduction](http://www.agilemodeling.com/artifacts/stateMachineDiagram.htm) tutorial
-   [State Machine Constructs](http://www.eetimes.com/document.asp?doc_id=1271837) tutorial from EE Times
-   [Finite State Machines for the Texas Instruments MSP430 microcontroller](http://www.ti.com/lit/an/slaa402a/slaa402a.pdf) application note

**Sequence Diagram**

-   [Official Documentation on Sequence Diagrams](https://www.uml-diagrams.org/sequence-diagrams.html)
-   [Interaction, Collaboration, and Sequence Diagrams with Examples](https://www.guru99.com/interaction-collaboration-sequence-diagrams-examples.html)
-   [What is a Sequence Diagram?](https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-uml/#sequence-diagram) from Visual Paradigm
-   [Difference between Sequence Diagram and Activity Diagram](https://www.geeksforgeeks.org/difference-between-sequence-diagram-and-activity-diagram/) from GeeksforGeeks

## What software do I use to create a UML diagram?

-   [ArgoUML](http://argouml.tigris.org/) is an excellent free open-source software engineering tool that supports the creation of a wide variety of UML diagrams. It runs on Windows, Mac OS X, and Linux.
-   [StarUML](http://staruml.io/) is another excellent freely-available program that supports the creation of a wide variety of UML diagrams. it runs on Windows, Mac OS X, and Linux.
-   
-   Draw.Io - Recommended. Add-on to google drive documents, free - [http://draw.io](http://draw.io/)
-   LucidChart - cloud-based collaborative diagramming app ASU has a site license if you use your ASU google account.  Or get an Education Account.  Add as a addin via google drive.

## What is pseudocode?

Pseudocode is a near-English representation of a program that allows you to represent the functionality of a program without worrying about the syntax. It is useful when planning how software will work. Pseudocode can be created in any text editor or word processing program. An example of pseudocode for the game Monopoly is available [here](http://www.wiley.com/college/busin/icmis/oakman/outline/chap05/slides/pseudo.htm).

*Many links above suggested by Cecilia La Place*
