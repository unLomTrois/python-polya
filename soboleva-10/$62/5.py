"""
Соболева ПКС-1
Постройте случайную перестановку чисел от 1 до N так,
чтобы первое число обязательно было равно 5.
"""

import random


n = int(input("введите число: "))

arr = [x for x in range(1, n + 1)]

random.shuffle(arr)

if n >= 5:
    arr.remove(5)
    arr = [5] + arr

print(arr)
