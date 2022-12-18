
'''
     . �������� ���������, ������� ��������� ������, � ����� ������� ������������ �� �����, 
       ������������� � ������� ��������� ���.
'''

from random import randint


def Sort(A):
    i = 0;
    while i < len(A)-1:
        j = i + 1;
        while j < len(A):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i];
            j+=1;
        i+=1;

    return A;


A = [randint(1,10) for x in range(30)];
print('before:', A);

A = Sort(A);
count = 1;
for i in range(len(A)-1, 0, -1):
    if A[i] == A[i-1]:
        count+=1;
    else:
        break;

print('after: ', A);
print(count);