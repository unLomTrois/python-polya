
import math;

print("����������� ���������� ����� ��������� ������� � ��������� ������������\n");

x1, y1 = map(float, input("������� ���������� 1-�� ����� (x y): ").split());
x2, y2 = map(float, input("������� ���������� 2-�� ����� (x y): ").split());

a = math.sqrt((x2-x1)**2 + (y2-y1)**2);
print("\n{:.3f}".format(a));


