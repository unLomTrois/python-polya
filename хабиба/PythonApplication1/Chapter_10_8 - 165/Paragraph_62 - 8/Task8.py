# -*- coding: cp1251 -*-

'''
     ��������� ������ ���������� ������� � ��������� 0..100 � ����������� �������� ������� 
     �������� ���� ���������, ������� < 50, � ������� �������� ���� ���������, ������� >= 50
'''

import random;


N = int(input("������� ���-�� ��������� --> "));

A = [];
for i in range(N):
    A.append(random.randint(0, 100));

print(A);

count = 0;
for a in A:
    if a < 50:
        count += 1;
print('�� �������� ����� < 50 - ', count, '|', f'{round(count/N*100, 2)}%');

count = 0;
for a in A:
    if a >= 50:
        count += 1;
print('�� �������� ����� >= 50 - ', count, '|', f'{round(count/N*100, 2)}%');
