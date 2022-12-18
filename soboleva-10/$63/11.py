"""
Соболева ПКС-1
Найдите в массиве все числа Фибоначчи и скопируйте их в новый массив.
"""

import random


def is_fibonacci(n):
    cur = 0
    fut = 1
    while True:
        a = cur
        cur = fut

        fut = a + fut

        if cur == n:
            return True
        if cur > n:
            break

    return False


arr = [random.randint(1, 100) for i in range(100)]

fibonacci_arr = [num for num in arr if is_fibonacci(num)]

print(fibonacci_arr)
