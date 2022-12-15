
'''
    3. * Задача о ранце. Есть N предметов, для каждого из которых известен вес pi(i=1,...,N) и 
    стоимость ci(i=1,...,N). В ранец можно взять предметы общим весом не более W. Напишите программу, 
    которая определяет самый дорогой набор предметов, который можно унести в ранце.
'''

import math
import itertools

volume = int(input('введите нужный вес: '))
cans = input('введите весы предметов: ').split()
prices = input('введите соответствующие цены предметов: ').split()
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

S = [] # размеры
for el in B:
	S.append(el[0])

A = [] # последовательности
C = [] # кол-ва
P = [] # цены
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