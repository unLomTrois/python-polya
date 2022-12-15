
'''
    5. Напишите программу, которая вводит из файла весовую матрицу графа и определяет 
    длины всех оптимальных маршрутов с помощью алгоритма Флойда-Уоршелла.
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
i = 1;
for row in W:
	print(f'от {i}:', row)
	i+=1