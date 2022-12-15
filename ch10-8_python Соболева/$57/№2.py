"""
Соболева П.
ПКС-1
4 курс
"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

# если a больше всех, то М = а
if a > b and a > c and a > d and a > e: M = a
# если b больше всех, кроме а, то M = b
elif b > c and b > d and b > e: M = b
# если c больше всех, кроме a и b, то M = c
elif c > d and c > e: M = c
# если d больше е, то M = d
elif d > e: M = d
# если всё ложь, то M = e
else: M = e

print(M)
