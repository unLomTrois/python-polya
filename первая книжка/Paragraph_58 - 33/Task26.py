# -*- coding: cp1251 -*-

'''
    �������� ���������, ������� ������ ����������� ����� A � N � ��������� A^N ��� ������������� �������� ���������� � �������.
'''

print('A^N..\n');

A = int(input("print A --> "));
N = int(input("print N --> "));

i, mult = 1, 1; # mult - ������������
while i <= N:
    mult *= A;
    i+=1;

print(f"\nA^N = {mult}");