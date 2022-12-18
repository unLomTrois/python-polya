"""
Соболева ПКС-1
Введите массив с клавиатуры и найдите (за один проход) количество элементов, имеющих максимальное значение.
"""

arr = []
arr_len = int(input("введите количество элементов массива: "))

for i in range(arr_len):
    arr.append(int(input(f"введите {i+1}-й элемент: ")))

max = arr[0]  # предполагаем максимальный элемент
counter = 0  # счетчик

for num in arr:
    if num > max:
        max = num
        counter = 0
    if num == max:
        counter += 1

print("максимальное число:", max, "встречено:", counter, "раз")
