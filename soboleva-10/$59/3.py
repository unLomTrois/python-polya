"""
Соболева ПКС-1 
Напишите процедуру, которая выводит на экран все делители переданного ей числа (в одну 
строчку).
"""


def find_delitel(num):
    res = ""
    # находим все делители
    for delitel in range(1, num // 2 + 1):
        if num % delitel == 0:
            res += str(delitel) + " "
    print(res)
    i = 1


n = int(input("введите число: "))


find_delitel(n)
