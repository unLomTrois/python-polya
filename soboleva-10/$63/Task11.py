"""
     Найдите в массиве все числа Фибоначчи и скопируйте их в новый массив.
"""

import random


def isFibNum(n):
    cur = 0
    # текущий
    fut = 1
    # следующий
    while True:
        a = cur
        cur = fut

        fut = a + fut

        if cur == n:
            return True
        if cur > n:
            break

    return False


n = 100
# кол-во элементов в списке
a = [random.randint(1, 100) for i in range(n)]

print("массив случайных чисел:\n", a, f" -> {n} элементов\n")

b = [num for num in a if isFibNum(num)]

print("вытекающий массив чисел из последовательности Фибоначчи:\n", b)
