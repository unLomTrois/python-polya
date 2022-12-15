"""
    Напишите функцию, которая вычисляет наименьшее общее кратное двух чисел
"""

# функция находит наименьшее общее кратное двух чисел - smallest common multiple
def scm(n1, n2):
    i = n1 if n1 < n2 else n2
    mult = -1
    while i > 1:
        if n1 % i == 0 and n2 % i == 0:
            mult = i
        i -= 1

    return mult


print(scm(63, 3))
