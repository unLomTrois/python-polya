
'''
    10. ���������� ��������� ��� ������ ���������� ����� � ����� ���, ����� ��� �������� �� 
    ������ ���������� �����, �� � ���� �������� ��� ������������������ ������� ������.
'''

from array import array
import itertools

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
Data = []
while True:
	start = int(input('\n������� ����� ���������� ������: '))
	if not 0 < start <= N: exit()
	end = int(input('������� ����� ��������� ������: '))
	if not 0 < end <= N: exit()

	flag = False
	for el in Data:
		if el[0] == start and el[1] == end:
			for e in el[2]:
				print(e)
			print(len(el[2]), '���������')
			flag = True
	if flag: continue

	G = [i for i in range(N)]
	allpathes = itertools.permutations(G)

	A = [];
	for path in allpathes:
		dist = 0;
		R = W[path[0]][:];

		for k in range(1, len(path)):
			if R[path[k]] == 99: break;
			dist += R[path[k]]
			R = W[path[k]][:]
			if k == len(path)-1:
				p = ''
				for el in path:
					p += str(el)
				A.append([p, dist]);


	# ����� ����������
	count = 0
	pathes = []
	for i in range(len(A)):
		path = A[i][0]
		if int(path[0]) == start-1 and path.find(str(end-1)) != -1:
			res = ''
			for j in range(len(path)):
				if j == len(path)-1 or int(path[j]) == end-1:
					res += '{:}'.format(int(path[j])+1)
					break
				else:
					res += '{:} {:} '.format(int(path[j])+1, '->')
			if res not in pathes:
				pathes.append(res)
				print(res)
				count+=1
	print(count, '���������')
	Data.append([start, end, pathes])