# -*- coding: cp1251 -*-

'''
    Добавьте в предыдущую программу процедуры обхода построенного дерева так, чтобы получить префиксную и постфиксную запись введенного выражения
'''

from bintree2 import makeTree, getPrefixExp, getPostfixExp

s = input('введите математическое выражение используя операции \'+-*/\':\n> ');

tree = makeTree(s)
print(' prefix expression: ', getPrefixExp(tree))
print('postfix expression: ', getPostfixExp(tree))