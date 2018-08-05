import colorama, time, random, dictionary

def messageReport():

    time.sleep(0.5)

    dictionary.stylishPrint(dictionary.initialisationPhrase, 0.025, False)

    for dots in range(1, 5):
        print(colorama.Fore.CYAN + '.', end='')
        time.sleep(0.4)
    print(colorama.Fore.RESET + '', end='\n')

    dictionary.stylishPrint(dictionary.successInitPhrase, 0.025, False)

    print('\n')


def load():

    time.sleep(0.5)

    for loadPhrase in dictionary.loadingPhrases:
        print(loadPhrase, end='', flush=True)
        for dots in range(random.randint(5, 15)):
            print(colorama.Fore.CYAN + '.', end='', flush=True)
            time.sleep(0.125)
        print(colorama.Fore.RESET + '', end='\n')
    print(colorama.Fore.RESET + '', end='\n')


def loadColor(colorGlobalArg):

    time.sleep(0.5)

    dictionary.stylishPrint(dictionary.readyColor, 0.035, False)

    for minus in range(0, 10):
        print(colorGlobalArg + '-', end='', sep='')
        time.sleep(0.10)
    print(colorGlobalArg + '>', end='\n')
    print('\n')