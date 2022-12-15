"""
Соболева
Полина
4 курс
ПКС-1
"""

from random import randint

n = int(input())

first = randint(1, n)
second = randint(1, n)

while second == first: # пока Д1 и Д2 равны, Д2 рандомится снова
    second = randint(1, n)

print(first, second)
