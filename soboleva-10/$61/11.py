"""
Соболева ПКС-1
Напишите рекурсивную процедуру для перевода числа из шестнадцатеричной системы 
счисления в десятичную.
"""


def dec(n, res=0, i=0):
    if i == 0:
        n = n[-1:0:-1] + n[0]

    if len(n) != i:
        mult = 0

        if n[i] == "F":
            mult = 15
        elif n[i] == "E":
            mult = 14
        elif n[i] == "D":
            mult = 13
        elif n[i] == "C":
            mult = 12
        elif n[i] == "B":
            mult = 11
        elif n[i] == "A":
            mult = 10
        else:
            mult = int(n[i])

        mult = mult * (16**i)

        res += dec(n, res, i + 1) + mult

    return res



print(dec("FF"))
