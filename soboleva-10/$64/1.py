"""
Соболева ПКС-1
Напишите программу, которая сортирует массив и находит количество различных чисел в нём.
"""

from random import randint


a = [randint(1, 100) for x in range(30)]
b = []

print("before:", a)

i = 0
while i < len(a) - 1:
    j = i + 1
    while j < len(a):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
        j += 1

    i += 1

i = 0
while i < len(a) - 1:
    if not a[i] in b:
        b.append(a[i])
    i += 1

print("after: ", a)
print("различных чисел:", len(b))
