"""
Соболева П.
ПКС-1
4 курс

Найдите все пятизначные числа, которые при делении на 133 дают в остатке 125, а при де-
лении на 134 дают в остатке 111.
"""

for i in range(10000, 99999):
    if i % 133 == 125 and i % 134 == 111:
        print(i)
    i += 1
