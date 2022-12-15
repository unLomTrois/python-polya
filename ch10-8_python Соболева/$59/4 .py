"""
Соболева ПКС-1  
Напишите процедуру, которая выводит на экран запись переданного ей числа в римской 
системе счисления.
"""


def rim(number):
    res = ""
    while number != 0:
        if number >= 1000:
            res += "M"
            number -= 1000
            continue
        if number >= 900:
            res += "CM"
            number -= 900
            continue

        if number >= 500:
            res += "D"
            number -= 500
            continue
        if number >= 400:
            res += "CD"
            number -= 400
            continue

        if number >= 100:
            res += "C"
            number -= 100
            continue
        if number >= 90:
            res += "XC"
            number -= 90
            continue

        if number >= 50:
            res += "L"
            number -= 50
            continue
        if number >= 40:
            res += "XL"
            number -= 40
            continue

        if number >= 10:
            res += "X"
            number -= 10
            continue
        if number >= 9:
            res += "IX"
            number -= 9
            continue

        if number >= 5:
            res += "V"
            number -= 5
            continue
        if number >= 4:
            res += "IV"
            number -= 4
            continue

        if number >= 1:
            res += "I"
            number -= 1
            continue

    print(res)


n = int(input("введите число:"))

rim(n)
