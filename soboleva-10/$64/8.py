"""
Соболева ПКС-1
Напишите программу, которая сортирует массив, а затем находит максимальное из чисел, 
встречающихся в массиве несколько раз
"""

import random


def sort(arr):
    i = 0
    n = len(arr)
    while i < n - 1:
        j = i + 1
        while j < n:
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            j += 1
        i += 1

    return arr


arr = [random.randint(1, 10) for x in range(100)]

arr = sort(arr)
count = 1
for i in range(len(arr) - 1, 0, -1):
    if arr[i] == arr[i - 1]:
        count += 1
    else:
        break

print(arr)
print(count)
