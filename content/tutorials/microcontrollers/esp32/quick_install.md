---
title: quick setup steps
published: True
---

1. install [miniconda](https://docs.conda.io/en/latest/miniconda.html) (win64)[https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe]
    1. if on a shared computer without administrative access, can be "just for me".
    2. ```pip install esp32 thonny```
2. Install [Silabs cp210x driver](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) (optional) [windows download](https://www.silabs.com/documents/public/software/CP210x_Universal_Windows_Driver.zip)
3. (optional if you are on an administratively locked pc) open cmd
    ```set PATH=C:\Users\daukes\Miniconda3;C:\Users\daukes\Miniconda3\Library\mingw-w64\bin;C:\Users\daukes\Miniconda3\Library\usr\bin;C:\Users\daukes\Miniconda3\Library\bin;C:\Users\daukes\Miniconda3\Scripts;%PATH%```
4. type in ```thonny```
5. download [firmware](https://micropython.org/resources/firmware/esp32-20220117-v1.18.bin)
6. open cmd and type ```thonny```
7. open up tools-->options, select the "interpreter" tab and in the bottom right hand corner select "install or update firmware".  select the right port corresponding to the "Silicon Labs CP210X USB to UART Bridge Com(XY)"
8. select the firmware you downloaded, eg "esp32-20220117-v1.18.bin" and hit "install"
9. wait for the install to finish
11. open up tools-->options, select the "interpreter" tab and ensure that "Micropython (ESP32)" is selected.  Select the "Silicon Labs CP210X USB to UART Bridge Com(XY)" down below.  Hit ok.
12. Look at the interpreter window.  You should see:

    ```
    MicroPython v1.18 on 2022-01-17; ESP32 module with ESP32
    
    Type "help()" for more information.
    >>> 
    ```

13. 