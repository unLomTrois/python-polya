# -*- coding: cp1251 -*-

'''
    *��������� ������ ���������� ������� � ��������� 10..12 � ������� ����� ����� ������� ������������������ ������� ����� ���������� �������������������
'''

import random;

N = 30; # ���-�� ��������� � �������
A = [random.randint(10, 12) for i in range(N)];

maxCount, count = 1, 1; # maxCount - ������������ ���-��, count - ������� ���-��
for i in range(1,N):
    if A[i-1] == A[i]:
        count += 1;
    else:
        if count >= maxCount:
            maxCount = count;
        count = 1;

if count > maxCount:
    maxCount = count;

print(A)
print(maxCount)