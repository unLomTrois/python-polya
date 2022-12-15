# -*- coding: cp1251 -*-

'''
    Напишите рекурсивную и нерекурсивную функции, вычисляющие НОД 
    двух натуральных чисел с помощью модифицированного алгоритма Евклида.
'''

    
# Функция возвращает НОД двух чисел. gcd - greatest common divisor - наибольший общий делитель
def GCD(n1, n2):
    while n1 != 0 and n2 != 0:
        if n1 > n2: 
            n1 %= n2;
        else:
            n2 %= n1;

    return n1+n2;

# Функция возвращает НОД двух чисел рекурсивно. gcd - greatest common divisor - наибольший общий делитель
def GCD_rec(n1, n2):
    if n1 == 0 or n2 == 0: return n1 + n2;
    else:
        if n1 > n2: 
            n1 %= n2;
        else:
            n2 %= n1;
        return GCD_rec(n1, n2)


num1 = int(input("введите 1-е число: "));
num2 = int(input("введите 2-е число: "));

res1 = GCD(num1, num2);
res2 = GCD_rec(num1, num2);

print('no recursion = ', res1);
print('   recursion = ', res2);
