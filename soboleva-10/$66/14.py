"""
Соболева ПКС-1
Выведите на экран все слова из К букв, в которых буква «Ы» встречается более 1 раза, и подсчитайте их количество.
"""


def TumbaWords(A, w, L):
    if len(w) == L:
        if w.find("ы") != -1:
            print(w)
        return

    for c in A:
        TumbaWords(A, w + c, L)


l = int(input("enter length: "))
A = ["ы", "ш", "ч", "о"]
TumbaWords(A, "", l)
