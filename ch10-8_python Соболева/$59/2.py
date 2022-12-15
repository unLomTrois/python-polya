"""
Соболева ПКС-1
Напишите процедуру, которая выводит на экран в столбик все цифры переданного ей числа, 
начиная с первой.
"""


def from_the_first(number):
    for digit in str(number):
        print(digit)

n = int(input("введите число:"))

from_the_first(n)
