
'''
    Объединение задач 19 и 20 + подсчет итераций циклов
'''


n1, n2 = map(int, input("введите числа (a и b): ").split()); # n - number | nc - number copy
nc1, nc2 = n1, n2;

c1 = 0; # count НОД
while nc1 != 0 and nc2 != 0:
    if nc1 > nc2:
        nc1 -= nc2;
    else:
        nc2 -= nc1
    c1+=1;
print("НОД =", nc1+nc2, "|", c1, " итераций (обычный алгоритм)");

nc1, nc2 = n1, n2;

c2 = 0; # count мод НОД
while nc1 != 0 and nc2 != 0:
    if nc1 > nc2:
        nc1 %= nc2;
    else:
        nc2 %= nc1
    c2+=1;
print("НОД =", nc1+nc2, "|", c2, " итераций (модифицированный алгоритм)");