"""
Соболева ПКС-1
Напишите программу для выполнения циклического сдвига массива вправо на 4 элемента.
"""


arr = [i for i in range(100)]

print("до:", arr)

arr = arr[-4:] + arr[:-4]

print("после:", arr)
