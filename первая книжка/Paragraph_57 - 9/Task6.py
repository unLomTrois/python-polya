
from datetime import date

print("����������� ���-�� ���������� ���� � ����\n");

month, day = map(int, input("������� ������� ���� � ������� MM.DD: ").split('.'));

if 1 <= month <= 12 and 1 <= day <= 31: print("�� ����� ���� ��������:", (date(2023, 1, 1) - date(2022, month, day)).days);
else: print("������! ������������ ������...");