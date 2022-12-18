"""
Соболева ПКС-1
Напишите программу, которая находит максимальный и минимальный из чётных положительных элементов массива. 
Если в массиве нет чётных положительных элементов, нужно вывести сообщение об этом.
"""

import random


n = int(input("введите кол-во элементов:"))

arr = [random.randint(-100, 100) for x in range(n)]

minN = 101
maxN = -101
for num in arr:
    if num > 0 and num % 2 == 0:
        if minN > num:
            minN = num
        if maxN < num:
            maxN = num

print("min =", minN)
print("max =", maxN)
