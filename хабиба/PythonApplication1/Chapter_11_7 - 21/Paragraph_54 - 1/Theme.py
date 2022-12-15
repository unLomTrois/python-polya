# -*- coding: cp1251 -*-

from simpletk import *
from int_edit import TIntEdit

app = TApplication('Шестнадцатиричная система')
app.size = (250, 36)
app.position = (200, 200)

f = ('Courier New', 14, 'bold')

hexLabel = TLabel(app, text='?', font=f, fg='navy')
hexLabel.position = (150, 5)

decEdit = TIntEdit(app, width=120, font=f)
decEdit.position = (5, 5)

def onNumChange(sender):
    hexLabel.text = "{:X}".format(sender.value)
decEdit.onChange = onNumChange

app.Run()