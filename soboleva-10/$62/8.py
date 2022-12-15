"""
Соболева ПКС-1
Заполните массив случайными числами в диапазоне 0..100 и подсчитайте отдельно среднее 
значение всех элементов, которые < 50, и среднее значение всех элементов, которые >= 50
"""

import random


n = int(input("введите длину массива: "))

arr = [random.randint(0, 100) for x in range(n)]

print(arr)

count = 0
sum = 0
for num in arr:
    if num < 50:
        count += 1
        sum += num
print("меньше 50:", count, "среднее:", sum / count )

count = 0
sum = 0
for num in arr:
    if num >= 50:
        count += 1
        sum += num 
print("больше 50:", count, "среднее:", sum / count)
