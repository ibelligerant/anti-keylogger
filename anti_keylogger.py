import psutil
import ctypes
import win32api
import win32con
import win32gui
import win32process
from ctypes import wintypes

def get_foreground_process():
    hwnd = win32gui.GetForegroundWindow()
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    return psutil.Process(pid).name()

def check_keyboard_hooks():
    user32 = ctypes.windll.user32
    hooks = user32.GetKeyboardLayout(0)
    if hooks != 0x4090409:  # Default US layout
        print("[WARNING] Suspicious keyboard hook detected!")
        return True
    return False

def scan_processes_for_keyloggers():
    keylogger_signatures = ["keylogger", "hook", "interceptor", "spy"]
    suspicious_processes = []
    
    for process in psutil.process_iter(['pid', 'name']):
        try:
            for sig in keylogger_signatures:
                if sig in process.info['name'].lower():
                    suspicious_processes.append(process.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    return suspicious_processes

def main():
    print("[INFO] Scanning for keyloggers...")
    if check_keyboard_hooks():
        print("[ALERT] Potential keylogger activity detected!")
    
    suspicious_processes = scan_processes_for_keyloggers()
    if suspicious_processes:
        print("[ALERT] Suspicious processes detected:")
        for proc in suspicious_processes:
            print(f"PID: {proc['pid']}, Name: {proc['name']}")
    else:
        print("[INFO] No suspicious keyloggers detected.")

if __name__ == "__main__":
    main()
