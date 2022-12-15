"""
Соболева
Полина
4 курс
ПКС-1
"""

a = -22
b = 4

c = a % b + b
print('а)', c)

c = a // b + a
print('б)', c)

b = a // b
c = a // b
print('в)', c)

b = a // b + b
c = a % b + a
print('г)', c)

b = a % b + 4
c = a % b + 1
print('д)', c)

b = a // b
c = a % (b + 1)
print('е)', c)

b = a % b
c = a // (b + 1)
print('ж)', c)
