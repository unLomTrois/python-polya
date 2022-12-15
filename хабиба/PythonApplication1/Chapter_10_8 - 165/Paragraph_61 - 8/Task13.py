# -*- coding: cp1251 -*-

'''
    �������� ����������� � ������������� �������, ����������� ��� 
    ���� ����������� ����� � ������� ����������������� ��������� �������.
'''

    
# ������� ���������� ��� ���� �����. gcd - greatest common divisor - ���������� ����� ��������
def GCD(n1, n2):
    while n1 != 0 and n2 != 0:
        if n1 > n2: 
            n1 %= n2;
        else:
            n2 %= n1;

    return n1+n2;

# ������� ���������� ��� ���� ����� ����������. gcd - greatest common divisor - ���������� ����� ��������
def GCD_rec(n1, n2):
    if n1 == 0 or n2 == 0: return n1 + n2;
    else:
        if n1 > n2: 
            n1 %= n2;
        else:
            n2 %= n1;
        return GCD_rec(n1, n2)


num1 = int(input("������� 1-� �����: "));
num2 = int(input("������� 2-� �����: "));

res1 = GCD(num1, num2);
res2 = GCD_rec(num1, num2);

print('no recursion = ', res1);
print('   recursion = ', res2);
