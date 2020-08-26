from core import changeDir, getHelp, createF, createD, getList, deleteFD, copyFD
import sys
import Games.findNumber
import Games.findCompNumber

commands = ['list',
            'createF',
            'createD',
            'deleteFD',
            'copyFD',
            'game',
            'cd',
            'help']
command = None
isCommand = False
param1 = None
param2 = None

try:
    command = sys.argv[1]
    if command in commands:
        isCommand = True
except IndexError:
    command = None

try:
    param1 = sys.argv[2]
except IndexError:
    param1 = None

try:
    param2 = sys.argv[3]
except IndexError:
    param2 = None

if isCommand:
    if command == 'list':
        if param1 == 'folders':
            getList(foldersOnly=True)
        else:
            getList()

    elif command == 'createF':
        if param1:
            createF(param1)
        else:
            print('введите имя файла\n')
            getHelp()

    elif command == 'createD':
        if param1:
            createD(param1)
        else:
            print('введите имя файла\n')
            getHelp()

    elif command == 'deleteFD':
        try:
            if param1:
                deleteFD(param1)
            else:
                print('введите имя файла\n')
                getHelp()
        except FileNotFoundError:
            print('Файл не найден')

    elif command == 'copyFD':
        if not param1 or not param2:
            print('введите копируемый и новый файлы')
            getHelp()
        else:
            try:
                copyFD(param1, param2)
            except FileNotFoundError:
                print('Файл не найден')

    elif command == 'game':
        if param1:
            if param1 == '1':
                Games.findNumber.start()
            elif param1 == '2':
                Games.findCompNumber.start()
        else:
            print('выберете игру (введите в качестве параметра 1 или 2)\n')


    elif command == 'cd':
        if param1:
            changeDir(param1)
        else:
            print('введите дирректорию для перехода\n')
            getHelp()


    elif command == 'help':
        getHelp()
else:
    print('введите команду\n')
    getHelp()
