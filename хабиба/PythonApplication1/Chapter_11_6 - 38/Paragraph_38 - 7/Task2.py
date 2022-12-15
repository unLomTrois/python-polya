
'''
    �������� ��� ���������, ������� ������� ��� ������� ����� � ��������� �� 2 �� N ����� 
    ������� ���������:
    �) ��������� ������� ����� �� ����� ��������� �� ��������;
    �) ��������� ������ ����������.
    �������� ����� ����� ����� (��� ����� ������) ���� �������� ��� ������ �������� N.
    ��������� ��� ������� �������� ����������� ���������� ����� �� N, �������� ������ � ��������� ����������
'''

from math import sqrt


N = int(input('enter number: '))

A = [True] * (N+1)
steps = 0;
for num in range(2, N+1):
    # �������� �����
    for i in range(2, num):
        steps+=1;
        if num % i == 0:
            A[num-1] = False;
            break;

print('a:', steps, 'steps')

B = [True] * (N+1)
steps = 0;
for k in range(2, int(sqrt(N))+1):
    if A[k]:
        for i in range(k*k, N, k):
            A[i] = False


print('�:', steps, 'steps')