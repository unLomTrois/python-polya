# -*- coding: cp1251 -*-

'''
    Напишите процедуру, которая выводит на экран в столбик все цифры переданного ей числа, 
    начиная с первой.
'''

def show_didits(number):
    for digit in str(number):
        print(digit);

show_didits(int(input('print number --> ')));