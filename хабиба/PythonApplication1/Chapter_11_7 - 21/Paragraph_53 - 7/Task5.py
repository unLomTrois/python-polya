# -*- coding: cp1251 -*-

'''
    5. Разработайте программу для перевода чисел из десятичной системы в двоичную, восьмеричную и шестнадцатеричную. 
'''

from simpletk import *

class ConvertorHumbers(TApplication):
    def __init__(self):
        TApplication.__init__(self, 'Конвертор')

        self.position = (300, 200)
        self.size = (250, 200)

        self.desc = TLabel(self, text='Конвертор чисел')
        self.desc.position = (70, 5)

        self.lbl10 = TLabel(self, text='10-я:        ->')
        self.edit10 = TEdit(self, width=100)

        self.lbl2 = TLabel(self, text='2-я:')
        self.edit2 = TEdit(self, width=100)

        self.lbl8 = TLabel(self, text='8-я:')
        self.edit8 = TEdit(self, width=100)

        self.lbl16 = TLabel(self, text='16-я:')
        self.edit16 = TEdit(self, width=100)

        self.lbl10.position = (25*1, 15*3)
        self.edit10.position = (25*4, 15*3)

        self.lbl2.position = (25*1, 15*5)
        self.edit2.position = (25*4, 15*5)

        self.lbl8.position = (25*1, 15*7)
        self.edit8.position = (25*4, 15*7)

        self.lbl16.position = (25*1, 15*9)
        self.edit16.position = (25*4, 15*9)
        
        self.edit10.onChange = self.onChange

    def onChange(self, sender):
        try:
            num = int(self.edit10.text)

            self.edit2.text = '{:0b}'.format(num)
            self.edit8.text = '{:0o}'.format(num)
            self.edit16.text = '{:0x}'.format(num)
        except:
            self.edit2.text = ''
            self.edit8.text = ''
            self.edit16.text = ''
    pass

app = ConvertorHumbers()
app.Run()