"""
Соболева ПКС-1
Напишите программу, которая сортирует массив и находит количество различных чисел в нём.
"""

import random


arr = [random.randint(1, 100) for x in range(100)]
diff_arr = []

i = 0
while i < len(arr) - 1:
    j = i + 1
    while j < len(arr):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        j += 1

    i += 1

i = 0
while i < len(arr) - 1:
    if not arr[i] in diff_arr:
        diff_arr.append(arr[i])
    i += 1

print(arr)
print("различных чисел:", len(diff_arr))
