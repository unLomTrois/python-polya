"""
Соболева П.
ПКС-1
4 курс

Напишите программу, которая вводит натуральное число N и выводит на экран все натуральные числа, не превосходящие N и делящиеся на каждую из своих цифр
"""

n = int(input("введите число N: "))

# для всех чисел от 1 до N
for num in range(1, n+1):
    good = True  # предполагается, что число делится на свои цифры
    # для всех цифр в числе num
    for digit in str(num):
        digit = int(digit) # поменять тип на int
        # если хотя бы одна из цифр это 0, или num не делится на одну из своих цифр, то пропустить
        if digit == 0 or num % digit != 0:
            good = False
            break
    if good:
        print(num)