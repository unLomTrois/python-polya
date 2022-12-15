"""
Соболева ПКС-1
Заполните массив случайными числами в диапазоне 20..100 
и подсчитайте отдельно число чётных и нечётных элементов.
"""

import random


n = int(input("введите длину массива: "))

arr = [random.randint(20, 100) for _ in range(n)]

print(arr)

count = 0
for element in arr:
    if element % 2 == 0:
        count += 1

print("четных:", count)
print("нечетных:", n - count)
