from view import * 
import view as vw  

from model import * 
import model as md  

from controller import * 
import controller as ctlr 

from tkinter import * 
from tkinter.ttk import *

import tkinter as tk 
import tkinter.ttk as ttk 

class App(tk.Tk):
	def __init__(self,*args,**kwargs):
		super().__init__()
		global delcolumnEntry
		delcolumnEntry = None
		def initiating():
			self.bgcolor = "#404040"
			self.geometry("500x500+300+100")
			self.configure(bg=self.bgcolor)
			self.title("Project Management System")
		initiating()
		v = vw.View(self)
		v.grid(row=0,column=0,padx=10,pady=10) 
		m = md.Model(self)
		c = ctlr.Controller(self)
		

if __name__ == "__main__":
	app = App()
	app.mainloop()


