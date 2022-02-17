---
title: quick setup steps
published: True
---

1. install [miniconda](https://docs.conda.io/en/latest/miniconda.html) [win6](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe)
    1. if on a shared computer without administrative access, can be "just for me".
    2. ```pip install esp32 thonny```
1. (optional) Install [Silabs cp210x driver](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) [windows download](https://www.silabs.com/documents/public/software/CP210x_Universal_Windows_Driver.zip)

    _This step is only required if the device is not recognized as a virtual COM port._

1. (optional) add anaconda to your path
 
    ```set PATH=C:\Users\<MYUSERNAME>\Miniconda3;C:\Users\<MYUSERNAME>\Miniconda3\Library\mingw-w64\bin;C:\Users\<MYUSERNAME>\Miniconda3\Library\usr\bin;C:\Users\<MYUSERNAME>\Miniconda3\Library\bin;C:\Users\daukes\Miniconda3\Scripts;%PATH%```
    
    * Replace <MYUSERNAME> with your username; confirm the path exists.
    * This step is required every time you load thonny if you installed "just for me" or are on an administratively locked pc.
    
1. type in ```thonny```
1. download [firmware](https://micropython.org/resources/firmware/esp32-20220117-v1.18.bin)
1. open cmd and type ```thonny```
1. open up tools-->options, select the "interpreter" tab and in the bottom right hand corner select "install or update firmware".  select the right port corresponding to the "Silicon Labs CP210X USB to UART Bridge Com(XY)"
1. select the firmware you downloaded, eg "esp32-20220117-v1.18.bin" and hit "install"
1. wait for the install to finish
1. open up tools-->options, select the "interpreter" tab and ensure that "Micropython (ESP32)" is selected.  Select the "Silicon Labs CP210X USB to UART Bridge Com(XY)" down below.  Hit ok.
1. Look at the interpreter window.  You should see:

    ```
    MicroPython v1.18 on 2022-01-17; ESP32 module with ESP32
    
    Type "help()" for more information.
    >>> 
    ```