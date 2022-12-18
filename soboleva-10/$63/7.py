"""
Соболева ПКС-1
Заполните массив из чётного количество элементов случайными числами и выполните ре-
верс отдельно для 1-ой и 2-ой половин массива.
"""

import random

arr = [random.randint(0, 9) for i in range(100)]

print("до:", arr)

for i in range(0, len(arr) // 4):
    arr[i], arr[len(arr) // 2 - i - 1] = arr[len(arr) // 2 - i - 1], arr[i]

for i in range(len(arr) // 2, int(len(arr) // 2 * 1.5)):
    arr[i], arr[len(arr) - i + len(arr) // 2 - 1] = (
        arr[len(arr) - i + len(arr) // 2 - 1],
        arr[i],
    )

print("после:", arr)
