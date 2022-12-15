# -*- coding: cp1251 -*-

'''
     �������� ���������, ������� ��������� ������ �������� ������� �� �����������, � ������ � �� �������� 
     (�������� �� ������ �������� �� ������ �������� �� ������ � ��������)
'''


from random import randint


def Sort(A):
    i = 0;
    while i < len(A) // 2 - 1:
        j = i + 1;
        while j < len(A) // 2:
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i];
            j+=1;
        i+=1;

    i = len(A) - 1;
    while i > len(A) // 2 + 1:
        j = i - 1;
        while j > len(A) // 2:
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i];
            j-=1;
        i-=1;

    return A;


A = [randint(1,10000) for x in range(30)];

print('before:', A);
print('after: ', Sort(A));