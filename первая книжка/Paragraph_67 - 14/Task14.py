
'''
    ��������� ������� �� N ����� � M �������� ���������� ��������� ���������� (������ 
    ������� ����� ���� ����� 0 ��� 1) � �������� � ��� ��� ���� ������� (������� ��������) 
    ���, ����� ���������� ������ � ������ ������ ���� ������).
'''

from random import randint

n, m = 3, 8; # ����������� �������
low, high = 0, 1; # ���������� ������� � �������

A = [[randint(low,high) for y in range(m)] for x in range(n)];

for el in A:
    print(el)

print('\n������ ���������...\n', )
for i in range(len(A)):
    count = 0;
    for j in range(len(A[i])):
        if A[i][j] == 1:
            count += 1;
    if count%2 == 1:
        A[i].append(1)
    else:
        A[i].append(0)

for el in A:
    print(el)