
'''
    2. *Найдите в Интернете информацию о других свойствах главного окна Toplevel и попробуйте их изменять. 
'''

from simpletk import *
from tkinter.messagebox import askokcancel
  
app = TApplication('Первая форма')
app.position = (100, 300)
app.size = (500, 200)
app.resizable = (True, False)
app.minsize = (100, 200)
# Изменение свойств
app.title = 'Вторая форма'
app.background = 'black'

def AskOnExit(sender):
    if askokcancel('Подтверждение', 'Вы действительно хотите выйти из программы?'):
        app.destroy()

def SwitchColor(sender):
    if app.background == 'black':
        app.background = 'white'
    else:
        app.background = 'black'

# Изменение свойств
app.onDblClick = SwitchColor
app.onCloseQuery = AskOnExit

app.Run()