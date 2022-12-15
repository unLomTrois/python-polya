
from simpletk import *
from tkinter import filedialog

class TImageViewer(TApplication):
  def __init__(self):
    TApplication.__init__(self, "�������� ��������")
    self.position = (200, 200)
    self.size = (300, 300)
    self.panel = TPanel(self, relief="raised", height=35, bd=1)
    self.panel.align = "top"
    self.image = TImage(self, bg="white")
    self.image.align = "client"
    self.openBtn = TButton(self.panel, width=105, text="������� ����")
    self.openBtn.position = (5, 5)
    self.openBtn.onClick = self.selectFile
    self.centerCb = TCheckBox(self.panel,text="� ������")
    self.centerCb.position = (115, 5)
    self.centerCb.onChange = self.cbChanged

  def selectFile(self, sender):
    fname = filedialog.askopenfilename(
       filetypes=[("����� GIF", "*.gif"), 
                  ("��� �����", "*.*")] )
    if fname:
      self.image.picture = fname

  def cbChanged(self, sender):
    self.image.center = sender.checked
    self.image.redrawImage()
  
app = TImageViewer()

app.Run()