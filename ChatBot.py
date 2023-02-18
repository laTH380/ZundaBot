from main import valueclass

def main():
    while valueclass.flag:
        if valueclass.getinputF():
            print("ChatBot")
            input = valueclass.getinput()
            ###送る文を生成する処理
            ###chatbotへinputを送る処理
            chat_output="こんにちはずんだもんなのだ"
            valueclass.setchat_output(chat_output)
            valueclass.setinputF(0)
            valueclass.setoutputF(1)

if __name__ == '__main__':
    main()