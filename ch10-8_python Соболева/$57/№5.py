"""
Соболева П.
ПКС-1
4 курс
"""

month = int(input("введите номер месяца: "))  # 1 - 12

# проверка на ошибки
if month < 1 or month > 12:
    print("таких месяцев не существует!")

if month == 1:
    print("31")
elif month == 2:
    print("28-29")
elif month == 3:
    print("31")
elif month == 4:
    print("30")
elif month == 5:
    print("31")
elif month == 6:
    print("30")
elif month == 7:
    print("31")
elif month == 8:
    print("31")
elif month == 9:
    print("30")
elif month == 10:
    print("31")
elif month == 11:
    print("30")
elif month == 12:
    print("31")
