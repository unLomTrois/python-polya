# -*- coding: cp1251 -*-

'''
    Напишите программу, которая вводит натуральные числа A и N и вычисляет A^N без использования операции возведения в степень.
'''

print('A^N..\n');

A = int(input("print A --> "));
N = int(input("print N --> "));

i, mult = 1, 1; # mult - произведение
while i <= N:
    mult *= A;
    i+=1;

print(f"\nA^N = {mult}");