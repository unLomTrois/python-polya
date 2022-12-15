# -*- coding: cp1251 -*-

'''
    Напишите рекурсивную процедуру для перевода числа из троичной уравновешенной
    системы счисления (см. § 14) в десятичную. Вместо цифры -1 используйте символ «#».
'''

# возвращает число в 3-ой уровновешенной системе счисления в виде текста
def toTern(num, isMinus=False, inc=0, i=0):
	res, s = '', ''
	if num < 0 and i == 0:
		num = -num;
		isMinus = True;

	s = num % 3 + inc;
	inc = 0;

	if s == 2:
		s = '#'
		inc = 1;
	if s == 3:
		s = '0'
		inc = 1;

	if num >= 3:	res += toTern(num// 3, isMinus, inc, i+1)
	elif inc:		res += toTern(0, isMinus, inc, i+1)

	if num == 0 and inc: res += '1'

	res = f'{res}{s}'
	if isMinus and i == 0:
			resN = '';
			for s in res:
				if s == '#': resN += '1';
				elif s == '1': resN += '#';
				else: resN += '0'
			res = resN;

	return res;

# переводит число из троичной уравновешенной системы в десятичную. ntb - ternary balanced number
def toDec(ntb, isMinus=False, res=0, i=0):
	if i == 0:
		ntb = ntb[-1:0:-1] + ntb[0]

	if len(ntb) != i:
		mult = 0;
		if ntb[i] == '#':
			mult = -1 * 3**i;
		else:
			mult = int(ntb[i]) * 3**i;

		if isMinus:
			res += toDec(ntb, isMinus, res, i+1) - mult;
		else:
			res += toDec(ntb, isMinus, res, i+1) + mult;

	if isMinus and i == 0:
		res = -res;
	return res;


num = int(input("введите число --> "));
isMinus = False;
if num < 0:
	isMinus = True;

numTB = toTern(num) # numTB - ternary balanced number
print('to ternary balanced: ', numTB)

numD = toDec(numTB, num < 0)
print('to decimal number: ', numD)