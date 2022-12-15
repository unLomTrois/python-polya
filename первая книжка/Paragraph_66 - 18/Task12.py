# -*- coding: cp1251 -*-

'''
    В условиях предыдущей задачи выведите в алфавитном порядке фамилии и имена всех 
    футболистов, которые забили хотя бы один гол. В списке не более 100 футболистов.
'''

print('Вам нужно сперва ввести кол-во вводимых данных, а после вводить данные в формате: <Фамилия> <Имя> <год рождения> <голы>\n')

n = int(input('enter number of footballers: '))
A = [];
for i in range(n):
    A.append(input(f'{i+1} - ').split());

B = [];
i = 1;
for data in A:
    if i == 100: break;

    if int(data[3]) > 0:
        B.append(data);
    i += 1;

# сортировка по фамилиям и именам
for k in range(len(B)):
    for l in range(k+1, len(B)):
        if B[k][0] > B[l][0] or B[k][0] == B[l][0] and B[k][1] > B[l][1]:
            B[k], B[l] = B[l], B[k];

i = 1;
for data in B:
    print(f'{i}. ', data[0], data[1])
    i += 1;