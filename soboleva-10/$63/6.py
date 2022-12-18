"""
Соболева ПКС-1
Заполните массив случайными числами и переставьте соседние элементы, 
поменяв 1-ый элемент со 2-м, 3-й – с 4-м и т.д.
"""

import random

arr = [random.randint(0, 4) for i in range(100)]
print("до перестановки:", arr)
for i in range(0, len(arr)):
    if i != len(arr) - 1 and i % 2 == 0:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

print("после перестановки:", arr)
