# -*- coding: cp1251 -*-

'''
     Заполните массив случайными числами в диапазоне 0..100 и подсчитайте отдельно среднее 
     значение всех элементов, которые < 50, и среднее значение всех элементов, которые >= 50
'''

import random;


N = int(input("введите кол-во элементов --> "));

A = [];
for i in range(N):
    A.append(random.randint(0, 100));

print(A);

count = 0;
for a in A:
    if a < 50:
        count += 1;
print('ср значение чисел < 50 - ', count, '|', f'{round(count/N*100, 2)}%');

count = 0;
for a in A:
    if a >= 50:
        count += 1;
print('ср значение чисел >= 50 - ', count, '|', f'{round(count/N*100, 2)}%');
