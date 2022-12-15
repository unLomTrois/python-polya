"""
Соболева П.
ПКС-1
4 курс

Добавьте в решение двух предыдущих задач вычисление количества шагов цикла. 
Заполните таблицу (шаги-1 и шаги-2 означают количество шагов двух версия алгоритма Евклида):
"""

a = int(input("введите 1-е число: "))
b = int(input("введите 2-е число: "))
c, d = a, b

iterations = 0
while a != 0 and b != 0:
    if a > b:
        a -= b
    else:
        b -= a
    iterations += 1

print("нод:", a+b, "итераций:", iterations)

iterations = 0
while c != 0 and d != 0:
    if c > d:
        c %= d
    else:
        d %= c
    iterations += 1


print("нод:", c+d, "итераций:", iterations)