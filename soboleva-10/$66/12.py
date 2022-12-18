"""
Соболева ПКС-1
В условиях предыдущей задачи выведите в алфавитном порядке фамилии и имена всех 
футболистов, которые забили хотя бы один гол. В списке не более 100 футболистов.
"""

n = int(input("введите количество футболистов: "))
print("введите в след формате: <Фамилия> <Имя> <год рождения> <голы>")

arr = []
for i in range(n):
    arr.append(input(f"футболист номер{i+1}: ").split(" "))

sorted = []
i = 1
for data in arr:
    if i == 100:
        break

    if int(data[3]) > 0:
        sorted.append(data)
    i += 1

# сортировка по фамилиям и именам
for k in range(len(sorted)):
    for l in range(k + 1, len(sorted)):
        if (
            sorted[k][0] > sorted[l][0]
            or sorted[k][0] == sorted[l][0]
            and sorted[k][1] > sorted[l][1]
        ):
            sorted[k], sorted[l] = sorted[l], sorted[k]

i = 1
for data in sorted:
    print(f"{i}. ", data[0], data[1])
    i += 1
