
'''
    Ввести адрес файла и «разобрать» его на части, разделенные знаком '/'. Каждую часть 
    вывести в отдельной строке.
'''

text = input('enter file path (\'/\'): ');
txts = text.split('/');
for txt in txts:
    print(txt);