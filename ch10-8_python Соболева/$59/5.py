"""
Соболева ПКС-1 
Напишите процедуру, которая выводит на экран запись числа, меньшего, чем 8^10, в виде 10
знаков в восьмеричной системе счисления.
"""


def sys_8(num):
    print("{:010o}".format(num))


sys_8(int(input("введите число: ")))
