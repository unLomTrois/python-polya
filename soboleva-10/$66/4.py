"""
Соболева ПКС-1
Вести строку, в которой записана сумма натуральных чисел, например, '1+25+3'. Вычислите это выражение.
"""

text = input("введите выражение (например, '1+25+3'): ")

sum = 0
for part in text.split("+"):
    sum += int(part)

print(sum)
