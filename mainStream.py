import threading
import gui
import ChatBot
import Output
import sys
import time

global flag
flag = True

def main():
    a = threading.Thread(target = gui.main)
    b = threading.Thread(target = ChatBot.main)
    c = threading.Thread(target = Output.main)
    a.start()
    b.start()
    c.start()
    cloth()


def cloth():
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        global flag
        flag=False
        sys.exit