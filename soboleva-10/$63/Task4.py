
'''
    *Заполните массив случайными числами в диапазоне 10..12 и найдите длину самой длинной последовательности стоящих рядом одинаковых последовательностей
'''

import random;

N = 30; # кол-во элементов в массиве
A = [random.randint(10, 12) for i in range(N)];

maxCount, count = 1, 1; # maxCount - максимальное кол-во, count - текущая кол-во
for i in range(1,N):
    if A[i-1] == A[i]:
        count += 1;
    else:
        if count >= maxCount:
            maxCount = count;
        count = 1;

if count > maxCount:
    maxCount = count;

print(A)
print(maxCount)