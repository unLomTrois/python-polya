"""
Соболева ПКС-1
Напишите функцию, которая вычисляет факториал натурального числа N
"""

def factorial(num):
    res = 1
    for n in range(1, num + 1):
        res *= n
    return res


n = int(input("введите число: "))

print(factorial(n))
