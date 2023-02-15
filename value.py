import inspect
from multiprocessing import Process, Value, Array, Manager
import ctypes

class value:
    inputF = None
    outputF = None
    finishF = None

    input = None
    chat_output = None
    

    def __init__(self):
        self.inputF = Value('i',0)#共有メモリによりプロセス間同期
        self.outputF = Value('i',0)
        self.finishF = Value('i',0)
        self.input = Value(ctypes.c_wchar_p, "Hello, World!")
        self.chat_output = Value(ctypes.c_wchar_p, "output")


    #view = "aaaa\r\ntt\na\na\naaaaaaaaa\naaaaaaa\na\naa\naa\naa\na\na\nf\nf\nf\nf\nf\nse\nr\nwd\ndf\ngf\nsdf"

    def setinputF(self,int):
        print(inspect.currentframe().f_back.f_code.co_filename)
        print(inspect.currentframe().f_back.f_lineno)
        self.inputF.value = int
        print("\n")
        print(self.inputF)
        
    def getinputF():
        return value.inputF

    def setoutputF(int):
        value.outputF=int
        
    def getoutputF():
        return value.outputF

    def setfinishF(int):
        value.finishF=int
        
    def getfinishF():
        return value.finishF

    def setinput(self,string):
        self.input = string

    def setchat_output(self,string):
        self.chat_output = string

    def getchat_output(self):
        return self.chat_output.value

    def getview():
        return value.view

    # def make_view_text():
    #     value.view = value.view + "\r\n" + value.input