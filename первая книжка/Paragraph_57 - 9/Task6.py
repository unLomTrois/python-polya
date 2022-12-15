
from datetime import date

print("Определение кол-ва оставшихся дней в году\n");

month, day = map(int, input("введите текущую дату в формате MM.DD: ").split('.'));

if 1 <= month <= 12 and 1 <= day <= 31: print("до конца года осталось:", (date(2023, 1, 1) - date(2022, month, day)).days);
else: print("Ошибка! Некорректные данные...");