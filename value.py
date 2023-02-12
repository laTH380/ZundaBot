class value:
    input = "あああああああ"
    chat_output = "おはよう"
    #view = "aaaa\r\ntt\na\na\naaaaaaaaa\naaaaaaa\na\naa\naa\naa\na\na\nf\nf\nf\nf\nf\nse\nr\nwd\ndf\ngf\nsdf"

def setinput(string):
    value.input=string

def getinput():
    return value.input

def setchat_output(string):
    value.chat_output = string

def getchat_output():
    return value.chat_output

def getview():
    return value.view

# def make_view_text():
#     value.view = value.view + "\r\n" + value.input