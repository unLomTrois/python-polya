
'''
    3. *��������� ��� ������ ������������ ��������� ������ ����� ��������, ���� �������������� 
    ��������� ������ ���� � ������������� ��� �� ����������� ���� ����. ������� ��� ��������� � ���������.
'''

class Edge():
	i = 0
	j = 0
	dist = 0
	pass

path = 'D:/�������/4 ����/�������� - ��/��������/Chapters/PythonApplication1/Chapter_11_6/Paragraph_43/';
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

# ����������� ������ ���� � ����������
edges = []
for i in range(N):
	for j in range(N):
		if W[i][j] < 99:
			edge = Edge()
			edge.i = i
			edge.j = j
			edge.dist = W[i][j]
			edges.append(edge)
for i in range(len(edges)):
	for j in range(len(edges)):
		if edges[i].dist < edges[j].dist:
			edges[i], edges[j] = edges[j], edges[i]
#****

ostov = []
for k in range(N-1):
	# ����� ����� � ����������� ����� 
	minDist = 1e10 # ����� ������� �����
	for edge in edges:
		if col[edge.i] != col[edge.j] and edge.dist < minDist:
			iMin = edge.i
			jMin = edge.j
			minDist = edge.dist

	# ���������� ����� � ������ ��������� 
	ostov.append((iMin, jMin))
	# �������������� ������
	c = col[jMin]
	for i in range(N):
		if col[i] == c:
			col[i] = col[iMin]

for edge in ostov:
	print ( "(", edge[0]+1, ",", edge[1]+1, ")" )