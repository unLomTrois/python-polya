"""
     Напишите программу, которая выполняет неполную сортировку массива: ставит в начало 
    массива три самых меньших по величине элемента в порядке возрастания (неубывания).
    Положение остальных элементов не важно.
"""


from random import randint


def Sort(A):
    i = 0
    while i < 3:
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
