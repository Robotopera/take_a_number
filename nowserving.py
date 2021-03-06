#Now Serving Counter
import wx
from random import randrange
from wx.lib.colourdb import *

class Clicker(wx.Frame):
 def __init__(self):
  wx.Frame.__init__(self, None, size=(200,200), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX, title='Now Serving')


  self.hija = Visor(self)
  self.hija.Show()
  #self.p= self.hija.p(self)


  self.Bind(wx.EVT_CLOSE, self.OnExit)


  self.lblname = wx.StaticText(self, label="Starting Number:", pos=(20,30))

  self.sc = wx.SpinCtrl(self, -1, '',  (110, 30), (60, -1))
  self.sc.SetRange(0, 99)
  self.sc.SetValue(0)

  self.sc.Bind(wx.EVT_TEXT_ENTER, self.OnEnter, self.sc)


  self.lblnumb = wx.StaticText(self, pos=(60,110))
  self.lblnumb.SetLabel('00')
  font = wx.Font(40, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
  self.lblnumb.SetFont(font)

  self.button =wx.Button(self, label="&Next", pos=(20, 70),size=(140,-1))
  self.button.SetFocus()


  #evento boton
  self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
  self.Bind(wx.EVT_KEY_DOWN, self.onKeyPress,self.button)


  self.colors = getColourList()
  self.timer = wx.Timer(self)
  self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
  self.timer.Start(1500)
  self.col_num = len(self.colors)


 def OnTimer(self, event):
  self.hija.SetBackgroundColour(wx.RED)
  position = randrange(0, self.col_num-1, 1)
  self.hija.SetBackgroundColour(self.colors[position])
  self.hija.Refresh()


 


 def OnClick(self,event):
  t = int(self.lblnumb.GetLabel())
  self.lblnumb.SetLabel(str(t+1))
  if t == 99:
  	self.lblnumb.SetLabel(str(00))

  num= int(self.lblnumb.GetLabel())
  self.hija.lblnumb.SetLabel(str(num))
 

  #winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)



 def OnEnter(self, event):
 	num = self.sc.GetValue()
 	self.lblnumb.SetLabel(str(num))
 	self.hija.lblnumb.SetLabel(str(num))


 def onKeyPress(self, event):
  keycode = event.GetKeyCode()
  if keycode ==  wx.WXK_SPACE:
  	t = int(self.lblnumb.GetLabel())
  	self.lblnumb.SetLabel(str(t+1))
  	if t == 99:
  		self.lblnumb.SetLabel(str(00))
  	num= int(self.lblnumb.GetLabel())
  	self.hija.lblnumb.SetLabel(str(num))


    
 		
 def OnExit(self,e):
 	#self.Close(True)  # Cerramos el frame
 	#self.hija.Close(True)
 	self.hija.Destroy()
 	self.Destroy()



class Visor(wx.Frame):
 def __init__(self, parent):

  wx.Frame.__init__(self, None, size=(960,900),style=wx.DEFAULT_FRAME_STYLE ^ wx.MINIMIZE_BOX ^ wx.RESIZE_BORDER ^ wx.CLOSE_BOX ^ wx.STAY_ON_TOP, title='Now Serving')
    #wx.MAXIMIZE_BOX
    
  self.panel = wx.Panel(self, -1, style=wx.TRANSPARENT_WINDOW)
  self.panel.SetBackgroundColour("BLACK")
     
  self.l1 = wx.StaticText(parent=self.panel,label = "Now Serving:",pos=(155,5), style = wx.ALIGN_CENTER )
  self.l1.SetForegroundColour((255,255,255))
  font = wx.Font(45, wx.DEFAULT, wx.NORMAL, wx.BOLD)
  self.l1.SetFont(font)
  
  
  self.lblnumb = wx.StaticText(parent=self.panel, label = "",pos=(30,90),style = wx.ALIGN_LEFT) 
  self.lblnumb.SetForegroundColour((255,0,0))
  font1 = wx.Font(500, wx.DEFAULT, wx.NORMAL, wx.BOLD)
  self.lblnumb.SetFont(font1)
    

 def OnExit(self,e):
 	self.Close(True) 


if __name__ == "__main__":

 App=wx.App()
 Clicker().Show()
 updateColourDB()
 App.MainLoop()

