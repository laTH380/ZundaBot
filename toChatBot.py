import value
import toVoicebox

def main():
    input = value.getinput()
    ###ここにchatbotへinputを送る処理
    chat_output="こんにちはずんだもんなのだ"
    value.setchat_output(chat_output)
    toVoicebox.main()


if __name__ == '__main__':
    main()