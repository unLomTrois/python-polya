"""
Соболева ПКС-1
Напишите процедуру, которая выводит на экран в столбик все цифры переданного ей числа, 
начиная с последней.
"""


def with_the_last(number):
    i = 1
    while number % i != number:
        print(number % (i * 10) // i)
        i *= 10


with_the_last(int(input("Введите число:")))
