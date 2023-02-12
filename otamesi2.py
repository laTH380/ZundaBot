import wx

class MyButton(wx.Window):
    def __init__(self, parent, id, label):
        wx.Window.__init__(self, parent, id, size=(100, 50), style=wx.NO_BORDER)
        self.label = label
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_UP, self.OnClick)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        dc.SetBrush(wx.Brush("#add8e6"))
        dc.SetPen(wx.Pen("#000000", 1))
        dc.DrawCircle(50, 25, 25)
        dc.DrawLabel(self.label, wx.Rect(0, 0, 100, 50), wx.ALIGN_CENTER)

    def OnClick(self, event):
        print("Button Clicked")

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "My Frame", size=(300, 300))
        panel = wx.Panel(self)
        button = MyButton(panel, -1, "Click Me")
        button.SetPosition((100, 100))

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
