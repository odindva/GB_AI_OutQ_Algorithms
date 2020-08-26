import random
def start():
    #v1
    # number = random.randint(1,100)
    # usNum = int(input('введите число: '))
    # while True:
    #     if usNum == number:
    #         print('угадали!')
    #         break
    #     elif usNum > number:
    #         usNum = int(input('введите число поменьше: '))
    #     else:
    #         usNum = int(input('введите число побольше: '))
    print('Игра "Угадай число"\n')
    count = 1
    levels = {1:10, 2:8, 3:7, 4:6, 5:5, 6:4, 7:3}
    level = int(input('выберете уровень сложности (1 - 7): '))
    maxCount = levels[level]

    usCount = int(input('введите количество игроков: '))
    users = []
    for i in range(usCount):
        userName = input(f'введите имя игрока {i+1} : ')
        users.append(userName)

    isWinner = False
    winners = []
    usNums = []

    while True:
        number = random.randint(1, 100)
        print(f'\nУровень {level} ({levels[level]} попыток)')

        while count < maxCount:

            print('\nпопытка №', count)
            i = 0
            for user in users:
                usNums.append(int(input(f'{user.upper()}, введите число: ')))
                if usNums[i] == number:
                    isWinner = True
                    winners.append(user)
                i +=1

            i= 0
            for usNum in usNums:
                if int(usNums[i]) > number:
                    print(f'{users[i].upper()}, число должно быть поменьше')
                elif int(usNums[i]) < number:
                    print(f'{users[i].upper()}, число должно быть побольше')
                i+=1

            count += 1
            usNums.clear()
            if isWinner == True:
                break

        level +=1
        if isWinner == True:
            print(f'\nугадали!\nпобедители: {winners}')
            maxCount = levels[level]
            count = 1
            isWinner = False
            winners = []
            continue
        else:
            print('\nвсе проиграли.')
            break
