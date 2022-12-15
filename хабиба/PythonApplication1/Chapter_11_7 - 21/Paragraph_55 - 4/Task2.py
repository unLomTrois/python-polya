# -*- coding: cp1251 -*-

'''
    2. Добавьте в программу обработку ошибок. Подумайте, какие ошибки может
    сделать пользователь. Какие ошибки могут возникнуть при вычислениях? 
    Как их обработать? 
'''

from simpletk import *
from model2 import Calc

app = TApplication("Калькулятор")
app.size = (300, 150)

Input = TComboBox(app, values=[], height=1)
Input.align = "top"
Input.text = "2+2"
Input.position = (10, 10)
Input.size = (280, 30)

Answers = TListBox(app, values=[])
Answers.align = "client"
Answers.position = (10, 50)
Answers.size = (280, 90)

def doCalc(event):
	expr = Input.text

	for s in expr:
		if s not in '0123456789.+-*/ ':
			return

	# проверка на лишние операции
	if expr[0] in '+-*/' or expr[-1] in '+-*/':
		print('Ошибка! Лишние операции')
		return

	for i in range(len(expr)-1):
		if expr[i] in '+-*/' and expr[i+1] in '+-*/':
			print('Ошибка! Подряд идущие знаки ' + expr[i])
			return

	x = Calc(expr)
	Answers.insert(0, expr+"="+str(x))
	if not Input.findItem(expr):
		Input.addItem(expr)
    
Input.bind('<Key-Return>', doCalc)
  
app.Run()