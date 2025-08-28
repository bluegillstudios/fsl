import os
import subprocess
import urllib.request
import zipfile
import sys

QEMU_DIR = "FSL/qemu"
QEMU_EXE = os.path.join(QEMU_DIR, "qemu-system-x86_64.exe")

def ensure_qemu():
    if os.path.exists(QEMU_EXE):
        return QEMU_EXE

    print("QEMU not found. Downloading... (This is a necessary step for FSL to run distros)")
    os.makedirs(QEMU_DIR, exist_ok=True)

    url = "https://qemu.weilnetz.de/w64/2025/qemu-w64-setup-20250210.exe"  # 2/10/25 release
    local_path = os.path.join(QEMU_DIR, "qemu-installer.exe")

    urllib.request.urlretrieve(url, local_path)
    print("QEMU downloaded. Installing...")

    # Run silent installation to FSL/qemu
    subprocess.call([local_path, "/S", "/D=" + os.path.abspath(QEMU_DIR)])
    os.remove(local_path)

    if not os.path.exists(QEMU_EXE):
        print("Failed to install QEMU. Please install manually.")
        sys.exit(1)

    return QEMU_EXE

def run_distro(distro_name):
    distro_dir = os.path.join("FSL/distros", distro_name)
    rootfs = os.path.join(distro_dir, "rootfs.img")
    kernel = os.path.join(distro_dir, "kernel")

    if not os.path.exists(rootfs) or not os.path.exists(kernel):
        print(f"{distro_name} is not installed correctly.")
        return

    qemu = ensure_qemu()

    print(f"Launching {distro_name} using QEMU...")
    subprocess.call([
        qemu,
        "-kernel", kernel,
        "-hda", rootfs,
        "-append", "root=/dev/sda console=ttyS0",
        "-nographic"
    ])