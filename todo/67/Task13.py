
'''
    Напишите программу, которая находит в матрице максимальный элемент и удаляет строку 
    и столбце, в которых он расположен.
'''

from random import randint

n, m = 5, 4; # размерность массива
low, high = 10, 99; # мнимальный элемент в массиве

A = [[randint(low,high) for y in range(m)] for x in range(n)];
for el in A:
    print(el)

maxN = A[0][0];
k, l = 0, 0;
for i in range(len(A)):
    for j in range(len(A[i])):
        if maxN < A[i][j]:
            maxN = A[i][j];
            k, l = i, j;

print('ряд:', k+1, 'столбец:', l+1);

B = [];
for i in range(len(A)):
    if i != k:
        row = [];
        for j in range(len(A[i])):
            if j != l:
                row.append(A[i][j])
        B.append(row)

for el in B:
    print(el)

