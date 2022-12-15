  # -*- coding: cp1251 -*-

'''
    3. *Найдите в Интернете информацию о других стандартных диалогах, входящих в модуль messagebox. Попробуйте их использовать. 
'''

from simpletk import *
from tkinter.messagebox import *
  
app = TApplication('Первая форма')
app.title = 'Вторая форма'
app.position = (100, 300)
app.size = (500, 200)
app.resizable = (True, False)
app.minsize = (100, 200)
app.background = 'black'

def AskOnExit(sender):
    if askokcancel('Подтверждение', 'Вы действительно хотите выйти из программы?'):
        app.destroy()

def SwitchColor(sender):
    # Применение нового диалога
    if askyesno('Переключение цвета', 'Хотите переключить цвет фона?'):
        if app.background == 'black':
            app.background = 'white'
        else:
            app.background = 'black'

app.onDblClick = SwitchColor
app.onCloseQuery = AskOnExit

app.Run()