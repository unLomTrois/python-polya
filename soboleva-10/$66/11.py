"""
Соболева ПКС-1
В условиях предыдущей задачи определите фамилию и имя футболиста, забившего наибольшее число голов, и количество забитых им голов
"""


n = int(input("введите количество футболистов: "))
print("введите в след формате: <Фамилия> <Имя> <год рождения> <голы>")

arr = []
for i in range(n):
    arr.append(input(f"футболист номер{i+1}: ").split(" "))

max = 0
best_futbolist = 0
for futbolist in arr:
    gols = futbolist[3]
    if gols > max:
        best_futbolist = futbolist


print(best_futbolist, max)
