"""
Соболева ПКС-1
Перестановки. К вам пришли K гостей. Напишите программу, которая выводит все 
перестановки – способы посадить их за столом. Гостей можно обозначить латинскими буквами.
"""

n = int(input("введите количество гостей: "))

sposoby = 1
for i in range(1, n + 1):
    sposoby *= i

print(sposoby)
