
'''
    �������� ���������, ������� ������ � ���������� ����� �� ��� ���, ���� �� ����� ������� 
    ����� 0. � ����� ������ ��������� �� ����� ��������� ����������� � ������������ �� 
    ��������� ����� (�� ������ 0).
'''

print('��������� ����� (1..N)..\n');

num = int(input("number --> "));

i, _f = 1, 1; # f - ���������
while i <= num:
    _f *= i;
    i+=1;

print(f"\n!{num} = {_f}");