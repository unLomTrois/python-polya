
'''
    1. Измените программу так, чтобы она вычисляла выражения с вещественными
    числами (для перевода вещественных чисел из символьного вида в числовой используйте функцию float). 
'''

from simpletk import *
from model1 import Calc

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
  x = Calc(expr)
  Answers.insert(0, expr+"="+str(x))
  if not Input.findItem(expr):
    Input.addItem(expr)
    
Input.bind('<Key-Return>', doCalc)
  
app.Run()