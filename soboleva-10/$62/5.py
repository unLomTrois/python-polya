
'''
    ��������� ��������� ������������ ����� �� 1 �� N ���, ����� ������ ����� ����������� ���� ����� 5.
'''

import random;


N = int(input("������� ����� --> "));

A = [x for x in range(1, N+1)];
B = list([5]);

if N >= 5: A.remove(5);
random.shuffle(A);

A = B + A;

print(A);