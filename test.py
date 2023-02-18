import threading
import wx

class GUI(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True

    def run(self):
        app = wx.App() 
        window = wx.Frame(None, title="Hello World!", size=(200, 100)) 
        panel = wx.Panel(window) 
        text = wx.StaticText(panel, label="Hello World!", pos=(0, 0)) 
        window.Show(True) 
        app.MainLoop()     

gui_thread = GUI()
gui_thread.start()