# -*- coding: cp1251 -*-

'''
    Напишите процедуры для сложения и вычитания длинных чисел (не используя «длинную арифметику» Python).
'''

# вычитает второе число с первого без
def longSub(num1, num2):
    resIsNeg = False;
    s1 = str(num1)
    s2 = str(num2)
    if num1 < num2:
        s1, s2 = s2, s1;
        resIsNeg = True;
    N1 = [s1[i] for i in range(len(s1)-1, -1, -1)]
    N2 = [s2[i] for i in range(len(s2)-1, -1, -1)]
    N3 = []

    i, f = 0, 0; # f - добавление числа при переносе единицы
    while len(N1) > i or len(N2) > i or f == 1:
        d = 0;
        if len(N1) > i and len(N2) > i:
            d = int(N1[i]) - int(N2[i]) - f;
        else:
            if len(N1) > i:
                d = int(N1[i]) - f;
            elif len(N2) > i:
                d = int(N2[i]) - f;
            else:
                d = f;

        f = 0;
        if d < 0:
            d += 10;
            f = 1;

        N3.append(d)

        i += 1;

    N3.reverse()
    res = '';
    for d in N3:
        res += str(d);

    if resIsNeg:
        res = '-' + res;

    return int(res)

# складывает два числа
def longAdd(num1, num2):
    s1 = str(num1)
    s2 = str(num2)
    N1 = [s1[i] for i in range(len(s1)-1, -1, -1)]
    N2 = [s2[i] for i in range(len(s2)-1, -1, -1)]
    N3 = []

    i, f = 0, 0; # f - добавление числа при переносе единицы
    while len(N1) > i or len(N2) > i or f == 1:
        d = 0;
        if len(N1) > i and len(N2) > i:
            d = int(N1[i]) + int(N2[i]) + f;
        else:
            if len(N1) > i:
                d = int(N1[i]) + f;
            elif len(N2) > i:
                d = int(N2[i]) + f;
            else: d = f;

        f = 0;
        if d >= 10:
            d -= 10;
            f = 1;

        N3.append(d)

        i += 1;

    N3.reverse()
    res = '';
    for d in N3:
        res += str(d);

    return int(res)


num1 = 20;
num2 = 32;

num3 = longAdd(num1, num2)
num4 = longSub(num1, num2)

print(num1, '+', num2, '=', num3)
print(num1, '-', num2, '=', num4)