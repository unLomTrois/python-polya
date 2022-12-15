# -*- coding: cp1251 -*-

'''
    ��������� ���������, ������� �������� � ����� ������, ���������� � ���� �����. ���� 
    ���� (������� ���������� ����� ������) ������ ����� ��������� �����������:
    �) �������� �������;
    �) ���������� �������;
    �) �������� �������;
    �) ���������� �� ������ �� �����.
'''

import pickle
from random import randint


class Heap:
    video = ''
    employee = ''
    plane = ''
    dog = ''
    pass

path = 'D:/�������/4 ����/�������� - ��/��������/Chapters/PythonApplication1/Chapter_11_6/Paragraph_39/';
dbName = 'db.txt';

# ������� ������ � ��������� �������
def Read():
    F = open(path + dbName, 'rb')
    A = pickle.load(F)

    for i in range(len(A)):
        print('{:}. {:} | {:} | {:} | {:}'.format(i+1, A[i].video, A[i].employee, A[i].plane, A[i].dog))

    return A

# ������� ������ ������ � ����
def Write(A = []):
    F = open(path + dbName, 'rb')
    B = []
    try:
        B = pickle.load(F)
    except:
        B = []

    F.close()

    C = A + B;
    F = open(path + dbName, 'wb')
    pickle.dump(C, F)

# ������� �������� �������
def Delete():
    F = open(path + dbName, 'wb')
    pickle.dump([], F)

# ������� ���������� ������� �� ��������� ����
def Sort(column = 0):
    F = open(path + dbName, 'rb')
    A = []
    try:
        A = pickle.load(F)
    except:
        return -1;

    for i in range(len(A) - 1):
        for j in range(i+1, len(A)):
            if A[i].plane > A[j].plane:
                A[i].plane, A[j].plane = A[j].plane, A[i].plane

    F = open(path + dbName, 'wb')
    pickle.dump(A, F)


while True:
    print('*'*16, '1 - ����������� ������', '2 - ������� ����� ������', '3 - ������� ��� ������', '4 - ����������� �� ����', sep='\n')
    action = int(input('> '))
    print()

    if not 1 <= action <= 4: continue

    # ��������� ������ ��� ������
    A = [Heap() for i in range(5)]
    for i in range(len(A)):
            A[i].video = 'supervideo.mp3' + str(randint(1,9))
            A[i].employee = 'Egor' + str(randint(1,9))
            A[i].plane = 'Airplane of agent Kingsman' + str(randint(1,9))
            A[i].dog = 'Bulldog' + str(randint(1,9))

    if action == 1:
        Read()
    if action == 2:
        Write(A)
    if action == 3:
        Delete()
    if action == 4:
        Sort()

    print()
    pass


