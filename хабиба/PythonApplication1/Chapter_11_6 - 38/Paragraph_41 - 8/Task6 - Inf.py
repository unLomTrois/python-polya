# -*- coding: cp1251 -*-

'''
    Найдите в литературе или в Интернете алгоритм перевода арифметического выражения из 
    инфиксной формы в постфиксную, и напишите программу, которая решает эту задачу.
'''

# преобразует математичпеское выражение из инфиксной(обычной) записи в постфиксную
def infixToPostfix(exp):
    prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    opStack = []
    resList = []

    symbList = exp.split()
    for symb in symbList:
        if symb in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or symb in "0123456789":
            resList.append(symb)
        elif symb == '(':
            opStack.append(symb)
        elif symb == ')':
            topToken = opStack.pop()
            while topToken != '(':
                resList.append(topToken)
                topToken = opStack.pop()
        else:
            while (opStack) and (prec[opStack[-1]] >= prec[symb]):
                  resList.append(opStack.pop())
            opStack.append(symb)

    while opStack:
        resList.append(opStack.pop())

    return " ".join(resList)

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
