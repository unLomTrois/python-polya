# -*- coding: cp1251 -*-

'''
    Напишите два варианта программы, которая вводит координаты точки на плоскости и опре-
    деляет, попала ли эта точка в заштрихованную область. Один вариант программы должен
    использовать сложные условия, второй – обходиться без них
'''

from math import sin


x = float(input('Координата Х: '))
y = float(input('Координата Y: '))

print('рисунок А:', end=' ')
if x <= 2 and y - x <= 0 and x**2 + y**2 -4 >= 0:
    print('+')
else:
    print('-')

print('рисунок Б:', end=' ')
if y <= 0.5 and y >= 0 and y - sin(x) <= 0:
    print('+')
else:
    print('-')

print('рисунок В:', end=' ')
if y < 2 - x**2 and (y > x or x > 0 ):
    print('+')
else:
    print('-')

print('рисунок Г:', end=' ')
if  y > x**2 -2 and (y < x or y < -x):
    print('+')
else:
    print('-')

print('рисунок Д:', end=' ')
if  x**2 + y**2 < 1 and (y > -x or y < x):
    print('+')
else:
    print('-')

print('рисунок Е:', end=' ')
if  x**2 + y**2 < 1 and (x < 0 or y > x):
    print('+')
else:
    print('-')

print('рисунок Ж:', end=' ')
if  (y > 2*x**2 and y > 1 - x and x < 1) or (y < 2*x**2 and y > 1 - x and x < 1):
    print('+')
else:
    print('-')

print('рисунок З:', end=' ')
if  y < 1 and x > 0 and (x**2 + y**2 < 1 or y > x - 1):
    print('+')
else:
    print('-')

print('рисунок И:', end=' ')
if  x**2 + y**2 < 1 or (x > 0 and y > 0 and y < 1 and x < 1):
    print('+')
else:
    print('-')
