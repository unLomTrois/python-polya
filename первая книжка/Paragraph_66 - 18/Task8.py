
'''
     �������� �������, ������� �������� � ����� ����� ���������� �� �������� (��������, 
    �� '.bak'). ������� ��������� ��� ���������: ��� ����� � ����� ����������. ������, 
    ��� � �������� ����� ���������� ����� ���� ������.
'''

text = input('enter file name: ');
extension = input('enter file extension: ');
res = '';

if text.find('.') != -1:
    txts = text.split('.');
    for i in range(len(txts)-1):
        res += f'{txts[i]}.';

    if extension.find('.') != -1:
        res += extension[1:len(extension)];
    else:
        res += extension;
else:
    if extension.find('.') != -1:
        res = text + extension;
    else:
        res = text + '.' + extension;

print(res);