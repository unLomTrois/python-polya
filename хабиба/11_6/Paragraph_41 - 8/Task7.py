
'''
	Напишите программу, которая выполняет заливку одноцветной области заданным цветом.
	Матрица, содержащая цвета пикселей, вводится из файла. Затем с клавиатуры вводятся 
	координаты точки заливки и цвет заливки. На экран нужно вывести матрицу, которая получилась после заливки
'''

filePath = input('введите полный путь к файлу:\n> ')
fileName = input('введите имя файла:\n> ');

A = []
F = open(filePath + fileName, 'r')
while True:
	line = F.readline().replace('\n', '')
	if not line: break
	data = map(int, line.split())
	A.append([el for el in data])

for line in A:
	print(line)

x0, y0 = map(int, input('введите два числа через пробел: ').split())
NEW_COLOR = int(input('введите цвет для покраски(число): '))
YMAX = len(A)
XMAX = len(A[0])
color = A[y0][x0]

Q = [(x0,y0)]
V = []
while len(Q) > 0:
	x, y = Q.pop(0)
	if A[y][x] == color:
		A[y][x] = NEW_COLOR
		if x > 0:		Q.append((x-1,y))
		if x < XMAX-1:	Q.append((x+1,y))
		if y > 0:		Q.append((x,y-1))
		if y < YMAX-1:	Q.append((x,y+1))

for line in A:
	print(line)