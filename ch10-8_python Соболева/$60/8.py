
"""
    Напишите функцию, которая вычисляет N-ое число Фибоначчи
"""

import random

# вычисление N-го числа в последовательности Фибоначчи
def fibonacci(number):
    i = 0
    cur = 0
    # текущий
    fut = 1
    # следующий
    while i < number:
        a = cur
        cur = fut

        fut = a + fut

        i += 1

    return cur


print(fibonacci(6))
