
'''
    13. � ����� �������� ������ � ����������� ����� ��������. ������ ������ �������� �������, 
    ��� � ���������� ������, ����������� ���������:
    <�������> <���> <���������� ������>
    ������� ������� � ����� ��� ��������, ������� �������� ������ 80 ������.
'''

path = 'D:/�������/4 ����/�������� - ��/��������/CH10_8/PythonApplication1/Chapter_8/Paragraph_68/';
txt1name, txt2name, txt3name = 'input.txt', 'input2.txt', 'output.txt';

for line in open(path + txt1name):
    data = line.split()
    if len(data) == 3 and data[2].isdigit():
        if int(data[2]) >= 80:
            print(data[0], data[1])