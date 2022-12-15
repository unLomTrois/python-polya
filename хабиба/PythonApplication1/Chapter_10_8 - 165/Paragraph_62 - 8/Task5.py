# -*- coding: cp1251 -*-

'''
    Постройте случайную перестановку чисел от 1 до N так, чтобы первое число обязательно было равно 5.
'''

import random;


N = int(input("введите число --> "));

A = [x for x in range(1, N+1)];
B = list([5]);

if N >= 5: A.remove(5);
random.shuffle(A);

A = B + A;

print(A);