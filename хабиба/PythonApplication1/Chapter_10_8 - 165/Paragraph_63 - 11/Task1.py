# -*- coding: cp1251 -*-

'''
    �������� ���������, ������� ������� ������������ � ����������� �� ������ ������������� 
    ��������� �������. ���� � ������� ��� ������ ������������� ���������, ����� ������� ��������� �� ����.
'''

import random;


N = int(input("������� ���-�� ��������� --> "));

A = [];
for i in range(N):
    A.append(random.randint(-100, 100));

print(A);

minN = 101;
maxN = -101;
for num in A:
    if num > 0 and num % 2 == 0:
        if minN > num: minN = num;
        if maxN < num: maxN = num;

print('min =', minN);
print('max =', maxN);
