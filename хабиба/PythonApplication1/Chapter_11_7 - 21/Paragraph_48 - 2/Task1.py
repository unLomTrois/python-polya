# -*- coding: cp1251 -*-

'''
    1. Добавьте в программу операторы, позволяющие изобразить на экране перемещение машин
    (в текстовом или графическом режиме). Подумайте, какие методы можно добавить для этого в класс TCar. 
'''

class TRoad:
    def __init__(self):
        self.length = 0
        self.width = 0
        pass
    def __init__(self, length, width):
        self.length = length if length > 0 else 0
        self.width = width if width > 0 else 0
        pass

    pass

class TCar:
    def __init__(self, road, p, v):
        self.road = road
        self.P = p
        self.V = v
        self.X = 0
        pass

    def move(self):
        self.X += self.V
        if self.X > self.road.length:
            self.X = 0
        pass

    def show(self):
        print('-'*(self.X+1))
        pass

    pass

road = TRoad(60, 3)

N = 3
cars = [] 
for i in range(N): 
    cars.append ( TCar(road, i+1, 2*(i+1)) )

for k in range(100): # 100 шагов
    for i in range(N): # для каждой машины
        cars[i].move()
        cars[i].show()
    print()

print("После 100 шагов:")
for i in range(N): 
    print(cars[i].X)