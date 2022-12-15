# -*- coding: cp1251 -*-

'''
    Напишите функцию, которая вычисляет наибольший общий делитель двух чисел.
'''

# функция находит наибольший общий делитель двух чисел - greatest common divisor
def gcd(n1, n2):
    i, div = 1, 0;
    while i <= n1 and i <= n2:
        if(n1 % i == 0 and n2 % i == 0):
            div = i;
        i+=1;

    return div;

print(gcd(63, 9));
