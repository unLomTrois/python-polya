
'''
    2. ������������ ��������� ��� �������� ������� ����� � ��������� (1 ���� = 1852 �). 
'''

from simpletk import *

class ConvertorMiles(TApplication):
    def __init__(self):
        TApplication.__init__(self, '���������')

        self.position = (300, 200)
        self.size = (250, 150)

        self.desc = TLabel(self, text='��������� ������� �����')
        self.desc.position = (45, 5)

        self.lbl = TLabel(self, text='= ')
        self.lbl.position = (25*6, 15*4)

        self.edit = TEdit(self, width = 50)
        self.edit.position = (25*3, 15*4)
        self.edit.onChange = self.onChange
        self.edit.focus_set()

    def onChange(self, sender):
        try:
            num = float(self.edit.text)
            self.lbl.text = '= {:}'.format(round(num*1.852, 4))
        except:
            self.lbl.text = '= '
    pass

app = ConvertorMiles()
app.Run()