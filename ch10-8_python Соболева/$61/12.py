"""
Соболева ПКС-1
Напишите рекурсивную процедуру для перевода числа из троичной уравновешенной
системы счисления (см. § 14) в десятичную. Вместо цифры -1 используйте символ «#».
"""

def toDec(n, is_negative=False, res=0, i=0):
    if i == 0:
        n = n[-1:0:-1] + n[0]

    if len(n) != i:
        mult = 0
        if n[i] == "#":
            mult = -1 * 3**i
        else:
            mult = int(n[i]) * 3**i

        if is_negative:
            res += toDec(n, is_negative, res, i + 1) - mult
        else:
            res += toDec(n, is_negative, res, i + 1) + mult

    if is_negative and i == 0:
        res = -res
    return res


n = "#1"

print(toDec(n))
