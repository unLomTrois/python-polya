# -*- coding: cp1251 -*-

'''
     Напишите программу, которая сортирует массив по убыванию и ищет в нем все значения, равные введенному числу.
'''

from random import randint

# сортирует массив методом пузырька. direct - направление сортировки (> and <)
def bubble_sort(arr, direct):
    count = 0;
    l = len(arr); # l - длина массива

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


num = int(input('enter number: '));
A = [randint(1,100) for x in range(100)];
bubble_sort(A, '<');

print('search in array:\n', A);

L, R = 0, len(A);
while L < R-1:
    c = (R + L) // 2;

    if num > A[c]:
        R = c;
    else:
        L = c;

    if num == A[c]:
        print('coincidence found:', c, 'index');