"""
    7. Дополните решение задачи о собаках, так чтобы программа обрабатывала ошибки в исходных данных.
    При любых ошибках программа не должна завершаться аварийно. 
"""

path = "D:/Колледж/4 курс/Панфилов - ПП/Сентябрь/CH10_8/PythonApplication1/Chapter_8/Paragraph_68/"
txt1name, txt2name, txt3name = "input.txt", "input2.txt", "output.txt"

fw = open(path + txt3name, "w")  # file2 write mode
for line in open(path + txt1name):
    data = line.split()
    if len(data) >= 2 and data[1].isdigit():
        age = int(line.split()[1])
        if age < 5:
            fw.write(line)
