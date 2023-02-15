import inspect
from multiprocessing import Process, Value, Array, Manager
import ctypes
import mainStream

def main():    
    inputF = Value('i',0)#共有メモリによりプロセス間同期
    outputF = Value('i',0)
    finishF = Value('i',0)
    input = Value(ctypes.c_wchar_p, "Hello, World!")
    chat_output = Value(ctypes.c_wchar_p, "output")
    mainStream.main()

def setinputF(self,int):
    print(inspect.currentframe().f_back.f_code.co_filename)
    print(inspect.currentframe().f_back.f_lineno)
    self.inputF.value = int
    print(self.getinputF())
    
def getinputF(self):
    return self.inputF.value

def setoutputF(self,int):
    self.outputF.value=int
    
def getoutputF(self):
    return self.outputF.value

def setfinishF(self,int):
    self.finishF.value=int
    
def getfinishF(self):
    return self.finishF.value

def setinput(self,string):
    self.input = string

def getinput(self):
    return self.input.value

def setchat_output(self,string):
    self.chat_output = string

def getchat_output(self):
    return self.chat_output.value 

if __name__ == '__main__':
    main()

