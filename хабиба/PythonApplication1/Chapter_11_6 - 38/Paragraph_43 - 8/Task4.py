
'''
	4. �������� ���������, ������� ������ �� ����� ������� ������� �����, ����� ������ � 
	���������� ������ ��������� � �������� ������ � ���������� ����������� �������.
'''

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

start = int(input('������� ����� ���������� ������: ')) - 1
end = int(input('������� ����� ��������� ������: '))

N = len(W[0])
active = [True]*N # �������� ����� ���������� �������
R = W[start][:] # ���� �� �������� ������
P = [0]*N # ����������

active[start] = False # ����� ���������� ������
P[0] = -1 # 
path = str(start+1)

for i in range(N-1):
	# ����� ����� ������� ������� R[j] -> min 
	minDist = 1e10 # ����� ������� �����
	for j in range(N):
		if active[j] and R[j] < minDist and R[j] != 99:
			minist = R[j]
			kMin = j
	active[kMin] = False
	path += str(kMin+1)
	# �������� ��������� ����� ������� kMin 
	for j in range(N):
		if R[kMin] + W[kMin][j] < R[j] and active[j]:
			R[j] = R[kMin] + W[kMin][j]
			P[j] = kMin


# ����� ����������
for s in path:
	if s == str(end):
		print(s)
		break
	else:
		print(s, '-> ', end='')