"""
    В языке племени «тумба-юмба» запрещено ставить две гласные буквы подряд. Выведите 
    все слова длины K, удовлетворяющие этому условию, и найдите их количество.
"""

"""
    рекурсивное построение всех возможныъ строк из указанного алфавита, где:
    - A - алфавит(массив символов)
    - w - слово как основа(к ней все и складывается)
    - L - размер слова
"""


def TumbaWords(A, w, L):
    if len(w) == L:
        if w.find("ыы") == -1 and w.find("оо") == -1:
            print(w)
        return

    for c in A:
        TumbaWords(A, w + c, L)


l = int(input("enter length: "))
A = ["ы", "ш", "ч", "о"]
TumbaWords(A, "", l)