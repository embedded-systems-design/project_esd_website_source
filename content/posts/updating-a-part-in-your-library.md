---
tags:
- ecad
- cadence
title: Updating a Part in your Library
---

## Updating a Part in your Library

[![](/figures/figure_071.png){class="img-fluid"}](/larger/image0253.png) Sometimes its necessary to make small changes to your parts as you learn more about them or need to define them better in order to identify more design mistakes during the design process. But it's difficult to know how to propagate these changes to a given schematic. Let's say you have made a part but forgot to add a part outline, but you already connected it up in your schematic.

## Steps

[](https://draft.blogger.com/blogger.g?blogID=6469592703220698319)

[](https://draft.blogger.com/blogger.g?blogID=6469592703220698319)

[](https://draft.blogger.com/blogger.g?blogID=6469592703220698319)

[](https://draft.blogger.com/blogger.g?blogID=6469592703220698319)

[](https://draft.blogger.com/blogger.g?blogID=6469592703220698319)

[](https://draft.blogger.com/blogger.g?blogID=6469592703220698319)

[](https://draft.blogger.com/blogger.g?blogID=6469592703220698319)

1.  Go into the project explorer and navigate to the library in which your custom part is, and open it up.

    [![](/figures/figure_073.png){class="img-fluid"}](/larger/image0254.png)

2.  Make the necessary changes to your part and save using "ctrl+s" or by right clicking on the active tab and selecting "save".

    [![](/figures/figure_074.png){class="img-fluid"}](/larger/image0255.png)

3.  Now you need to propagate your changes to your schematic. In the project explorer, go up to the affected schematic, expand until you find the design cache, identify the changed part, right click, and select "update cache". Select yes to all the dialog boxes and go back to your schematic.

    [![](/figures/figure_075.png){class="img-fluid"}](/larger/image0256.png)

4.  Your schematic is now updated. Make sure you fix any connection problems if you updated pin names or numbers.

[![](/figures/figure_072.png){class="img-fluid"}](/larger/image0257.png)
