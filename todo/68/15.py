"""
    15. В той же задаче сократить имя до одной буквы и поставить перед фамилией:
    1) В. Иванов
    2) П. Петров 
"""

path = "D:/Колледж/4 курс/Панфилов - ПП/Сентябрь/CH10_8/PythonApplication1/Chapter_8/Paragraph_68/"
txt1name, txt2name, txt3name = "input.txt", "input2.txt", "output.txt"

i = 1
for line in open(path + txt1name):
    data = line.split()
    if len(data) == 3 and data[2].isdigit():
        if int(data[2]) >= 80:
            print(i, ". {:}. {:}".format(data[1][0], data[0]), sep="")
    i += 1
