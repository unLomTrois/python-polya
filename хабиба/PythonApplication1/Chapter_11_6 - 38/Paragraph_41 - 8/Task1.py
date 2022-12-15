
'''
     Напишите программу, которая «переворачивает» массив, записанный в файл, 
     с помощью стека. Размер массива неизвестен.
'''

filePath = input('введите полный путь к файлу:\n> ')
fileName = input('введите имя файла:\n> ');

try:
    stack, arr = [], []
    with open(filePath+fileName, 'r') as F:
        while True:
            el = F.readline()
            if not el: break;
            el = el.replace('\n', '')
            stack.append(el)

    F = open(filePath+fileName, 'w')
    while len(stack) > 0:
        F.write(str(stack.pop()) + '\n')
    F.close()


except:
    print('Файла нет в папке:\n ', filePath+fileName)