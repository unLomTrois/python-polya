"""
Соболева ПКС-1
Напишите рекурсивную процедуру для перевода числа в троичную уравновешенную систему счисления (см. § 14). 
Вместо цифры -^1 используйте символ «#»
"""

def toTern(num, is_negative=False, inc=0, i=0):
    res, s = "", ""
    if num < 0 and i == 0:
        num = -num
        is_negative = True

    s = num % 3 + inc
    inc = 0

    if s == 2:
        s = "#"
        inc = 1
    if s == 3:
        s = "0"
        inc = 1

    if num >= 3:
        res += toTern(num // 3, is_negative, inc, i + 1)
    elif inc:
        res += toTern(0, is_negative, inc, i + 1)

    if num == 0 and inc:
        res += "1"

    res = f"{res}{s}"
    if is_negative and i == 0:
        resN = ""
        for s in res:
            if s == "#":
                resN += "1"
            elif s == "1":
                resN += "#"
            else:
                resN += "0"
        res = resN

    return res


n = int(input("введите число: "))

print(toTern(n))
