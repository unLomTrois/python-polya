# -*- coding: cp1251 -*-

"""
    �������� �������, ������� ��������� ��������� ������������ ����� N
"""

import random

# ���������� ���������� �����
def fact(number):
    res, i = 1, 1
    while i <= number:
        res *= i
        i += 1

    return res


print(fact(7))
