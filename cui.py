from main import valueclass

def main():
    while True:
        text = input()
        while True:
            if text == "":
                break
            if valueclass.getfinishF() == 0:
                valueclass.setinput(text)
                valueclass.setinputF(1)
                valueclass.setfinishF(1)
                break

if __name__ == '__main__':
    main()