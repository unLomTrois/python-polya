# -*- coding: cp1251 -*-

'''
    Напишите процедуру, которая выводит на экран все делители переданного ей числа (в одну строчку).
'''

def show_divisiors_of_number(number):
     i = 1;
     while i <= number // 2:
         if(number % i == 0):
             print(i, "|", end=" ");
         i += 1;
     print();

show_divisiors_of_number(int(input('print number --> ')));