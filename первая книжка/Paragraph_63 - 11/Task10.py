# -*- coding: cp1251 -*-

'''
     Найдите в массиве все простые числа и скопируйте их в новый массив.
'''

import random;

# проверяет простое ли число или нет
def isPrime(n):
    k = 2;
    while k*k <= n and n % k != 0:
        k += 1;

    return (k*k > n);

n = 100; # кол-во элементов в списке
a = [random.randint(1,1000) for i in range(n)];

print('массив случайных чисел:\n', a, f' -> {n} элементов\n');

b = [num for num in a if isPrime(num)];

print('вытекающий массив простых чисел:\n', b);