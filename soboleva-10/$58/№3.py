"""
Соболева П.
ПКС-1
4 курс
"""

n = int(input("введите число: "))
result = 0

# цикл с условием
i = 0
while i < n + 1:
    result += i
    i += 1
    
print(result)

# обнуление результата
result = 0

# цикл с переменной
for i in range(n + 1):
    result += i
    i += 1
    
print(result)
