import os, shutil, datetime


def create_f(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)
    save_info(f'create file {name} ({os.environ.get("USERNAME")})')


def create_d(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Папка уже есть')
    save_info(f'create folder {name}')


def get_list(foldersOnly=False):
    allList = os.listdir()
    if foldersOnly:
        allList = [f for f in allList if os.path.isdir(f)]
    print(allList)


def delete_fd(name):
    os.rmdir(name) if os.path.isdir(name) else os.remove(name)
    save_info(f'delete file/folder {name}')


def copy_fd(name, newName):
    try:
        shutil.copytree(name, newName) if os.path.isdir(name) \
            else shutil.copyfile(name, newName)
    except FileExistsError:
        print('Папка уже есть')
    save_info(f'copy file {name} to file {newName}')


def save_info(message):
    currentTime = datetime.datetime.now()
    result = f'{currentTime} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
       f.write(result + '\n')


def get_help():
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

def change_dir(dir):
    try:
        os.chdir(dir)
    except NotADirectoryError:
        print('введите корректную директорию')
    except FileNotFoundError:
        print('введите корректную директорию')
    else:
        save_info(f'move to {dir}')

if __name__ == '__main__':
    change_dir('..\\')