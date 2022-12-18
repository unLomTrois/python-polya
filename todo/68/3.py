"""
    3. В файле в столбик записаны целые числа. Напишите программу, которая определяет длину 
    самой длинной цепочки идущих подряд одинаковых чисел и выводит результат в другой файл. 

"""

path = "D:/Колледж/4 курс/Панфилов - ПП/Сентябрь/CH10_8/PythonApplication1/Chapter_8/Paragraph_68/"
txt1name, txt2name = "input.txt", "output.txt"

nums = []
for numS in open(path + txt1name):
    nums.append(int(numS))

# начало считывания значений
maxCount, count = 1, 1
# maxCount - максимальное кол-во, count - текущая кол-во
for i in range(1, len(nums)):
    if nums[i - 1] == nums[i]:
        count += 1
    else:
        if count >= maxCount:
            maxCount = count
        count = 1
if count > maxCount:
    maxCount = count
# конец считывания значений

with open(path + txt2name, "w") as f:
    f.write("length = {:}\n".format(maxCount))
