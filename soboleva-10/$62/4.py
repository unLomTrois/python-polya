"""
Соболева ПКС-1
Заполните массив из N элементов случайными целыми числами в диапазоне 1..N так, 
что-бы в массив обязательно вошли все числа от 1 до N (постройте случайную перестановку). 
"""

import random


N = int(input("введите число: "))

A = [x for x in range(1, N + 1)]
random.shuffle(A)

print(A)
