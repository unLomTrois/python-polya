"""
Соболева П.
ПКС-1
4 курс

Напишите программу, которая вводит с клавиатуры числа до тех пор, пока не будет введено
число 0. В конце работы программы на экран выводится сумма и произведение введенных чисел (не считая 0).
"""

sum = 0
mult = 1
while True:
    n = int(input(f"введите число (или ноль): "))
    if n == 0:
        break
    sum += n
    mult *= n

print("сумма:", sum, "произведение:", mult)
