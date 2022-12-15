# -*- coding: cp1251 -*-

'''
    Напишите вариант предыдущей программы, в котором в качестве стека используется символьная строка
'''

s = input('введите скобки в логическом, математическом порядке:\n> ')

L = "([{<"
R = ")]}>"

stack = ''
err = False;

i = 0
for c in s:
    if c in L:
        stack += c
    p = R.find(c)
    if p >= 0:
        if not stack: err = True;
        else:
            top = stack[-1]
            stack = stack[:-1]

            if p!= L.find(top):
                err = True
    if err:
        print('символ:', i+1, 'ошибочен')
        break
    i+=1
if len(stack) > 0: err = True
if err:
    print('не хватает закрывающейся(ихся) скобок в конце |', not err)
else:
    print(not err);