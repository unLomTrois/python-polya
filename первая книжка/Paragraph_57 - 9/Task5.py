# -*- coding: cp1251 -*-

print("����������� ���-�� ���� � ������..\n");

month = int(input("������� ����� (1..12): "));

if 1 <= month <= 12:
    if   month == 2:     print("28 (29)");
    elif month % 2 == 1: print(31);
    else:                print(30);

else: print("������! ������������ �����...");