
'''
     Напишите программу, которая заполняет матрицу 7x7 случайными числами, а затем 
     записывает в элементы, отмеченные на рисунках, число 99:
'''

from random import randint

k, l = 7, 7;
low, high = -9, -1;

A = [[randint(low,high) for y in range(l)] for x in range(k)];

# вывод рисунка A
for i in range(len(A)):
    for j in range(len(A[i])):
        if (i > 0 and i < len(A)-1) and (j > 0 and j < len(A[i])-1):
            if j >= len(A) - i - 1:
                A[i][j] = 99;
for i in range(len(A)):
    print(A[i])
print()

A = [[randint(low,high) for y in range(l)] for x in range(k)];

# вывод рисунка Б
for i in range(len(A)):
    for j in range(len(A[i])):
        if (i > 0 and i < len(A)-1) and (j > 0 and j < len(A[i])-1):
            if j < len(A) - i:
                A[i][j] = 99;
for i in range(len(A)):
    print(A[i])
print()

A = [[randint(low,high) for y in range(l)] for x in range(k)];

# вывод рисунка В
for i in range(4):
    for j in range(3-i, 3+i+1): A[i][j] = 99;
    for j in range(3-i, 3+i+1): A[6-i][j] = 99;

for i in range(len(A)):
    print(A[i])
print()