---
title: The First Three Questions You Should Ask When Debugging Your PCB and Possible Solutions
tags: [debugging,]
---

## Are Connections Continuous?

1. Conduct a continuity check on your board with a multimeter.

    As soon as you receive you PCB, the first thing you should always do is double check that all traces and pins that should be connected are, and those that should not be, aren't. Conducting a quick continuity test on your board not only take you about 5 minutes to do but could save you hours of trouble in the long run when you already have half your board populated and no idea where to start when a problem does arise. At least by checking the board first, you can eliminate the possibility of a manufacturing or trace drawing error from your list of reason why something does not work.
    
    ![A picture containing text, device Description automatically generated]
    
1. Check all your soldering points for continuity between the board and the pin.

    For many, this may be the first time you do some serious soldering. Soldering, while an easy concept to grasp, can be hard than it looks if not done properly. If you take your multimeter to your board and touch the pin of your already soldered component and the pad (on the backside if a through hole) or the trace the component is directly connected to and find there is no continuity, you are most likely just need to solder your pin again. Try to place some flux from a pen or as a paste onto your board before soldering and notice how much easier the solder will stick to the pad.

    However, be sure to also look for possible shorts! Shorts look like the photo shown below and can happen all the time between pins and pads that are very close to each other. Sometimes our hands are a little shaky or we did not remove enough solder form on old connection that needed to be changed. For or information about how to better your soldering skills, check out [this article] on the blog.

    ![Diagram Description automatically generated]
    
## Are Traces Correctly Routed and Pads Sticking?

1. Jump incorrect traces or fallen pads to test points or another trace.

    Sometimes we design our PCB's and notice after they are manufactured that some traces are incorrect or not continuous where we need them to be. Have no fear! You don't need a new board if a few traces are off, you can simply jump traces to where they need to be by soldering a wire between a pad to another test point or to the trace that you need to connect. This process can seem very messy, when in all honesty it's bound to happen and is normal in many hardware projects. Here are some ideas you can consider when jumping or rerouting traces:

    * Expose some of the copper on a trace by using an exacto-knife to gently scratch off some of the solder mask to prep a new connection or disconnect traces completely.

        ![A picture containing circuit, electronics Description automatically generated]

    * Use wires or a part of a wire to jump connections.

        ![A close-up of a machine Description automatically generated with low confidence]

    * Use wires to jump pins to their correct trace or missing pad to a test point.

        ![A picture containing electronics, circuit Description automatically generated]
    
        ![Close-up of a circuit board Description automatically generated with medium confidence]

##  **Is Your Pin Layout Correct?**

1.  *Compare your PCB Designer pin layout versus the datasheet's pinout.*

    One of the most seen problems every year in 304/314 is that students assume all voltage regulators have the same pin layout as each other. Students will create a 5V regulator part in Cadence and then use the same layout, make a copy, and name it a 3.3V regulator. Without checking the datasheet. Don't be this student!

    Lots of students use the LM7805 and LD1117 which are 5V and 3.3V regulators respectively. However, if you look at their pinout's, they are different:

    ![LM7805 5V Pin Layout][1]

    ![LD1117 3.3V Pin Layout][2]

    If you are in this situation like this with regulators or any other part, there are a few simple ways to fix this.

    * One option is to physically move the pins of the regulator to go through the proper holes made on the PCB. An example of this is shown below with a through-hole MOSFET:

        ![][3]

    * The second option is to alter your PCB board by cutting and re-routing traces as mentioned earlier. It's recommended you try the first option and then purse this option next if it's absolutely not possible to move the pin of a part around.

1.  *Try using a brand new copy of your component.*

    If you compare your PCB Design against the datasheets of your components and find all traces and pin layouts are correct, try switching out the part for a brand new one from the bag. This is the importance of order multiple copies of your parts. It is possible to burn out the chip by touching the soldering iron to the pins of a part at too high of a heat or too often. Sometimes if a part is from an untrusted manufacturer such as an Amazon order, parts may come faulty as well. On this note however, you should never order parts from a website or company that does not come with a datasheet or is not approved by the teaching staff beforehand.

  [A picture containing text, device Description automatically generated]: image1.jpg 
  [this article]: http://esdresources.blogspot.com/2016/02/soldering-and-desoldering-tips-and.html
  [Diagram Description automatically generated]: image2.jpeg 
  [A picture containing circuit, electronics Description automatically generated]: image3.jpeg 
  [A close-up of a machine Description automatically generated with low confidence]: image4.jpeg 
  [A picture containing electronics, circuit Description automatically generated]: image5.jpg 
  [Close-up of a circuit board Description automatically generated with medium confidence]: image6.jpg 
  [1]: image7.jpg 
  [2]: image8.jpg 
  [3]: image9.jpeg 
