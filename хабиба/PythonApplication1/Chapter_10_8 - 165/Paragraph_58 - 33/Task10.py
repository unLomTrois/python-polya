# -*- coding: cp1251 -*-

'''
    �������� ���������, ������� ������ ����������� ����� N � ������� �� ����� ��� ����������� �����, �� ������������� N � ��������� �� ������ �� ����� ����.
'''

num = int(input("������� �����: "));

for i in range(num):
    log = True;
    for j in str((i)):
        j = int(j);
        if j != 0 and i % j == 0: continue
        else: log = False;

    if log: print(i);