
'''
     ������� � ������� ��� ������� ����� � ���������� �� � ����� ������.
'''

import random;

# ��������� ������� �� ����� ��� ���
def isPrime(n):
    k = 2;
    while k*k <= n and n % k != 0:
        k += 1;

    return (k*k > n);

n = 100; # ���-�� ��������� � ������
a = [random.randint(1,1000) for i in range(n)];

print('������ ��������� �����:\n', a, f' -> {n} ���������\n');

b = [num for num in a if isPrime(num)];

print('���������� ������ ������� �����:\n', b);