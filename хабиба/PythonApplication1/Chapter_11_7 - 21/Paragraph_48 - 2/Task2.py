
'''
    2. *Добавьте в модель светофор, который переключается автоматически по программе (например, 5 с горит красный свет, затем 1 с – жёлтый, потом 5 с – зеленый и т.д.). Измените
    классы так, чтобы машина запрашивала у объекта Дорога местоположение ближайшего светофора, а затем обращалась к светофору для того, чтобы узнать, какой сигнал горит. Машины
    должны останавливаться у светофора с запрещающим сигналом.
'''

from random import randint


class TRoad:
    def __init__(self):
        self.length = 0
        self.width = 0
        self.SVS = []
        pass
    def __init__(self, length, width):
        self.length = length if length > 0 else 0
        self.width = width if width > 0 else 0
        self.SVS = []
        pass

    def addSvetofor(self, sv):
        self.SVS.append(sv)
        pass

    def getSvetofor(self, x):
        sv = None
        for el in self.SVS:
            if x < el.X:
                sv = el
                break
        return sv
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
        sv = self.road.getSvetofor(self.X)
        if sv != None:
            color = sv.getColor()
            if self.X + self.V > sv.X and color == 'Red':
                print(color)
                self.X = sv.X
            else:
                self.X += self.V
        else:
            self.X += self.V

        if self.X > self.road.length:
            self.X = 0
        pass

    def show(self):
        print('-'*(self.X+1))
        pass

    pass

class TSvetofor:
    def __init__(self, x, color):
        self.X = x
        self.color = color
        pass

    def switch(self):
        self.color += 1
        pass

    def getColor(self):
        if 0 <= self.color % 12 < 5: return 'Red'
        if 6 <= self.color % 12 < 11: return 'Green'
        return 'Yellow'
        pass

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