
class TPen:
    def __init__(self):
        self.__color = 0
        pass

    def __setColor(self, newColor):
        self.__color = int(newColor, 16) if len(newColor) == 6 else 0
        pass

    def __getColor(self):
        return '{:06x}'.format(self.__color)

    color = property(__getColor, __setColor)

    pass

class TCar:
    def __init__(self):
        self.__v = 0
        pass

    v = property(lambda x: x.__v)

pen = TPen()
pen.color = 'FFAA00'
print(pen.color)