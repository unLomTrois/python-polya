"""
Соболева ПКС-1
Напишите функцию, которая моделирует бросание двух игральных кубиков (на каждом может выпасть от 1 до 6 очков). (Используйте генератор псевдослучайных чисел.)
"""

import random

def kubik():
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    return a+b


print(kubik())