---
title: Fall 2022 Software Install
weight: 1
summary: The following is the approach you can use to quickly get software installed.
author: Dan Aukes
---

## Introduction

The following is the approach you can use to quickly get software installed

## Chocolatey

Chocolatey is a windows-based package manager that automates downloading and installing a ton of software for windows.  We'll use it where we can.

1. open up powershell (start-->"Windows Powershell") in administrative mode (click on the arrow to the right of "Windows Powershell" text in the start menu and "run as administrator")

1. paste in the following line to install chocolatey

    <!--Set-ExecutionPolicy AllSigned-->

    ```bash
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    ```

1. close the powershell window and open a new one;

    ```bash
    choco install -y putty.install kicad vcredist2013
    ```

1. optional but really useful tools:

    ```bash
    choco install -y adobereader notepadplusplus 7zip grepwin kdiff3
    ```
## VB 3.5

1. go to start-->control panel-->programs
1. on the left side bar, select "turn windows features on or off"
1. select ".net framework 3.5"


## Visual C++ Redistributable

if you did not follow the chocolatey install instructions above you can download it here:

http://updates.cypress.com/updates/prerequisite/vcredist_x86_2013.exe

## Discrete Installers

1. Create an account with Infineon
1. Download and install [PSoC Creator](https://www.infineon.com/cms/en/design-support/tools/sdk/psoc-software/psoc-creator/)
    1. Choose Typical Installation 


## Optional or Separate Installers

* [PSoC Programmer](https://www.infineon.com/cms/en/design-support/tools/programming-testing/psoc-programming-solutions/) is included with PSoC Creator install as a plugin, so no need to reinstall.
* The [CySmart Bluetooth Tool](https://www.infineon.com/cms/en/design-support/tools/utilities/wireless-connectivity/cysmart-bluetooth-le-test-and-debug-tool/)
* The CySmart Phone App can be installed on your phone to communicate with the bluetooth device directly. ([Android](https://play.google.com/store/apps/details?id=com.cypress.cysmart&hl=en_US&gl=US)
 / [iOS](https://apps.apple.com/us/app/cysmart/id928939093))
