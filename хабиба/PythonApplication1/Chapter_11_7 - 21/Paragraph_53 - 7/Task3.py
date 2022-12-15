
'''
    3. Разработайте программу для решения системы двух линейных уравнений. Обратите внимание на обработку ошибок при вычислениях. 
'''

from simpletk import *
import numpy

def obrabotka(s1, s2):
    s1 = s1.replace(' ', '')
    s2 = s2.replace(' ', '')

    i1op = s1.find('+')
    if i1op == -1:
        i1op = s1.find('-')
    i1e = s1.find('=')

    i2op = s2.find('+')
    if i2op == -1:
        i2op = s2.find('-')
    i2e = s2.find('=')

    num11 = float(s1[:i1op-1])
    num12 = float(s1[i1op:i1e-1])
    num13 = float(s1[i1e+1:])

    num21 = float(s2[:i2op-1])
    num22 = float(s2[i2op:i2e-1])
    num23 = float(s2[i2e+1:])

    return [[num11, num12], [num21, num22]], [num13, num23]

def calc(arr1, arr2):
    M1 = numpy.array(arr1)
    V1 = numpy.array(arr2)
    nparr = numpy.linalg.solve(M1, V1)

    return [nparr[0], nparr[1]]

class ConvertorMiles(TApplication):
    def __init__(self):
        TApplication.__init__(self, 'Калькулятор')

        self.position = (300, 200)
        self.size = (350, 150)

        self.desc = TLabel(self, text='Калькулятор системы линейных уравнений')
        self.desc.position = (50, 10)

        self.edit1 = TEdit(self, width=95)
        self.edit1.position = (25*1, 15*3)

        self.edit2 = TEdit(self, width=95)
        self.edit2.position = (25*1, 15*5)

        self.btnCalc = TButton(self, text='Вычислить')
        self.btnCalc.position = (35*1, 15*7)

        self.lblRes = TLabel(self, text='Вводите в формате:\n2x + 5y = 1\n1x - 10y = 3\nДоступные операции: +-\nИспользуйте имена: x и y\nв таком же порядке')
        self.lblRes.position = (25*7, 15*2.5)

        self.btnCalc.onClick = self.onClick
        self.edit1.focus_set()

    def onClick(self, sender):
        try:
            s1 = self.edit1.text
            s2 = self.edit2.text

            M1, V1 = obrabotka(s1, s2)
            res = calc(M1, V1)

            self.lblRes.text = 'Result:\nx={:}\ny={:}'.format(res[0], res[1])
        except:
            self.lblRes.text = 'Result: None'
    pass

app = ConvertorMiles()
app.Run()