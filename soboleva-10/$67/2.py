"""
Соболева ПКС-1
Напишите программу, которая находит минимальный и максимальный из чётных 
положительных элементов матрицы и их индексы. Учтите, что таких элементов в матрице может и не быть.
"""
import random

matrix = [[random.randint(1, 100) for x in range(3)] for row in range(3)]
print(matrix)

min = matrix[0][0]
min_row_index = 0
min_num_index = 0
max = matrix[0][0]
max_row_index = 0
max_num_index = 0

row_index = 0
for row in matrix:
    num_index = 0
    for num in row:
        if num % 2 == 0 and num > max:
            max = num
            max_row_index = row_index
            max_num_index = num_index

        if num % 2 == 0 and num < min:
            min = num
            min_row_index = row_index
            min_num_index = num_index
        num_index += 1
    row_index += 1


print(min, min_row_index, min_num_index)
print(max, max_row_index, max_num_index)
