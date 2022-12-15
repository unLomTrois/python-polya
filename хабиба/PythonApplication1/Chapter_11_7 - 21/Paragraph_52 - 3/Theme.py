
from simpletk import *

app = TApplication('Первая форма')
app.Run()

app.position = (100, 300)
app.size = (500, 200)
app.resizable = (True, False)
app.minsize = (100, 200)
