# -*- coding: cp1251 -*-

'''
     �������� ���������, ������� ������� �� ����� ������ �������, ����� ��������� ������� ����������.
'''

A = [[44, 55, 66], [11, 77, 69], [34, 78, 17]];
print(A)

B = [sum(row) for row in A];

print(A[B.index(max(B))])