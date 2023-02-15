from multiprocessing import Process, Manager, set_start_method
import gui
import ChatBot
import Output

def main():
    a = Process(target = gui.main)
    b = Process(target = ChatBot.main)
    c = Process(target = Output.main)
    a.start()
    b.start()
    c.start()

def testprocess():
    