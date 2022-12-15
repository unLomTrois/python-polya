# -*- coding: cp1251 -*-

'''
    � ������������� ��������� ���������� ������� ���� �� ��� �������� ������ ������, 
    ������ ��������, ��� � ����� �� ��� � ����, � � ���� ������ � �����. ����� ����� ������� 
    ��������� ���� ������ ���� (�� �� ���, ������� ������ ��������) � ���������� ������ ������� �����, �� ��� ����� ����� ����������� �������. ��������� ��������������� �����,
    ��������� ������������� 1000 ������� ���� ���� � ����������, ��� �������� ������ ��������� ���������: ������� ��� �� ����, ��� � � ������ ����, ��� ������
'''

from random import randint

rounds = 1000;
wins_nochoice = 0; # ������ � ������� ����
wins_choice = 0; # ������ �� ������� ����
first_choice = -1;
for i in range(rounds):
    prize = randint(1,3)

    # ����� ����� �� 3 �������
    choice = randint(1,3);
    if i == 0: first_choice = choice;
    opened = -1;
    while True:
        opened = randint(1,3)
        if opened != choice: break;

    # �������� ������
    if prize == opened:
        wins_nochoice += 1;
        continue;

    # ����� ����� �� 2 ���������� �������
    while True:
        choice = randint(1,3)
        if opened != choice: break;

    # �������� ������
    if prize == choice:
        wins_choice += 1;

print('Total games:', rounds)
print('Simple wins: ', round(wins_nochoice/rounds*100, 2), '%', sep='')
print('Magic wins: ', round(wins_choice/rounds*100, 2), '%', sep='')
print('first choice =', first_choice)