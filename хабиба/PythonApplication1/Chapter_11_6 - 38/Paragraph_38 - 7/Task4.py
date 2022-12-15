
'''
    �������� ��� ��������� � ��������� 100!. ������� ���� ������ � ��� �����?
'''

mult = 1;
for i in range(2, 101):
    mult *= i;

print('100! =', mult);
print(len(str(mult)), 'digits')