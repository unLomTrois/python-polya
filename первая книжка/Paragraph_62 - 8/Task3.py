# -*- coding: cp1251 -*-

'''
    ��������� ������ ������� ������� ���������.
'''


N = int(input("������� ����� --> "));

A = [];

cur, fut = 0, 1; # �������, ���������
for i in range(N):
    a = cur;
    cur = fut;

    A.append(cur);

    fut = a + fut; 

print(A);