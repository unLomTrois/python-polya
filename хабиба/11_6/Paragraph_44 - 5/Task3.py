
'''
    3. * ������ � �����. ���� N ���������, ��� ������� �� ������� �������� ��� pi(i=1,...,N) � 
    ��������� ci(i=1,...,N). � ����� ����� ����� �������� ����� ����� �� ����� W. �������� ���������, 
    ������� ���������� ����� ������� ����� ���������, ������� ����� ������ � �����.
'''

import math
import itertools

volume = int(input('������� ������ ���: '))
cans = input('������� ���� ���������: ').split()
prices = input('������� ��������������� ���� ���������: ').split()
for i in range(len(cans)):
	cans[i] = int(cans[i])
	prices[i] = int(prices[i])

length = math.ceil(volume/min(cans))
A = itertools.product(cans, repeat=length)
B = []
for el in A:
	row = []
	for e in el:
		row.append(e)
	B.append(row)

S = [] # �������
for el in B:
	S.append(el[0])

A = [] # ������������������
C = [] # ���-��
P = [] # ����
for i in range(len(S)):
	count = 1
	price = prices[cans.index(B[i][0])]
	buff = [B[i][0]]

	for j in range(1, len(B[i])):
		if S[i]+B[i][j] < volume:
			buff.append(B[i][j])
			S[i] += B[i][j]
			count+=1
			price += prices[cans.index(B[i][0])]
		else: break

	A.append(buff)
	C.append(count)
	P.append(price)


i = P.index(max(P))
print(A[i], '=', S[i], '|', C[i], '-', P[i], '$')