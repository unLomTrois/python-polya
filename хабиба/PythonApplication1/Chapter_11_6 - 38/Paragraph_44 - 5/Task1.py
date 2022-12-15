# -*- coding: cp1251 -*-

'''
	1. Напишите программу, которая определяет оптимальный набор бидонов в задаче с молоком. 
	С клавиатуры или из файла вводится объём цистерны, количество типов бидонов и их размеры.

	В цистерне N литров молока. Есть бидоны объемом 1, 5 и 6 литров. Нужно разлить молоко в бидоны так, 
	чтобы все используемые бидоны были заполнены и их количество было минимальным.
'''

import math
import itertools

volume = int(input('введите нужный объём: '))
cans = input('введите через пробел типы объем бидонов: ').split()
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
if sum(A[i]) == volume:
	print(A[i], '|', C[i])
else:
	print('невозможно')