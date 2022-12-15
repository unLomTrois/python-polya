# -*- coding: cp1251 -*-

'''
     �������� ���������, ������� ������� ������� ����� ����� ��� �������� ������ ��� ������� �� 32 ��������� 
     � ��������� 0..100. ��� ������ ����������� 1000 ��������� ����� � ���� �� ���������.
'''

from random import randint

# ��������� ������ ������� ��������. direct - ����������� ���������� (> and <)
def bubble_sort(arr, direct):
    count = 0;
    l = len(arr); # l - ����� �������

    if direct == '>':
        for i in range(l):
            for j in range(l-i-1):
                if arr[j+1] < arr[j]: 
                    arr[j], arr[j+1] = arr[j+1], arr[j];
                    count += 1;
    else:
        for i in range(l):
            for j in range(l-i-1):
                if arr[j+1] > arr[j]: 
                    arr[j], arr[j+1] = arr[j+1], arr[j];
                    count += 1;

    return count;


A = [randint(0,100) for x in range(32)];
bubble_sort(A, '<');

print('search in array:\n', A);

summa = 0;
for i in range(1000):
    num = randint(0, 100);
    L, R = 0, len(A);
    j = 0; # ������� �����
    while L < R-1:
        j += 1;
        c = (R + L) // 2;

        if num > A[c]:
            R = c;
        else:
            L = c;

        if num == A[c]:
            break;

    summa += j;

print('avg number of steps:', round(summa/1000, 2));