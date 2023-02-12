import wx

class MyFrame(wx.Frame):#一番外側のウィンドウ
    def __init__(self):
        super().__init__(None, id=-1, title='wxPython')
        panel = MyPanel(self)
        # メニュー作成
        self.create_menu_bar()
        self.Show()

    ########################################################
    #  必要ならば、メニューバー、ステータスバー、ツールバーを作成する
    ########################################################
    def create_menu_bar(self):
        # 引数numberに、区切りたいエリア数を設定
        sb = self.CreateStatusBar(number=3)
        # 各エリアの広さを、比で設定 (1: 2: 1 の割合)
        sb.SetStatusWidths([-1, -2, -1])
        # 表示したい文字と、表示したいエリア番号を指定（0より開始）
        sb.SetStatusText('aaaa', 0)
        sb.SetStatusText('bbbb', 1)
        sb.SetStatusText('cccc', 2)

        # 「ファイル」のメニューを作成
        f_menu = wx.Menu()
        # 下記の第一引数は「メニューコマンド ID」 
        # なんでもOKの場合、-1
        f_menu.Append(-1, '新規作成\tCtrl-N', '新規作成をします。')
        f_menu.Append(-1, '保存')
        f_menu.Append(-1, '終了')

        # 「編集」のメニューを作成
        s_menu = wx.Menu()
        s_menu.Append(-1, '画像サイズ変更')
        s_menu.Append(-1, 'グレーイメージ化')

        # メニューバーを作成
        m_bar = wx.MenuBar()
        m_bar.Append(f_menu, 'ファイル(&F)')
        m_bar.Append(s_menu, '編集')

        # メニューバーをFrameに設定
        self.SetMenuBar(m_bar)

        # メニューのイベントリンクの登録
        self.Bind(wx.EVT_MENU, self.OnExit)

    # メニューのイベントハンドラ
    def OnExit(self, event):
        # 終了作業
        self.Close()



class MyPanel(wx.Panel):#cssでいうbox
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        ######################################
        #  ここにSizer(自動レイアウト調整), ボタン等のウィジェットを記載
        ######################################
        self.text = wx.TextCtrl(self, -1)
        self.text.SetBackgroundColour('gray')
        button = wx.Button(self, -1, 'Click')

        box_sizer = wx.BoxSizer(wx.VERTICAL)
        box_sizer.Add(self.text, 1, wx.EXPAND | wx.ALL, 10)
        box_sizer.Add(button, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        self.SetSizer(box_sizer)

        # イベント処理時、どのメソッドを呼び出すかを登録する
        button.Bind(wx.EVT_BUTTON, self.OnButtonPress)

    ######################################################
    #  ここにボタンを押下等のイベント処理を、メソッドで記載することが多い
    ######################################################
    def OnButtonPress(self, event):
        self.text.SetLabel('クリック')

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()