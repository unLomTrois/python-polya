
'''
    Опишите структуру, в которой хранится информация о
    а) видеозаписи;
    б) сотруднике фирмы «Рога и Копыта»;
    в) самолёте;
    г) породистой собаке.
'''

import pickle


class Heap1:
    video = ''
    employee = ''
    plane = ''
    dog = ''
    pass


a = Heap1();
a.video = 'supervideo.mp3'
a.employee = 'Egor'
a.plane = 'Airplane of agent Kingsman'
a.dog = 'Bulldog'

print(a.video)
print(a.employee)
print(a.plane)
print(a.dog)