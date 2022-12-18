"""
Соболева ПКС-1
Напишите программу, которая сортирует первую половину массива по возрастанию, а вторую – по убыванию 
(элементы из первой половины не должны попадать во вторую и наоборот)
"""


import random


def sort(arr):
    i = 0
    n = len(arr)
    while i < n // 2 - 1:
        j = i + 1
        while j < n // 2:
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            j += 1
        i += 1

    i = n - 1
    while i > n // 2 + 1:
        j = i - 1
        while j > n // 2:
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            j -= 1
        i -= 1

    return arr


arr = [random.randint(1, 100) for x in range(100)]

print("несортированный:", arr)
print("сортированный: ", sort(arr))
