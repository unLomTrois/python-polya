
"""
    �������� �������, ������� ��������� N-�� ����� ���������
"""

import random

# ���������� N-�� ����� � ������������������ ���������
def fibonacci(number):
    i = 0
    cur = 0
    # �������
    fut = 1
    # ���������
    while i < number:
        a = cur
        cur = fut

        fut = a + fut

        i += 1

    return cur


print(fibonacci(6))
