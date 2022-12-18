"""
     Напишите программу, которая находит минимальный и максимальный из чётных 
     положительных элементов матрицы и их индексы. Учтите, что таких элементов в матрице может и не быть.
"""

A = [[44, 55, 66], [11, 77, 69], [34, 78, 17]]
print(A)

minResereve = 0
maxResereve = 0

if A[0][0] >= 0:
    minN = A[0][0]
    maxN = A[0][0]
else:
    minN = minResereve
    maxN = maxResereve

i1, i2, j1, j2 = 0, 0, 0, 0
# i1 - row index min, i2 = row index max, j1 - column index min, j2 - column index max
for k in range(len(A)):
    for l in range(len(A[k])):
        if A[k][l] >= 0 and A[k][l] % 2 == 0:
            if A[k][l] < minN:
                minN = A[k][l]
                i1, j1 = k, l
            if A[k][l] > maxN:
                maxN = A[k][l]
                i2, j2 = k, l

if minN == minResereve:
    print("минимального значения подходящего под условия нет")
else:
    print("min =", minN, " | ", i1, j1)

if maxN == maxResereve:
    print("максимального значения подходящего под условия нет")
else:
    print("max =", maxN, " | ", i2, j2)
