# -*- coding: cp1251 -*-

print("Поиск максимального и минимального числа из 5-ти введенных чисел..\n");

n1, n2, n3, n4, n5 = map(int, input("введите пять чисел через пробел (a b c d e): ").split());

print();

if   n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5: print("min =", n1);
elif n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5: print("min =", n2);
elif n3 < n1 and n3 < n2 and n3 < n4 and n3 < n5: print("min =", n3);
elif n4 < n1 and n4 < n2 and n4 < n3 and n4 < n5: print("min =", n4);
else:                                             print("min =", n5);

if   n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5: print("max =", n1);
elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5: print("max =", n2);
elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5: print("max =", n3);
elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5: print("max =", n4);
else:                                             print("max =", n5);
