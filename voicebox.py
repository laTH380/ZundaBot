#カレントディレクトリからしかなぜか動かない
from main import valueclass
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('./voicebox')#カレントディレクトリがここでも一つ上でも動作するように二つ追加する
sys.path.append('../')
from pathlib import Path
from voicevox_core import VoicevoxCore, METAS
import value

core = VoicevoxCore(open_jtalk_dict_dir=Path("open_jtalk_dic_utf_8-1.11"))
speaker_id = 3

def main():
    text = valueclass.getchat_output()
    if not core.is_model_loaded(speaker_id):  # モデルが読み込まれていない場合
        core.load_model(speaker_id)  # 指定したidのモデルを読み込む
    wave_bytes = core.tts(text, speaker_id)  # 音声合成を行う
    with open("./output/output.wav", "wb") as f:
        f.write(wave_bytes)  # ファイルに書き出す

if __name__ == '__main__':
    # print(sys.path)#この中に書いてある順にimportを探しに行く
    main()