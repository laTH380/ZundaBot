import inspect
from multiprocessing import Process, Value, Array, Manager
import ctypes
import mainStream

def main():  
    mainStream.main()

def setinputF(int):
    print(inspect.currentframe().f_back.f_code.co_filename)
    print(inspect.currentframe().f_back.f_lineno)
    global inputF
    inputF.value = int
    
def getinputF():
    return inputF.value

def setoutputF(int):
    global outputF
    outputF.value=int
    
def getoutputF():
    return outputF.value

def setfinishF(int):
    global finishF
    finishF.value=int
    
def getfinishF():
    return finishF.value

def setinput(string):
    global input
    input = string

def getinput():
    return input.value

def setchat_output(string):
    global chat_output
    chat_output = string

def getchat_output():
    return chat_output.value 

if __name__ == '__main__':
    global inputF
    global input
    global outputF, finishF, chat_output
    inputF = Value('i',0)#共有メモリによりプロセス間同期
    outputF = Value('i',0)
    finishF = Value('i',0)
    input = Value(ctypes.c_wchar_p, "Hello, World!")
    chat_output = Value(ctypes.c_wchar_p, "output")
    main()

