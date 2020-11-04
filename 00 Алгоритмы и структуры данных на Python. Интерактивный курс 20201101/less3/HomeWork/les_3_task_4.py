# 4. Определить, какое число в массиве встречается чаще всего.
from random import randint

arr = [randint(0, 4) for _ in range(10)]
print(arr)
nums = dict()
for i in arr:
    if i in nums:
        nums[i] += 1
    else:
        nums[i] = 1

max_ = 0
max_k = 0
for k, v in nums.items():
    if v > max_:
        max_ = v
        max_k = k
print(f'число {max_k} встречается чаще остальных: {max_} раз(а)')
