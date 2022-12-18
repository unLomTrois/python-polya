"""
    14. В предыдущей задаче добавить к списку нумерацию, например:
    1) Иванов Вася
    2) Петров Петя
"""

path = "D:/Колледж/4 курс/Панфилов - ПП/Сентябрь/CH10_8/PythonApplication1/Chapter_8/Paragraph_68/"
txt1name, txt2name, txt3name = "input.txt", "input2.txt", "output.txt"

i = 1
for line in open(path + txt1name):
    data = line.split()
    if len(data) == 3 and data[2].isdigit():
        if int(data[2]) >= 80:
            print(i, ". {:} {:}".format(data[0], data[1]), sep="")
    i += 1
