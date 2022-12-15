
'''
    ������� ������ � ���������� � ������� (�� ���� ������) ���������� ���������, ������� 
    ������������ ��������.
'''


print('������� ����� ����� (10) ��� ����� � ������');

A = [];
count, maxN = 1, 0;

num = int(input("-> "));
maxN = num;
A.append(num);
for i in range(9):
    num = int(input("-> "));
    if maxN < num:
        maxN = num;
        count = 0;
    if maxN == num: count += 1;

    A.append(num);

print('\n', A, '\n', 'max count =', count, '|', maxN);
