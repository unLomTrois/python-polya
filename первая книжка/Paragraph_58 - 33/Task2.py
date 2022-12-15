
print("Произведение чисел без оператора умножения..\n");

a = int(input("1-е число: "));
b = int(input("2-е число: "));

_sum = 0;
i = 0;

if a < 0 and b > 0 or a > 0 and b > 0:
    while i < b:
        _sum += a;
        i += 1;
elif a < 0 and b < 0:
    while i < -b:
        _sum -= a;
        i += 1;
else:
    while i < -b:
        _sum += a;
        i += 1;

print("sum =", _sum);