# -*- coding: cp1251 -*-

'''
    Напишите программу, которая заполняет матрицу случайными числами, а затем записывает 
    нули во все элементы выше главной диагонали.

    B = [[57, -4, -57, -22], [63, 40, 54, -77], [-63, -92, -37, -95], [-4, 8, 58, -7], [-93, 12, 49, -56]]
'''

from random import randint

k, l = 5, 5;

A = [[randint(1,9) for y in range(l)] for x in range(k)]

for i in range(len(A)):
    for j in range(len(A[i])):
        if j > i:
            A[i][j] = 0;

for i in range(len(A)):
    print(A[i])
