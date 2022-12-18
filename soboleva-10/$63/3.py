"""
Соболева ПКС-1
Найдите за один проход по массиву три его различных элемента, которые меньше всех остальных («три минимума»)
"""

import random

arr = [random.randint(0, 1000) for x in range(100)]

a, b, c = arr[0], arr[0], arr[0]

for i in range(1, len(arr)):
    if arr[i] < a:
        a, b, c = arr[i], a, b

print("минимумы:", a, b, c)
