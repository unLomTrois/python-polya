
'''
    �������� ���������, ������� ������ ����������� ����� a � b � ������� ��� ������� ����� 
    � ��������� �� a �� b.
'''

print('����� ���� ������ ����� � ��������� ���������..\n');

a = int(input("print a --> "));
b = int(input("print b --> "));

while a <= b:
    i = 2;
    _log = True;
    while i < a // 2:
        if(a % i == 0):
           _log = False;
           break;
        i+=1;

    if _log: print(a);

    a+=1;
