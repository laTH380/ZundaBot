from main import valueclass
import rinna

def main():
    init = True
    while valueclass.flag:
        if valueclass.getinputF():
            print("ChatBot")
            ###送る文を生成してchatbotへinputを送る処理。返り値はその結果
            if init:
                inputtext = "こんにちは"
                input = valueclass.gethistory() + inputtext + "\n回答:"
                chat_output = rinna.generate_text(input)
                init = False
                valueclass.setinputF(0)
                valueclass.setfinishF(0)
                print("準備完了。ここからお話しできます")
            else:
                inputtext = valueclass.getinput()
                input = valueclass.gethistory() + inputtext + "\n回答:"
                chat_output = rinna.generate_text(input)
                print(chat_output)
                valueclass.setchat_output(chat_output)
                valueclass.sethistory(input + chat_output + "\n質問:")
                valueclass.setinputF(0)
                valueclass.setoutputF(1)
                #以下はcuiの現在のみ必要
                valueclass.setoutputF(0)
                valueclass.setfinishF(0)        

if __name__ == '__main__':
    main()