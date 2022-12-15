"""
Соболева ПКС-1 
Напишите процедуру, которая выводит на экран все делители переданного ей числа (в одну 
строчку).
"""


def delitel(number):
    i = 1
    while i <= number // 2:
        if number % i == 0:
            print(i, "|", end=" ")
        i += 1
    print()


delitel(int(input("Введите число:")))
