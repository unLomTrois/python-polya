
'''
    � �������� ��������� ������� � ������ �� 15 ��, 17 ��, 21 ��. ��� ������ ����� 185 �� �������, �� �������� �����? ��������� ��������� ����� ��� �������?
'''


weight = 185;
a, b, c = 15, 17, 21;
count = 0;
print("{:4d} {:4d} {:4d}".format(15, 17, 18));
for i in range(0, int(weight/a) + 1):
    for j in range(0, int(weight/b) + 1):
        for k in range(0, int(weight/c) + 1):
            if a*i + b*j + k*c == weight:
                print("{:4d} {:4d} {:4d}".format(i, j, k));
                count += 1

print("\n", count, "���������")