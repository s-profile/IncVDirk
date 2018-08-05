import colorama, time
colorama.init()

loadingPhrases = ['Загружаем мир', 'Печатаем диалоги', 'Полируем пол', 'Убиваем монстров', 'Отдыхаем']
initialisationPhrase = list('Процесс инициализации игры')
successInitPhrase = list('Успешно!')
requireInf = list('Обязательно посетите пункт "информация" в главном меню!')
readyColor = list('Готово!   ')
chooseColorAlert = list('Внимание, перед запуском главного меню Вам требуется выбрать цвет интерфейса')
colorRed = list('Красный (1)')
colorBlue = list('Синий (2)')
colorWhite = list('Белый (3)')
colorGreen = list('Зеленый(4)')
welcomeMenu = list('Добро пожаловать в главное меню!')
newGame = list('Новая игра (1)')
countinueGame = list('Продолжить (2)')
informationAbout = list('[!] Информация (3)')
settingsGame = list('Настройки (4)')
exitGame = list('Выход (5)')
bye = list('До свидания!')
changeColor = list('Изменить цвет (1)')
changeSpeed = list('Изменить задержку появления символов (2)')
changeColorCycle = list('Введите число 1-2')
menuCycle = list('Введите число 1-5')
changeColorCycle2 = list('Введите число 1-4')
informFirstP1 = list('1. Все сохранения находятся в файле save.txt, а настройки в settings.txt. Во избижание ошибок программы рекомендуется ')
informFirstP2 = list('НЕ ')
informFirstP3 = list('изменять содержимое файлов')
informSecond = list('2. Игра сохранятеся посредством ввода save (обязательно в нижнем регистре) во время игры.')
backMenuWhileGame = list('3. Для выхода в меню во время игры введите mainMenu (обязательно в таком регистре) во время игры')
lostSettingsAlert = list('4. В случае ошибки программы/необходимости сброса настроек просто удалите файл settings.txt')
backMenu = list('Выйти в главое меню (1)')
chooseSpeedAlert = list('А теперь, пожалуйста, выберите задержку появления символов (0.1 - 2)')
chooseSpeedAlert2 = list('Выберите задержку появления символов (0.1 - 2)')

def stylishPrint(letters, delay, transference):
    for let in letters:
        print(let, end='', flush=True)
        time.sleep(delay)
    if transference == True:
        print('', end='\n')

def colorStylishPrint(letters, delay, transference, colorGlobalArg):
    for let in letters:
        print(colorGlobalArg + let, end='', flush=True)
        time.sleep(delay)
    if transference == True:
        print('', end='\n')

def colorStylishPrint2(letters, delay, transference, colorGlobalArg, style):
    for let in letters:
        print(style + colorGlobalArg + let, end='', flush=True)
        time.sleep(delay)
    if transference == True:
        print('', end='\n')
