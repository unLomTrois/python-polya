
'''
    6. Разработайте программу для вычисления информационного объема рисунка по его размерам и количеству цветов в палитре. 
'''

from simpletk import *

class PictCalc(TApplication):
    def __init__(self):
        TApplication.__init__(self, 'Калькулятор')

        self.position = (300, 200)
        self.size = (300, 200)

        self.desc = TLabel(self, text='Вычисление размера фотки')
        self.desc.position = (70, 5)

        self.lblH = TLabel(self, text='height:')
        self.editH = TEdit(self, width=100)

        self.lblW = TLabel(self, text='width:')
        self.editW = TEdit(self, width=100)

        self.lblC = TLabel(self, text='кол-во цветов:')
        self.editC = TEdit(self, width=100)

        self.lblR = TLabel(self, text='Результат:')
        self.editR = TEdit(self, width=150)

        self.lblH.position = (25*1, 15*3)
        self.lblW.position = (25*1, 15*5)
        self.lblC.position = (25*1, 15*7)
        self.lblR.position = (25*1, 15*9)

        self.editH.position = (25*5, 15*3)
        self.editW.position = (25*5, 15*5)
        self.editC.position = (25*5, 15*7)
        self.editR.position = (25*5, 15*9)


        self.editH.onChange = self.onChange
        self.editR.onChange = self.onChange
        self.editC.onChange = self.onChange

    def onChange(self, sender):
        try:
            height = int(self.editH.text)
            width = int(self.editW.text)
            count = int(self.editC.text)

            self.editR.text = '{:}'.format(height*width*count)
        except:
            self.editR.text = ''
    pass

app = PictCalc()
app.Run()