# -*- coding: cp1251 -*-

'''
    �������� �������, ������� ����������, ������� ��� ������ � ���������� ������ �������� �����.
'''

text = input('enter text: ');
substr = input('enter substring: ');
count, i = 0, text.find(substr);

while i != -1:
    count += 1;
    text = text[i+1:];
    i = text.find(substr);

print(count);