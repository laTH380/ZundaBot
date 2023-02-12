from pathlib import Path
from voicevox_core import VoicevoxCore, METAS
from pprint import pprint

core = VoicevoxCore(open_jtalk_dict_dir=Path("open_jtalk_dic_utf_8-1.11"))
pprint(METAS)