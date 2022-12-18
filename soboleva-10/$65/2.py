"""
Соболева ПКС-1
Напишите программу, которая считает среднее число шагов при двоичном поиске для массива из 32 элементов 
в диапазоне 0..100. Для поиска используйте 1000 случайных чисел в этом же диапазоне.
"""

from random import randint


def bubble_sort(arr, direct):
    count = 0
    n = len(arr)

    if direct == ">":
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j + 1] < arr[j]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    count += 1
    else:
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j + 1] > arr[j]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    count += 1

    return count


arr = [randint(0, 100) for x in range(32)]
bubble_sort(arr, "<")

print(arr)

sum = 0
for i in range(1000):
    num = randint(0, 100)
    L, R = 0, len(arr)
    j = 0
    while L < R - 1:
        j += 1
        c = (R + L) // 2

        if num > arr[c]:
            R = c
        else:
            L = c

        if num == arr[c]:
            break

    sum += j

print("среднее число шагов:", round(sum / 1000, 2))
