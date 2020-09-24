import random

hiddenWord = ''
privateWord = ''
attempt = 5


def createPrivateWord():
    global privateWord, hiddenWord
    lenOfHidWord = len(hiddenWord)
    indexOfLen = 0
    while indexOfLen < lenOfHidWord:
        privateWord += '_'
        indexOfLen += 1


def checkInputChar(text):
    if (len(text) > 1):
        print("Input more 1 value\n")
        return False
    elif (len(text) == 0):
        print("Input never value\n")
        return False
    return True


def setSymoblInPrivateWord(symbol):
    global hiddenWord, privateWord
    index = 0
    statusOfEidtingString = False
    for s in hiddenWord:
        if (symbol == s):
            privateWord = privateWord[:index] + symbol + privateWord[index + 1:]
            statusOfEidtingString = True
        index += 1
    return statusOfEidtingString


def createHiddenWord():
    global hiddenWord
    fileOfWorlds = open(r"word.txt", "r")
    randomint = random.randint(0, 149)
    while randomint != 0:
        fileOfWorlds.readline()
        randomint -= 1
    hiddenWord =  fileOfWorlds.readline().rstrip('\n')


def isFinish(statusOfSymbol):
    global hiddenWord, privateWord, attempt
    if not statusOfSymbol:
        attempt -= 1
        print(attempt, 'attempts left')
        if (not attempt):
            print("Lost you!")
            return True
    else:
        if hiddenWord == privateWord:
            print("Win you!")
            return True
    return False

if __name__ == '__main__':
    createHiddenWord()
    createPrivateWord()
    print(hiddenWord)
    attempt = 5
    while attempt > 0:
        symbol = input("input char: ")
        if not checkInputChar(symbol):
            continue
        statusOfSymbol = setSymoblInPrivateWord(symbol)
        print(privateWord)
        if isFinish(statusOfSymbol):
            break
