
'''
    ����������� ����� 19 � 20 + ������� �������� ������
'''


n1, n2 = map(int, input("������� ����� (a � b): ").split()); # n - number | nc - number copy
nc1, nc2 = n1, n2;

c1 = 0; # count ���
while nc1 != 0 and nc2 != 0:
    if nc1 > nc2:
        nc1 -= nc2;
    else:
        nc2 -= nc1
    c1+=1;
print("��� =", nc1+nc2, "|", c1, " �������� (������� ��������)");

nc1, nc2 = n1, n2;

c2 = 0; # count ��� ���
while nc1 != 0 and nc2 != 0:
    if nc1 > nc2:
        nc1 %= nc2;
    else:
        nc2 %= nc1
    c2+=1;
print("��� =", nc1+nc2, "|", c2, " �������� (���������������� ��������)");