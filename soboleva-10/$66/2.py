"""
Соболева ПКС-1
Ввести символьную строку и проверить, является ли она палиндромом (палиндром читается 
одинаково в обоих направлениях, например, «казак»).
"""

text = input("введите текст: ")

i = 0
is_polindrom = True
while i < len(text) // 2:
    # проверка, что i-тый элемент, и i-й с конца элемент одинаковы
    if text[i] != text[-i - 1]:
        is_polindrom = False
        break
    i += 1

print(is_polindrom)
