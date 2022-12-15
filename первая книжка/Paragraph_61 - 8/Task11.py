
'''
	�������� ����������� ��������� ��� �������� ����� �� ����������������� ������� ��������� � ����������.
'''

# ���������� ����� � 16-�� ������� ���������
def toHex(num):
	res = ''
	if num >= 16:
		res += toHex(num // 16);

	s = num % 16;
	if   s == 15: res += 'F';
	elif s == 14: res += 'E';
	elif s == 13: res += 'D';
	elif s == 12: res += 'C';
	elif s == 11: res += 'B';
	elif s == 10: res += 'A';
	else: res += str(num);

	return res;

def toDec(numHex, res=0, i=0):
	if i == 0:
		numHex = numHex[-1:0:-1] + numHex[0]

	if len(numHex) != i:
		mult = 0;

		if   numHex[i] == 'F': mult = 15;
		elif numHex[i] == 'E': mult = 14;
		elif numHex[i] == 'D': mult = 13;
		elif numHex[i] == 'C': mult = 12;
		elif numHex[i] == 'B': mult = 11;
		elif numHex[i] == 'A': mult = 10;
		else:				   mult = int(numHex[i]);

		mult = mult * (16**i)

		res += toDec(numHex, res, i+1) + mult;

	return res


num = int(input("������� ����� --> "));

numHex = toHex(num)
print('to hex from dec:', numHex)
num = toDec(numHex)
print('to dec from hex:', num)

