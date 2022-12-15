# -*- coding: cp1251 -*-

'''
    Напишите процедуру, которая выводит на экран в столбик все цифры переданного ей числа, 
    начиная с последней.
'''

def show_reverese_didits(number):
    i = 1;
    while number % i != number:
        print(number % (i*10) // i);
        i *= 10;

show_didits(int(input('print number --> ')));