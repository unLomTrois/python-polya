"""
Соболева ПКС-1
Напишите программу, в которой сортировка выполняется «методом камня» – самый тяжёлый» элемент опускается в конец массива.
"""

import random


def rock_sort(arr):
    i = 0
    n = len(arr)
    while i < n:
        j = i + 1
        while j < n:
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            j += 1
        i += 1

    return arr


arr = [random.randint(1, 100) for x in range(100)]

print("несортированный:", arr)
print("сортированный: ", rock_sort(arr))
