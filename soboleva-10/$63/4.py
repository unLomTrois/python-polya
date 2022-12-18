"""
Соболева ПКС-1
Заполните массив случайными числами в диапазоне 10..12 
и найдите длину самой длинной последовательности стоящих рядом одинаковых последовательностей
"""

import random

arr = [random.randint(10, 12) for x in range(100)]

max, counter = 1, 1

for i in range(1, len(arr)):
    if arr[i - 1] == arr[i]:
        counter += 1
    else:
        if counter >= max:
            max = counter
        counter = 1

if counter > max:
    max = counter

print(arr)
print(max)
