"""
     *В матрице, содержащей N строк и M столбцов, записана карта островного государства Лимония 
     (нули обозначают море, а единицы – сушу). Все острова имеют форму прямоугольника. 
     Написать программу, которая по готовой карте определяет количество островов.
"""

from random import randint

n, m = 3, 7
# размерность массива
low, high = 0, 1
# мнимальный элемент в массиве

A = [[randint(low, high) for y in range(m)] for x in range(n)]

for row in A:
    print(row)

count, f = 0, False
for i in range(n):
    f = False
    for j in range(m):
        if A[i][j] == 1 and not f:
            count += 1
            f = True

for row in A:
    print(row)

print(count)
