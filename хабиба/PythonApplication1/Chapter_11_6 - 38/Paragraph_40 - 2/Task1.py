# -*- coding: cp1251 -*-

'''
    ��������� ������ ���������, ������� ���������� ���������-��������� ������� ��� ��������� ����� �� ������� ����
'''


path = input('������� ������ ���� � �����:\n')
fileName = input('������� ��� �����:\n')

try:
    D = {}
    for word in open(path + fileName, 'r'):
        word = word.replace('\n', '')
        D[word] = D.get(word, 0) + 1

    for i, k in D.items():
        print(i, k)
except:
    print('����� ��� � �����:\n ', path+fileName)