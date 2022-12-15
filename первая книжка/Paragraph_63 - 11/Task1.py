# -*- coding: cp1251 -*-

'''
    Напишите программу, которая находит максимальный и минимальный из чётных положительных 
    элементов массива. Если в массиве нет чётных положительных элементов, нужно вывести сообщение об этом.
'''

import random;


N = int(input("введите кол-во элементов --> "));

A = [];
for i in range(N):
    A.append(random.randint(-100, 100));

print(A);

minN = 101;
maxN = -101;
for num in A:
    if num > 0 and num % 2 == 0:
        if minN > num: minN = num;
        if maxN < num: maxN = num;

print('min =', minN);
print('max =', maxN);
