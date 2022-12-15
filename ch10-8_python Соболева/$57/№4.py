"""
Соболева П.
ПКС-1
4 курс
"""

month = int(input()) # 1 - 12

if month < 1 or month > 12:
    print("таких месяцев не существует!")

if (month == 12 or month == 1 or month == 2):
    print("зима")
elif month >= 3 and month < 6:
    print("весна")
elif month >= 6 and month < 9:
    print("лето")
elif month >= 9 and month < 12:
    print("осень")