
'''
    ��������� ���������� ��������� ���, ����� ��� ���������� ����� ���������� ������� � ������.
'''

s = input('������� ������ � ����������, �������������� �������:\n> ')

L = "([{<"
R = ")]}>"

stack = []
err = False;

i = 0
for c in s:
    if c in L:
        stack.append(c)
    p = R.find(c)
    if p >= 0:
        if not stack: err = True;
        else:
            top = stack.pop()
            if p!= L.find(top):
                err = True
    if err:
        print('������:', i+1, '��������')
        break
    i+=1
if len(stack) > 0: err = True
if err:
    print('�� ������� �������������(����) ������ � ����� |', not err)
else:
    print(not err);