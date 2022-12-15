# -*- coding: cp1251 -*-

'''
    *Напишите процедуры для умножения и деления длинных чисел (не используя «длинную арифметику» Python).
'''

def longMult(num1, num2):
    num1 = str(num1)[::-1]
    num2 = str(num2)[::-1]
    length = len(num1) + len(num2) + 1;
    C = [0] * (length+1);

    for i in range(len(num1)):
        for j in range(len(num2)):
            C[i+j] += int(num1[i]) * int(num2[j])

    for i in range(length):
        C[i+1] += C[i]//10;
        C[i] %= 10;

    res = '';
    C.reverse()
    for d in C:
        res += str(d);

    return int(res)

def longDiv(num1, num2):
    num1S = str(num1)[::-1]
    num2S = str(num2)[::-1]
    length = len(num1S) + len(num2S) + 1;
    C = [0] * (length+1);

    for i in range(len(num1S)):
        for j in range(len(num2S)):
            C[i+j] += int(num1S[i]) * int(num2S[j])

    for i in range(length):
        C[i+1] += C[i]//10;
        C[i] %= 10;

    res = '';
    C.reverse()
    for d in C:
        res = str(num1//num2)

    return int(res);



num1 = int(input('введите 1-е целое число: '))
num2 = int(input('введите 2-е целое число: '))

num3 = longMult(num1, num2)
num4 = longDiv(num1, num2)

print(num1, '*', num2, '=', num3)
print(num1, '/', num2, '=', num4)