# -*- coding: cp1251 -*-

'''
     ��������� ������ ���������� ������� � ��������� 20..100 � ����������� �������� ����� ������ � �������� ���������.
'''

import random;


N = int(input("������� ���-�� ��������� --> "));

A = [];
for i in range(N):
    A.append(random.randint(20, 100));

print(A);

count = 0;
for a in A:
    if a % 2 == 0:
        count += 1;

print('������ ����� - ', count, '|', f'{round(count/N*100, 2)}%');
print('�������� ����� - ', N-count, '|', f'{round((N-count)/N*100, 2)}%');
