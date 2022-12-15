
'''
    1. Напишите программу для построения RGB-кода цвета в стиле ООП, «убрав» все действия по
    созданию формы в конструктор класса. Обработчики событий также должны быть членами класса. 
'''

from simpletk import *

class RGBColorViewer(TApplication):
    def __init__(self):
        TApplication.__init__(self, 'RGB-кодирование')
        self.size = (210, 90) 
        self.position = (200, 200) 

        self.f = ('MS Sans Serif', 12)
        self.lblR = TLabel(self, text='R = ', font=self.f)
        self.lblR.position = (5, 5) 
        self.lblG = TLabel(self, text='G = ', font=self.f)
        self.lblG.position = (5, 30) 
        self.lblB = TLabel(self, text='B = ', font=self.f)
        self.lblB.position = (5, 55)

        self.fc = ('Courier New', 16, 'bold')
        self.rgbLabel = TLabel(self, text = '#000000', font = self.fc, fg = 'navy')
        self.rgbLabel.position = (100, 5) 
        self.rgbRect = TLabel(self, text = '', width = 90, height = 40)
        self.rgbRect.position = (105, 35)

        self.rEdit = TEdit(self, font = self.f, width = 50)
        self.rEdit.position = (45, 5)
        self.rEdit.text = '123'
        self.gEdit = TEdit(self, font = self.f, width = 50)
        self.gEdit.position = (45, 30) 
        self.gEdit.text = '56'
        self.bEdit = TEdit(self, font = self.f, width = 50)
        self.bEdit.text = '80'
        self.bEdit.position = (45, 55)

        self.rEdit.onChange = self.onChange
        self.gEdit.onChange = self.onChange
        self.bEdit.onChange = self.onChange
        pass

    def onChange(self, sender):
        r = int(self.rEdit.text)
        g = int(self.gEdit.text)
        b = int(self.bEdit.text)
        s = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        self.rgbRect.background = s
        self.rgbLabel.text = s
    pass

app = RGBColorViewer() 
app.Run()