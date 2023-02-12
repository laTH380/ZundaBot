import wx

class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        multi_line_text = "これは複数行のテキストです。\nこのテキストは下基準に表示されます。aaaa\na\na\naaaaaaaaa\naaaaaaa\na\naa\naa\naa\na\na\nf\nf\nfaaaa\na\na\naaaaaaaaa\naaaaaaa\na\naa\naa\naa\na\na\nf\nf\nf\nf\nf\nse\nr\nwd\ndf\ngf\nsdf\nf\nf\nse\nr\nwd\ndf\ngf\nsdf"

        # StaticTextを作成
        self.text = wx.StaticText(self, label=multi_line_text, style=wx.ALIGN_BOTTOM)
        self.text2 = wx.StaticText(self, label=multi_line_text, style=wx.ALIGN_BOTTOM)

        # BoxSizerを作成してStaticTextを配置
        box_sizer = wx.BoxSizer(wx.VERTICAL)
        box_sizer.Add(self.text, 1)
        box_sizer.Add(self.text2, 0)
        self.SetSizer(box_sizer)

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, id=-1, title='wxPython')

        self.SetSize(500, 500)
        MyPanel(self)
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
