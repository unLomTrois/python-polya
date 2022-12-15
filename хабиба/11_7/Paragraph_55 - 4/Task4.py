
'''
	4. Постройте программу «Калькулятор» для выполнения вычислений с целыми числами (см. рисунок). 
'''

from simpletk import *
from model4 import Calc

class TCalculator(TApplication):
	def __init__(self):
		TApplication.__init__(self, 'Калькулятор')

		f = ('Courier New', 12)

		self.size = (160, 192)

		self.disp = TEdit(self, width=145, font=f)
		self.disp.position = (8, 8)

		bNames = ['7', '8', '9', 'C', 
		   '4', '5', '6', '/',
		   '1', '2', '3', '*', 
		   '0', '=', '+', '-']
		btn = []
		for r in range(4):
			for c in range(4):
				k = 4*r + c
				btn.append(TButton(self, text=bNames[k], font=f, width=2))
				btn[k].position = (8+38*c, 40+38*r)
				btn[k].size = (30,30)

		btn[3]['fg'] = 'red'
		for k in [0, 1, 2, 4, 5, 6, 8, 9, 10, 12]:
			btn[k].onClick = self.doDigit

		for k in [7, 11, 14, 15]:
			btn[k].onClick = self.doOperation

		btn[13].onClick = self.doCalc
		btn[3].onClick = self.doClear
		pass
	
	def doClear(self, sender):
		self.disp.text = ''

	def doCalc(self, sender):
		text = self.disp.text

		for s in text:
			if s not in '0123456789.+-*/() ':
				print('Ошибка! Некорректное выражение')
				return

		# проверка на целостность скобок
		cs, ce = 0, 0
		for d in text:
			if d == '(': cs+=1
			if d == ')': ce+=1
		if cs != ce:
			print('Ошибка! Не хватает скобок')
			return None

		# проверка на лишние операции
		if text[0] in '+-*/' or text[-1] in '+-*/':
			print('Ошибка! Лишние операции')
			return

		for i in range(len(text)-1):
			if text[i] in '+-*/' and text[i+1] in '+-*/':
				print('Ошибка! Подряд идущие знаки ' + text[i])
				return

		x = Calc(text)
		self.disp.text = str(x)
		pass
	
	def doOperation(self, sender):
		self.disp.text += str(sender['text'])
	
	def doDigit ( self, sender ):
		self.disp.text += sender['text']

app = TCalculator()
app.Run()