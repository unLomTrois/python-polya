
'''
     ������� � ������� ��� ����� ��������� � ���������� �� � ����� ������.
'''

import random;


def isFibNum(n):
    cur = 0; # �������
    fut = 1; # ���������
    while True:
        a = cur;
        cur = fut;

        fut = a + fut

        if cur == n: return True;
        if cur > n: break;

    return False;

n = 100; # ���-�� ��������� � ������
a = [random.randint(1,100) for i in range(n)];

print('������ ��������� �����:\n', a, f' -> {n} ���������\n');

b = [num for num in a if isFibNum(num)];

print('���������� ������ ����� �� ������������������ ���������:\n', b);