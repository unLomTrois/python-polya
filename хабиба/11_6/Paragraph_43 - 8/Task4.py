
'''
	4. Напишите программу, которая вводит из файла весовую матрицу графа, затем вводит с 
	клавиатуры номера начальной и конечной вершин и определяет оптимальный маршрут.
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

start = int(input('введите номер начального города: ')) - 1
end = int(input('введите номер конечного города: '))

N = len(W[0])
active = [True]*N # создание карты посещенных городов
R = W[start][:] # пути от текущего города
P = [0]*N # расстояния

active[start] = False # выбор начального города
P[0] = -1 # 
path = str(start+1)

for i in range(N-1):
	# поиск новой рабочей вершины R[j] -> min 
	minDist = 1e10 # очень большое число
	for j in range(N):
		if active[j] and R[j] < minDist and R[j] != 99:
			minist = R[j]
			kMin = j
	active[kMin] = False
	path += str(kMin+1)
	# проверка маршрутов через вершину kMin 
	for j in range(N):
		if R[kMin] + W[kMin][j] < R[j] and active[j]:
			R[j] = R[kMin] + W[kMin][j]
			P[j] = kMin


# вывод результата
for s in path:
	if s == str(end):
		print(s)
		break
	else:
		print(s, '-> ', end='')