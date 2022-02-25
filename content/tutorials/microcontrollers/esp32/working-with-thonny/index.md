---
title: Working with Thonny
---


## Menu & Icons

### File

![File Menu](filemenu.png)

* File --> Open(ctrl+o): If the ESP32 is connected it permits you to open a file either on your computer or from the ESP32's file space.

    ![Local vs. Remote File System Selection](local-remote.png)

* File --> Save(ctrl+s): Saves the file to the current destination
* File --> Save As(ctrl+shift+s): Permits you to save the file to a new destination, as well as to switch between saving to PC or ESP32

## Run

![Run Menu](runmenu.png)

* Run --> Run current script(f5): This runs whatever code is in your current window.  If the file is not saved, it will ask where to save it, but the code is executed _through the shell_ rather than through the normal startup execution of the ESP32.  You can save your code to your computer and run it on the ESP32 just by hitting f5, but then this means that once restarted, the ESP32 will not be able to run the code without running it again through Thonny.
* Run --> Stop/Restart Backend: This will attempt to restart the shell, if for example you want to put the ESP32 in "interactive" mode after it was restarted and began to run its internal boot.py --> main.py sequence.


## Shell / Python Interpreter

![Shell](shell.png)

The shell is at the bottom, and permits you to interact directly with the ESP32.  Type in a python command and it will run it and (usually) return a value.

For example:

```python
MicroPython v1.18 on 2022-01-17; ESP32 module with ESP32
Type "help()" for more information.
>>> a=1
>>> a
1
>>> 
```

### Shortcuts

![Interrupted Code Execution](interrupt.png)

* Ctrl+C: This stops (interrupts) execution of your code, wherever it is.  Python throws an exception and indicates where it was stopped.

## Files

* boot.py: If this file is present on the ESP32, it will be the first code to run after a hard reset
* main.py: If this file is present, it will be the second script that gets run automatically after a hard reset.  It only runs once, so you have to implement a ``while``` loop if you want code to continue running.

## ESP32

* Reset Button (EN): Use this button to restart the ESP32
* Bootloader Button (Boot): This doesn't seem to be necessary to program or work with micropython.  It is most likely used for programming with other tools/languages/IDE's to initiate "bootloader mode".
