# -*- coding: cp1251 -*-

'''
    3. *Используя материалы Интернета, выясните, как можно создать абстрактный класс с помощью модуля ABCMeta.
    Внесите соответствующие изменения в программу. Какой из подходов вам больше нравится? Почему?
'''

# Для выполнения задания была создана копия файла logelement - logelement2, в которой и был применен астрактный класс ABCMeta

from logelement2 import *

elXor = TXor()
elAndNot = TNotAnd()
elOrNot = TNotOr()

print(" A | B | A xor B | not A and B | not A or B");
print("-"*44);
for k in range(2):
    elXor.In1 = bool(k)
    elAndNot.In1 = bool(k)
    elOrNot.In1 = bool(k)
    for l in range(2):
        elXor.In2 = bool(l)
        elAndNot.In2 = bool(l)
        elOrNot.In2 = bool(l)
        print(" {:} | {:} |    {:}    |      {:}      |     {:}     ".format(k, l, int(elXor.Res), int(elAndNot.Res), int(elOrNot.Res)))