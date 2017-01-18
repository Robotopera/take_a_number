# -*- coding: utf-8 -*-
# vetx.py
try:
	import wx
except ImportError:
    raise ImportError,"Se requiere el modulo wxPython"

class ArmaTurno(wx.Frame):
    def __init__(self):
    	wx.Frame.__init__(self, None, size=(200,200), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX, title='Ve el Turno')
        

        self.hija = Visor(self)
        self.hija.Show()

        self.Bind(wx.EVT_CLOSE, self.OnExit)


        self.lblname = wx.StaticText(self, label="Ingrese Turno:", pos=(20,30))

        self.sc = wx.SpinCtrl(self, -1, '',  (110, 30), (60, -1))
        self.sc.SetRange(0, 99)
        self.sc.SetValue(0)

        self.sc.Bind(wx.EVT_TEXT_ENTER, self.OnEnter, self.sc)


        self.lblnumb = wx.StaticText(self, pos=(60,110))
        self.lblnumb.SetLabel('00')
        font = wx.Font(40, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.lblnumb.SetFont(font)

        self.button =wx.Button(self, label="&Turno", pos=(20, 70),size=(140,-1))
        self.button.SetFocus()


        #evento boton
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)


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

 		
    def OnExit(self,e):
    	#self.Close(True)  # Cerramos el frame
    	#self.hija.Close(True)
    	self.hija.Destroy()
    	self.Destroy()



class Visor(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, None, size=(350,350),style=wx.DEFAULT_FRAME_STYLE ^ wx.MINIMIZE_BOX ^ wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER ^ wx.CLOSE_BOX , title='Visor de Turno')
        self.parent = parent
      


        self.lblnumb = wx.StaticText(self, pos=(20,100))
        font = wx.Font(200, wx.DECORATIVE, wx.ITALIC, wx.BOLD)
        self.lblnumb.SetFont(font)
           

    def OnExit(self,e):
    	self.Close(True) 


if __name__ == "__main__":

    App=wx.PySimpleApp()
    ArmaTurno().Show()
    App.MainLoop()

