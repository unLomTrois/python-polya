# -*- coding: cp1251 -*-

'''
    Соберите всю программу и вычислите 100!. Сколько цифр входит в это число?
'''

mult = 1;
for i in range(2, 101):
    mult *= i;

print('100! =', mult);
print(len(str(mult)), 'digits')