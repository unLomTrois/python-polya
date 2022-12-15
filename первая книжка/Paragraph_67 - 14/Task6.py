# -*- coding: cp1251 -*-

'''
    Напишите программу, которая заполняет матрицу случайными числами, а затем записывает 
    нули во все элементы выше побочной диагонали.
'''

from random import randint

k, l = 5, 5;

A = [[randint(1,9) for y in range(l)] for x in range(k)]

for i in range(len(A)):
    for j in range(len(A[i])):
        if j < len(A) - i - 1:
            A[i][j] = 0;

for i in range(len(A)):
    print(A[i])