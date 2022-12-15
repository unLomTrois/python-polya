"""
Соболева П.
ПКС-1
4 курс
"""

a = int(input("введите число a: "))
b = int(input("введите число b: "))

result = 0
for i in range(a, b + 1):
    result += i*i

print(result)