# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
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

a, b = None, None
if max_i < min_i:
    a = max_i
    b = min_i
else:
    a = min_i
    b = max_i

sum_ = 0
for i in arr[a + 1: b]:
    sum_ += i

print(f'max number in index {max_i}, min number in index {min_i}, sum between them: {sum_}')
