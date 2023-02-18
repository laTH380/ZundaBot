import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from main import valueclass
import voicebox
import multiprocessing
from playsound import playsound
from main import valueclass

def main():
    while valueclass.flag:
        if valueclass.getoutputF():
            print("Output")
            text = valueclass.getchat_output()
            #感情推定
            #描画処理
            ###voicevox処理
            voicebox.main(text)
            path = os.path.dirname(__file__)
            #playsound(path + "\output\output.wav")
            #playsound("./output/output.wav")

            p = multiprocessing.Process(target=playsound, args=("./output/output.wav",))
            p.start()
            # input("press ENTER to stop playback")
            # p.terminate()
            valueclass.setoutputF(0)
            valueclass.setfinishF(1)


if __name__ == '__main__':
    main()