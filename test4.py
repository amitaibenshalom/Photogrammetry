import win32gui
import win32con
import time

def hide_taskbar():
    win32gui.ShowWindow(win32gui.FindWindow("Shell_TrayWnd", None), win32con.SW_HIDE)

def restore_taskbar():
    win32gui.ShowWindow(win32gui.FindWindoanyw("Shell_TrayWnd", None), win32con.SW_RESTORE)


def hide_start_menu():
    win32gui.ShowWindow(win32gui.FindWindow("Windows.UI.Core.CoreWindow", None), win32con.SW_HIDE)

def restore_start_menu():
    win32gui.ShowWindow(win32gui.FindWindow("Windows.UI.Core.CoreWindow", None), win32con.SW_RESTORE)

if __name__ == "__main__":

    # hide the Taskbar
    hide_taskbar()
    # Hide the Start Menu
    hide_start_menu()

    # Wait for 5 seconds
    time.sleep(5)

    # Restore the Start Menu
    restore_start_menu()
    # Restore the Taskbar
    restore_taskbar()