# -*- coding: cp1251 -*-

'''
     Заполните массив случайными числами в диапазоне 20..100 и подсчитайте отдельно число чётных и нечётных элементов.
'''

import random;


N = int(input("введите кол-во элементов --> "));

A = [];
for i in range(N):
    A.append(random.randint(20, 100));

print(A);

count = 0;
for a in A:
    if a % 2 == 0:
        count += 1;

print('четных чисел - ', count, '|', f'{round(count/N*100, 2)}%');
print('нечетных чисел - ', N-count, '|', f'{round((N-count)/N*100, 2)}%');
