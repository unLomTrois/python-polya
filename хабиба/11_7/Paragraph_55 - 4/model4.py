
def priority(op):
	if op in "+-": return 10
	if op in "*/": return 20
	return 100

def lastOp(s):
	minPrt = (50, 50)
	k, lvl = -1, 0
	for i in range(len(s)):
		if s[i] == '(':
			lvl+=1
			continue
		if s[i] == ')':
			lvl-=1
			continue

		prt = priority(s[i])
		if lvl < minPrt[1] and prt < 50:
			minPrt = (prt, lvl)
			k = i
		if lvl == minPrt[1] and prt <= minPrt[0] and prt < 50:
			minPrt = (prt, lvl)
			k = i

	return k

def Calc(s):
	flag = True
	for d in s:
		if d in '+-*/':
			flag = False
			break
	if flag:
		s = s.replace('(', '').replace(')', '')

	k = lastOp(s)
	if k < 0:         # вся строка - число
		return int(s) 
	else:
		n1 = Calc(s[:k])
		n2 = Calc(s[k+1:])

		if   s[k] == "+": return n1 + n2
		elif s[k] == "-": return n1 - n2
		elif s[k] == "*": return n1 * n2
		else: return n1 // n2