
'''
    1. Добавьте в иерархию классов элементы «исключающее ИЛИ», «И-НЕ» и «ИЛИ-НЕ».

    доделать, возможно конструкции были не совершенны
'''

import logelement

elXor = logelement.TXor()
elAndNot = logelement.TNotAnd()
elOrNot = logelement.TNotOr()

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
