# -*- coding: cp1251 -*-

'''
    7. �������� ���������, ������� ������ ������ ������������ ��� 5 ������� ������� 
    ������� ��������. ����� �� ������������ �� ��� 50 �������?
'''

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
G = [i for i in range(N)]
pathes = itertools.permutations(G)

A = [];
for path in pathes:
	dist = 0;
	R = W[path[0]][:];

	for k in range(1, len(path)):
		if R[path[k]] == 99: break;
		dist += R[path[k]]
		R = W[path[k]][:]
		if k == len(path)-1:
			A.append([path, dist]);



# ����� ����������
for i in range(len(A)):
	for j in range(len(A[i][0])):
		if j == len(A[i][0])-1:
			print(A[i][0][k]+1, '<', A[i][1])
			break
		else:
			print(A[i][0][j]+1, '-> ', end='')