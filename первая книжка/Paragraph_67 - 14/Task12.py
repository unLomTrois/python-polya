# -*- coding: cp1251 -*-

'''
     *� �������, ���������� N ����� � M ��������, �������� ����� ���������� ����������� ������� 
     (���� ���������� ����, � ������� � ����). ��� ������� ����� ����� ��������������. 
     �������� ���������, ������� �� ������� ����� ���������� ���������� ��������.
'''

from random import randint

n, m = 3, 7; # ����������� �������
low, high = 0, 1; # ���������� ������� � �������

A = [[randint(low,high) for y in range(m)] for x in range(n)];

for row in A:
    print(row)

count, f = 0, False;
for i in range(n):
    f = False;
    for j in range(m):
        if A[i][j] == 1 and not f:
            count += 1;
            f = True;

for row in A:
    print(row)

print(count)