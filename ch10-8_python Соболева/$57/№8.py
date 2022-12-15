"""
Соболева П.
ПКС-1
4 курс
"""

num = int(input("введите число до 100: "))

if num > 100:
    print("вы ввели больше 100")
else:
    word = ""
    # 10 - 19
    if num == 10:
        word = "десять"
    if num == 11:
        word = "одиннадцать"
    if num == 12:
        word = "двенадцать"
    if num == 13:
        word = "тринадцать"
    if num == 14:
        word = "четырнадцать"
    if num == 15:
        word = "пятнадцать"
    if num == 16:
        word = "шестнадцать"
    if num == 17:
        word = "семнадцать"
    if num == 18:
        word = "восемнадцать"
    if num == 19:
        word = "девятнадцать"

    # десятки в прописи
    if num > 19:
        if num >= 20 and num < 30:
            word = "двадцать"
        if num >= 30 and num < 40:
            word = "тридцать"
        if num >= 40 and num < 50:
            word = "сорок"
        if num >= 50 and num < 60:
            word = "пятьдесят"
        if num >= 60 and num < 70:
            word = "шестьдесят"
        if num >= 70 and num < 80:
            word = "семьдесят"
        if num >= 80 and num < 90:
            word = "восемьдесят"
        if num >= 90 and num < 100:
            word = "девяносто"
        word += " "

    # единицы
    if num % 10 != 0:
        if num % 10 == 1:
            word += "один"
        if num % 10 == 2:
            word += "два"
        if num % 10 == 3:
            word += "три"
        if num % 10 == 4:
            word += "четыре"
        if num % 10 == 5:
            word += "пять"
        if num % 10 == 6:
            word += "шесть"
        if num % 10 == 7:
            word += "семь"
        if num % 10 == 8:
            word += "восемь"
        if num % 10 == 9:
            word += "девять"

    print(word)
