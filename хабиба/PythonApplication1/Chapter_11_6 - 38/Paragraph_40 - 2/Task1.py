# -*- coding: cp1251 -*-

'''
    Постройте полную программу, которая составляет алфавитно-частотный словарь для заданного файла со списком слов
'''


path = input('введите полный путь к файлу:\n')
fileName = input('введите имя файла:\n')

try:
    D = {}
    for word in open(path + fileName, 'r'):
        word = word.replace('\n', '')
        D[word] = D.get(word, 0) + 1

    for i, k in D.items():
        print(i, k)
except:
    print('Файла нет в папке:\n ', path+fileName)