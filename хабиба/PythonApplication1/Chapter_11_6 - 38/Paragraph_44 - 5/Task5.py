# -*- coding: cp1251 -*-

'''
    5. � ����������� ����������� ��� �������, ������� ��������� ������:
        1. ������� 1
        2. ������ �� 3
        3. ������ �� 4
    �������� ���������, ������� ���������, ������� ���������� ��������� 
    ��������, ������������� ����� 1 � ����� N, ��������� � ����������.
'''

def calc(i, res):
    if i > res:
        return 0
    if i == res:
        return 1
    return calc(i+1, res)+calc(i+3, res)+calc(i*4, res)
 
print(calc(1, int(input('������� N: '))), '��������')