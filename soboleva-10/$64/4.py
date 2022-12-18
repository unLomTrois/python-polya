"""
Соболева ПКС-1
Напишите вариант метода пузырька, который заканчивает работу, если на очередном шаге внешнего цикла не было перестановок.
"""

import random


def sort(arr):
    i = 0
    n = len(arr)
    while i < n - 1:
        j = i + 1
        log = True
        while j < n:
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                log = False
            j += 1

        if log:
            break
        i += 1

    return arr


arr = [random.randint(1, 100) for x in range(100)]

print("несортированный:", arr)
print("сортированный: ", sort(arr))
