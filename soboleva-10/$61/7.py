"""
Соболева ПКС-1
Напишите рекурсивную процедуру для перевода числа в шестнадцатеричную систему 
счисления.
"""


def hex(num):
    res = ""
    if num >= 16:
        res += hex(num // 16)

    lastdigit = num % 16
    if lastdigit == 10:
        res += "A"
    elif lastdigit == 11:
        res += "B"
    elif lastdigit == 12:
        res += "C"
    elif lastdigit == 13:
        res += "D"
    elif lastdigit == 14:
        res += "E"
    elif lastdigit == 15:
        res += "F"
    else:
        res += str(num)

    return res


n = int(input("введите число: "))

print(hex(n))
