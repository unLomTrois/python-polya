# -*- coding: cp1251 -*-

'''
    5. �������� ��������� ��� ����� ������� ����� �� ����� � ������ (������).
'''


'''
    �� �������� ������ ������ ��������� � ����� ����� ����� ��������� ������� ����� � �����.
    ������� � �����, ��� ����� ���: �� ������ ������ �����, ����� ��������� �����
'''

path = 'D:/�������/4 ����/�������� - ��/��������/Chapters/PythonApplication1/Chapter_11_6/Paragraph_38/';
txt1name, txt2name = 'input.txt', 'output.txt';

# ���������� ��� ����� ��������������� ����� �� ���������� ����� � ������
def search(filePath, arr):
    for string in open(filePath):
        arr.append(int(string))


arr = []
search(path+txt1name, arr)

for num in arr:
    print(num)