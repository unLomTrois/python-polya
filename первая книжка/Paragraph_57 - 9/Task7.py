
print("����� �������� �� ������ ���, ���� ��� ���..\n");

age = int(input("������� �������: "));

if 1 <= age <= 120:
    print(age, end=" ");

    if age == 11 or age == 12 or age == 13 or age == 14 or age % 10 == 0 or age % 10 > 4: print("���");
    elif age % 10 == 1: print("���");
    else: print("����");
else: print("������! ������������ �������...");