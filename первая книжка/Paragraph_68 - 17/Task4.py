
'''
    4. В файле записаны в столбик целые числа. Отсортировать их по возрастанию последней цифры и записать в другой файл.
'''

# возвращает последнюю цифру переданного числа
def get_last_digit(num):
    return int(str(num)[-1]);


path = 'D:/Колледж/4 курс/Панфилов - ПП/Сентябрь/CH10_8/PythonApplication1/Chapter_8/Paragraph_68/';
txt1name, txt2name = 'input.txt', 'output.txt';

nums = [];
for numS in open(path + txt1name):
    nums.append(int(numS))

# начало считывания значений
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if get_last_digit(nums[i]) > get_last_digit(nums[j]):
            nums[i], nums[j] = nums[j], nums[i];
    
# конец считывания значений

with open(path + txt2name, 'w') as f:
    for num in nums:
        f.write('{:}\n'.format(num));