
'''
    6. В двух файлах записаны отсортированные по возрастанию массивы неизвестной длины. 
    Объединить их и записать результат в третий файл. Полученный массив также должен быть 
    отсортирован по возрастанию. Не разрешается использовать списки.
'''

# возвращает сумму цифр переданного числа
def get_sum_digits(num):
    s = 0;
    for symbol in str(num):
        s += int(symbol)
    return s;


path = 'D:/Колледж/4 курс/Панфилов - ПП/Сентябрь/CH10_8/PythonApplication1/Chapter_8/Paragraph_68/';
txt1name, txt2name, txt3name = 'input1.txt', 'input2.txt', 'output.txt';

fr1 = open(path + txt1name) # file1 read mode
fr2 = open(path + txt2name) # file2 read mode
fw = open(path + txt3name, 'w') # file write mode

num1, num2 = ' ', ' ';
while True:
    if num1 == ' ': num1 = fr1.readline()
    if num2 == ' ': num2 = fr2.readline()

    if not num1 and not num2: break;

    if num1 and num2:
        if int(num1) < int(num2):
            fw.write('{:}\n'.format(int(num1)))
            num1 = ' ';
        elif int(num1) >= int(num2):
            fw.write('{:}\n'.format(int(num2)))
            num2 = ' ';
    else:
        if num1:
            fw.write('{:}\n'.format(int(num1)))
            num1 = ' ';
        if num2:
            fw.write('{:}\n'.format(int(num2)))
            num2 = ' ';
