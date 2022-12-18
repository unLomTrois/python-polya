"""
Соболева ПКС-1
Напишите программу, которая выполняет неполную сортировку массива: ставит в начало 
массива три самых меньших по величине элемента в порядке возрастания (неубывания).
Положение остальных элементов не важно.
"""


import random


def sort(arr):
    i = 0
    while i < 3:
        j = i + 1
        while j < len(arr):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            j += 1
        i += 1

    return arr


arr = [random.randint(1, 100) for x in range(100)]

print("несортированный:", arr)
print("сортированный: ", sort(arr))
