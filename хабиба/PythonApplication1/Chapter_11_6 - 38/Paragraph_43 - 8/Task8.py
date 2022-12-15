
'''
    8. *Напишите программу, которая решает задачу о размещении школы. Для определения 
    кратчайших путей используйте алгоритм Флойда-Уоршелла. Весовую матрицу графа вводите из файла.

	Имеется N населенных пунктов, в каждом из которых живет pi школьников (i=1,...,N). 
	Надо разместить школу в одном из них так, чтобы общее расстояние, проходимое всеми 
	учениками по дороге в школу, было минимальным. В каком пункте нужно размес тить школу?
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
for k in range(N):
	for i in range(N):
		for j in range(N):
			if W[i][k] + W[k][j] < W[i][j]:
				W[i][j] = W[i][k] + W[k][j]

print()
maxD, locality = 0, -1
for row in W:
	for i in range(len(row)):
		if maxD < row[i]:
			maxD = row[i]
			locality = i+1

print(f'в {locality} населенном пункте')