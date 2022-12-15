# -*- coding: cp1251 -*-

'''
      Напишите программу, которая сортирует массив по возрастанию первой цифры числа.
'''


from random import randint


def Sort(A):
    i = 0;
    while i < len(A) - 1:
        j = i + 1;
        while j < len(A):
            if A[i] // (10 ** (len(str(A[i])) - 1)) > A[j] // (10 ** (len(str(A[j])) - 1)):
                A[i], A[j] = A[j], A[i];
            j+=1;

        i+=1;

    return A;


A = [randint(1,10000) for x in range(30)];

print('before:', A);
print('after: ', Sort(A));