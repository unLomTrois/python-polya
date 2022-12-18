"""
Соболева ПКС-1
Напишите программу, которая выводит на экран строку матрицы, сумма элементов которой наибольшая.
"""

import random

matrix = [[random.randint(1, 100) for x in range(3)] for row in range(3)]
print(matrix)

sum_of_rows = [sum(row) for row in matrix]
print(sum_of_rows)
max_row = max(sum_of_rows)
n = sum_of_rows.index(max_row)

print(matrix[n])
