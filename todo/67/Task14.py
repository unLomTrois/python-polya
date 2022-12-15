
'''
    Заполните матрицу из N строк и M столбцов случайными двоичными значениями (каждый 
    элемент может быть равен 0 или 1) и добавьте к ней ещё один столбец (столбец чётности) 
    так, чтобы количество единиц в каждой строке было чётным).
'''

from random import randint

n, m = 3, 8; # размерность массива
low, high = 0, 1; # мнимальный элемент в массиве

A = [[randint(low,high) for y in range(m)] for x in range(n)];

for el in A:
    print(el)

print('\nначало обработки...\n', )
for i in range(len(A)):
    count = 0;
    for j in range(len(A[i])):
        if A[i][j] == 1:
            count += 1;
    if count%2 == 1:
        A[i].append(1)
    else:
        A[i].append(0)

for el in A:
    print(el)