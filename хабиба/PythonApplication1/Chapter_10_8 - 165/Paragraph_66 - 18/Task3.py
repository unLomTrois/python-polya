# -*- coding: cp1251 -*-

'''
    ������ ����� ����� � ����������� ��� �� �����, ����������� ������ '/'. ������ ����� 
    ������� � ��������� ������.
'''

text = input('enter file path (\'/\'): ');
txts = text.split('/');
for txt in txts:
    print(txt);