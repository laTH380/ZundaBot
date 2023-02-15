import valuecopy

def main():
    while True:
        if valuecopy.getinputF():
            print("ChatBot")
            input = valuecopy.getinput()
            ###送る文を生成する処理
            ###chatbotへinputを送る処理
            chat_output="こんにちはずんだもんなのだ"
            valuecopy.setchat_output(chat_output)
            valuecopy.setinputF(0)
            valuecopy.setoutputF(1)

if __name__ == '__main__':
    main()