"""
Соболева П.
ПКС-1
4 курс
"""

import math

# без сложных условий

x = float(input("введите x: "))
y = float(input("введите y: "))

# a
if y <= x:
    if x**2 + y**2 >= 4:
        if x <= 2:
            print("а) попала")

# б
if y <= 0.5:
    if y <= math.sin(x):
        print("б) попала")

# в
if y <= 2 - x**2:
    if (y >= x >= 0):
        print("в) попала")
    if (x > 0):
        print("в) попала")

# г
if y >= x**2 - 2:
    if (y <= x > 0):
        print("г) попала")
    if (y <= -x < 0):
        print("г) попала")

# д
if x*2+y*2 <= 1:
    if y >= x:
        print("д) попала")
    if y <= x < 0:
        print("д) попала")

# е
if x*2+y*2 <= 1:
    if not (-x >= y >= x):
        print("е) попала")

# ж
if y >= 2 * x**2:
    if y >= 1 - x:
        if x <= 1:
            print("ж) попала")

# з
if y <= 1:
    if x >= 0:
        if x*2+y*2 <= 1:
            print("з) попала")
        if y >= x - 1:
            print("з) попала")

# з
if x*2+y*2 <= 1:
    print("и) попала")
if 0 < x < 1:
    if 0 < y < 1:
        print("и) попала") 