"""
Соболева П.
ПКС-1
4 курс

Напишите программу, которая вводит натуральное число N и выводит на экран N псевдослу-
чайных чисел. Запустите её несколько раз, объясните результаты опыта.
"""

import random

n = int(input("введите кол-во случайных чисел: "))

for i in range(n):
    print(random.random())
