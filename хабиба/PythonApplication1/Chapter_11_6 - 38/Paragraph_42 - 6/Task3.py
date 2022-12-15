# -*- coding: cp1251 -*-

'''
    *Добавьте в предыдущую программу процедуру обхода дерева в ширину.
'''

from bintree3 import makeTree, getInfixExp

s = input('введите математическое выражение используя операции \'+-*/\':\n> ');

tree = makeTree(s)
print('infix expression: ', getInfixExp(tree))