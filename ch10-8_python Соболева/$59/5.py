"""
Соболева ПКС-1 
Напишите процедуру, которая выводит на экран запись числа, меньшего, чем 8^10, в виде 10
знаков в восьмеричной системе счисления.
"""


def sys_8(num):
    if num <= 8**10:
        print("{:010o}".format(num))


n = int(input("введите число: "))

sys_8(n)
