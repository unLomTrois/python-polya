
'''
    13. В файле записаны данные о результатах сдачи экзамена. Каждая строка содержит фамилию, 
    имя и количество баллов, разделенные пробелами:
    <Фамилия> <Имя> <Количество баллов>
    Вывести фамилии и имена тех учеников, которые получили больше 80 баллов.
'''

path = 'D:/Колледж/4 курс/Панфилов - ПП/Сентябрь/CH10_8/PythonApplication1/Chapter_8/Paragraph_68/';
txt1name, txt2name, txt3name = 'input.txt', 'input2.txt', 'output.txt';

for line in open(path + txt1name):
    data = line.split()
    if len(data) == 3 and data[2].isdigit():
        if int(data[2]) >= 80:
            print(data[0], data[1])