# -*- coding: cp1251 -*-

'''
    Напишите программу, которая вводит натуральное число N и выводит на экран все натуральные числа, не превосходящие N и делящиеся на каждую из своих цифр.
'''

num = int(input("введите число: "));

for i in range(num):
    log = True;
    for j in str((i)):
        j = int(j);
        if j != 0 and i % j == 0: continue
        else: log = False;

    if log: print(i);