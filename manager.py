import os
import urllib.request
import sys

DISTROS = {
    "ubuntu": {
        "rootfs_url": "https://cdimage.ubuntu.com/ubuntu-base/releases/focal/release/ubuntu-base-20.04.5-base-amd64.tar.gz",
        "kernel_url": "https://cloud-images.ubuntu.com/releases/focal/release-20230731/vmlinuz",
    },
    "alpine": {
        "rootfs_url": "https://dl-cdn.alpinelinux.org/alpine/v3.14/releases/x86_64/alpine-minirootfs-3.14.0-x86_64.tar.gz",
        "kernel_url": "https://dl-cdn.alpinelinux.org/alpine/v3.14/releases/x86_64/vmlinuz-lts",
    }
}

def list_distros():
    print("Available distros:")
    for d in DISTROS:
        print(f" - {d}")

def get_remote_file_size(url):
    try:
        with urllib.request.urlopen(url) as u:
            return int(u.info().get("Content-Length", -1))
    except Exception:
        return -1

def human_readable_size(size):
    for unit in ['B','KB','MB','GB','TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} PB"

def download_file(url, dest):
    file_size = get_remote_file_size(url)
    if file_size > 0:
        print(f"File size: {human_readable_size(file_size)}")
        confirm = input("Proceed with download? [y/N]: ").strip().lower()
        if confirm != 'y':
            print("Download cancelled.")
            return False

    def progress(count, block_size, total_size):
        percent = int(count * block_size * 100 / total_size)
        sys.stdout.write(f"\rDownloading: {percent}%")
        sys.stdout.flush()

    print(f"Downloading {url} ...")
    urllib.request.urlretrieve(url, dest, reporthook=progress if file_size > 0 else None)
    print("\nSaved to", dest)
    return True

def install_distro(name):
    if name not in DISTROS:
        print(f"Distro {name} not found.")
        return

    folder = os.path.join("FSL/distros", name)
    os.makedirs(folder, exist_ok=True)

    rootfs_path = os.path.join(folder, "rootfs.img")
    kernel_path = os.path.join(folder, "kernel")

    if not os.path.exists(rootfs_path):
        if not download_file(DISTROS[name]["rootfs_url"], rootfs_path):
            return
    else:
        print("Rootfs already exists.")

    if not os.path.exists(kernel_path):
        if not download_file(DISTROS[name]["kernel_url"], kernel_path):
            return
    else:
        print("Kernel already exists.")

    print(f"{name} installed successfully!")
