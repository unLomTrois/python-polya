
'''
     �������� ����������� ��������� ��� �������� ����� �� �������� ������� ��������� � ����������.
'''


# ��������� �������� ����� ���� 10001 � ���������� (��� ���� int)
def toDec(num, res =- 1):
    if num == 0:
        return 0
    res += 1
    return (num % 10) * (1 << res) + toDec(num // 10, res)

print(toDec(1000));