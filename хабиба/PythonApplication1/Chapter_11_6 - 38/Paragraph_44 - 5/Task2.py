
'''
    2. Ќапишите программу, котора€ решает задачу о куче камней заданного веса, рассмотренную в тексте параграфа.

    »з камней весом pi(i=1,...,N) набрать кучу весом ровно W или, если это невозможно,
    максимально близкую к W (но меньшую, чем W). ¬се веса камней и значение W Ц целые числа
'''

import math
import itertools

volume = int(input('введите нужный вес: '))
cans = input('введите весы камней: ').split()
for i in range(len(cans)):
	cans[i] = int(cans[i])
cans.sort()

length = math.ceil(volume/cans[0])
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
for i in range(len(S)):
	count = 1
	buff = [B[i][0]]

	for j in range(1, len(B[i])):
		if S[i] < volume:
			buff.append(B[i][j])
			S[i] += B[i][j]
			count+=1
		else: break

	A.append(buff)
	C.append(count)

i = C.index(min(C))
print(A[i], '=', S[i], '|', C[i])