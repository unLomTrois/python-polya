# -*- coding: cp1251 -*-

'''
     �������� ��������� �������� ���� �������� �����, �� ������������ ��������. ���������� ��������� �������, 
     ������� �� ������ ��������� ���������� ��������� ��������� �� ���.
'''

from operator import contains

def TumbaWords(A, length):
    size = len(A); # ������ ����������� ����� ������ �������
    dial = [0 for x in range(length)] # ������� �����

    for k in range(size**length):
        word = ''
        for j in range(len(dial)):
            if dial[j]+1 <= size:
                word += A[dial[j]];
        print(word)

        for i in range(len(dial)):
            if dial[i]+1 >= size:
                dial[i] = 0;
            else:
                dial[i] += 1;
                break;

l = int(input('enter length: '))
A = ['�', '�', '�', '�'];
TumbaWords(A, l);