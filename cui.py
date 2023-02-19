from main import valueclass

def main():
    text = input()
    if text != "" and valueclass.getfinishF() == 0:
        valueclass.setinput(text)
        valueclass.setinputF(1)
        valueclass.setfinishF(1)

if __name__ == '__main__':
    main()