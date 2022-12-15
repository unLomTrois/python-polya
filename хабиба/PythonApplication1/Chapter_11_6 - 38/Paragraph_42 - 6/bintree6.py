
class TNode:
	data = None
	left = None
	right = None
	pass

def newNode(data):
	node = TNode()
	node.data = data
	return node

# iD - уровень погружения, iP - индекс родителя
def makeTree(s, lock=False, tree=[], iD=0, iP=0, offset=0):
	if not lock:
		# проверка на целостность скобок
		cs, ce = 0, 0
		for d in s:
			if d == '(': cs+=1
			if d == ')': ce+=1
		if cs != ce:
			print('Ошибка! Не хватает скобок')
			return None
		# проверка на лишнии операции
		for i in range(len(s)-1):
			if s[i] in '+-*/' and s[i+1] in '+-*/':
				print('Ошибка! Подряд идущие знаки ' + s[i])
				return None

	flag = True
	for d in s:
		if d in '+-*/':
			flag = False
			break
	if flag:
		s = s.replace('(', '').replace(')', '')

	l = len(tree)
	while len(tree) <= sum([2**i for i in range(iD+1)]):
		tree.append(0)

	k = lastOp(s)

	iC = iP*2+offset;
	if k < 0:
		tree[iC] = s
	else:
		tree[iC] = s[k]
		makeTree(s[:k], True, tree, iD+1, iC, 1)
		makeTree(s[k+1:], True, tree, iD+1, iC, 2)

	return tree

def calcTree(tree, iP=0, offset=0):
	if tree is None: return

	iC = iP*2 + offset

	if tree[iC] not in '+-*/':
		return float(tree[iC])
	else:
		n1 = calcTree(tree, iC, 1)
		n2 = calcTree(tree, iC, 2)

		if tree[iC] == "+": res = n1 + n2
		elif tree[iC] == "-": res = n1 - n2
		elif tree[iC] == "*": res = n1 * n2
		else: res = n1 / n2

		return res

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

def getPrefixExp(Tree):
	stack=[]
	stack.append(Tree)
	res = ''

	while stack:
		tree = stack.pop()
		res += tree.data

		if tree.right:
			stack.append(tree.right)
		if tree.left:
			stack.append(tree.left)

	return res

def getInfixExp(Tree, stack=[]):
	res = ''
	switch = 0

	# посещение левого звена
	if Tree.left: res += getInfixExp(Tree.left, stack)
	else: switch += 1

	if switch != 1: res += Tree.data

	# посещение правого звена
	if Tree.right: res += getInfixExp(Tree.right, stack)
	else: switch += 1

	if switch == 2: res += Tree.data

	return res

def getPostfixExp(Tree):
	stack=[]
	stack.append(Tree)
	res = ''

	while stack:
		tree = stack.pop()
		res += tree.data

		if tree.left:
			stack.append(tree.left)
		if tree.right:
			stack.append(tree.right)

	return res[::-1]