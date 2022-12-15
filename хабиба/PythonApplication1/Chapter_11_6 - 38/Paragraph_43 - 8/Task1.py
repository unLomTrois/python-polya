# -*- coding: cp1251 -*-

'''
	1. Напишите программу, которая вводит из файла весовую матрицу графа и строит для него 
	минимальное остовное дерево.
'''

path = 'D:/Колледж/4 курс/Панфилов - ПП/Сентябрь/Chapters/PythonApplication1/Chapter_11_6/Paragraph_43/';
name = 'input.txt';

W = []
F = open(path+name)
while True:
	row = F.readline()
	if not row: break
	row = row.replace('\n', '')
	row = row.split()
	for i in range(len(row)):
		row[i] = int(row[i])
	W.append(row)

for row in W:
	print(row)

N = len(W[0])
col = [i for i in range(N)]

ostov = []
for k in range(N-1):
		# поиск ребра с минимальным весом 
	minDist = 1e10 # очень большое число
	for i in range(N):
		for j in range(N):
			if col[i] != col[j] and W[i][j] < minDist: 
				iMin = i 
				jMin = j 
				minDist = W[i][j]
		# добавление ребра в список выбранных 
	ostov.append((iMin, jMin))
		# перекрашивание вершин
	c = col[jMin]
	for i in range(N):
		if col[i] == c:
			col[i] = col[iMin]

for edge in ostov:
	print ( "(", edge[0]+1, ",", edge[1]+1, ")" )