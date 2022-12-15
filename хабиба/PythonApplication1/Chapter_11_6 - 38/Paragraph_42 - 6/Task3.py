
'''
    *�������� � ���������� ��������� ��������� ������ ������ � ������.
'''

from bintree3 import makeTree, getInfixExp

s = input('������� �������������� ��������� ��������� �������� \'+-*/\':\n> ');

tree = makeTree(s)
print('infix expression: ', getInfixExp(tree))