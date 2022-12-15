# -*- coding: cp1251 -*-

'''
    �������� � ���������� ��������� ��������� ������ ������������ ������ ���, ����� �������� ���������� � ����������� ������ ���������� ���������
'''

from bintree2 import makeTree, getPrefixExp, getPostfixExp

s = input('������� �������������� ��������� ��������� �������� \'+-*/\':\n> ');

tree = makeTree(s)
print(' prefix expression: ', getPrefixExp(tree))
print('postfix expression: ', getPostfixExp(tree))