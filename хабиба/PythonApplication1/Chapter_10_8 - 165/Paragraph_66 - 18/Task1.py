# -*- coding: cp1251 -*-

'''
    �������� ���������, ������� �� ��������� ���������� ������ �������� ��� ����� �� �� 
    ����� �� � ��������, ��� ���������, ��� � ��������. ��� ����� ������ '������' ������ 
    ���������� ��������� '������'
'''

text = input('enter text: ');
txt = '';

for symbol in text:
    if symbol == '�': symbol = '�';
    elif symbol == '�': symbol = '�';
    if symbol == '�': symbol = '�';
    elif symbol == '�': symbol = '�';
    txt += symbol;

print(txt);
