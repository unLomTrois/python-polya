# -*- coding: cp1251 -*-

'''
	 Заполните квадратную матрицу случайными числами и выполните её поворот на 90 градусов:
'''

from random import randint

'''
	Поворачивает матрицу на ... 90 градусов.
	Ограничения:
	- работает только с квадратными матрицами
'''
def rotate_matrix(arr):
	res = [[0 for y in range(len(arr[0]))] for x in range(len(arr))];

	i, k = 0, len(arr[0])-1;
	while i < len(arr):
		j, l = 0, 0;
		while j < len(arr[i]):
			res[l][k] = arr[i][j];
			j+=1;
			l+=1;

		i+=1;
		k-=1;

	return res;


n, m = 5, 5;
low, high = 10, 99;

arr = [[randint(low,high) for y in range(m)] for x in range(n)];
for row in arr:
	print(row)

res = rotate_matrix(arr)
print()

for row in res:
	print(row)