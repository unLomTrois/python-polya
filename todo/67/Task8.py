
'''
	Заполните матрицу, содержащую N строк и M столбцов, натуральными числами по спирали и 
	змейкой, как на рисунках:
'''

from random import randint

n, m = 3, 8; # размерность массива
low, high = 0, 0; # мнимальный элемент в массиве

A = [[randint(low,high) for y in range(m)] for x in range(n)];

# вывод рисунка A
num = 1;
for k in range(min(n // 2 + 1, m //2 + 1)):  
	for j in range(k, m - k):
		if A[k][j] == 0:
			A[k][j] = num;
			num += 1;
	for i in range(1 + k, n - k):
		if A[i][m - k - 1] == 0:
			A[i][m - k - 1] = num;
			num += 1;
	for j in range(m - k - 2, k - 1, -1):
		if A[n - k - 1][j] == 0:
			A[n - k - 1][j] = num;
			num += 1;
	for i in range(n - k - 2, k, -1):
		if A[i][k] == 0:
			A[i][k] = num;
			num += 1;
for i in range(len(A)):
	print(A[i])
print()


A = [[randint(low,high) for y in range(m)] for x in range(n)];

# вывод рисунка Б
num, k, l = 1, 0, 0;
while k < n and l < m:
	while k < n and l > -1:
		A[k][l] = num;
		num += 1;
		k+=1;
		l-=1;

	l+=1;
	if k == n:
		k-=1;
		l+=1;

	while k > -1 and l < m:
		A[k][l] = num;
		num += 1;
		k -= 1;
		l += 1;

	k+=1;
	if l == m:
		k+=1;
		l-=1;

for i in range(len(A)):
	print(A[i])
print()


A = [[randint(low,high) for y in range(m)] for x in range(n)];

# вывод рисунка В
num = 1;
for j in range(0,m,2):
	for i in range(n):
		A[i][j] = num;
		num += 1;
	for i in range(n):
		if m > j + 1: A[-i-1][j+1] = num;
		num += 1;
for i in range(len(A)):
	print(A[i])
print()