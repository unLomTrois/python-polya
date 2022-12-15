# -*- coding: cp1251 -*-

'''
    Измените программу рекурсивного перебора так, чтобы длину слова можно было ввести с клавиатуры.

    def TumbaWords(A, w, L):
    if len(w) == L:
        print(w)
        return;

    for c in A:
        TumbaWords(A, w+c, L)
'''

'''
    рекурсивное построение всех возможныъ строк из указанного алфавита, где:
    - A - алфавит(массив символов)
    - w - слово как основа(к ней все и складывается)
    - L - размер слова
'''
def TumbaWords(A, w, L):
    if len(w) == L:
        print(w)
        return;

    for c in A:
        TumbaWords(A, w+c, L)


l = int(input('enter length: '))
A = ['ы', 'ш', 'ч', 'о'];
TumbaWords(A, '', l);