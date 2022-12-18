"""
Соболева ПКС-1
Напишите программу, которая находит минимальный и максимальный элементы матрицы и их индексы.
"""

matrix = [[44, 55, 66], [11, 77, 69], [34, 78, 17]]
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
        if num > max:
            max = num
            max_row_index = row_index
            max_num_index = num_index

        if num < min:
            min = num
            min_row_index = row_index
            min_num_index = num_index
        num_index += 1
    row_index += 1


print(min, min_row_index, min_num_index)
print(max, max_row_index, max_num_index)
