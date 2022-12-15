"""
Напишите рекурсивную процедуру для перевода числа в двоичную систему, которая пра-
вильно работала бы для нуля (выводила 0).
"""

def show_in_binary(number):
    if number >= 2:
        show_in_binary(number // 2)
    print(number % 2, end="")


n = int(input("введите число: "))

show_in_binary(n)
