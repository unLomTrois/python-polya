
class TNode:
	data = None
	left = None
	right = None
	pass

def newNode(data):
	node = TNode()
	node.data = data
	return node

def makeTree(s, lock=False):
	if not lock:
		# проверка на целостность скобок
		cs, ce = 0, 0
		for d in s:
			if d == '(': cs+=1
			if d == ')': ce+=1
		if cs != ce:
			print('Ошибка! Не хватает скобок')
			return None
		# проверка на лишние операции
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

	k = lastOp(s)

	if k < 0:
		Tree = newNode(s)
	else:
		Tree = newNode(s[k])
		Tree.left = makeTree(s[:k], True)
		Tree.right = makeTree(s[k+1:], True)

	return Tree

def calcTree(Tree):
	if Tree is None: return

	if Tree.left == None:
		return float(Tree.data)
	else:
		n1 = calcTree(Tree.left)
		n2 = calcTree(Tree.right)

		if Tree.data == "+": res = n1 + n2
		elif Tree.data == "-": res = n1 - n2
		elif Tree.data == "*": res = n1 * n2
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