"""
Соболева П.
ПКС-1
4 курс

Напишите программу, которая строит последовательность из N случайных чисел на отрезке
от 0 до 1 и определяет, сколько из них попадает на отрезки [0; 0,25), [0,25; 0,5), [0,5; 0,75) и
[0,75; 1). Сравните результаты, полученные при N = 10, 100, 1000, 10000.
"""

import random

n = int(input("введите кол-во случайных чисел: "))

# отрезки
quarter1 = 0
quarter2 = 0
quarter3 = 0
quarter4 = 0

for i in range(n):
    num = random.random()

    if 0 <= num < 0.25:
        quarter1 += 1
    if 0.25 <= num < 0.50:
        quarter2 += 1
    if 0.50 <= num < 0.75:
        quarter3 += 1
    if 0.75 <= num < 1:
        quarter4 += 1

# чем выше N, тем ближе отношение количества чисел в каждом отрезке к 1/4-й
print("[0; 0,25):", quarter1, quarter1/n)
print("[0,25; 0,5):", quarter2, quarter2/n)
print("[0,5; 0,75):", quarter3, quarter3/n)
print("[0,75; 1):", quarter4, quarter4/n)