"""
Соболева П.
ПКС-1
4 курс
"""

import math

# со сложными условиями

x = float(input("введите x: "))
y = float(input("введите y: "))

# a
if x**2 + y**2 >= 4 and y <= x and x <= 2:
    print("а) попала")
# б
if y <= math.sin(x) and y <= 0.5:
    print("б) попала")
# в
if y <= 2 - x**2 and ((y >= x < 0) or (x > 0 and y >= 0)):
    print("в) попала")
else:
    print("в) не попала")

# г
if y >= x**2 - 2 and ((y <= x and x > 0) or (y <= -x and x < 0)):
    print("г) попала")
else:
    print("г) не попала")

# д
if x*2+y*2 <= 1 and (y >= x or (y <= x < 0)):
    print("д) попала")
else:
    print("д) не попала")

# е
if x*2+y*2 <= 1 and (-x <= y >= x):
    print("е) попала")
else:
    print("е) не попала")

# ж
if y >= 2 * x**2 and y >= 1 - x and x <= 1:
    print("ж) попала")
else:
    print("ж) не попала")

# з
if (x*2+y*2 <= 1 or y >= x - 1) and x >= 0 and y <= 1:
    print("з) попала")
else:
    print("з) не попала")

# з
if x*2+y*2 <= 1 or (x >= 0 and y >= 0 and (x <= 1 and y <= 1)):
    print("и) попала")
else:
    print("и) не попала")
