# -*- coding: cp1251 -*-

'''
     �������� ���������, ������� ��������� �������� ���������� �������: ������ � ������ 
    ������� ��� ����� ������� �� �������� �������� � ������� ����������� (����������).
    ��������� ��������� ��������� �� �����.
'''


from random import randint


def Sort(A):
    i = 0;
    while i < 3:
        j = i + 1;
        while j < len(A):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i];
            j+=1;
        i+=1;

    return A;


A = [randint(1,100) for x in range(30)];

print('before:', A);
print('after: ', Sort(A));