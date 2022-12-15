"""
Соболева П.
ПКС-1
4 курс
"""

a = 3
b = 2
c = 1

if a > b: M = a
else: M = b
if c > b: M = c
else: M = b

print(M) # 2, потому что сначала M = a, но потом M = b, т.к. b > c

# надо поменять if на elif:

a = 3
b = 2
c = 5

if a > b and a > c: M = a
elif c > b: M = c
else: M = b

print(M) # 8, потому что elif дальше не вычисляется