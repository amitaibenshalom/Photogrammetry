import win32gui
import win32con
import time

def hide_taskbar():
    win32gui.ShowWindow(win32gui.FindWindow("Shell_TrayWnd", None), win32con.SW_HIDE)

def restore_taskbar():
    win32gui.ShowWindow(win32gui.FindWindow("Shell_TrayWnd", None), win32con.SW_RESTORE)

if __name__ == "__main__":
    # Hide the taskbar
    hide_taskbar()

    # Wait for 5 seconds
    time.sleep(5)

    # Restore the taskbar
    restore_taskbar()
