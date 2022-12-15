
'''
    Напишите программу, которая вычисляет значение арифметического выражения, записанного 
    в постфиксной форме. Выражение вводится с клавиатуры в виде символьной строки. Предусмотрите сообщения об ошибках.
'''

data = input('введите математическое выражение по правилам Яна Лукашевича в постфиксной форме (+-*/):\n> ').split()

try:
    stack = []
    for x in data:
        if x in "+-*/":
            op2 = int(stack.pop())
            op1 = int(stack.pop())

            if   x == "+": res = op1 + op2
            elif x == "-": res = op1 - op2
            elif x == "*": res = op1 * op2
            else:          res = op1 // op2

            stack.append(res)
        else:
            stack.append(x)

    print('=', stack[0])

except:
    print('выражение построено неверно');
    pass