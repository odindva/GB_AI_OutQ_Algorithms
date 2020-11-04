# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.
from random import randint

min_, min_i = 100, 0
arr = [randint(1, 100) for _ in range(10)]
print(arr)

# Вариант 1:
print(sorted(arr)[:2])

# Вариант 2:
k = 0
while True:
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            k += 1
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
    if k == 0:
        break
    else:
        k = 0
print(arr[:2])
