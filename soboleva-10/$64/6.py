"""
      Напишите программу, которая сортирует массив по убыванию суммы цифр числа.
"""


from random import randint


# суммирует цифры числа
def SumDigs(num):
    _sum = 0
    for digit in str(num):
        digit = int(digit)
        _sum += digit ** len(str(num))

    return _sum


def Sort(A):
    i = 0
    while i < len(A) - 1:
        j = i + 1
        while j < len(A):
            if SumDigs(A[i]) > SumDigs(A[j]):
                A[i], A[j] = A[j], A[i]
            j += 1

        i += 1

    return A


A = [randint(1, 10000) for x in range(30)]

print("before:", A)
print("after: ", Sort(A))
