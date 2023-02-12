import wx

class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        #bitで表現させる
        bitmap = wx.Image('C:/Users/thiro/Downloads/ththrsth.png').ConvertToBitmap()
        # # イメージコントロールを配置
        self.image = wx.StaticBitmap(parent=self,
                        bitmap=bitmap,
                        size=bitmap.GetSize()
                        )
        self.image.SetBackgroundColour('white')
        button = wx.Button(self, -1, 'Open_File')

        box_sizer = wx.BoxSizer(wx.VERTICAL)
        box_sizer.Add(self.image, 2, wx.EXPAND)
        box_sizer.Add(button, 0, wx.ALIGN_CENTER | wx.ALL, 10)#このゼロは伸縮しないことを意味する
        self.SetSizer(box_sizer)

        ######################################################
        #  この部分に、イベントとイベントハンドラを関連付ける処理を記載
        ######################################################
        button.Bind(wx.EVT_BUTTON, self.OnBrowse)

    ######################################################
    #  この部分に、イベントハンドラを記載
    ######################################################
    def OnBrowse(self, event):
        with wx.FileDialog(self, 'Select Image File',
                            wildcard='PNG files (*.png)|*.png',
                            style=wx.FD_OPEN) as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                bitmap = wx.Image(dialog.GetPaths()[0]).ConvertToBitmap()
                self.image.SetBitmap(bitmap)
                self.Layout()

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, id=-1, title='wxPython')
        ######################################
        #  ウインドウサイズを設定
        #  アイコンに関するコードを記載
        ######################################
        self.SetSize(500, 500)
        icon = wx.Icon('C:/Users/thiro/Downloads/ththrsth.png', wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)
        MyPanel(self)
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()