# -*- coding: cp1251 -*-

'''
    �������� ��� �������� ���������, ������� ������ ���������� ����� �� ��������� � ����-
    ������, ������ �� ��� ����� � �������������� �������. ���� ������� ��������� ������
    ������������ ������� �������, ������ � ���������� ��� ���
'''

from math import sin


x = float(input('���������� �: '))
y = float(input('���������� Y: '))

print('������� �:', end=' ')
if x <= 2 and y - x <= 0 and x**2 + y**2 -4 >= 0:
    print('+')
else:
    print('-')

print('������� �:', end=' ')
if y <= 0.5 and y >= 0 and y - sin(x) <= 0:
    print('+')
else:
    print('-')

print('������� �:', end=' ')
if y < 2 - x**2 and (y > x or x > 0 ):
    print('+')
else:
    print('-')

print('������� �:', end=' ')
if  y > x**2 -2 and (y < x or y < -x):
    print('+')
else:
    print('-')

print('������� �:', end=' ')
if  x**2 + y**2 < 1 and (y > -x or y < x):
    print('+')
else:
    print('-')

print('������� �:', end=' ')
if  x**2 + y**2 < 1 and (x < 0 or y > x):
    print('+')
else:
    print('-')

print('������� �:', end=' ')
if  (y > 2*x**2 and y > 1 - x and x < 1) or (y < 2*x**2 and y > 1 - x and x < 1):
    print('+')
else:
    print('-')

print('������� �:', end=' ')
if  y < 1 and x > 0 and (x**2 + y**2 < 1 or y > x - 1):
    print('+')
else:
    print('-')

print('������� �:', end=' ')
if  x**2 + y**2 < 1 or (x > 0 and y > 0 and y < 1 and x < 1):
    print('+')
else:
    print('-')
