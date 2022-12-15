"""
Соболева П.
ПКС-1
4 курс

Напишите программу, которая считает количество чётных цифр введённого числа.
"""


n = int(input("введите число: "))

count = 0
for digit in str(n):
    digit = int(digit)
    if digit % 2 == 0:
        count += 1

print(count)
