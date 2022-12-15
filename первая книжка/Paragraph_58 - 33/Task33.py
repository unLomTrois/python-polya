
'''
    Ввести натуральное число N и вывести значение числа 1/N, выделив период дроби. Например, 1/2=0,5 или 1/7=0,(142857).
'''

num = int(input('enter number: '))
 
rems = [] # remainders
rem = 1 # remainder
numS = '' # result calculating

# вычисление ответа
while not (rem in rems):
    rems.append(rem)
    numS += str(rem // num)
    rem = (rem % num) * 10

# нахождение начала периода, для его выделения в строке
start_pos = 0
for i in rems:
    if i == rem:
        break
    start_pos += 1

# выделение перода
numS = '{:}.{:}({:})'.format(numS[0:1], numS[1:start_pos], numS[start_pos:])

print(1, '/', num, '=', numS)