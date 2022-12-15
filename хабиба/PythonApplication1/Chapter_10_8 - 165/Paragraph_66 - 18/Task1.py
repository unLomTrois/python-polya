# -*- coding: cp1251 -*-

'''
    Напишите программу, которая во введенной символьной строке заменяет все буквы «а» на 
    буквы «б» и наоборот, как заглавные, так и строчные. При вводе строки 'абсАБС' должен 
    получиться результат 'басБАС'
'''

text = input('enter text: ');
txt = '';

for symbol in text:
    if symbol == 'а': symbol = 'б';
    elif symbol == 'б': symbol = 'а';
    if symbol == 'А': symbol = 'Б';
    elif symbol == 'Б': symbol = 'А';
    txt += symbol;

print(txt);
