
'''
    ��������� ������ �� ������� ���������� ��������� ���������� ������� � ��������� ������ �������� ��� 1-�� � 2-�� ������� �������.
'''

import random;

N = 12; # ���-�� ��������� � ������
A = [random.randint(0, 9) for i in range(N)];


print('�� ������� �������:\n', A, '\n');

# ������ ������ �������� ������
for i in range(0,N//4):
    A[i], A[N//2 - i - 1] = A[N//2 - i - 1], A[i];

# ������ ������ �������� ������
for i in range(N//2, int(N//2*1.5)):
    A[i], A[N - i + N//2 - 1] = A[N - i + N//2 - 1], A[i];

print('����� ������� �������:\n', A);