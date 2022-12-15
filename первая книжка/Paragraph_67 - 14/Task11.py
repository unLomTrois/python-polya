
'''
     *�������� ���������, ������� ������ � ��������� � ��������-������
'''


from random import randint


def isEmpty(arr):
    res = False;

    for row in arr:
        for el in row:
            if el == ' ':
                res = True;

    return res;

# ����������� ������ ������� � ������ �����
def get_rows_string(arr):
    res = [];

    for row in arr:
        s = '';
        for el in row:
            s += el;
        res.append(s);

    return res;

# ����������� ������� ������� � ������ �����
def get_columns_string(arr):
    res = [];

    for i in range(len(arr)):
        s = '';
        for j in range(len(arr[i])):
            s += arr[j][i];
        res.append(s);

    return res;

# ����������� ��������� ������� � ������ �����
def get_diagonals_string(arr):
    res = [];

    text = '';
    for i in range(len(arr)):
        text += arr[i][i];
    res.append(text)

    text = '';
    for i in range(len(arr)):
        text += arr[-i-1][i];
    res.append(text)

    return res;




print('��������-������\n')

A = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']];

end = 0; # 0 - ���� ������������, 1 - ������, 2 - ���������
while isEmpty(A):
    print('*'*10)
    for el in A:
        print(el)

    k, l = map(int, input('������� ���������� ����� ������: ').split())
    if A[k][l] == ' ': A[k][l] = 'x';
    else: continue;

    while True and isEmpty(A):
        k, l = randint(0,2), randint(0,2);
        if A[k][l] == ' ':
            A[k][l] = 'o';
            break;

    for el in get_rows_string(A):
        if el == 'xxx':
            end = 1;
            break;
        if el == 'ooo':
            end = 2;
            break;
    if end != 0: break;

    for el in get_columns_string(A):
        if el == 'xxx':
            end = 1;
            break;
        if el == 'ooo':
            end = 2;
            break;
    if end != 0: break;

    for el in get_diagonals_string(A):
        if el == 'xxx':
            end = 1;
            break;
        if el == 'ooo':
            end = 2;
            break;
    if end != 0: break;

if end == 1:
    print('victory')
else:
    print('lose')