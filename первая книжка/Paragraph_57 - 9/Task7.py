
print("Вывод возраста со словом год, года или лет..\n");

age = int(input("введите возраст: "));

if 1 <= age <= 120:
    print(age, end=" ");

    if age == 11 or age == 12 or age == 13 or age == 14 or age % 10 == 0 or age % 10 > 4: print("лет");
    elif age % 10 == 1: print("год");
    else: print("года");
else: print("Ошибка! Некорректный возраст...");