import wx
import time
from main import valueclass
import pyautogui as pag
import threading
scr_w,scr_h= pag.size()

class firstFrame(wx.Frame):#起動画面
    def __init__(self):
        super().__init__(None, id=-1, title='wxPython',pos=(scr_w-500,0))
        self.SetSize(500, scr_h*0.95)
        bitmap = wx.Image('./image/zzm_zunmon_3002_logo.png').ConvertToBitmap()
            #イメージコントロールを配置(ウィジェットは～コントロールという名前の関数で作る)
        self.image = wx.StaticBitmap(parent=self,
            bitmap=bitmap,
            size=bitmap.GetSize()
            )
        box_sizer0 = wx.BoxSizer(wx.VERTICAL)
            # 各ウィジェットをSizerにAddしていく
        box_sizer0.Add(self.image, 1, wx.ALIGN_CENTER)
        #タイマー作成
        self.timer = wx.Timer(self,wx.ID_ANY)
        self.Bind(wx.EVT_TIMER, self.change, self.timer)#一定時間ごとにself.update()を実行
        self.timer.Start(30000)#千ミリ秒ごと
        self.Show()

    #更新関系
    def change(self, event):
        self.timer.Stop()
        frame = MyFrame()
        self.Destroy()

class MyFrame(wx.Frame):#一番外側のウィンドウ
    def __init__(self):
        super().__init__(None, id=0, title='wxPython',pos=(scr_w-500,0))
        panel = MyPanel(self)
        self.SetSize(500, scr_h*0.95)

        # メニュー作成
        self.create_menu_bar()
        self.Show()

    ########################################################
    #メニューバー、ステータスバー、ツールバーを作成する
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

        # 閉じるイベント
        self.Bind(wx.EVT_CLOSE, self.frame_close)

    # メニューのイベントハンドラ
    def OnExit(self, event):
        # 終了作業
        self.Close()

    def frame_close(self, event):
        """ 閉じたときに発生するイベント """
        #wx.MessageBox('イベント発生！', 'title')
        valueclass.flag = False

        #event.Skip()
        self.panel.timer.Stop()
        self.Destroy()


class MyPanel(wx.Panel):#cssでいうbox(とはいえふつうはこれ一つでオッケー)
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        #self.green = wx.TextAttr(wx.Colour(100,30,200),wx.NullColour,wx.NullFont)
        #タイマー作成
        self.timer = wx.Timer(self,wx.ID_ANY)
        self.Bind(wx.EVT_TIMER, self.update, self.timer)#一定時間ごとにself.update()を実行
        self.timer.Start(10000)#千ミリ秒ごと
        ######################################
        #Sizer, ボタン等のウィジェットを記載(frame>panel>sixer>wijet)
        ######################################
        #sizer2
            #ウィジェット作成
                #テキストボックス
        self.text_box = wx.TextCtrl(self, size=(280, 25),style=wx.TE_PROCESS_ENTER)
        self.text_box.Bind(wx.EVT_TEXT_ENTER, self.OnTextEnter)
                # ボタン
        button = wx.Button(self, label='enter', size=(280, 25))
        button.Bind(wx.EVT_BUTTON, self.OnTextEnter)#これがイベント発生に対応してどの関数を呼び出すかの設定
           #sizer2を作る
        box_sizer2 = wx.BoxSizer(wx.HORIZONTAL)
            # 各ウィジェットをSizerにAddしていく
        box_sizer2.Add(self.text_box,4)
        box_sizer2.Add(button,1)
        #sizer1
            #ウィジェット作成
                #画像ウィジェット
        bitmap = wx.Image('./image/zzm_zunmon_3002.png').ConvertToBitmap()
                #イメージコントロールを配置(ウィジェットは～コントロールという名前の関数で作る)
        self.image = wx.StaticBitmap(parent=self,
                        bitmap=bitmap,
                        size=bitmap.GetSize()
                        )
        #sizer3
                #テキストビュー
        self.text_view = wx.TextCtrl(self, wx.ID_ANY, style=wx.TE_MULTILINE | wx.TE_READONLY)#selfつけると親のものになるのでコンストラクト外からアクセス可能
        self.text_view.SetBackgroundColour('#d3d3d3')
        font = wx.Font(15, wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.text_view.SetFont(font)
        self.text_view.Disable()
        text_view_parts = wx.StaticText(self, wx.ID_ANY, "LOG",style=wx.Bottom)
        text_view_parts.SetBackgroundColour('#d3d3d3')
        box_sizer3 = wx.BoxSizer(wx.VERTICAL)
        box_sizer3.Add(text_view_parts,0,wx.EXPAND)
        box_sizer3.Add(self.text_view,1,wx.EXPAND,)

            #sizerを作る
        box_sizer1 = wx.BoxSizer(wx.VERTICAL)
            # 各ウィジェットをSizerにAddしていく
        box_sizer1.Add(self.image, 1, wx.ALIGN_CENTER)
        box_sizer1.Add(box_sizer3,1,wx.EXPAND | wx.RIGHT | wx.LEFT, 10)
        box_sizer1.Add(box_sizer2, 0, wx.ALIGN_CENTER | wx.ALL, 10)
            # Panleの規定Sizerに指定
        self.SetSizer(box_sizer1)

    #更新関係
    def onStartTimer(self,event):
        output = valueclass.getchat_output()
        if valueclass.oldview != output:
            self.text_view.AppendText(">" + output +"\r\n")
            valueclass.setoldview(output)
            valueclass.setfinishF(0)

    def update(self, event):
        self.onStartTimer(event)

    ######################################################
    #ボタンを押下等のイベント処理を、メソッドで記載
    ######################################################
    def OnTextEnter(self, event):#入ロを受け付けた時
        text = self.text_box.GetValue()
        if text != "" and valueclass.getfinishF() == 0:
            valueclass.setinput(text)
            valueclass.setinputF(1)
            #print(str(self.green.GetTextColour()))
            #self.text_view.SetDefaultStyle(self.green)色がつくはずなのになぜかつかない
            self.text_view.AppendText(text+"\r\n")
            self.text_box.SetLabel("")
            # w = threading.Thread(target=wait,args=(valueclass.getfinishF(),1))
            # w.start()
            # w.join()
            # self.text_view.AppendText(">" + valueclass.getchat_output() +"\r\n")
            valueclass.setfinishF(1)
            #wx.MessageBox(text, 'Text Box Content', wx.OK | wx.ICON_INFORMATION)

def main():
    app = wx.App()
    frame = firstFrame()
    app.MainLoop()

if __name__ == '__main__':
    main()