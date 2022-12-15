a = int(input("print number (a): "));
b = int(input("print number (b): "));

c = a;
a = b;
b = c;

print(f"\na = {a}\nb = {b}");