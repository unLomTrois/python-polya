# -*- coding: cp1251 -*-

'''
    7. ������������ ��������� ��� ���������� ��������������� ������ ��������� ����� ��� ���������
    ������������ �����, ������� ������������� � ������� ����������� (����� ��� �� ������).
'''

from simpletk import *

class AudioCalc(TApplication):
    def __init__(self):
        TApplication.__init__(self, '�����������')

        self.position = (300, 200)
        self.size = (350, 200)

        self.desc = TLabel(self, text='���������� ������� �����')
        self.desc.position = (70, 5)

        self.lblH = TLabel(self, text='������������ � �.:')
        self.editH = TEdit(self, width=100)

        self.lblW = TLabel(self, text='������� �������������:')
        self.editW = TEdit(self, width=100)

        self.lblC = TLabel(self, text='������� �����������:')
        self.editC = TEdit(self, width=100)

        self.lblR = TLabel(self, text='���������:')
        self.editR = TEdit(self, width=150)

        self.lblH.position = (25*1, 15*3)
        self.lblW.position = (25*1, 15*5)
        self.lblC.position = (25*1, 15*7)
        self.lblR.position = (25*1, 15*9)

        self.editH.position = (25*7, 15*3)
        self.editW.position = (25*7, 15*5)
        self.editC.position = (25*7, 15*7)
        self.editR.position = (25*7, 15*9)


        self.editH.onChange = self.onChange
        self.editR.onChange = self.onChange
        self.editC.onChange = self.onChange

    def onChange(self, sender):
        try:
            # �������� �������� (google translate) !!!
            t = int(self.editH.text) # time
            F = int(self.editW.text) # sampling frequence
            i = int(self.editC.text) # encoding depth

            self.editR.text = '{:}'.format(t*F*i) # Internet !!!
        except:
            self.editR.text = ''
    pass

app = AudioCalc()
app.Run()