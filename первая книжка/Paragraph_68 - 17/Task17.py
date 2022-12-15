
'''
    17. *В той же задаче отсортировать список по убыванию полученного балла (вывести балл в выходной файл).
'''

path = 'D:/Колледж/4 курс/Панфилов - ПП/Сентябрь/CH10_8/PythonApplication1/Chapter_8/Paragraph_68/';
txt1name, txt2name, txt3name = 'input.txt', 'input2.txt', 'output.txt';

arr = [];
for line in open(path + txt1name):
    data = line.split()
    if len(data) == 3 and data[2].isdigit():
        arr.append(line)

# sorting
for i in range(len(arr)):
    d1 = arr[i].split()
    for j in range(i+1, len(arr)):
        d2 = arr[j].split()
        if int(d1[2]) < int(d2[2]):
            arr[i], arr[j] = arr[j], arr[i];

i = 1;
fw = open(path + txt3name, 'w') # file2 write mode
for line in arr:
    data = line.split()
    if int(data[2]) >= 80:
            print(i, '. {:}. {:} - {:}'.format(data[1][0], data[0], data[2]), sep='')
            fw.write('{:}\n'.format(data[2]))
    i+=1;