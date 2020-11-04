# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint

max_, max_i = 0, 0
min_, min_i = 100, 0
arr = [randint(max_, min_) for _ in range(10)]
print(arr)

for i in range(len(arr)):
    if arr[i] > max_:
        max_ = arr[i]
        max_i = i
    if arr[i] < min_:
        min_ = arr[i]
        min_i = i

arr[min_i], arr[max_i] = max_, min_
print(arr)
