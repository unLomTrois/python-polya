# -*- coding: cp1251 -*-

money = float(input("Денег в год: "));
years = int(input("Кол-во лет: "));
precent = 1 + float(input("% годовых: ")) / 100;

i = 1;
sumM = 0.0;
while i <= years:
    sumM += money;
    sumM *= precent;
    sumM = round(sumM);

    string = f"*****\nГод: {i}\nТекущий капитал: {sumM}\n";
    print(string);

    i+=1;

print("\n", sumM, " вместо ", money*years, sep = "");