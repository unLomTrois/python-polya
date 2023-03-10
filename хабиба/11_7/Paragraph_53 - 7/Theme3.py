
from simpletk import *
from tkinter import filedialog


def onChange ( sender ): 
    r = int ( rEdit.text )
    g = int ( gEdit.text )
    b = int ( bEdit.text ) 
    s = "#{:02x}{:02x}{:02x}".format(r, g, b)
    rgbRect.background = s
    rgbLabel.text = s

app = TApplication ( "RGB-кодирование" ) 
app.size = (210, 90) 
app.position = (200, 200) 

f = ( "MS Sans Serif", 12 ) 
lblR = TLabel ( app, text = "R = ", font = f ) 
lblR.position = (5, 5) 
lblG = TLabel ( app, text = "G = ", font = f ) 
lblG.position = (5, 30) 
lblB = TLabel ( app, text = "B = ", font = f ) 
lblB.position = (5, 55)

fc = ( "Courier New", 16, "bold" ) 
rgbLabel = TLabel ( app, text = "#000000", font = fc, fg = "navy" ) 
rgbLabel.position = (100, 5) 
rgbRect = TLabel ( app, text = "", width = 90, height = 40 ) 
rgbRect.position = (105, 35)

rEdit = TEdit ( app, font = f, width = 50 ) 
rEdit.position = (45, 5) 
rEdit.text = "123"
gEdit = TEdit ( app, font = f, width = 50 ) 
gEdit.position = (45, 30) 
gEdit.text = "56"
bEdit = TEdit ( app, font = f, width = 50 ) 
bEdit.text = "80"
bEdit.position = (45, 55)

rEdit.onChange = onChange
gEdit.onChange = onChange
bEdit.onChange = onChange

app.Run()