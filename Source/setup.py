import importlib
import subprocess
import platform

def install(package):
    subprocess.check_call(["python", "-m", "pip", "install", package])

def check_install(package):
    try:
        importlib.import_module(package)
    except ImportError:
        return False
    return True

def wait_for_key():
    if platform.system() == 'Windows':
        import msvcrt
        msvcrt.getch()
    else:
        import termios
        import sys
        import tty
        tty.setcbreak(sys.stdin.fileno())
        sys.stdin.read(1)

def main():
    packages = ["opencv-python", "Pillow", "pyscreeze", "pyautogui", "keyboard"]

    for package in packages:
        if not check_install(package):
            print(f"Installing {package}...")
            install(package)
            print(f"{package} installed successfully.")

    print("All required packages are installed.")

    print("Press any key to exit...")
    wait_for_key()

if __name__ == "__main__":
    main()
