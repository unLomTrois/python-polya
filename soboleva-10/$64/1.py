"""
Соболева ПКС-1
Напишите программу, которая сортирует массив и находит количество различных чисел в нём.
"""

from random import randint


A = [randint(1, 100) for x in range(30)]
B = []

print("before:", A)

i = 0
while i < len(A) - 1:
    j = i + 1
    while j < len(A):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]
        j += 1

    i += 1

i = 0
while i < len(A) - 1:
    if not A[i] in B:
        B.append(A[i])
    i += 1

print("after: ", A)
print("различных чисел:", len(B))
