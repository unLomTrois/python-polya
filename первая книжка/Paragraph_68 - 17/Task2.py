# -*- coding: cp1251 -*-

'''
    2. �������� ���������, ������� ������� ����������� � ������������ ����� ������ ������������� �����,
    ���������� � �����, � ������� ��������� � ������ ����. ������, ��� ����� ����� ����� ������ �� ����.
'''


path = 'D:/�������/4 ����/�������� - ��/��������/CH10_8/PythonApplication1/Chapter_8/Paragraph_68/';
txt1name, txt2name = 'input.txt', 'output.txt';

nums = []
for line in open(path + txt1name):
    for num in map(int, line.split()):
        if num > -1 and num%2 == 0:
            nums.append(num);

with open(path + txt2name, 'w') as f:
    f.write('min = {:}\n'.format(min(nums)));
    f.write('max = {:}'.format(max(nums)));