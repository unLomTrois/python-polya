"""
Соболева ПКС-1
Заполните массив случайными числами в диапазоне 0..4 
и выведите на экран номера всех элементов, равных значению X (оно вводится с клавиатуры).
"""

import random

x = int(input("введите число между 0 и 4: "))

arr = [random.randint(0, 4) for i in range(100)]

nomera = []
for i in range(0, len(arr)):
    if x == arr[i]:
        nomera.append(i)

print("номера:", nomera)
