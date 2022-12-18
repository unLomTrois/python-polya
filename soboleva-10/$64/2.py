"""
     Напишите программу, в которой сортировка выполняется «методом камня» – самый тяжёлый» элемент опускается в конец массива.
"""

from random import randint


def Sort(A):
    i = 0
    while i < len(A) - 1:
        j = i + 1
        while j < len(A):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
            j += 1
        i += 1

    return A


A = [randint(1, 100) for x in range(30)]

print("before:", A)
print("after: ", Sort(A))
