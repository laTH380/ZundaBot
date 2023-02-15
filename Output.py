import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import valuecopy
import voicebox
import multiprocessing
from playsound import playsound

def main():
    while True:
        if valuecopy.getoutputF():
            print("Output")
            #感情推定
            #描画処理
            ###voicevox処理
            voicebox.main()
            path = os.path.dirname(__file__)
            #playsound(path + "\output\output.wav")
            #playsound("./output/output.wav")

            p = multiprocessing.Process(target=playsound, args=("./output/output.wav",))
            p.start()
            # input("press ENTER to stop playback")
            # p.terminate()
            valuecopy.setoutputF(0)
            valuecopy.setfinishF(1)


if __name__ == '__main__':
    main()