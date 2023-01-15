from controller import *
import controller as ctlr

from tkinter import * 
from tkinter.ttk import *  
from tkinter.messagebox import * 

import tkinter as tk 
import tkinter.ttk as ttk  
import tkinter.messagebox as mb 

class View(tk.Frame):
	def __init__(self,parent,*args):
		super().__init__()

		self.bgcolor = parent.bgcolor
		self.fgcolor = "cyan"
		self.entrybgcolor = "#1D2228"
		self.configure(bg=parent.bgcolor)
		
		def default_databases_creater():
			ctlr.Controller.default_databases_creater()

		def login():
			username = tk.Label(self,text="Username",fg=self.fgcolor,bg=self.bgcolor)
			password = tk.Label(self,text="Password",fg=self.fgcolor,bg=self.bgcolor)
			level = tk.Label(self,text="Level",fg="cyan",bg=self.bgcolor)
			
			self.username_entry = tk.Entry(self,width=15,fg=self.fgcolor,bg=self.entrybgcolor,border=None)
			self.password_entry = tk.Entry(self,width=15,fg=self.fgcolor,bg=self.entrybgcolor,show="*",border=None)
			value = ctlr.Controller._logincombobox()
			value_ = ["supervisor","leader","crew"]
			self.level_entry = ttk.Combobox(self,width=14,values=value_,state="readonly")
			self.level_entry.current(0)

			username.grid(row=0,column=0,padx=20,pady=20,sticky=W)
			password.grid(row=1,column=0,padx=20,pady=20,sticky=W)
			level.grid(row=2,column=0,padx=20,pady=20,sticky=W)

			self.username_entry.grid(row=0,column=1,padx=20,pady=20,sticky=W)
			self.password_entry.grid(row=1,column=1,padx=20,pady=20,sticky=W)
			self.level_entry.grid(row=2,column=1,padx=20,pady=20,sticky=W)

			button = tk.Button(self,text="Login",bg="#1D2228",fg="cyan",border=0,command=logincheck)
			button.grid(row=3,column=0,padx=20,pady=20)

		def _quit():
			try:
				parent.win.destroy()
				parent.win.quit()
				parent.destroy()
				parent.quit()
			except Exception:
				parent.destroy()
				parent.quit()
			

		def _logout():
			destory_loginpage()
			login()

		def adjust_workspace():
			fx = self.winfo_width()
			fy = self.winfo_height()
			wx = parent.winfo_width()
			wy = parent.winfo_height()
			ffx = wx/2.5 - fx/2.5
			ffy = wy/2.5 - fy/2.5
			self.place(x=ffx,y=ffy)

		def adjust_workspace2():
			fy = self.winfo_height()
			wy = parent.winfo_height()
			ffy = wy/8 - fy/8
			self.place(x=10,y=ffy)

		def _hidedb():
			for i in self.winfo_children():
				i.destroy()
				adminpage() 

		def _createdb():
			self.set_dbname = self.e1
			if ctlr.Controller._createdb(self.set_dbname.get()):
					_showdb()

		def _createcol():
			self.set_colname = self.cole1.get()
			self.choose_dbname = self.temp2
			if ctlr.Controller._createcol(self.set_colname,self.choose_dbname):
				_usedb()
				#_showcol(self.showtemp,self.temp2)
#for teacher createcol==============================================================================================================


		def _teacher_createcol():
			self.set_colname = self.cole1.get()
			self.choose_dbname = self.db
			if ctlr.Controller._teacher_createcol(self.set_colname,self.choose_dbname):
				_teacher_usedb()
			print(self.set_colname)


#for admin retrievedoc============================================================================================================
		def _retrievedoc():
			self.delcolumnEntry = None
			self.recol = self.cole2.get()
			self.choose_dbname = self.temp2
			self.keyList = ctlr.Controller._retrievedoc(self.recol,self.choose_dbname)[0]
			self.doc = ctlr.Controller._retrievedoc(self.recol,self.choose_dbname)[1]
			parent.win = tk.Tk()
			parent.win.title(self.recol)
			parent.win.geometry("{}x{}+400+100".format(parent.winfo_width(),parent.winfo_height()))
			parent.tview = ttk.Treeview(parent.win)
			parent.tview['columns'] = (self.keyList)
			parent.tview.column('#0',width=0,stretch=NO)
			parent.tview.heading('#0',text='',anchor=CENTER)
			number = len(self.keyList)
			for i in range(number):
				parent.tview.column(self.keyList[i],anchor=CENTER,width=100)
				parent.tview.heading(self.keyList[i],text=self.keyList[i],anchor=CENTER)
			List = []
			for data in self.doc:
				for v in data.values():
					List.append(v)
				parent.tview.insert('', tk.END, values=List[1:])
				print(List)
				#List = []
				#print(List[1:])
				List = []
			def item_selected(event):
				for wiget in parent.win.winfo_children():
						if hasattr(wiget,"get"):
							if wiget != parent.win.winfo_children()[1]:
								wiget.delete(0,END)
				for selected_item in parent.tview.selection():
					item = parent.tview.item(selected_item)
					record = item['values']
					showinfo(title='Information', message=','.join(str(record)))
					counter = 0
					lenrecord = len(record) -1
					for wiget in parent.win.winfo_children():
						if hasattr(wiget,"get"):
							if counter <= lenrecord:
								if wiget != parent.win.winfo_children()[1]:
									wiget.insert(counter,record[counter])
									counter += 1

							
			parent.tview.bind('<<TreeviewSelect>>', item_selected)
			parent.tview.grid(row=0,column=0,padx=10,pady=10)


			vsb = ttk.Scrollbar(parent.win, orient="vertical", command=parent.tview.yview)
			vsb.grid(row=0,column=1,padx=0,pady=10,sticky=N+S+W)
			parent.tview.configure(yscrollcommand=vsb.set)

			def table_inputfield():
				j = 0
				for i in self.keyList:
					parent.win.label = tk.Label(parent.win,text=i,fg="cyan",bg=self.bgcolor,font=('Terminal',12,'bold'))
					parent.win.label.grid(row=j,column=2,padx=10,pady=10,sticky=W)
					parent.win.entry = tk.Entry(parent.win,width=10,fg="cyan",bg="#1D2228",font=('Terminal',12,'bold'))
					parent.win.entry.grid(row=j,column=3,padx=10,pady=10,sticky=W) 
					parent.win.jj = j + 1
					j += 1
					parent.tview.grid(rowspan=j)
					vsb.grid(rowspan=j)
					#print(parent.win.jj)
			table_inputfield()
			def _refresh_win():
				parent.win.destroy()
				_retrievedoc()

			def _insertDoc():
				if ctlr.Controller._insertDoc(self.recol,self.choose_dbname,parent.win):
					_refresh_win()

			def _updateDoc():
				if ctlr.Controller._updateDoc(self.recol,self.choose_dbname,parent.win):
					_refresh_win()
			def _deleteDoc():
				if ctlr.Controller._deleteDoc(self.recol,self.choose_dbname,parent.win):
					_refresh_win()

			def _delcolumn():
				if ctlr.Controller._delcolumn(self.recol,self.choose_dbname,self.delcolumnEntry.get()):
					_refresh_win()
				
			def _addcolumn():
				if ctlr.Controller._addcolumn(self.recol,self.choose_dbname,self.addcolumnEntry.get()):
					_refresh_win()
				
				#_refresh_win()
			def _delcolumnCombobox():
				List = ctlr.Controller._delcolumnCombobox(self.recol,self.choose_dbname,parent.win)
				return List

			parent.win.insertDoc = tk.Button(parent.win,text="Insert Doc",fg="cyan",bg="#1D2228",font=('Terminal',12,'bold'),command=_insertDoc)
			parent.win.insertDoc.grid(row=parent.win.jj,column=1,padx=10,pady=10,sticky="nesw")
			parent.win.updateDoc = tk.Button(parent.win,text="Update Doc",fg="cyan",bg="#1D2228",font=('Terminal',12,'bold'),command=_updateDoc)
			parent.win.updateDoc.grid(row=parent.win.jj+1,column=1,padx=10,pady=10,sticky="nesw")
			parent.win.deleteDoc = tk.Button(parent.win,text="Delete Doc",fg="cyan",bg="#1D2228",font=('Terminal',12,'bold'),command=_deleteDoc)
			parent.win.deleteDoc.grid(row=parent.win.jj+2,column=1,padx=10,pady=10,sticky="nesw")
			parent.win.delcolumn = tk.Button(parent.win,text="Delete Column",fg="cyan",bg="#1D2228",font=('Terminal',12,'bold'),command=_delcolumn)
			parent.win.delcolumn.grid(row=parent.win.jj+3,column=1,padx=10,pady=10,sticky="nesw")
			value = _delcolumnCombobox()
			parent.win.delcolumnEntry = ttk.Combobox(parent.win,width=12,values=value,state="readonly")
			parent.win.delcolumnEntry.current(0)
			self.delcolumnEntry = parent.win.delcolumnEntry
			parent.win.delcolumnEntry.grid(row=parent.win.jj+3,column=2,padx=10,pady=10,sticky=W)
			parent.win.addcolumn = tk.Button(parent.win,text="Add Column",fg="cyan",bg="#1D2228",font=('Terminal',12,'bold'),command=_addcolumn)
			parent.win.addcolumn.grid(row=parent.win.jj+4,column=1,padx=10,pady=10,sticky="nesw")
			parent.win.addcolumnEntry = tk.Entry(parent.win,width=10,fg="cyan",bg="#1D2228",font=('Terminal',12,'bold'))
			parent.win.addcolumnEntry.grid(row=parent.win.jj+4,column=2,padx=10,pady=10,sticky=W)
			self.addcolumnEntry = parent.win.addcolumnEntry
			parent.win.configure(bg=self.bgcolor)
			parent.win.mainloop()

#for admin delecol=================================================================================================================
		
		def _deletecol():
			self.delcol = self.cole2.get()
			self.choose_dbname = self.temp2
			if ctlr.Controller._deletecol(self.delcol,self.choose_dbname):
				#_showcol(self.delcol,self.choose_dbname)
				_usedb()
#for student retrievedoc =======================================================================================================

		def _student_retrievedoc():
			self.delcolumnEntry = None
			self.recol = self.cole2.get()
			u = self.u 
			p = self.p 
			l = self.l 
			
			self.stuid = ctlr.Controller._student_id(self.u,self.p,self.l) 
			self.choose_dbname = ctlr.Controller._student_db(self.recol,self.stuid)
			#self.keyList = 
			collection = ctlr.Controller._student_retrievedoc(self.recol,self.stuid)
			if collection is not False:
				col = collection
			elif collection is False:
				col = {"id":"none","database":"wrong","collection":"wrong"}
			self.keyList = []
			if col is None:
				ctlr.Controller._none_collection_err()
			for key in col:
				if key != "_id":
					self.keyList.append(key)
			

			self.doc = ctlr.Controller._student_retrievedoc_data(self.recol,self.stuid)
			#print(self.stuid)
			#print(self.keyList)
			#print(self.doc)
			parent.win = tk.Tk()
			parent.win.title(self.recol)
			parent.win.geometry("{}x{}+400+100".format(parent.winfo_width(),parent.winfo_height()))
			parent.tview = ttk.Treeview(parent.win)
			
			parent.tview['columns'] = (self.keyList)
			parent.tview.column('#0',width=0,stretch=NO)
			parent.tview.heading('#0',text='',anchor=CENTER)
			number = len(self.keyList)
			print(number)
			print(self.keyList)
			#print(self.keyList)
			#print(self.recol)
			#print(self.cole2.get())
			#print(self.choose_dbname)
			#print(self.db)
			for i in range(number):
				parent.tview.column(self.keyList[i],anchor=CENTER,width=100)
				parent.tview.heading(self.keyList[i],text=self.keyList[i],anchor=CENTER)
			List = []
			
			for data in self.doc:
				for v in data.values():
					List.append(v)
				parent.tview.insert('', tk.END, values=List[1:])
				#print(List)
				#List = []
				#print(List[1:])
				List = []
			def item_selected(event):
				for wiget in parent.win.winfo_children():
						if hasattr(wiget,"get"):
							if wiget != parent.win.winfo_children()[1]:
								wiget.delete(0,END)
								#print(wiget)
				for selected_item in parent.tview.selection():
					item = parent.tview.item(selected_item)
					record = item['values']
					showinfo(title='Information', message=','.join(str(record)))
					counter = 0
					lenrecord = len(record) -1
					for wiget in parent.win.winfo_children():
						if hasattr(wiget,"get"):
							if counter <= lenrecord:
								if wiget != parent.win.winfo_children()[1]:
									wiget.insert(counter,record[counter])
									counter += 1

						
			parent.tview.bind('<<TreeviewSelect>>', item_selected)
		
			parent.tview.grid(row=0,column=0,padx=10,pady=10)

			vsb = ttk.Scrollbar(parent.win, orient="vertical", command=parent.tview.yview)
			vsb.grid(row=0,column=1,padx=0,pady=10,sticky=N+S+W)
			parent.tview.configure(yscrollcommand=vsb.set)


			
			def table_inputfield():
				j = 0
				for i in self.keyList:
					parent.win.label = tk.Label(parent.win,text=i,fg="cyan",bg=self.bgcolor,font=('Terminal',12,'bold'))
					parent.win.label.grid(row=j,column=2,padx=10,pady=10,sticky=W)
					parent.win.entry = tk.Entry(parent.win,width=10,fg="cyan",bg="#1D2228",font=('Terminal',12,'bold'))
					parent.win.entry.grid(row=j,column=3,padx=10,pady=10,sticky=W) 
					parent.win.jj = j + 1
					j += 1
					parent.tview.grid(rowspan=j)
					vsb.grid(rowspan=j)
					#print(parent.win.jj)
			table_inputfield()
			
			def _student_refresh_win():
				parent.win.destroy()
				_student_retrievedoc()

			def _student_insertDoc():
				if ctlr.Controller._student_insertDoc(self.recol,self.stuid,parent.win):
					_student_refresh_win()

			def _student_updateDoc():
				if ctlr.Controller._student_updateDoc(self.recol,self.stuid,parent.win):
					_student_refresh_win()
			
			def _student_deleteDoc():
				if ctlr.Controller._student_deleteDoc(self.recol,self.stuid,parent.win):
					_student_refresh_win()


			parent.win.insertDoc = tk.Button(parent.win,text="Insert Doc",fg="cyan",bg="#1D2228",font=('Terminal',12,'bold'),command=_student_insertDoc)
			parent.win.insertDoc.grid(row=parent.win.jj,column=1,padx=10,pady=10,sticky="nesw")
			parent.win.updateDoc = tk.Button(parent.win,text="Update Doc",fg="cyan",bg="#1D2228",font=('Terminal',12,'bold'),command=_student_updateDoc)
			parent.win.updateDoc.grid(row=parent.win.jj+1,column=1,padx=10,pady=10,sticky="nesw")
			parent.win.deleteDoc = tk.Button(parent.win,text="Delete Doc",fg="cyan",bg="#1D2228",font=('Terminal',12,'bold'),command=_student_deleteDoc)
			parent.win.deleteDoc.grid(row=parent.win.jj+2,column=1,padx=10,pady=10,sticky="nesw")
			"""parent.win.delcolumn = tk.Button(parent.win,text="Delete Column",fg="cyan",bg="#1D2228",font=('Terminal',12,'bold'),command=_teacher_delcolumn)
			parent.win.delcolumn.grid(row=parent.win.jj+3,column=1,padx=10,pady=10,sticky="nesw")
			value = _teacher_delcolumnCombobox()
			parent.win.delcolumnEntry = ttk.Combobox(parent.win,width=12,values=value,state="readonly")
			parent.win.delcolumnEntry.current(0)
			self.delcolumnEntry = parent.win.delcolumnEntry
			parent.win.delcolumnEntry.grid(row=parent.win.jj+3,column=2,padx=10,pady=10,sticky=W)
			parent.win.addcolumn = tk.Button(parent.win,text="Add Column",fg="cyan",bg="#1D2228",font=('Terminal',12,'bold'),command=_teacher_addcolumn)
			parent.win.addcolumn.grid(row=parent.win.jj+4,column=1,padx=10,pady=10,sticky="nesw")
			parent.win.addcolumnEntry = tk.Entry(parent.win,width=10,fg="cyan",bg="#1D2228",font=('Terminal',12,'bold'))
			parent.win.addcolumnEntry.grid(row=parent.win.jj+4,column=2,padx=10,pady=10,sticky=W)
			
			self.addcolumnEntry = parent.win.addcolumnEntry 
			"""



			parent.win.configure(bg=self.bgcolor)
			parent.win.mainloop()


#for teacher retrievedoc ==========================================================================================================

		def _teacher_retrievedoc():
			self.delcolumnEntry = None
			self.recol = self.cole2.get()
			self.choose_dbname = self.db
			self.keyList = ctlr.Controller._teacher_retrievedoc(self.recol,self.choose_dbname)
			self.doc = ctlr.Controller._teacher_retrievedoc_data(self.recol,self.choose_dbname)
			parent.win = tk.Tk()
			parent.win.title(self.recol)
			parent.win.geometry("{}x{}+400+100".format(parent.winfo_width(),parent.winfo_height()))
			parent.tview = ttk.Treeview(parent.win)
			parent.tview['columns'] = (self.keyList)
			parent.tview.column('#0',width=0,stretch=NO)
			parent.tview.heading('#0',text='',anchor=CENTER)
			number = len(self.keyList)
			print(self.keyList)
			#print(self.keyList)
			#print(self.recol)
			#print(self.cole2.get())
			#print(self.choose_dbname)
			#print(self.db)
			for i in range(number):
				parent.tview.column(self.keyList[i],anchor=CENTER,width=100)
				parent.tview.heading(self.keyList[i],text=self.keyList[i],anchor=CENTER)
			List = []
			for data in self.doc:
				for v in data.values():
					List.append(v)
				parent.tview.insert('', tk.END, values=List[1:])
				print(List)
				#List = []
				#print(List[1:])
				List = []
			def item_selected(event):
				for wiget in parent.win.winfo_children():
						if hasattr(wiget,"get"):
							if wiget is not parent.win.winfo_children()[1]:
								wiget.delete(0,END)
				for selected_item in parent.tview.selection():
					item = parent.tview.item(selected_item)
					record = item['values']
					showinfo(title='Information', message=','.join(str(record)))
					counter = 0
					lenrecord = len(record) -1
					for wiget in parent.win.winfo_children():
						if hasattr(wiget,"get"):
							if counter <= lenrecord:
								if wiget != parent.win.winfo_children()[1]:
									wiget.insert(counter,record[counter])
									counter += 1

							
			parent.tview.bind('<<TreeviewSelect>>', item_selected)
			parent.tview.grid(row=0,column=0,padx=10,pady=10)
			vsb = ttk.Scrollbar(parent.win, orient="vertical", command=parent.tview.yview)
			vsb.grid(row=0,column=1,padx=0,pady=10,sticky=N+S+W)
			parent.tview.configure(yscrollcommand=vsb.set)
			def table_inputfield():
				j = 0
				for i in self.keyList:
					parent.win.label = tk.Label(parent.win,text=i,fg="cyan",bg=self.bgcolor,font=('Terminal',12,'bold'))
					parent.win.label.grid(row=j,column=2,padx=10,pady=10,sticky=W)
					parent.win.entry = tk.Entry(parent.win,width=10,fg="cyan",bg="#1D2228",font=('Terminal',12,'bold'))
					parent.win.entry.grid(row=j,column=3,padx=10,pady=10,sticky=W) 
					parent.win.jj = j + 1
					j += 1
					parent.tview.grid(rowspan=j)
					vsb.grid(rowspan=j)
					#print(parent.win.jj)
			table_inputfield()
			
			def _teacher_refresh_win():
				parent.win.destroy()
				_teacher_retrievedoc()

			def _teacher_insertDoc():
				if ctlr.Controller._teacher_insertDoc(self.recol,self.choose_dbname,parent.win):
					_teacher_refresh_win()

			def _teacher_updateDoc():
				if ctlr.Controller._teacher_updateDoc(self.recol,self.choose_dbname,parent.win):
					_teacher_refresh_win()
			
			def _teacher_deleteDoc():
				if ctlr.Controller._teacher_deleteDoc(self.recol,self.choose_dbname,parent.win):
					_teacher_refresh_win()

			def _teacher_delcolumn():
				if ctlr.Controller._teacher_delcolumn(self.recol,self.choose_dbname,self.delcolumnEntry.get()):
					_teacher_refresh_win()
				
			def _teacher_addcolumn():
				if ctlr.Controller._teacher_addcolumn(self.recol,self.choose_dbname,self.addcolumnEntry.get()):
					_teacher_refresh_win()
				
				#_refresh_win()
			def _teacher_delcolumnCombobox():
				List = ctlr.Controller._teacher_delcolumnCombobox(self.recol,self.choose_dbname,parent.win)
				return List 

			parent.win.insertDoc = tk.Button(parent.win,text="Insert Doc",fg="cyan",bg="#1D2228",font=('Terminal',12,'bold'),command=_teacher_insertDoc)
			parent.win.insertDoc.grid(row=parent.win.jj,column=1,padx=10,pady=10,sticky="nesw")
			parent.win.updateDoc = tk.Button(parent.win,text="Update Doc",fg="cyan",bg="#1D2228",font=('Terminal',12,'bold'),command=_teacher_updateDoc)
			parent.win.updateDoc.grid(row=parent.win.jj+1,column=1,padx=10,pady=10,sticky="nesw")
			parent.win.deleteDoc = tk.Button(parent.win,text="Delete Doc",fg="cyan",bg="#1D2228",font=('Terminal',12,'bold'),command=_teacher_deleteDoc)
			parent.win.deleteDoc.grid(row=parent.win.jj+2,column=1,padx=10,pady=10,sticky="nesw")
			parent.win.delcolumn = tk.Button(parent.win,text="Delete Column",fg="cyan",bg="#1D2228",font=('Terminal',12,'bold'),command=_teacher_delcolumn)
			parent.win.delcolumn.grid(row=parent.win.jj+3,column=1,padx=10,pady=10,sticky="nesw")
			value = _teacher_delcolumnCombobox()
			parent.win.delcolumnEntry = ttk.Combobox(parent.win,width=12,values=value,state="readonly")
			parent.win.delcolumnEntry.current(0)
			self.delcolumnEntry = parent.win.delcolumnEntry
			parent.win.delcolumnEntry.grid(row=parent.win.jj+3,column=2,padx=10,pady=10,sticky=W)
			parent.win.addcolumn = tk.Button(parent.win,text="Add Column",fg="cyan",bg="#1D2228",font=('Terminal',12,'bold'),command=_teacher_addcolumn)
			parent.win.addcolumn.grid(row=parent.win.jj+4,column=1,padx=10,pady=10,sticky="nesw")
			parent.win.addcolumnEntry = tk.Entry(parent.win,width=10,fg="cyan",bg="#1D2228",font=('Terminal',12,'bold'))
			parent.win.addcolumnEntry.grid(row=parent.win.jj+4,column=2,padx=10,pady=10,sticky=W)
			self.addcolumnEntry = parent.win.addcolumnEntry
			



			parent.win.configure(bg=self.bgcolor)
			parent.win.mainloop()
#for teacher deletecol=======================================================================================================
		def _teacher_deletecol():
			self.delcol = self.cole2.get()
			self.choose_dbname = self.db
			if ctlr.Controller._teacher_deletecol(self.delcol,self.choose_dbname):
				_teacher_usedb()
			else:
				print("no drop")

#for admin showcol=================================================================================================================

		def _showcol(temp,temp2):
			#self.showtemp = temp #for refresh
			self.temp2 = temp2
			collection = temp[0]
			style = ttk.Style(self)
			style.theme_use('clam')
			style.configure('Treeview',background="#1D2228",fieldbackground="#1D2228",foreground="white",font=('Terminal',9,'bold'))
			style.configure('Treeview.Heading',background="#1D2228",font=('Terminal',12,'bold'),foreground="cyan")
			self.tv = ttk.Treeview(self)
			self.tv['columns'] = ("Collection_Name")
			self.tv.column('#0', width=0, stretch=NO)
			self.tv.column('Collection_Name', anchor=CENTER, width=160)
			self.tv.heading('#0',text='',anchor=CENTER)
			self.tv.heading('Collection_Name',text="Collection_Name",anchor=CENTER)
			List = []
			for name in collection:
				List.append(name)
				self.tv.insert('',tk.END,values=List)
				List = []
			def item_selected(event):
				for selected_item in self.tv.selection():
					item = self.tv.item(selected_item)
					record = item['values']
					#showinfo(title='Information', message=','.join(record))
			self.tv.bind('<<TreeviewSelect>>', item_selected)
			self.tv.grid(row=1,column=4,padx=10,pady=10,rowspan=5,sticky='nesw')
			self.l1 = tk.Label(self,text="Set Collection Name",bg=self.bgcolor,fg="cyan")
			self.l2 = tk.Label(self,text="Choose Collection",bg=self.bgcolor,fg="cyan")
			self.cole1 = tk.Entry(self,width=20,bg="#1D2228",fg="cyan")
			self.b1 = tk.Button(self,text="Create Collection",bg=self.bgcolor,fg="lightgreen",command=_createcol)
			value = temp[0]
			self.cole2 = ttk.Combobox(self,values=value,state="readonly")
			self.cole2.current(0)
			self.b2 = tk.Button(self,text="Retrieve Document",bg=self.bgcolor,fg="lightgreen",command=_retrievedoc)
			self.b3 = tk.Button(self,text="Delete Collection",bg=self.bgcolor,fg="lightgreen",command=_deletecol)
			
			self.b3.grid(row=5,column=5,padx=10,pady=10,sticky="nesw")
			self.b2.grid(row=4,column=5,padx=10,pady=10,sticky="nesw")
			self.cole2.grid(row=3,column=6,padx=10,pady=10,sticky="nesw")
			self.b1.grid(row=2,column=5,padx=10,pady=10,sticky="nesw")
			self.cole1.grid(row=1,column=6,padx=10,pady=10,sticky="nesw")
			self.l2.grid(row=3,column=5,padx=10,pady=10,sticky=W)
			self.l1.grid(row=1,column=5,padx=10,pady=10,sticky="nesw")
			adjust_workspace2()			

#for teacher showcol==============================================================================================================

		def _teacher_showcol(col,db):
			self.db = db
			self.l1 = tk.Label(self,text="Set Collection Name",bg=self.bgcolor,fg="cyan")
			self.l2 = tk.Label(self,text="Choose Collection",bg=self.bgcolor,fg="cyan")
			self.cole1 = tk.Entry(self,width=20,bg="#1D2228",fg="cyan")
			self.b1 = tk.Button(self,text="Create Collection",bg=self.bgcolor,fg="lightgreen",command=_teacher_createcol)
			self.cole2 = ttk.Combobox(self,values=col,state="readonly")
			self.cole2.current(0)
			self.b2 = tk.Button(self,text="Retrieve Document",bg=self.bgcolor,fg="lightgreen",command=_teacher_retrievedoc)
			self.b3 = tk.Button(self,text="Delete Collection",bg=self.bgcolor,fg="lightgreen",command=_teacher_deletecol)
			
			self.b3.grid(row=5,column=5,padx=10,pady=10,sticky="nesw")
			self.b2.grid(row=4,column=5,padx=10,pady=10,sticky="nesw")
			self.cole2.grid(row=3,column=6,padx=10,pady=10,sticky="nesw")
			self.b1.grid(row=2,column=5,padx=10,pady=10,sticky="nesw")
			self.cole1.grid(row=1,column=6,padx=10,pady=10,sticky="nesw")
			self.l2.grid(row=3,column=5,padx=10,pady=10,sticky=W)
			self.l1.grid(row=1,column=5,padx=10,pady=10,sticky="nesw")
			adjust_workspace2()	

#for student showcol==============================================================================================================
		def _student_showcol():
			#self.db = db
			self.u = self.student_username
			self.p = self.student_password
			self.l = self.student_level
			#self.l1 = tk.Label(self,text="Set Collection Name",bg=self.bgcolor,fg="cyan")
			self.l2 = tk.Label(self,text="Choose Collection",bg=self.bgcolor,fg="cyan")
			#self.cole1 = tk.Entry(self,width=20,bg="#1D2228",fg="cyan")
			#self.b1 = tk.Button(self,text="Create Collection",bg=self.bgcolor,fg="lightgreen",command=_teacher_createcol)
			collection = ctlr.Controller._student_showcol(self.u,self.p,self.l)
			col = ["fake0","fake1","fake2"]
			idList = []
			for dictionary in collection:
				for key in dictionary:
					if key == "id":
						idList.append(dictionary[key])
			#print(collection)
			self.cole2 = ttk.Combobox(self,values=idList,state="readonly")
			self.cole2.current(0)
			self.b2 = tk.Button(self,text="Retrieve Document",bg=self.bgcolor,fg="lightgreen",command=_student_retrievedoc)
			#self.b3 = tk.Button(self,text="Delete Collection",bg=self.bgcolor,fg="lightgreen")
			
			#self.b3.grid(row=5,column=5,padx=10,pady=10,sticky="nesw")
			self.b2.grid(row=2,column=1,padx=10,pady=10,sticky="nesw")
			self.cole2.grid(row=1,column=2,padx=10,pady=10,sticky="nesw")
			#self.b1.grid(row=2,column=5,padx=10,pady=10,sticky="nesw")
			#self.cole1.grid(row=1,column=6,padx=10,pady=10,sticky="nesw")
			self.l2.grid(row=1,column=1,padx=10,pady=10,sticky=W)
			#self.l1.grid(row=1,column=5,padx=10,pady=10,sticky="nesw")
			adjust_workspace2()

#for admin usedb==================================================================================================================
		def _usedb():
			self.choose_dbname = self.e2
			self.temp = ctlr.Controller._usedb(self.choose_dbname.get())
			if True in self.temp:
				_showcol(self.temp,self.choose_dbname.get())
				_showdb()
#for teacher usedb=========================================================================================================================

		def _teacher_usedb():
			self.choose_dbname = self.e2 
			self.temp = ctlr.Controller._teacher_usedb(self.choose_dbname.get())
			try:
				_teacher_showcol(self.temp,self.choose_dbname.get())
				_teacher_showdb()
			except Exception:
				_teacher_showdb()

#for admin dropdb======================================================================================================================

		def _dropdb():
			self.choose_dbname = self.e2
			ctlr.Controller._dropdb(self.choose_dbname.get())
			_showdb()
								
#for admin showdb==================================================================================================================================


		def _showdb():
			self.l1 = tk.Label(self,text="Set Database Name",bg=self.bgcolor,fg="cyan")
			self.l2 = tk.Label(self,text="Choose Database",bg=self.bgcolor,fg="cyan")
			self.e1 = tk.Entry(self,width=20,bg="#1D2228",fg="cyan")
			self.b1 = tk.Button(self,text="Create Database",bg=self.bgcolor,fg="lightgreen",command=_createdb)
			dbnames = ctlr.Controller._showdb()
			value = dbnames
			self.e2 = ttk.Combobox(self,values=value,state="readonly")
			self.e2.current(0)
			self.b2 = tk.Button(self,text="Use Database",bg=self.bgcolor,fg="lightgreen",command=_usedb)
			self.b3 = tk.Button(self,text="Drop Database",bg=self.bgcolor,fg="lightgreen",command=_dropdb)
			
			self.b3.grid(row=5,column=2,padx=10,pady=10,sticky="nesw")
			self.b2.grid(row=4,column=2,padx=10,pady=10,sticky="nesw")
			self.e2.grid(row=3,column=3,padx=10,pady=10,sticky="nesw")
			self.b1.grid(row=2,column=2,padx=10,pady=10,sticky="nesw")
			self.e1.grid(row=1,column=3,padx=10,pady=10,sticky="nesw")
			self.l2.grid(row=3,column=2,padx=10,pady=10,sticky=W)
			self.l1.grid(row=1,column=2,padx=10,pady=10,sticky="nesw")
			adjust_workspace2()
			self.hidedbbutton = tk.Button(self,text="Refresh Space",bg=self.bgcolor,fg="lightgreen",font=('Terminal',12,'bold'),command=_hidedb)
			self.hidedbbutton.grid(row=4,column=0,padx=10,pady=10,sticky="nesw")
			style = ttk.Style(self)
			style.theme_use('clam')
			style.configure('Treeview',background="#1D2228",fieldbackground="#1D2228",foreground="white",font=('Terminal',9,'bold'))
			style.configure('Treeview.Heading',background="#1D2228",font=('Terminal',12,'bold'),foreground="cyan")
			self.tv = ttk.Treeview(self)
			self.tv['columns'] = ("Database_Name")
			self.tv.column('#0', width=0, stretch=NO)
			self.tv.column('Database_Name', anchor=CENTER, width=160)
			self.tv.heading('#0',text='',anchor=CENTER)
			self.tv.heading('Database_Name',text="Database_Name",anchor=CENTER)
			List = []
			for name in dbnames:
				List.append(name)
				self.tv.insert('',tk.END,values=List)
				List = []
			def item_selected(event):
				for selected_item in self.tv.selection():
					item = self.tv.item(selected_item)
					record = item['values']
					#showinfo(title='Information', message=','.join(record))
			self.tv.bind('<<TreeviewSelect>>', item_selected)
			self.tv.grid(row=1,column=1,padx=10,pady=10,rowspan=5,sticky='nesw')
			obj = self.winfo_children()

#for teacher showdb========================================================================================================================================

		def _teacher_showdb():
			u = self.teacher_username
			p = self.teacher_password
			l = self.teacher_level
			dbnames = ctlr.Controller._teacher_showdb(u,p,l)
			adjust_workspace2()
			self.l2 = tk.Label(self,text="Choose Database",bg=self.bgcolor,fg="cyan")
			self.e2 = ttk.Combobox(self,values=dbnames,state="readonly")
			if self.e2.current(0) is not None or self.e2.current(0) is not False:
				self.e2.current(0)
			#print(dbnames)
			#print(u,p,l)
			self.e2.grid(row=1,column=3,padx=10,pady=10,sticky="nesw")
			self.l2.grid(row=1,column=2,padx=10,pady=10,sticky="nesw")


			self.b2 = tk.Button(self,text="Use Database",bg=self.bgcolor,fg="lightgreen",command=_teacher_usedb)
			self.b2.grid(row=2,column=2,padx=10,pady=10,sticky="nesw")
#========================================================================================================================================


		def admin_workspace():
			self.showdb = tk.Button(self,text="Show Database",bg=self.bgcolor,fg="lightgreen",border=0,font=('Terminal',12,'bold'),command=_showdb)
			self.showdb.grid(row=1,column=0,padx=10,pady=10,sticky="nesw")
			logout = tk.Button(self,text="logout",bg=self.bgcolor,fg="lightgreen",border=0,font=('Terminal',12,'bold'),command=_logout)
			logout.grid(row=2,column=0,padx=10,pady=10,sticky="nesw")
			quitbutton = tk.Button(self,text="Quit",bg=self.bgcolor,fg="lightgreen",border=0,font=('Terminal',12,'bold'),command=_quit)
			quitbutton.grid(row=3,column=0,padx=10,pady=10,sticky="nesw")


#=======================================================================================================================================



		def student_workspace(u,p,l):
			self.student_username = u
			self.student_password = p
			self.student_level = l
			self.student_showcol = tk.Button(self,text="Show Collections",bg=self.bgcolor,fg='lightgreen',border=0,font=('Terminal',12,'bold'),command=_student_showcol)
			self.student_showcol.grid(row=1,column=0,padx=10,pady=10,sticky="nesw")
			
			logout = tk.Button(self,text="logout",bg=self.bgcolor,fg="lightgreen",border=0,font=('Terminal',12,'bold'),command=_logout)
			logout.grid(row=2,column=0,padx=10,pady=10,sticky="nesw")
			quitbutton = tk.Button(self,text="Quit",bg=self.bgcolor,fg="lightgreen",border=0,font=('Terminal',12,'bold'),command=_quit)
			quitbutton.grid(row=3,column=0,padx=10,pady=10,sticky="nesw")


#=======================================================================================================================================


		def teacher_workspace(u,p,l):
			self.teacher_username = u
			self.teacher_password = p
			self.teacher_level = l
			self.teacher_showdb = tk.Button(self,text="Show Database",bg=self.bgcolor,fg='lightgreen',border=0,font=('Terminal',12,'bold'),command=_teacher_showdb)
			self.teacher_showdb.grid(row=1,column=0,padx=10,pady=10,sticky="nesw")
			logout = tk.Button(self,text="logout",bg=self.bgcolor,fg="lightgreen",border=0,font=('Terminal',12,'bold'),command=_logout)
			logout.grid(row=2,column=0,padx=10,pady=10,sticky="nesw")
			quitbutton = tk.Button(self,text="Quit",bg=self.bgcolor,fg="lightgreen",border=0,font=('Terminal',12,'bold'),command=_quit)
			quitbutton.grid(row=3,column=0,padx=10,pady=10,sticky="nesw")


#=======================================================================================================================================

		def destory_loginpage():
			for wigets in self.winfo_children():
				wigets.destroy()

		def adminpage():
			admin_workspace()
			parent.configure(bg="lightgreen")
			self.configure(bg=self.bgcolor)
			fx = self.winfo_width()
			fy = self.winfo_height()
			wx = parent.winfo_width()
			wy = parent.winfo_height()
			ffx = wx/2 - fx/2
			ffy = wy/2 - fy/2
			self.place(x=ffx,y=ffy)
			la = tk.Label(self,text="Supervisor Workspace",fg=self.fgcolor,bg=self.bgcolor) 
			la.grid(row=0,column=0,padx=10,pady=10,sticky=W)

#=====================================================================================================================

		

		def teacherpage(u,p,l):
			teacher_workspace(u,p,l)
			parent.configure(bg="lightblue")
			self.configure(bg=self.bgcolor)
			fx = self.winfo_width()
			fy = self.winfo_height()
			wx = parent.winfo_width()
			wy = parent.winfo_height()
			ffx = wx/2 - fx/2
			ffy = wy/2 - fy/2
			#self.place(x=ffx,y=ffy)
			adjust_workspace2()
			parent.geometry("{}x{}".format(parent.winfo_width(),parent.winfo_height()))
			la = tk.Label(self,text="Leader Workspace",fg=self.fgcolor,bg=self.bgcolor)
			la2 = tk.Label(self,text="Name",fg=self.fgcolor,bg=self.bgcolor)
			leadername = ctlr.Controller.leadername(u,p,l)
			la3 = tk.Label(self,text=leadername,fg=self.fgcolor,bg=self.bgcolor)
			la.grid(row=0,column=0,padx=100,pady=100,sticky=W)
			la2.grid(row=0,column=2,padx=100,pady=100,sticky="nesw")
			la3.grid(row=0,column=3,padx=10,pady=100,sticky=W)
			
		
#======================================================================================================================

		def studentpage(u,p,l):
			student_workspace(u,p,l)
			parent.configure(bg="#C3FDB8")
			self.configure(bg=self.bgcolor)
			fx = self.winfo_width()
			fy = self.winfo_height()
			wx = parent.winfo_width()
			wy = parent.winfo_height()
			ffx = wx/2 - fx/2
			ffy = wy/2 - fy/2
			adjust_workspace2()
			#self.place(x=ffx,y=ffy)
			la = tk.Label(self,text="Crew Workspace",fg=self.fgcolor,bg=self.bgcolor)
			la2 = tk.Label(self,text="Name",fg=self.fgcolor,bg=self.bgcolor)
			leadername = ctlr.Controller.leadername(u,p,l)
			la3 = tk.Label(self,text=leadername,fg=self.fgcolor,bg=self.bgcolor)
			la.grid(row=0,column=0,padx=100,pady=100,sticky=W)
			la2.grid(row=0,column=1,padx=100,pady=100,sticky="nesw")
			la3.grid(row=0,column=2,padx=10,pady=100,sticky=W)
			
#=========================================================================================================================

		def logincheck():
			self.username = self.username_entry.get()
			self.password = self.password_entry.get()
			self.level = self.level_entry.get()
			if ctlr.Controller.when_login(self.username,self.password,self.level) is True :
				destory_loginpage()
				if self.level == "supervisor":
					adminpage()
				elif self.level == "leader":
					teacherpage(self.username,self.password,self.level)
				elif self.level == "crew":
					studentpage(self.username,self.password,self.level) 

		default_databases_creater()
		login()
#============================================================================ apaw ka codes are binded to parent --> main htal ka har ko pyaw dar 
#=================================================================== out ka codes are owning by itself 

	def con_err_msg():
		mb.showerror("Connection Fail","Connection can't establish!")
	def field_err_msg():
		mb.showerror("Login Fail ", "You must fill all fields !")
	def user_err_msg():
		mb.showerror("Invalid ", "You are an invalid user !")
	def dbfield_err_msg():
		mb.showerror("Data Definition Error ","You must define the name of Database !")
	def drop_fail_msg():
		mb.showerror("Permission Error","User is not allow this action !")
	def drop_success_msg(e2):
		mb.showinfo("Success drop ","{} is dropped successfully".format(e2))
	def colfield_err_msg():
		mb.showerror("Collection Definition Error ", "You must define the name of Collection!")
	def in_out_err_msg():
		mb.showerror("I/O Error","Sorry , Input/Output Error Happening !")
	def input_err_msg():
		mb.showerror("I/O Error","Sorry, This id is already used !")
	def db_err_msg():
		mb.showerror("Database not found ", "This database name is not in cluster !")
	def _none_collection_err():
		mb.showerror("Collection not found","Related database or collection does not exist !")
#==================================================================== out ka codes for admin 
#==================================================================== dan dan tan :)

if __name__ == "__main__":
	view = View()
	view.mainloop()

