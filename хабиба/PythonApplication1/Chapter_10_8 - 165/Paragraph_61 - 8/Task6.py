# -*- coding: cp1251 -*-

'''
    �������� ����������� ��������� ��� �������� ����� � �������� �������, ������� ��������� �������� �� ��� ���� (�������� 0)
'''

# ������� ����� � �������� ������� ���������
def show_in_binary(number):
    if number >= 2:
        show_in_binary(number // 2);
    print(number%2, end="");

N = int(input("������� ����� --> "));

show_in_binary(N);
