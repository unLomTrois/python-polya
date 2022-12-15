
'''
    В предыдущей задаче выведите все найденные слова в файл в порядке убывания частоты, то 
    есть в начале списка должны стоять слова, которые встречаются в файле чаще всех.
'''

path = input('введите полный путь к файлу:\n> ')
fileIn = input('введите имя файла:\n> ')
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
    print('Файла нет в папке:\n ', path+fileIn)