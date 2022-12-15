# -*- coding: cp1251 -*-

import math;

print("Калькулятор расстояния между заданными точками в двумерном пространстве\n");

x1, y1 = map(float, input("введите координаты 1-ой точки (x y): ").split());
x2, y2 = map(float, input("введите координаты 2-ой точки (x y): ").split());

a = math.sqrt((x2-x1)**2 + (y2-y1)**2);
print("\n{:.3f}".format(a));


