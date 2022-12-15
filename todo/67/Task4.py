
'''
     Напишите программу, которая выводит на экран столбец матрицы, сумма элементов которой наименьшая.
'''

A = [[44, 55, 66], [11, 77, 69], [34, 78, 17]];
for i in range(len(A)):
    print(A[i])

B = [sum([A[i][j] for i in range(len(A))]) for j in range(len(A[0]))]

print(B.index(min(B)))