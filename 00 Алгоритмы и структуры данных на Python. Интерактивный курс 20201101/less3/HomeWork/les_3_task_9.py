# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import randint

rows = int(input('rows: '))
cols = int(input('columns: '))
minimals = [100] * cols
max_ = 0
arr = [[randint(max_, minimals[0]) for j in range(cols)] for i in range(rows)]
for row in arr:
    for i in range(len(row)):
        print(f'{row[i]:>5}', end='')
        if row[i] < minimals[i]:
            minimals[i] = row[i]
    print()

# простой вариант:
print(f'minimal elements: {minimals}; \nmaximum of them: {max(minimals)}')

# вариант 2:
print()
for i in minimals:
    if i > max_:
        max_ = i
print(f'minimal elements: {minimals}; \nmaximum of them: {max_}')
