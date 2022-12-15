"""
Соболева ПКС-1
Напишите функцию, которая вычисляет N-ое число Фибоначчи
"""


def fibonacci(n):
    f1 = 0
    f2 = 1
    f_n = f1
    for i in range(0, n):
        f_n = f1
        f1 = f2
        f2 = f_n + f2

    return f1


n = int(input("введите число: "))

print(fibonacci(n))
