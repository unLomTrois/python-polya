# -*- coding: cp1251 -*-

'''
    ��������� ������ ��������� ����� 2 (�� 2^1 �� 2^N).
'''


N = int(input("������� ����� --> "));

A = [2**x for x in range(1, N+1)];

print(A);