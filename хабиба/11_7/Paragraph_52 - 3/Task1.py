
'''
    1. ��������� ��������� � �������� ���������� �� ���������� ������. ���������� �������� �������� �������� ����. 
'''

from simpletk import *
from tkinter.messagebox import askokcancel
  
app = TApplication('������ �����')
app.position = (100, 300)
app.size = (500, 200)
app.resizable = (True, False)
app.minsize = (100, 200)

def AskOnExit(sender):
    if askokcancel('�������������', '�� ������������� ������ ����� �� ���������?'):
        app.destroy()

app.onCloseQuery = AskOnExit

app.Run()