# -*- coding: cp1251 -*-

"""
    Напишите функцию, которая вычисляет факториал натурального числа N
"""

import random

# вычисление факториала числа
def fact(number):
    res, i = 1, 1
    while i <= number:
        res *= i
        i += 1

    return res


print(fact(7))
