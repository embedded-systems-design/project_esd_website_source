---
title: Anaconda (Python) Installation Tutorial
---

## Introduction

This tutorial is for installing the anaconda python distribution on windows.

## Windows Installation

These installation instructions are for computers that **do** **not** have Python or Anaconda installed already. Python and Anaconda do not come installed by default on most computers so if you haven't installed them intentionally, these instructions likely apply to you. If you **do** have another version of Python installed, then please ask Dr. Aukes for further details.

1.  Download and install [*Anaconda*](https://www.anaconda.com/products/individual#Downloads) (Python 3.9, x64) with the following options:
    -   Install for "All Users (requires admin privileges)" to the default directory (e.g., C:\\ProgramData\\Anaconda3 )
    -   Check the "Add Anaconda3 to the system PATH environment variable" box
    -   Check the "Register Anaconda3 as the system Python 3.9" box
2.  Install additional software packages
    a.  In Windows, go to the search bar and type "cmd". Once you see the Command Prompt app in the list, right click on it and choose "Run as administrator" from the contextual menu.
    b.  Paste each of the following lines (one at a time) at the command prompt and press enter:

``` {.bash}
conda update --all
pip install thonny
```
