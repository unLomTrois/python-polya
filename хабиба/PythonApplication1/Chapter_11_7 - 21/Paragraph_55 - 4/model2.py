# -*- coding: cp1251 -*-

def priority(op):
	if op in "+-": return 1
	if op in "*/": return 2
	return 100

def lastOp(s):
	minPrt = 50
	k = -1
	for i in range(len(s)):
		if priority(s[i]) <= minPrt:
			minPrt = priority(s[i])
			k = i
	return k

def Calc(s):
	k = lastOp(s)
	if k < 0:         # вся строка - число
		return float(s) 
	else:
		n1 = Calc(s[:k])
		n2 = Calc(s[k+1:])

		if   s[k] == "+": return n1 + n2
		elif s[k] == "-": return n1 - n2
		elif s[k] == "*": return n1 * n2
		else: return n1 // n2