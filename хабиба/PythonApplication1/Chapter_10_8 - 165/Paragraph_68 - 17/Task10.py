# -*- coding: cp1251 -*-

'''
    10. ��������� ����� �� ����� � ������� � ������ ���� ������ �� ������, � ������� ���� �����, ������������ � ����� �.
'''

path = 'D:/�������/4 ����/�������� - ��/��������/CH10_8/PythonApplication1/Chapter_8/Paragraph_68/';
txt1name, txt2name, txt3name = 'input.txt', 'input2.txt', 'output.txt';

fw = open(path + txt3name, 'w') # file2 write mode
for line in open(path + txt1name):
    flag = False;
    for data in line.split():
        if data.startswith('A') or data.startswith('a'): # A � a - ����������
            flag = True;
            break;
    if flag: fw.write(line)