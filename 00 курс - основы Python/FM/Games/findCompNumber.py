def start():
    print('Игра "Угадай число - наоборот"\n')
    lastNumber = input('Загадайте число от 1 до 100.\n'
          'Нажмите "ввод", когда будете готовы.')
    min = 1
    max = 101
    while True:
        number = min + (max - min) // 2
        if number == lastNumber:
            print('Так нечестно.')
            break
        result = input(f'Это число {number}?\n'
                       f'"=" - да, '
                       f'"+" - ваше число больше, '
                       f'"-" - ваше чило меньше\n')
        if result == '=':
            print('Ура!')
            break
        elif result == '+':
            min = number
        elif result == '-':
            max = number
        lastNumber = number
