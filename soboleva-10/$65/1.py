"""
Соболева ПКС-1
Напишите программу, которая сортирует массив по убыванию и ищет в нем все значения, равные введенному числу.
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


num = int(input("введите число: "))
arr = [randint(1, 100) for x in range(100)]
bubble_sort(arr, "<")

print(arr)

L, R = 0, len(arr)
while L < R - 1:
    c = (R + L) // 2

    if num > arr[c]:
        R = c
    else:
        L = c

    if num == arr[c]:
        print("найдено на позиции:", c)
