# -*- coding: cp1251 -*-

'''
    �������� ���������, ������� ��������� ������������ ���������� ��������� � �������� ������ ������: (), [], {} � <>.
'''

s = input('������� ������ � ����������, �������������� �������:\n> ')

L = "([{<"
R = ")]}>"

stack = []
err = False;

for c in s:
    if c in L:
        stack.append(c)
    p = R.find(c)
    if p >= 0:
        if not stack: err = True;
        else:
            top = stack.pop()
            if p!= L.find(top):
                err = True
    if err: break
if len(stack) > 0: err = True

print(not err)