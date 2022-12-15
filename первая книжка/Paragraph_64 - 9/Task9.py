
'''
     *�������� ���������, ������� ���������� ���������� ������������ ��� ���������� ������ � 
     ���� �� ������� ������� ��������. ��������� ������������ ��� ������������ ������������������ 
     (��� ���������������), ��������� (��������������� � �������� �������) � ���������.
'''


from random import randint


# ��������� ������ ������� ��������. direct - ����������� ���������� (> and <)
def bubble_sort(arr, direct):
    count = 0;
    l = len(arr); # l - ����� �������

    if direct == '<':
        for i in range(l):
            for j in range(l-i-1):
                if arr[j+1] < arr[j]: 
                    arr[j], arr[j+1] = arr[j+1], arr[j];
                    count += 1;
    else:
        for i in range(l):
            for j in range(l-i-1):
                if arr[j+1] > arr[j]: 
                    arr[j], arr[j+1] = arr[j+1], arr[j];
                    count += 1;

    return count;

# ��������� ������ ������� ���������� ����������. direct - ����������� ���������� (> and <) 
def selection_sort(arr, direct):
    count = 0;
    l = len(arr); # l - ����� �������

    if direct == '<':
        for i in range(l-1):
            nMin = i;
            for j in range(i+1,l):
                if arr[j] < arr[nMin]:
                    nMin = j;
                if i!= nMin:
                    arr[i], arr[nMin] = arr[nMin], arr[i];
                    count += 1;
    else:
        for i in range(l-1):
            nMin = i;
            for j in range(i+1,l):
                if arr[j] > arr[nMin]:
                    nMin = j;
                if i!= nMin:
                    arr[i], arr[nMin] = arr[nMin], arr[i];
                    count += 1;

    return count;

# ��������� ���������� ������ ������� ������� ����������. direct - ����������� ���������� (> and <) (��� ����, ����� ������������� ���� ������, ����� ������� ��� ��������� ���: qSort (A,0,N-1) )
def quick_sort(arr, nStart, nEnd, direct):
    count = 0;

    if nStart >= nEnd: return count;

    L = nStart; R = nEnd;
    X = arr[(L+R)//2];
    while L <= R:
        while arr[L] < X: L += 1;
        while arr[R] > X: R -= 1;
        if L <= R:
            arr[L], arr[R] = arr[R], arr[L];
            L += 1; R -= 1;
            count += 1;

    count += quick_sort(arr, nStart, R, direct);
    count += quick_sort(arr, L, nEnd, direct);

    return count;

    



A = [x for x in range(10,100,2)];
B = [x for x in range(98,8,-2)];
C = [randint(1,10) for x in range(30)];

print(' arrays for sort:', '\n1 - ', A, '\n2 - ', B, '\n3 - ', C );


# ������������ �������� ������� ��������
print('\n', 'bubble sort:');
Acopy = A.copy();
Bcopy = B.copy();
Ccopy = C.copy();
print(' -> asc sort');
counterA = bubble_sort(Acopy, '>');
counterB = bubble_sort(Bcopy, '>');
counterC = bubble_sort(Ccopy, '>');
print(f' array 1: {counterA} ������������\n array 2: {counterB} ������������\n array 3: {counterC} ������������');
Acopy = A.copy();
Bcopy = B.copy();
Ccopy = C.copy();
print(' -> desc sort');
counterA = bubble_sort(Acopy, '<');
counterB = bubble_sort(Bcopy, '<');
counterC = bubble_sort(Ccopy, '<');
print(f' array 1: {counterA} ������������\n array 2: {counterB} ������������\n array 3: {counterC} ������������');
#****************************


# ������������ �������� ������� �������
print('\n', 'selection sort:');
Acopy = A.copy();
Bcopy = B.copy();
Ccopy = C.copy();
print(' -> asc sort');
counterA = selection_sort(Acopy, '>');
counterB = selection_sort(Bcopy, '>');
counterC = selection_sort(Ccopy, '>');
print(f' array 1: {counterA} ������������\n array 2: {counterB} ������������\n array 3: {counterC} ������������');
Acopy = A.copy();
Bcopy = B.copy();
Ccopy = C.copy();
print(' -> desc sort');
counterA = selection_sort(Acopy, '<');
counterB = selection_sort(Bcopy, '<');
counterC = selection_sort(Ccopy, '<');
print(f' array 1: {counterA} ������������\n array 2: {counterB} ������������\n array 3: {counterC} ������������');
#****************************


# ������������ �������� ������� ������� ����������
print('\n', 'quick sort:');
Acopy = A.copy();
Bcopy = B.copy();
Ccopy = C.copy();
print(' -> asc sort');
counterA = quick_sort(Acopy, 0, len(A)-1, '>');
counterB = quick_sort(Bcopy, 0, len(B)-1, '>');
counterC = quick_sort(Ccopy, 0, len(C)-1, '>');
print(f' array 1: {counterA} ������������\n array 2: {counterB} ������������\n array 3: {counterC} ������������');
Acopy = A.copy();
Bcopy = B.copy();
Ccopy = C.copy();
print(' -> desc sort');
counterA = quick_sort(Acopy, 0, len(A)-1, '<');
counterB = quick_sort(Bcopy, 0, len(B)-1, '<');
counterC = quick_sort(Ccopy, 0, len(C)-1, '<');
print(f' array 1: {counterA} ������������\n array 2: {counterB} ������������\n array 3: {counterC} ������������');
#****************************
