# -*- coding: cp1251 -*-

import random;

print("Вывод 5 случайный целых чисел в интервале между указанными числами a и b (a < b)..\n");

a = int(input("введите a: "));
b = int(input("введите b: "));

print("\nn1 = ", random.randint(a, b));
print("n2 = ", random.randint(a, b));
print("n3 = ", random.randint(a, b));
print("n4 = ", random.randint(a, b));
print("n5 = ", random.randint(a, b));