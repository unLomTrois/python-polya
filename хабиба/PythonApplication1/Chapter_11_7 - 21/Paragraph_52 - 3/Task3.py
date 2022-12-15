  # -*- coding: cp1251 -*-

'''
    3. *������� � ��������� ���������� � ������ ����������� ��������, �������� � ������ messagebox. ���������� �� ������������. 
'''

from simpletk import *
from tkinter.messagebox import *
  
app = TApplication('������ �����')
app.title = '������ �����'
app.position = (100, 300)
app.size = (500, 200)
app.resizable = (True, False)
app.minsize = (100, 200)
app.background = 'black'

def AskOnExit(sender):
    if askokcancel('�������������', '�� ������������� ������ ����� �� ���������?'):
        app.destroy()

def SwitchColor(sender):
    # ���������� ������ �������
    if askyesno('������������ �����', '������ ����������� ���� ����?'):
        if app.background == 'black':
            app.background = 'white'
        else:
            app.background = 'black'

app.onDblClick = SwitchColor
app.onCloseQuery = AskOnExit

app.Run()