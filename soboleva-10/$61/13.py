"""
Соболева ПКС-1

Напишите рекурсивную и нерекурсивную функции, вычисляющие НОД 
двух натуральных чисел с помощью модифицированного алгоритма Евклида.
"""


def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a

    return a + b


def nod_rec(a, b):
    if b == 0:
        return a
    return nod_rec(b, a%b)


a = int(input("введите 1-е число: "))
b = int(input("введите 2-е число: "))

print(nod(a, b), nod_rec(a, b))
