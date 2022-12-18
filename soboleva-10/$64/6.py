"""
Соболева ПКС-1
Напишите программу, которая сортирует массив по убыванию суммы цифр числа.
"""


import random


# суммирует цифры числа
def sum_digit(num):
    sum = 0
    for digit in str(num):
        digit = int(digit)
        sum += digit ** len(str(num))

    return sum


def sort(arr):
    i = 0
    n = len(arr)
    while i < n - 1:
        j = i + 1
        while j < n:
            if sum_digit(arr[i]) > sum_digit(arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
            j += 1

        i += 1

    return arr


arr = [random.randint(1, 100) for x in range(100)]

print("несортированный:", arr)
print("сортированный: ", sort(arr))
