# -*- coding: cp1251 -*-

'''
    ����������� �����. ����������� ����� ���������� �����������, ���� ��� ����� ��������� ������ ������ ��������.
    ��������, 252 = 625. �������� ���������, ������� ������ ����������� ����� N � ������� �� ����� ��� ����������� �����, �� ������������� N
'''

print("����� ���� ����������� ����� �� ���������� �����..\n");

N = int(input("������� �����: "));

for num in range(1, N):
    num2 = num**2;

    if str(num2).endswith(str(num)): print(num);