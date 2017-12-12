import time
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


SENDMESSAGE = "sendmessage"
PIXEL = "pixel"
CLEAR = "clear"
MESSAGESINGLELETTER = "singleLetter"
MESSAGESINGLELETTERSLEEP = 1
HELP = "help"

def ipixel(x, y, onOff):
    print("pixel x:" + str(x) + " y: " + str(y) + " " + str(onOff))
    # matrix.pixel...

def isendMessage(mess):
    print("Message: " + mess)
    # matrix.sendMessage
def iclear():
    print("Matrix Clear")
    # matrix.clear

def sendMessageSingleLetter(mess):
    letterList = list(mess)
    i = 1
    for letter in letterList:
        isendMessage(letter)
        time.sleep(MESSAGESINGLELETTERSLEEP)
        i = i + 1
        if i != len(letterList):
            iclear()

def hilfe():
    print(bcolors.FAIL + bcolors.UNDERLINE + "LED-Matrix-Console")
    print(bcolors.OKGREEN + " -- " + bcolors.OKBLUE + SENDMESSAGE + bcolors.WARNING + " Gibt eine Nachricht auf der Matrix aus." + bcolors.HEADER + " Für mehr infos:" + bcolors.OKBLUE + " >>> " + bcolors.OKGREEN + SENDMESSAGE)
    print(bcolors.OKGREEN + " -- " + bcolors.OKBLUE + PIXEL + bcolors.WARNING + " Schaltet bestimmte Pixel an oder aus." + bcolors.HEADER + " Für mehr infos:" + bcolors.OKBLUE + " >>> " + bcolors.OKGREEN + PIXEL)
    print(bcolors.OKGREEN + " -- " + bcolors.OKBLUE + CLEAR + bcolors.WARNING + " Schaltet alle Lichter der Matrix aus." + bcolors.HEADER + " Für mehr infos:" + bcolors.OKBLUE + " >>> " + bcolors.OKGREEN + CLEAR)
    print(bcolors.OKGREEN + " -- " + bcolors.OKBLUE + MESSAGESINGLELETTER + bcolors.WARNING + " Zeigt einen Text in einzelnen Buchstaben an." + bcolors.HEADER + " Für mehr infos:" + bcolors.OKBLUE + " >>> " + bcolors.OKGREEN + MESSAGESINGLELETTER)
    print(bcolors.OKGREEN + " -- " + bcolors.OKBLUE + HELP + bcolors.WARNING + " Zeigt dieses Menü an.")

while True:
    print(bcolors.OKGREEN + "Matrix " + bcolors.OKBLUE + ">>> " + bcolors.WARNING + " ", end="")
    inp = input()
    inpList = inp.split()
    newString = ""
    err = False
    if len(inpList) == 0:
        continue
    if inpList[0] == HELP:
        if len(inpList) > 1:
            print("Usage: " + HELP)
        else:
            hilfe()
    elif inpList[0] == SENDMESSAGE:
        if len(inpList) > 1:
            for word in inpList[1:]:
                newString = newString + " " + word
            isendMessage(newString)
        else:
            print("Usage: " + SENDMESSAGE + " message(String)")
    elif inpList[0] == PIXEL:
        try:
            x = int(inpList[1])
            y = int(inpList[2])
            if inpList[3] == "True":
                onOff = True
            if inpList[3] == "False":
                onOff = False
            if inpList[3] != "True" and inpList[3] != "False":
                err = True
                print("Usage: " + PIXEL + " x(int) y(int) anAus(boolean)")

        except Exception:
            print("Usage: " + PIXEL + " x(int) y(int) anAus(boolean)")
            err = True
        if err == False:
            ipixel(x, y, onOff)
    elif inpList[0] == CLEAR:
        if len(inpList) >= 2:
            print("Usage: " + CLEAR)
        else:
            iclear()
    elif inpList[0] == MESSAGESINGLELETTER:
        if len(inpList) > 1:
            sendMessageSingleLetter(inpList[1:])
        else:
            print("Usage: " + MESSAGESINGLELETTER + " message(String)")
    else:
        print("Befehl nicht gefunden!")