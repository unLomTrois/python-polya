# -*- coding: cp1251 -*-

money = float(input("����� � ���: "));
years = int(input("���-�� ���: "));
precent = 1 + float(input("% �������: ")) / 100;

i = 1;
sumM = 0.0;
while i <= years:
    sumM += money;
    sumM *= precent;
    sumM = round(sumM);

    string = f"*****\n���: {i}\n������� �������: {sumM}\n";
    print(string);

    i+=1;

print("\n", sumM, " ������ ", money*years, sep = "");