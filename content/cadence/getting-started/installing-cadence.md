---
tags:
- asu
- software
- cadence
- pcb
title: Installing Cadence
---

## Installation

### System Requirements

-   **PC:** Windows 7, 8, 8.1, 10, or greater ([Hardware and Software Requirements](https://www.ema-eda.com/sites/ema/files/resources/files/Cadence%20Allegro%20and%20OrCAD%20Hardware%20and%20Software%20Requirements%20-%2017.2-2016%20Release.pdf))
-   **Mac:** Windows 7, 8, 8.1, 10 or greater running on [Boot Camp](https://www.apple.com/support/bootcamp/) or [Parallels](http://www.parallels.com/)

### Before Installing...

Cadence has been known to change environment variables used by other software.  One of those is the HOME variable.  If left unset, it will add this variable and define it as "C:/Cadence/SPB_Data-Silent/"

It is therefore recommended to set that variable so that your other software remains working

Open up the file explorer (win+e)

Navigate to "This PC", right click and select properties.

On the left hand side select "advanced system settings-->environment variables"

In the **top** window, look for the HOME environment variable.  If it exists, you leave it as is

1.  If it doesn't exist, select "new"
2.  In variable name, type HOME (all caps)
3.  In the value field, enter the path to your user directory "c:/users/MYUSERNAME".  You can browse to the right directory

Save your changes.

### Instructions

1.  Go to Canvas and find the announcement from Dr. Jordan on Cadence installation.
2.  Download Cadence17.4.zip from the link provided. The installer is over 8.2 GB so make sure you are using high-speed Internet at home or on campus.

Double-click the Cadence17.4.zip file to decompress the installer. You can delete the ZIP file after it is decompressed.

Open the Cadence17.4 folder and double-click InstallTPSCadence.vbs to initiate the installation. There is no status bar or completion message during the installation process, which may take up to an hour. You will know it is complete when the installer icon disappears from the task bar. You can delete the installation folder after it has finished installation.

Download the HotFix  from the link provided. The HotFix is over 4.66 GB so make sure you are using high-speed Internet at home or on campus.

Decompress the Hotfix ZIP file. You can delete the ZIP file after it is decompressed.

Launch setup.exe to initiate the HotFix installation. The HotFix has a status bar indicating when it is complete.

Confirm that Cadence has installed correctly by launching Start > Cadence PCB 17.4-2019 > Capture CIS 17.4. This program allows you to model electronic schematics.

Follow the [Configuring Cadence](/configuring-cadence/) instructions to configure and optimize Cadence for the ASU Polytechnic engineering programs.

## Using Cadence On Campus

-   Cadence is available in the following computer labs at ASU: PRLTA 103, PRLTA 109, and PRLTA 117.
-   You can also use Cadence on campus when connected to the ASU wifi network.

## Using Cadence in On Campus Housing or Off Campus

In order to use Cadence on your computer either in on-campus housing or off campus, you must connect to the [ASU VPN](https://sslvpn.asu.edu/) prior to launching Cadence. This allows Cadence to connect to the ASU license server.

## Most Common Errors

**Q:** What if I don't have enough hard drive space to install Cadence on my computer?

**A: **

1.  Free space on your hard drive
2.  Use an external hard drive on your computer
3.  Use Cadence on the computers in PRLTA 103/109/117

**Q:** During installation, I get an error about a potential Trojan horse. What should I do?

**A:** Right click on the installer and click "Run as administrator".

**Q:** During installation, the installer fails because it cannot find a file. What should I do?

**A:** Make sure to unzip the Cadence17.4.zip file to a folder before running Install_Cadence17.4.exe. Also make sure that there are no spaces in the folder path that in which the installer is located.
