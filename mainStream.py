import threading
import gui
import ChatBot
import Output

def main():
    #a = threading.Thread(target = gui.main)
    b = threading.Thread(target = ChatBot.main)
    c = threading.Thread(target = Output.main)
    #a.start()
    b.start()
    c.start()
    gui.main()
    #a.join()
    b.join()
    c.join()