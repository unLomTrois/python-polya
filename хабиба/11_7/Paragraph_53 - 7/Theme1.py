
from simpletk import *
from tkinter import filedialog

app = TApplication("Просмотр рисунков")
app.position = (200, 200)
app.size = (300, 300)

panel = TPanel(app, relief="raised", height=35, bd=1)
panel.align = "top"

image = TImage(app, bg="white")
image.align = "client"
#image.picture = "flower.gif"

def selectFile(sender):
  fname = filedialog.askopenfilename(
     filetypes=[("Файлы GIF", "*.gif"), 
                ("Все файлы", "*.*")] )
  if fname:
    image.picture = fname

openBtn = TButton(panel, width=105, text="Открыть файл")
openBtn.position = (5, 5)
openBtn.onClick = selectFile

def cbChanged(sender):
  image.center = sender.checked
  image.redrawImage()
  
centerCb = TCheckBox(panel,text="В центре")
centerCb.position = (115, 5)
centerCb.onChange = cbChanged

app.Run()