class value:
    def __init__(self):
        self.flag = True
        self.inputF = 1
        self.outputF = 1
        self.finishF = 1
        self.input = "一緒に遊びましょ"
        self.chat_output = "ずんだもんなのだ"
        self.oldview = ""
        self.history = ""
        memorypath = "./memory.txt"
        with open(memorypath, "r", encoding='utf-8') as f:
            i=1
            for line in f:
                if i>=2 and i<=17:
                    self.history = self.history + line
                i=i+1


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

    def sethistory(self,string):
        self.history = string

    def gethistory(self):
        return self.history
    
    def setoldview(self,string):
        self.oldview = string

    def getoldview(self):
        return self.oldview

    # def make_view_text():
    #     value.view = value.view + "\r\n" + value.input

