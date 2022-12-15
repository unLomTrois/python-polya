# -*- coding: cp1251 -*-

'''
    4. Разработайте программу для перевода суммы в рублях в другие валюты. 
'''

from simpletk import *

class ConvertorMoneys(TApplication):
    def __init__(self):
        TApplication.__init__(self, 'Конвертор')

        self.position = (300, 200)
        self.size = (250, 125)

        self.desc = TLabel(self, text='Конвертор рублей в другие валюты')
        self.desc.position = (25, 5)


        self.val1 = TLabel(self, text='руб/долл')
        self.val1.position = (25*1, 15*3)

        self.lbl1 = TLabel(self, text='= ')
        self.lbl1.position = (25*7, 15*3)

        self.edit1 = TEdit(self, width = 50)
        self.edit1.position = (25*4, 15*3)

        self.val2 = TLabel(self, text='руб/евро')
        self.val2.position = (25*1, 15*5)

        self.lbl2 = TLabel(self, text='= ')
        self.lbl2.position = (25*7, 15*5)

        self.edit2 = TEdit(self, width = 50)
        self.edit2.position = (25*4, 15*5)


        self.edit1.onChange = self.onChange
        self.edit2.onChange = self.onChange

    def onChange(self, sender):
        dollar = 61
        euro = 63

        try:
            num = float(self.edit1.text)
            self.lbl1.text = '= {:}'.format(round(num/dollar, 4))
        except:
            self.lbl1.text = '= '

        try:
            num = float(self.edit2.text)
            self.lbl2.text = '= {:}'.format(round(num/euro, 4))
        except:
            self.lbl2.text = '= '
    pass

app = ConvertorMoneys()
app.Run()