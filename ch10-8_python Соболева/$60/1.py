"""
Соболева ПКС-1
Напишите функцию, которая вычисляет максимальное из трёх чисел, не используя встроенную функцию max.
"""

# вычисляет максимальное из трех чисел
def my_max(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    if n2 > n1 and n2 > n3:
        return n2
    return n3


print(my_max(4, 2, 88))
