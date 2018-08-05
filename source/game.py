import colorama, data, settings, loadingpy, menu
colorama.init()

dataImport = data.allData

loadingpy.messageReport() #Доклад об успехе
loadingpy.load() #Загрузка


settingsExistanceValue = settings.settingsExistance() #Проверка наличия файла настроек
colorVar, speedVar = settings.checkFileSettings(settingsExistanceValue) #Переменной ColorVar и SpeedVar присваивается значение цвета и скорости в формате команды и числа

colorGlobalArg = colorVar #Задается условно глобальная перемнная цвета
colorGlobalArgExe = eval(colorGlobalArg)

speedGlobalArg = speedVar #Задается условно глобальная перемнная скорости
speedGlobalArg = float(speedGlobalArg)



loadingpy.loadColor(colorGlobalArgExe) #Анимация загрузки цвета

menu.mainMenu(colorGlobalArgExe, speedGlobalArg, 0, colorGlobalArg) #Главное меню
