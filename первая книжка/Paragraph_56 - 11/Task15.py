
import random;

print("Вывод 5 случайный вещественных чисел в полуинтервале между указанными числами a и b (a < b)..\n");

a = float(input("введите a: "));
b = float(input("введите b: "));

print("\nn1", a + random.random() * (b - a));
print("n2", a + random.random() * (b - a));
print("n3", a + random.random() * (b - a));
print("n4", a + random.random() * (b - a));
print("n5", a + random.random() * (b - a));