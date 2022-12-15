# -*- coding: cp1251 -*-

'''
    Напишите две программы, которые находят все простые числа в диапазоне от 2 до N двумя 
    разными способами:
    а) проверкой каждого числа из этого диапазона на простоту;
    б) используя решето Эратосфена.
    Сравните число шагов цикла (или время работы) этих программ для разных значений N.
    Постройте для каждого варианта зависимость количества шагов от N, сделайте выводы о сложности алгоритмов
'''

from math import sqrt


N = int(input('enter number: '))

A = [True] * (N+1)
steps = 0;
for num in range(2, N+1):
    # проверка числа
    for i in range(2, num):
        steps+=1;
        if num % i == 0:
            A[num-1] = False;
            break;

print('a:', steps, 'steps')

B = [True] * (N+1)
steps = 0;
for k in range(2, int(sqrt(N))+1):
    if A[k]:
        for i in range(k*k, N, k):
            A[i] = False


print('б:', steps, 'steps')