
'''
    �������� ����������� ��������� ��� �������� ����� � ����������������� ������� ���������.
'''

# ���������� ����� � 16-�� ������� ���������
def toHex(num):
    res = ''
    if num >= 16:
        res += toHex(num // 16);

    s = num % 16;
    if   s == 15: res += 'F';
    elif s == 14: res += 'E';
    elif s == 13: res += 'D';
    elif s == 12: res += 'C';
    elif s == 11: res += 'B';
    elif s == 10: res += 'A';
    else: res += str(num);

    return res;

N = int(input("������� ����� --> "));

print(toHex(N));
