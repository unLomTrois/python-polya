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


print(max(4, 2, 88))
