"""
Соболева ПКС-1 
Напишите процедуру, которая принимает параметр – натуральное число N – и выводит на
экран линию из N символов '–'.
"""


def show_sys_symbol(number):
    print("-" * number)


show_sys_symbol(int(input("print number --> ")))
