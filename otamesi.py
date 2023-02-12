import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, id=-1, title='wxPython GUI Example')
        
        # フレームのパネル
        panel = wx.Panel(self)
        
        # テキストボックス
        self.text_box = wx.TextCtrl(panel, pos=(10, 10), size=(280, 25))
        
        # ボタン
        button = wx.Button(panel, label='Show Text', pos=(10, 50), size=(280, 25))
        button.Bind(wx.EVT_BUTTON, self.on_button_click)
        
        # クライアントサイズの設定
        self.SetClientSize(wx.Size(300, 100))
        
        # フレームの表示
        self.Show()
        
    def on_button_click(self, event):
        text = self.text_box.GetValue()
        wx.MessageBox(text, 'Text Box Content', wx.OK | wx.ICON_INFORMATION)

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
