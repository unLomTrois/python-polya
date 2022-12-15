
'''
    9. Прочитать текст из файла и подсчитать количество слов в нём.
'''

path = 'D:/Колледж/4 курс/Панфилов - ПП/Сентябрь/CH10_8/PythonApplication1/Chapter_8/Paragraph_68/';
txt1name, txt2name, txt3name = 'input.txt', 'input2.txt', 'output.txt';

count = 0;
for line in open(path + txt1name):
    count += len(line.split())

print(count)