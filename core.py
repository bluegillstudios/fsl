import sys
import os
from manager import list_distros, install_distro
from shell import run_distro

def ensure_dirs():
    os.makedirs("FSL/distros", exist_ok=True)

def main():
    if len(sys.argv) < 2:
        print("Usage: python core.py [list|install|run] [distro_name]")
        return

    cmd = sys.argv[1]
    ensure_dirs()

    if cmd == "list":
        list_distros()
    elif cmd == "install":
        if len(sys.argv) < 3:
            print("Specify a distro to install.")
            return
        install_distro(sys.argv[2])
    elif cmd == "run":
        if len(sys.argv) < 3:
            print("Specify a distro to run.")
            return
        run_distro(sys.argv[2])
    else:
        print("Unknown command.")

if __name__ == "__main__":
    main()
