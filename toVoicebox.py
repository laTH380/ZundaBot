import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import voicebox
import multiprocessing
from playsound import playsound

def main():
    ###ここにvoicevoxを組み込んで音声出力
    voicebox.main()
    path = os.path.dirname(__file__)
    #playsound(path + "\output\output.wav")
    #playsound("./output/output.wav")

    p = multiprocessing.Process(target=playsound, args=("./output/output.wav",))
    p.start()
    # input("press ENTER to stop playback")
    # p.terminate()


if __name__ == '__main__':
    main()