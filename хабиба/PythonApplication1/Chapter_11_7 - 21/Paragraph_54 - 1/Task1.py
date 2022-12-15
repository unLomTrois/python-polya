# -*- coding: cp1251 -*-

'''
    1. Разработайте компонент, который позволяет вводить шестнадцатеричные числа. 
'''

# компонент был создан в файле int_edit.py

from simpletk import *
from int_edit import THexIntEdit

def toDec(numHex, res=0, i=0):
	if i == 0:
		numHex = numHex[-1:0:-1] + numHex[0]

	numHex = numHex.upper()

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

app = TApplication('Шестнадцатиричная система')
app.size = (250, 36)
app.position = (200, 200)

f = ('Courier New', 14, 'bold')

hexLabel = TLabel(app, text='?', font=f, fg='navy')
hexLabel.position = (150, 5)

decEdit = THexIntEdit(app, width=120, font=f)
decEdit.position = (5, 5)

def onNumChange(sender):
	try:
		hexLabel.text = "{:}".format(toDec(sender.value))
	except:
		hexLabel.text = '0'

decEdit.onChange = onNumChange

app.Run()