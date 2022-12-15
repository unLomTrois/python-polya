"""
Соболева П.
ПКС-1
4 курс

В телевикторине участнику предлагают выбрать один из трёх закрытых чёрных ящиков, причём известно, что в одном из них – приз, а в двух других – пусто.
После этого ведущий открывает один пустой ящик (но не тот, который выбрал участник) и предлагает заново сделать выбор,но уже между двумя оставшимися ящиками.
Используя псевдослучайные числа, выполните моделирование 1000 раундов этой игры и определите, 
что выгоднее делать участнику викторины: выбрать тот же ящик, что и в начале игры, или другой
"""

import random

player_change_box = bool(
    int(input("игрок поменяет ящик? (0 - нет, 1 - да): ")))

rounds = 1000
win_count = 0

for round in range(rounds):

    # массив ящиков
    boxes = [0, 0, 0]

    # номер выигрышного ящика
    win_box = random.randint(0, 2)

    # добавляем в ящики выигрышный ящик
    boxes[win_box] = 1

    # выбор игрока
    player_choice = random.randint(0, 2)
    # print("игрок выбрал ящик номер", player_choice)

    # ведущий открывает один пустой ящик
    empty_box = 0
    for i in range(len(boxes)):
        # выбирается ящик, который точно пустой, и который не выбрал игрок
        if player_choice != i and boxes[i] == 0:
            empty_box = i
            break

    # print("ящик номер", empty_box, "пуст!")
    # print("будет ли игрок менять ящик?")

    # если игрок поменяет ящик
    if player_change_box:
        # print("да, буду")
        for i in range(len(boxes)):
            if i != empty_box and i != player_choice:
                player_choice = i
                # print("игрок выбрал ящик номер", player_choice)
                break
    # else:
        # print("нет, не буду")

    # print("правильный ответ!", win_box)
    if player_choice == win_box:
        win_count += 1
        # print("игрок победил!")

    # print(win_box, player_choice)

# если игрок меняет ящик, то он чаще выигрывает
print("шанс побед:", f"{win_count/rounds * 100}%")
