
'''
    Найдите за один проход по массиву три его различных элемента, которые меньше всех остальных («три минимума»)
'''

import random;

A = [];
for i in range(18):
    A.append(random.randint(0, 1000));

min1, min2, min3 = A[0], A[0], A[0]; # минимальныe значений
for i in range(1, len(A)):
    if A[i] < min1:
        min1, min2, min3 = A[i], min1, min2;

print(A);
print('1 min = ', min1);
print('2 min = ', min2);
print('3 min = ', min3);
