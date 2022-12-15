# -*- coding: cp1251 -*-

'''
    Заполните квадратную матрицу случайными числами и выполните её транспонирование: 
    так называется процедура, в результате которой строки матрицы становятся столбцами, а 
    столбцы – строками:
'''

from random import randint

'''
    Функция транспонирования матрицы. Ограничения:
    - работает только с квадратными матрицами
'''
def trans_matrix(arr):
    res = [[0 for y in range(len(arr[0]))] for x in range(len(arr))];
    for i in range(len(arr[0])):
        for j in range(len(arr)):
            res[j][i] = arr[i][j];

    return res;



n, m = 5, 5;
low, high = 10, 99;

arr = [[randint(low,high) for y in range(m)] for x in range(n)];
for row in arr:
    print(row)

res = trans_matrix(arr)
print()

for row in res:
    print(row)
