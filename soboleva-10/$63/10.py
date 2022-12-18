"""
Соболева ПКС-1
Найдите в массиве все простые числа и скопируйте их в новый массив.
"""

import random


def is_prime(num):
    # предположим, что оно простое
    isprime = True
    # чтобы провериь на простоту,
    # надо проверить на то,
    # что число не делится ни на что между 2 и числом
    for n in range(2, num):
        # если оно делится, то оно не простое
        if (num % n) == 0:
            isprime = False
            break

    return isprime


arr = [random.randint(1, 1000) for i in range(100)]
prime_arr = [num for num in arr if is_prime(num)]

print(prime_arr)
