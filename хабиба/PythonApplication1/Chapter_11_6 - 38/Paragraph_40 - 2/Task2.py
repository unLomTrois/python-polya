
'''
    � ���������� ������ �������� ��� ��������� ����� � ���� � ������� �������� �������, �� 
    ���� � ������ ������ ������ ������ �����, ������� ����������� � ����� ���� ����.
'''

path = input('������� ������ ���� � �����:\n> ')
fileIn = input('������� ��� �����:\n> ')
fileOut = 'output.txt'

try:
    D = {}
    for word in open(path + fileIn, 'r'):
        word = word.replace('\n', '')
        D[word] = D.get(word, 0) + 1

    A = []
    for i, k in D.items():
        A.append([i, k])

    for i in range(len(A) - 1):
        for j in range(i, len(A)):
            if A[i][1] < A[j][1]:
                A[i][1], A[j][1] = A[j][1], A[i][1];

    D = {}
    for i in range(len(A)):
        D[A[i][0]] = A[i][1];

    F = open(path + fileOut, 'w')
    for i in D.keys():
        print(i, D[i])
        F.write(i + '\n')
    F.close()

except:
    print('����� ��� � �����:\n ', path+fileIn)