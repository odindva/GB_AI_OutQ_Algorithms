from core import change_dir, get_help, create_f, create_d, get_list, delete_fd, copy_fd
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
            get_list(foldersOnly=True)
        else:
            get_list()

    elif command == 'createF':
        if param1:
            create_f(param1)
        else:
            print('введите имя файла\n')
            get_help()

    elif command == 'createD':
        if param1:
            create_d(param1)
        else:
            print('введите имя файла\n')
            get_help()

    elif command == 'deleteFD':
        try:
            if param1:
                delete_fd(param1)
            else:
                print('введите имя файла\n')
                get_help()
        except FileNotFoundError:
            print('Файл не найден')

    elif command == 'copyFD':
        if not param1 or not param2:
            print('введите копируемый и новый файлы')
            get_help()
        else:
            try:
                copy_fd(param1, param2)
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
            change_dir(param1)
        else:
            print('введите дирректорию для перехода\n')
            get_help()


    elif command == 'help':
        get_help()
else:
    print('введите команду\n')
    get_help()
