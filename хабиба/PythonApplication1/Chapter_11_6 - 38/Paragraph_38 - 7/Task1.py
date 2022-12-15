# -*- coding: cp1251 -*-

'''
    Докажите, что если у числа k нет ни одного делителя в в диапазоне от 2 до k^0.5 , то оно простое
'''

from math import sqrt


num = int(input('enter number: '))
log = True;
for i in range(2, round(sqrt(num)) + 1):
    if num % i == 0:
        log = False;
        break;

print(num, 'is prime:', log);