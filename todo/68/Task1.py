
'''
    1. �������� ���������, ������� ������� ������� �������������� ���� �����, ���������� � 
    ����� � �������, � ������� ��������� � ������ ����.
'''

path = 'D:/�������/4 ����/�������� - ��/��������/CH10_8/PythonApplication1/Chapter_8/Paragraph_68/';
txt1name, txt2name = 'input.txt', 'output.txt';

s = 0; # sum of numbers
for line in open(path + txt1name):
    s += int(line)

f = open(path + txt2name, 'w')
f.write(str(s))