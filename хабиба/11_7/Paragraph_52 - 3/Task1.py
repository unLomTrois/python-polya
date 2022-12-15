
'''
    1. Постройте программу с запросом разрешения на завершение работы. Попробуйте изменять свойства главного окна. 
'''

from simpletk import *
from tkinter.messagebox import askokcancel
  
app = TApplication('Первая форма')
app.position = (100, 300)
app.size = (500, 200)
app.resizable = (True, False)
app.minsize = (100, 200)

def AskOnExit(sender):
    if askokcancel('Подтверждение', 'Вы действительно хотите выйти из программы?'):
        app.destroy()

app.onCloseQuery = AskOnExit

app.Run()