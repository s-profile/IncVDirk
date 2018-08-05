import time, os, dictionary, colorama
from goto import with_goto

newLine = print('\n')


def chooseColor():

    time.sleep(0.5)

    dictionary.colorStylishPrint(dictionary.requireInf, 0.015, True, colorama.Style.BRIGHT)
    print(colorama.Style.NORMAL + '')

    color = 'colorama.Fore.WHITE'
    dictionary.stylishPrint(dictionary.chooseColorAlert, 0.015, True)
    dictionary.stylishPrint(dictionary.colorRed, 0.025, True)
    dictionary.stylishPrint(dictionary.colorBlue, 0.025, True)
    dictionary.stylishPrint(dictionary.colorWhite, 0.025, True)
    dictionary.stylishPrint(dictionary.colorGreen, 0.025, False)
    print('\n')

    startColor = input('->>>')
    while startColor != '1' and startColor !='2' and startColor !='3' and startColor !='4':
        print('Введите число 1-4 \n')
        startColor = input('->>>')
    if startColor == '1':
        color = 'colorama.Fore.RED'
        funcCreateFileSave = open('settings.txt', 'w')
        funcCreateFileSave.write(str(color) + '\n')
        funcCreateFileSave.close()

        speedLocalVar = chooseSpeed()
        funcCreateFileSave = open('settings.txt', 'a')
        funcCreateFileSave.write(str(speedLocalVar) + '\n')
        funcCreateFileSave.close()
        return color, speedLocalVar

    elif startColor == '2':
        color = 'colorama.Fore.CYAN'
        funcCreateFileSave = open('settings.txt', 'w')
        funcCreateFileSave.write(str(color) + '\n')
        funcCreateFileSave.close()

        speedLocalVar = chooseSpeed()
        funcCreateFileSave = open('settings.txt', 'a')
        funcCreateFileSave.write(str(speedLocalVar) + '\n')
        funcCreateFileSave.close()
        return color, speedLocalVar
    elif startColor == '3':
        color = 'colorama.Fore.WHITE'
        funcCreateFileSave = open('settings.txt', 'w')
        funcCreateFileSave.write(str(color) + '\n')
        funcCreateFileSave.close()

        speedLocalVar = chooseSpeed()
        funcCreateFileSave = open('settings.txt', 'a')
        funcCreateFileSave.write(str(speedLocalVar) + '\n')
        funcCreateFileSave.close()
        return color, speedLocalVar
    elif startColor == '4':
        color = 'colorama.Fore.GREEN'
        funcCreateFileSave = open('settings.txt', 'w')
        funcCreateFileSave.write(str(color) + '\n')

        funcCreateFileSave.close()
        speedLocalVar = chooseSpeed()
        funcCreateFileSave = open('settings.txt', 'a')
        funcCreateFileSave.write(str(speedLocalVar) + '\n')
        funcCreateFileSave.close()
        return color, speedLocalVar


def settingsExistance():
    return os.path.isfile('settings.txt')


def checkFileSettings(settingsExistanceValue):
    if settingsExistanceValue == False:
        colorString, speedString = chooseColor()  # Присваивание цвета при первом запуске
        return colorString, speedString

    else:
        saveColorFile = open('settings.txt', 'r')
        colorString = saveColorFile.readlines()
        colorString = colorString[0]
        colorString = colorString.replace('\n', '')
        saveColorFile.close()

        saveSpeedFile = open('settings.txt', 'r')
        speedString = saveSpeedFile.readlines()
        speedString = speedString[1]
        speedString = speedString.replace('\n', '')
        saveSpeedFile.close()

        return colorString, speedString

@with_goto
def chooseSpeed():

    time.sleep(0.5)

    dictionary.stylishPrint(dictionary.chooseSpeedAlert, 0.025, False)
    print('\n')
    label .firstCycle
    speedInput = input('->>>')

    while True:
        try:
            speedInput = float(speedInput)
        except ValueError:
            print('Введите число (0.1 - 2)\n')
            speedInput = input('->>>')
        else:
            while speedInput < 0.1 or speedInput > 2:
                print('Введите число (0.1 - 2)\n')
                goto .firstCycle
            break


    return speedInput




