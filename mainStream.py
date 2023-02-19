import threading
import gui
import ChatBot
import Output
import sys
import debugpy
from getpass import getpass

def main():
    b = threading.Thread(target = ChatBot.main)
    c = threading.Thread(target = Output.main)
    b.start()
    c.start()
    gui.main()
    b.join()
    c.join()

def debug():
    b = threading.Thread(target = ChatBot.main)
    b.start()
    while True:
        x = input()
        debugpy.set(x)

