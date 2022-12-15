# -*- coding: cp1251 -*-

'''
    8. В исходном файле записана речь подростка, в которой часто встречается слово-паразит 
    «короче», например: «Мама, короче, мыла, короче, раму.» Убрать из текста все слова-паразиты 
    (должно остаться «Мама мыла раму.»).
'''

path = 'D:/Колледж/4 курс/Панфилов - ПП/Сентябрь/CH10_8/PythonApplication1/Chapter_8/Paragraph_68/';
txt1name, txt2name, txt3name = 'input.txt', 'input2.txt', 'output.txt';

fw = open(path + txt3name, 'w') # file2 write mode
for line in open(path + txt1name):
    for data in line.split():
        if data != 'короче':
            fw.write(data)