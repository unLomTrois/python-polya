# -*- coding: cp1251 -*-

'''
    ��������, ��� ���� � ����� k ��� �� ������ �������� � � ��������� �� 2 �� k^0.5 , �� ��� �������
'''

from math import sqrt


num = int(input('enter number: '))
log = True;
for i in range(2, round(sqrt(num)) + 1):
    if num % i == 0:
        log = False;
        break;

print(num, 'is prime:', log);