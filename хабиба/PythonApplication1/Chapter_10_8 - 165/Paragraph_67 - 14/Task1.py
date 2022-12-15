# -*- coding: cp1251 -*-

'''
    Напишите программу, которая находит минимальный и максимальный элементы матрицы и их индексы.
'''

A = [[44, 55, 66], [11, 77, 69], [34, 78, 17]];
print(A)

minN = A[0][0];
maxN = A[0][0];
i1, i2, j1, j2 = 0, 0, 0, 0; # i1 - row index min, i2 = row index max, j1 - column index min, j2 - column index max
for k in range(len(A)):
    for l in range(len(A[k])):
        if A[k][l] < minN:
            minN = A[k][l];
            i1, j1 = k, l;
        if A[k][l] > maxN:
            maxN = A[k][l];
            i2, j2 = k, l;

print('min =', minN, ' | ', i1, j1)
print('max =', maxN, ' | ', i2, j2)