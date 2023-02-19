import threading
import gui
import ChatBot
import Output
import cui
import debugpy
from getpass import getpass

def main():
    b = threading.Thread(target = ChatBot.main)
    #c = threading.Thread(target = Output.main_kari)
    b.start()
    #c.start()
    cui.main()
    #gui.main()

def debug():
    b = threading.Thread(target = ChatBot.main)
    b.start()
    while True:
        x = input()
        debugpy.set(x)

