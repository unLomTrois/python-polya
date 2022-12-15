
class TNode:
	data = None
	left = None
	right = None
	pass

def newNode(data):
	node = TNode()
	node.data = data
	return node

def makeTree(s):
	k = lastOp(s)

	if k < 0:
		Tree = newNode(s)
	else:
		Tree = newNode(s[k])
		Tree.left = makeTree(s[:k])
		Tree.right = makeTree(s[k+1:])

	return Tree

def calcTree(Tree):
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

def priority ( op ):
	if op in "+-": return 1
	if op in "*/": return 2
	return 100

def lastOp(s):
	minPrt = 50 # любое между 2 и 100
	k = -1
	for i in range(len(s)):
		if priority(s[i]) <= minPrt:
			minPrt = priority(s[i])
			k = i
	return k