
'''
     Напишите вариант метода пузырька, который заканчивает работу, если на очередном шаге внешнего цикла не было перестановок.
'''

from random import randint


def Sort(A):
    i = 0;
    while i < len(A) - 1:
        j = i + 1;
        log = True;
        while j < len(A):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i];
                log = False;
            j+=1;

        if log: break;
        i+=1;

    return A;


A = [randint(1,100) for x in range(30)];

print('before:', A);
print('after: ', Sort(A));