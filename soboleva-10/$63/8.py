"""
Соболева ПКС-1
Заполните массив случайными числами и выполните реверс для части массива между элементами с индексами K и M (включая эти элементы).
"""

import random

arr = [random.randint(0, 9) for i in range(100)]

print("до:", arr)

k = int(input("введите начальный индекс: "))
m = int(input("введите конечный индекс: "))

arr = arr[:k] + arr[m : k - 1 : -1] + arr[m + 1 :]


print("после:", arr)
