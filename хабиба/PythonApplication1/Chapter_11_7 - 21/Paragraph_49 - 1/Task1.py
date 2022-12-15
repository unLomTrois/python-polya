# -*- coding: cp1251 -*-

'''
    Измените построенную ранее программу моделирования движения так, чтобы все поля у объектов были закрытыми. Используйте свойства для доступа к данным
'''

from random import randint


class TRoad:
    def __init__(self):
        self.__length = 0
        self.__width = 0
        self.__SVS = []
        pass
    def __init__(self, length, width):
        self.__length = length if length > 0 else 0
        self.__width = width if width > 0 else 0
        self.__SVS = []
        pass

    def addSvetofor(self, sv):
        self.__SVS.append(sv)
        pass

    def getSvetofor(self, x):
        sv = None
        for el in self.__SVS:
            if x < el.X:
                sv = el
                break
        return sv
        pass

    def __setLength(self, length):
        self.__length = length if length > 0 else 0
        pass

    def __setWidth(self, width):
        self.__length = width if width > 0 else 0
        pass

    length = property(lambda x: x.__length, __setLength)
    width = property(lambda x: x.__width, __setWidth)
    SVS = property(lambda x: x.__SVS)

    pass

class TCar:
    def __init__(self, road, p, v):
        self.__road = road
        self.__P = p
        self.__V = v
        self.__X = 0
        pass

    def move(self):
        sv = self.__road.getSvetofor(self.__X)
        if sv != None:
            color = sv.getColor()
            if self.__X + self.__V > sv.X and color == 'Red':
                print(color)
                self.__X = sv.X
            else:
                self.__X += self.__V
        else:
            self.__X += self.__V

        if self.__X > self.__road.length:
            self.__X = 0
        pass

    def show(self):
        print('-'*(self.__X+1))
        pass

    def __setRoad(self, road):
        self.__road = road
    def __setX(self, X):
        self.__X = X
    def __setV(self, V):
        self.__V = V
    def __setP(self, P):
        self.__P = P

    road = property(lambda x: x.__road, __setRoad)
    P = property(lambda x: x.__P, __setP)
    V = property(lambda x: x.__V, __setV)
    X = property(lambda x: x.__X, __setX)

    pass

class TSvetofor:
    def __init__(self, x, color):
        self.__X = x
        self.__color = color
        pass

    def switch(self):
        self.__color += 1
        pass

    def getColor(self):
        if 0 <= self.__color % 11 < 5: return 'Red'
        if 6 <= self.__color % 11 < 11: return 'Green'
        return 'Yellow'
        pass

    def __setColor(self, color):
        self.__color = color
    def __setX(self, X):
        self.__X = X

    color = property(lambda x: x.__road, __setColor)
    X = property(lambda x: x.__X, __setX)

    pass



road = TRoad(70, 3)

N = 3
cars = [] 
for i in range(N): 
    cars.append(TCar(road, i+1, 2*(i+1)))
svs = []
for i in range(N):
    svs.append(TSvetofor((i+2)**3, randint(1,11)))

for sv in svs:
    road.addSvetofor(sv)

for k in range(100):
    for i in range(N):
        cars[i].move()
        cars[i].show()
    for sv in svs:
            sv.switch()
    print()

print("После 100 шагов:")
for i in range(N): 
    print(cars[i].X)