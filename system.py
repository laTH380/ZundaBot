import sys
import time
from main import valueclass

def cloth():
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        valueclass.flag=False
        sys.exit