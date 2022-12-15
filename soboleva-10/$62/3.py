"""
Соболева ПКС-1
Заполните массив первыми числами Фибоначчи.
"""


n = int(input("введите число: "))

arr = []

f1 = 0
f2 = 1
f_n = f1
for i in range(0, n):
    f_n = f1
    f1 = f2
    arr.append(f1)
    f2 = f_n + f2

print(arr)
