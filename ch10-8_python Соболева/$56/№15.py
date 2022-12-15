"""
Соболева
Полина
4 курс
ПКС-1
"""
from random import random

a = float(input())
b = float(input())
# используем функцию random для получения случайного вещественного числа на полуинтервале [a, b)
r1 = a + (b - a) * random()
r2 = a + (b - a) * random()
r3 = a + (b - a) * random()
r4 = a + (b - a) * random()
r5 = a + (b - a) * random()

print(r1, r2, r3, r4, r5)
