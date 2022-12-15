"""
Соболева П.
ПКС-1
4 курс

Напишите программу, которая определяет, верно ли, что введённое число содержит две одинаковых цифры, стоящие рядом (как, например, 221).
"""

n = int(input("введите число: "))

prev = ""
right = False
for num in str(n):
    if num == prev:
        right = True
        break
    prev = num

if right:
    print("число содержит две одинаковые цифры, стоящие рядом")
else:
    print("нету стоящих рядом одинаковых цифр")