
'''
    Ќапишите программу, котора€ вводит натуральные числа a и b и выводит все простые числа 
    в диапазоне от a до b.
'''

print('¬ывод всех постых чисел в указанном диапозоне..\n');

a = int(input("print a --> "));
b = int(input("print b --> "));

while a <= b:
    i = 2;
    _log = True;
    while i < a // 2:
        if(a % i == 0):
           _log = False;
           break;
        i+=1;

    if _log: print(a);

    a+=1;
