# -*- coding: cp1251 -*-

#�������� ���������, ������� ������ ���������� ����� �� ��������� � ����������, ������
#�� ��� ����� � �������������� �������.

x = float(input('���������� �: '))
y = float(input('���������� Y: '))

print('������� �:', end=' ')
if y <= 1:
    print('+')
else:
    print('-')

print('������� �:', end=' ')
if x + y <= 0:
    print('+')
else:
    print('-')

print('������� �:', end=' ')
if x**2 + y**2 -1 <= 0:
    print('+')
else:
    print('-')

print('������� �:', end=' ')
if (x-1)**2 + y**2 - 1 <= 0:
    print('+')
else:
    print('-')