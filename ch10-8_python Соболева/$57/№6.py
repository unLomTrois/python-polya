"""
Соболева П.
ПКС-1
4 курс
"""

month = int(input("Введите номер месяца: "))
day = int(input("введите день месяца: "))
visokos = bool(int(input("год високосный? (1 - да, 0 - нет) ")))

# проверка на ошибки
if month < 1 or month > 12:
    print("таких месяцев не существует!")
if day > 31 and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
    print("в этом месяце не больше 31 дня!")
elif day > 30 and (month == 4 or month == 6 or month == 9 or month == 11):
    print("в этом месяце не больше 30 дней!")
elif day > 29 and month == 2:
    print("в феврале не больше 29 дней!")
elif not visokos and day == 29 and month == 2:
    print("в невисокосный год не может быть 29 день в феврале!")
else:
    # добавляем к основанию даты количество дней предыдущего месяца
    if month >= 1:
        base = 0
    if month >= 2:
        # 31 за январь
        base += 31
    if month >= 3:
        # 28-29 за февраль
        if visokos:
            base += 29
        else:
            base += 28
    if month >= 4:
        # 31 за март
        base += 31
    if month >= 5:
        # 30 за апрель
        base += 30
    if month >= 6:
        # 31 за май
        base += 31
    if month >= 7:
        # 30 за июнь
        base += 30
    if month >= 8:
        # 31 за июль
        base += 31
    if month >= 9:
        # 31 за август
        base += 31
    if month >= 10:
        # 30 за сентябрь
        base += 30
    if month >= 11:
        # 31 за октябрь
        base += 31
    if month >= 12:
        # 30 за ноябрь
        base += 30

    # номер дня от начала года, добавляем к основанию день в месяце
    num_of_day = base + day + 1  # 1 это поправка на то, что текущий день не закончился
    # из всех 365 дней вычитаем номер дня в году
    before_new_year = 365 - num_of_day

    print("до нового года:", before_new_year)
