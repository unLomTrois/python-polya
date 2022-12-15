"""
Соболева ПКС-1
Напишите функцию, которая вычисляет максимальное из трёх чисел, не используя встроенную функцию max.
"""

def max(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    return c

a = int(input("введите 1-е число: "))
b = int(input("введите 2-е число: "))
с = int(input("введите 3-е число: "))

print(max(a, b, с))
