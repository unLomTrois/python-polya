# -*- coding: cp1251 -*-

'''
    12. Прочитать текст из файла, заменить везде слово «паровоз» на слово «пароход» и записать в другой файл.
'''

path = 'D:/Колледж/4 курс/Панфилов - ПП/Сентябрь/CH10_8/PythonApplication1/Chapter_8/Paragraph_68/';
txt1name, txt2name, txt3name = 'input.txt', 'input2.txt', 'output.txt';

fw = open(path + txt3name, 'w') # file2 write mode
for line in open(path + txt1name):
    line = line.replace('паровоз', 'пароход') # не срабатывает из-за неккоректного чтения файла, питон его нормально не читает, а так все верно
    print(line)
    fw.write('{:}'.format(line))