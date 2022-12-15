# -*- coding: cp1251 -*-

'''
    В телевикторине участнику предлагают выбрать один из трёх закрытых чёрных ящиков, 
    причём известно, что в одном из них – приз, а в двух других – пусто. После этого ведущий 
    открывает один пустой ящик (но не тот, который выбрал участник) и предлагает заново сделать выбор, но уже между двумя оставшимися ящиками. Используя псевдослучайные числа,
    выполните моделирование 1000 раундов этой игры и определите, что выгоднее делать участнику викторины: выбрать тот же ящик, что и в начале игры, или другой
'''

from random import randint

rounds = 1000;
wins_nochoice = 0; # победы с первого раза
wins_choice = 0; # победы со второго раза
first_choice = -1;
for i in range(rounds):
    prize = randint(1,3)

    # выбор одной из 3 коробок
    choice = randint(1,3);
    if i == 0: first_choice = choice;
    opened = -1;
    while True:
        opened = randint(1,3)
        if opened != choice: break;

    # проверка выбора
    if prize == opened:
        wins_nochoice += 1;
        continue;

    # выбор одной из 2 оставшихся коробок
    while True:
        choice = randint(1,3)
        if opened != choice: break;

    # проверка выбора
    if prize == choice:
        wins_choice += 1;

print('Total games:', rounds)
print('Simple wins: ', round(wins_nochoice/rounds*100, 2), '%', sep='')
print('Magic wins: ', round(wins_choice/rounds*100, 2), '%', sep='')
print('first choice =', first_choice)