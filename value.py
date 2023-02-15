class value:
    def __init__(self):
        self.inputF = 0
        self.outputF = 0
        self.finishF = 0
        self.input = "Hello, World!"
        self.chat_output = "output"


    #view = "aaaa\r\ntt\na\na\naaaaaaaaa\naaaaaaa\na\naa\naa\naa\na\na\nf\nf\nf\nf\nf\nse\nr\nwd\ndf\ngf\nsdf"

    def setinputF(self,int):
        self.inputF = int
        
    def getinputF(self):
        return self.inputF

    def setoutputF(self,int):
        self.outputF=int
        
    def getoutputF(self):
        return self.outputF

    def setfinishF(self,int):
        self.finishF=int
        
    def getfinishF(self):
        return self.finishF

    def setinput(self,string):
        self.input = string

    def getinput(self):
        return self.input

    def setchat_output(self,string):
        self.chat_output = string

    def getchat_output(self):
        return self.chat_output

    def getview():
        return value.view

    # def make_view_text():
    #     value.view = value.view + "\r\n" + value.input

