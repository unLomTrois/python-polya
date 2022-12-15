# -*- coding: cp1251 -*-

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

    pass

road = TRoad(60, 3)

N = 3
cars = [] 
for i in range(N): 
    cars.append ( TCar(road, i+1, 2*(i+1)) )

for k in range(100): # 100 шагов
    for i in range(N): # для каждой машины
        cars[i].move()

print("После 100 шагов:")
for i in range(N): 
    print(cars[i].X)