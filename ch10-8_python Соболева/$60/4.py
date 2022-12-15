"""
Соболева ПКС-1
Напишите функцию, которая вычисляет наименьшее общее кратное двух чисел
"""

def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a

    return a + b

# нок вычисляется по (а*б) / нод(а, б) 
def nok(a, b):
    return (a * b) / nod(a, b)


print(nok(7, 57))
