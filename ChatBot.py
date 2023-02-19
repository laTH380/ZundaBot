from main import valueclass
from multiprocessing import Process, Value
import rinna

def main():
    #初期処理
    inputtext = "こんにちは"
    input = valueclass.gethistory() + inputtext + "\n回答:"
    output = Value('str',"")
    process = Process(target=rinna.generate_text,args=(input))
    process.start()
    process.join()
    print(output)
    valueclass.setinputF(0)
    #通常
    while valueclass.flag:
        if valueclass.getinputF():
            print("ChatBot")
            ###送る文を生成してchatbotへinputを送る処理。返り値はその結果
            inputtext = valueclass.getinput()
            input = valueclass.gethistory() + inputtext + "\n回答:"
            chat_output = rinna.generate_text(input)
            print(chat_output)
            valueclass.setchat_output(chat_output)
            valueclass.sethistory(input + chat_output + "\n質問:")
            valueclass.setinputF(0)
            valueclass.setoutputF(1)

if __name__ == '__main__':
    main()