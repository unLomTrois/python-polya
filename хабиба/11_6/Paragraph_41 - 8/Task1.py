
'''
     �������� ���������, ������� ��������������� ������, ���������� � ����, 
     � ������� �����. ������ ������� ����������.
'''

filePath = input('������� ������ ���� � �����:\n> ')
fileName = input('������� ��� �����:\n> ');

try:
    stack, arr = [], []
    with open(filePath+fileName, 'r') as F:
        while True:
            el = F.readline()
            if not el: break;
            el = el.replace('\n', '')
            stack.append(el)

    F = open(filePath+fileName, 'w')
    while len(stack) > 0:
        F.write(str(stack.pop()) + '\n')
    F.close()


except:
    print('����� ��� � �����:\n ', filePath+fileName)