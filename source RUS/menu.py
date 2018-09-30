import colorama, time, loadingpy, dictionary, sys
colorama.init()


def mainMenu(colorArg, speedArg, index, NonExecutableColor):

    NonExecutableColorInner = NonExecutableColor


    colorama.init()

    time.sleep(0.5)

    if index == 0:
        z=0
    else:
        loadingpy.loadColor(colorArg)

    dictionary.colorStylishPrint(dictionary.welcomeMenu, speedArg * 0.015, True, colorArg)
    print('\n')
    dictionary.colorStylishPrint(dictionary.newGame, speedArg * 0.015, True, colorArg)
    dictionary.colorStylishPrint(dictionary.countinueGame, speedArg * 0.015, True, colorArg)
    dictionary.colorStylishPrint(dictionary.informationAbout, speedArg * 0.015, True, colorArg)
    dictionary.colorStylishPrint(dictionary.settingsGame, speedArg * 0.015, True, colorArg)
    dictionary.colorStylishPrint(dictionary.exitGame, speedArg * 0.015, False, colorArg)

    print('\n')

    mainMenuComand = input('->>>')
    while mainMenuComand !='1' and mainMenuComand !='2' and mainMenuComand !='3' and mainMenuComand !='4' and mainMenuComand !='5':
        dictionary.colorStylishPrint(dictionary.menuCycle, speedArg * 0.015, False, colorArg)
        print('\n')
        mainMenuComand = input('->>>')

    if mainMenuComand == '1':
        z = 1
    elif mainMenuComand == '2':
        z = 1
    elif mainMenuComand == '3':

        dictionary.colorStylishPrint(dictionary.informFirstP1, speedArg * 0.015, False, colorArg)
        styleB = colorama.Style.BRIGHT
        dictionary.colorStylishPrint2(dictionary.informFirstP2, speedArg * 0.015, False, colorArg, styleB)
        styleN = colorama.Style.NORMAL
        dictionary.colorStylishPrint2(dictionary.informFirstP3, speedArg * 0.015, True, colorArg, styleN)
        dictionary.colorStylishPrint(dictionary.informSecond, speedArg * 0.015, True, colorArg)
        dictionary.colorStylishPrint(dictionary.backMenuWhileGame, speedArg * 0.015, True, colorArg)
        dictionary.colorStylishPrint(dictionary.lostSettingsAlert, speedArg * 0.015, True, colorArg)
        print('\n')
        dictionary.colorStylishPrint(dictionary.backMenu, speedArg * 0.015, False, colorArg)
        print('\n')
        informationExit = input('->>>')
        print('\n')
        while informationExit !='1':
            dictionary.colorStylishPrint(dictionary.changeColorCycle, speedArg * 0.015, True, colorArg)
            informationExit = input('->>>')
            print('\n')

        mainMenu(colorArg, speedArg, 0, NonExecutableColorInner)


    elif mainMenuComand == '4':
        dictionary.colorStylishPrint(dictionary.changeColor, speedArg * 0.015, True, colorArg)
        dictionary.colorStylishPrint(dictionary.changeSpeed, speedArg * 0.015, False, colorArg)
        print('\n')
        mainMenuComandLVL2 = input('->>>')
        while mainMenuComandLVL2 !='1' and mainMenuComandLVL2 !='2':
            dictionary.colorStylishPrint(dictionary.changeColorCycle, speedArg * 0.015, False, colorArg)
            print('\n')
            mainMenuComandLVL2 = input('->>>')
        if mainMenuComandLVL2 == '1':
            dictionary.colorStylishPrint(dictionary.colorRed, speedArg * 0.015, True, colorArg)
            dictionary.colorStylishPrint(dictionary.colorBlue, speedArg * 0.015, True, colorArg)
            dictionary.colorStylishPrint(dictionary.colorWhite, speedArg * 0.015, True, colorArg)
            dictionary.colorStylishPrint(dictionary.colorGreen, speedArg * 0.015, False, colorArg)
            print('\n')
            mainMenuComandLVL2_2 = input('->>>')
            while mainMenuComandLVL2_2 != '1' and mainMenuComandLVL2_2 !='2' and mainMenuComandLVL2_2 !='3' and mainMenuComandLVL2_2 !='4':
                dictionary.colorStylishPrint(dictionary.changeColorCycle2, speedArg * 0.015, False, colorArg)
                print('\n')
                mainMenuComandLVL2_2 = input('->>>')
            if mainMenuComandLVL2_2 == '1':
                colorArg = 'colorama.Fore.RED'

                funcCreateFileSave = open('settings.txt', 'w')
                funcCreateFileSave.write(str(colorArg) + '\n' + str(speedArg) + '\n')
                funcCreateFileSave.close()

                readFile1 = open('settings.txt', 'r')
                readArg = readFile1.readlines()
                readArg = readArg[0]
                colorArg = readArg
                colorArg = eval(colorArg)
                readFile1.close()
                print('\n')
                mainMenu(colorArg, speedArg, 1, NonExecutableColorInner)
            elif mainMenuComandLVL2_2 == '2':
                colorArg = 'colorama.Fore.CYAN'

                funcCreateFileSave = open('settings.txt', 'w')
                funcCreateFileSave.write(str(colorArg) + '\n' + str(speedArg) + '\n')
                funcCreateFileSave.close()

                readFile1 = open('settings.txt', 'r')
                readArg = readFile1.readlines()
                readArg = readArg[0]
                colorArg = readArg
                colorArg = eval(colorArg)
                readFile1.close()
                print('\n')
                mainMenu(colorArg, speedArg, 1, NonExecutableColorInner)
            elif mainMenuComandLVL2_2 == '3':
                colorArg = 'colorama.Fore.WHITE'

                funcCreateFileSave = open('settings.txt', 'w')
                funcCreateFileSave.write(str(colorArg) + '\n' + str(speedArg) + '\n')
                funcCreateFileSave.close()

                readFile1 = open('settings.txt', 'r')
                readArg = readFile1.readlines()
                readArg = readArg[0]
                colorArg = readArg
                colorArg = eval(colorArg)
                readFile1.close()
                print('\n')
                mainMenu(colorArg, speedArg, 1, NonExecutableColorInner)
            elif mainMenuComandLVL2_2 == '4':
                colorArg = 'colorama.Fore.GREEN'

                funcCreateFileSave = open('settings.txt', 'w')
                funcCreateFileSave.write(str(colorArg) + '\n' + str(speedArg) + '\n')
                funcCreateFileSave.close()

                readFile1 = open('settings.txt', 'r')
                readArg = readFile1.readlines()
                readArg = readArg[0]
                colorArg = readArg
                colorArg = eval(colorArg)
                readFile1.close()
                print('\n')
                mainMenu(colorArg, speedArg, 1, NonExecutableColorInner)

        elif mainMenuComandLVL2 == '2':
            dictionary.colorStylishPrint(dictionary.chooseSpeedAlert2, speedArg * 0.025, False, colorArg)
            print('\n')


            def checkFloat():
                speedInput = input('->>>')
                while True:
                    try:
                        speedInput = float(speedInput)
                    except ValueError:
                        return False
                    else:
                        if speedInput >= 0.1 and speedInput <= 2:
                            return speedInput
                        else:
                            return False

            CF = checkFloat()

            while CF == False:
                print('Введите число (0.1 - 2)\n')
                CF = checkFloat()
            else:
                speedArg2 = CF

                readFile2 = open('settings.txt', 'r')
                readArg2 = readFile2.readlines()
                colorArgInner = readArg2[0]
                colorArgInner = colorArgInner.replace('\n', '')
                colorArg2 = eval(colorArgInner)
                readFile2.close()

                funcCreateFileSave = open('settings.txt', 'w')
                funcCreateFileSave.write(colorArgInner + '\n' + str(speedArg2))
                funcCreateFileSave.close()

                mainMenu(colorArg2, speedArg2, 1, str(colorArgInner))


        elif mainMenuComand == '5':
            dictionary.colorStylishPrint(dictionary.bye, speedArg * 0.075, True, colorArg)
            time.sleep(3.5)
            sys.exit()
