# FSL (Franchuk Subsystem for Linux)
**Run Linux distros from a franchukOS app. This is a separate repository for organization reasons.**

**Version 1.0.0.0**

*FSL is a lightweight Linux subsystem for FranchukOS, inspired by WSL (Windows Subsystem for Linux). It allows users to install and run multiple Linux distributions directly from FranchukOS, using QEMU for virtualization.*

## Features

**Multiple Linux distributions: Starting with Ubuntu and Alpine, more coming in future releases.**

**Simple commands: list, install, and run distros.**

**Automatic QEMU management: FSL detects and downloads QEMU if it's missing.**

**Integration with FranchukOS terminal: Launch Linux distros directly from the GUI terminal.**

**Cross-platform support: Works on Windows PCs using FranchukOS.**

## Setup Requirements

FranchukOS Catalina (35.0) and above

Python 3.11+

Internet connection (for downloading Linux root filesystems and QEMU)

Windows-based PC (current supported platform)

## Setup

Boot FranchukOS. If you don't have it, install it here: https://github.com/bluegillstudios/franchukOS/releases. Follow the setup guides on our discord server. It is linked in this repo.

Next, use the Terminal. In the taskbar, go to System --> Terminal. 

FSL should be automatically installed. Let's set up a distro.

In the Terminal, run `fsl list`. This should output available distros to install. 

Now, let's install! Run `fsl install` and pick a distro. For example, ubuntu:

`fsl install ubuntu` 

*If you do not have QEMU installed, it will auto-install at this step in fsl/QEMU.*

FSL will automatically download the root filesystem and any required files. Once complete, you’ll see a confirmation message:

`ubuntu installed successfully.`


## Running a Linux Distribution

After installation, you can launch your distro using:

`fsl run ubuntu` (for ubuntu only)

This will open the Linux environment using QEMU in a separate thread.

Your FranchukOS terminal remains responsive while Linux runs.

To close the Linux environment, use standard Linux commands inside the distro (exit or shutdown).

## Thank you!

Thanks for using our garbage software!
