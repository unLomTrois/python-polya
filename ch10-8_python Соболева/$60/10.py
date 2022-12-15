"""
Соболева ПКС-1
Напишите программу, которая вводит натуральное число N и находит все числа в интервале 
[0,N], сумма цифр которых не меняется при умножении на 2, 3, 4, 5, 6, 7, 8 и 9 (например, число 9).
Используйте функцию для вычисления суммы цифр числа.
"""


def sum_of_digits(num):
    # if a < 10: return a
    sum = 0
    for digit in str(num):
        sum += int(digit)
    return sum


n = int(input("введите число: "))

for a in range(0, n + 1):
    sum = sum_of_digits(a)
    for b in range(2, 10):
        if sum_of_digits(a * b) != sum:
            break
        if b == 9:
            print(a)
