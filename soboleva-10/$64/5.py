"""
Соболева ПКС-1
Напишите программу, которая сортирует массив по возрастанию первой цифры числа.
"""


import random


def sort(arr):
    i = 0
    while i < len(arr) - 1:
        j = i + 1
        while j < len(arr):
            if arr[i] // (10 ** (len(str(arr[i])) - 1)) > arr[j] // (
                10 ** (len(str(arr[j])) - 1)
            ):
                arr[i], arr[j] = arr[j], arr[i]
            j += 1

        i += 1

    return arr


arr = [random.randint(1, 1000) for x in range(100)]

print("несортированный:", arr)
print("сортированный: ", sort(arr))
