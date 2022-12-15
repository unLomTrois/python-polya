# -*- coding: cp1251 -*-

'''
    5. Напишите процедуру для ввода длинных чисел из файла в массив (список).
'''


'''
    По условиям данной задачи неопнятно в каком ввиде будут храниться длинные числа в файле.
    Поэтому я решил, что будут так: на каждой строке файла, будет отдельное число
'''

path = 'D:/Колледж/4 курс/Панфилов - ПП/Сентябрь/Chapters/PythonApplication1/Chapter_11_6/Paragraph_38/';
txt1name, txt2name = 'input.txt', 'output.txt';

# записывает все числа нефиксированной длины из указанного файла в список
def search(filePath, arr):
    for string in open(filePath):
        arr.append(int(string))


arr = []
search(path+txt1name, arr)

for num in arr:
    print(num)