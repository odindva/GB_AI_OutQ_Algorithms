import os, shutil, datetime


def createF(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)
    saveInfo(f'create file {name} ({os.environ.get("USERNAME")})')


def createD(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Папка уже есть')
    saveInfo(f'create folder {name}')


def getList(foldersOnly=False):
    allList = os.listdir()
    if foldersOnly:
        allList = [f for f in allList if os.path.isdir(f)]
    print(allList)


def deleteFD(name):
    os.rmdir(name) if os.path.isdir(name) else os.remove(name)
    saveInfo(f'delete file/folder {name}')


def copyFD(name, newName):
    try:
        shutil.copytree(name, newName) if os.path.isdir(name) \
            else shutil.copyfile(name, newName)
    except FileExistsError:
        print('Папка уже есть')
    saveInfo(f'copy file {name} to file {newName}')


def saveInfo(message):
    currentTime = datetime.datetime.now()
    result = f'{currentTime} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
       f.write(result + '\n')


def getHelp():
    print('help:\n'
          'list           - без параметра список файлов и папок\n'
          '     [folders] - с параметром "folders" - список папок\n'
          'createF [name.txt] - создает файл name\n'
          'createD [name] - создает папку name\n'
          'deleteFD [name] - удаляет папку или фйл name\n'
          'copyFD [name1][name2] - копирует файл name1 в файл name2\n'
          'game - начать игру (введите в качестве параметра 1 или 2)\n'
          'cd - аналог CD в ОС\n'
          '')

def changeDir(dir):
    try:
        os.chdir(dir)
    except NotADirectoryError:
        print('введите корректную директорию')
    except FileNotFoundError:
        print('введите корректную директорию')
    else:
        saveInfo(f'move to {dir}')

if __name__ == '__main__':
    changeDir('..\\')