"""
Соболева ПКС-1
Напишите рекурсивную процедуру для перевода числа в двоичную систему, которая пра-
вильно работала бы для нуля (выводила 0).
"""

def show_in_binary(num):
    print('{0:b}'.format(num))


n = int(input("введите число "))

show_in_binary(n)
