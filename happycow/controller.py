from model import *
import model as md

from view import *
import view as vw



class Controller:
	def __init__(*args,**kwargs):
		pass

	def default_databases_creater():
		if md.Model.connection_check():
			md.Model.default_databases_creater()
		else:
			vw.View.con_err_msg()

	def _logincombobox():
		return md.Model._logincombobox()

	def when_login(username,password,level):
		if md.Model.connection_check():  
			if md.Model.field_check(username,password,level):
				if md.Model.user_check(username,password,level):
					return True
				else:
					vw.View.user_err_msg()
			elif md.Model.field_check(username,password,level) is False:
				vw.View.field_err_msg()
		else:
			vw.View.con_err_msg()

#for teacher and student leadername ============================================================================================

	def leadername(u,p,l):
		return md.Model.leadername(u,p,l)

#=======================================================================================================
	def _showdb():
		if md.Model.connection_check():
			return md.Model._showdb()

		elif md.Model.connection_check() is False:
			return vw.View.con_err_msg()

#for leader showdb========================================================================


	def _teacher_showdb(u,p,l):
		if md.Model.connection_check():
			return md.Model._teacher_showdb(u,p,l)
		else:
			vw.View.con_err_msg()


#========================================================================


	def _createdb(e1):
		if md.Model._createdbfield_check(e1):
			if md.Model.connection_check():
				md.Model._createdb(e1)
				return True
			elif md.Model.connection_check() is False:
				vw.View.con_err_msg()
		elif md.Model._createdbfield_check(e1) is False:
			return vw.View.dbfield_err_msg()

	def _usedb(e2):
		return md.Model._usedb(e2)

	def _dropdb(e2):
		answer = vw.askyesno(title="do yo want to continue",message="are you sure?")
		if answer:
			if md.Model._dropdb(e2) is False:
				vw.View.drop_fail_msg()
			else:
				vw.View.drop_success_msg(e2)
				return md.Model._dropdb(e2)

	def _createcol(e1,choose_db):
		if md.Model.connection_check():
			if md.Model._createcol_field_check(e1):
				md.Model._createcol(e1,choose_db)
				return True
			else:
				vw.View.colfield_err_msg()
		else:
			vw.View.con_err_msg()

#for _teacher_createcol ========================================================================================================

	def _teacher_createcol(col,db):
		if md.Model.connection_check():
			if md.Model._teacher_createcol_field_check(col):
				md.Model._teacher_createcol(col,db)
				return True 
			else:
				vw.View.colfield_err_msg()
		else:
			vw.View.con_err_msg()



#for admin retrievedoc ========================================================================================================


	def _retrievedoc(e2,choose_db):
		if md.Model.connection_check():
			try:
				md.Model._retrievedoc(e2,choose_db)
				return md.Model._retrievedoc(e2,choose_db)
			except Exception:
				vw.View.in_out_err_msg()
		else:
			vw.View.con_err_msg()

	def _retrievedoc_data(e2,choose_db):
		if md.Model.connection_check():
			try:
				md.Model._retrievedoc_data(e2,choose_db)
				return md.Model._retrievedoc_data(e2,choose_db)
			except Exception:
				vw.View.in_out_err_msg()
		else:
			vw.View.con_err_msg()

#for teacher retrievedoc =====================================================================================================

	def _teacher_retrievedoc(col,db):
		if md.Model.connection_check():
			try:
				md.Model._teacher_retrievedoc(col,db)
				return md.Model._teacher_retrievedoc(col,db)
			except Exception:
				vw.View.in_out_err_msg()

		else:
			vw.View.con_err_msg()

	def _teacher_retrievedoc_data(col,db):
		if md.Model.connection_check():
			try:
				md.Model._teacher_retrievedoc_data(col,db)
				return md.Model._teacher_retrievedoc_data(col,db)
			except Exception:
				vw.View.in_out_err_msg()
		else:
			vw.View.con_err_msg()

#for admin deletecol===========================================================================================================			

	def _deletecol(e2,choose_db):
		answer = vw.askyesno(title="do yo want to continue",message="are you sure?")
		if answer:
			if md.Model.connection_check():
				try:
					md.Model._deletecol(e2,choose_db)
					return True
				except Exception:
					vw.View.in_out_err_msg()
					#print(e2)
					#print(choose_db)
			else:
				vw.View.con_err_msg()

#for teacher deletecol===========================================================================================================

	def _teacher_deletecol(e2,db):
		answer = vw.askyesno(title="do yo want to continue",message="are you sure?")
		if answer:
			if md.Model.connection_check():
				try:
					md.Model._teacher_deletecol(e2,db)
					return True 
				except Exception:
					vw.View.in_out_err_msg()
					#print(e2)
					#print(db)
			else:
				vw.View.con_err_msg() 

#for admin isertDoc============================================================================================================

	def _insertDoc(col,db,pwin):
		winchild = [] 
		for i in pwin.winfo_children():
			winchild.append(i)
		all_items = len(winchild)
		label_entry_items = all_items - 9

		List = [] 
		emptycounter = 0
		setcounter = 0
		for wiget in pwin.winfo_children()[:-4]:
			if hasattr(wiget,"get"):
				if wiget.get() == "":
					emptycounter += 1
				elif wiget.get() != "" and wiget.get() is not None:
					setcounter += 1
					List.append(wiget.get())
		print(emptycounter, " . This emptycounter ")
		print(setcounter, " . This is setcounter")
		#print(List[1:])
		if emptycounter != 0:
			vw.View.field_err_msg()
		elif emptycounter == 0:
			Listing = List[1:]
			if md.Model._insertDoc(col,db,Listing):
				return True
			elif md.Model._insertDoc(col,db,Listing) is False:
				vw.View.input_err_msg()

		"""winchild = [] 
		for i in pwin.winfo_children():
			winchild.append(i)
		all_items = len(winchild)
		label_entry_items = all_items - 8
		j = 0
		k = 0
		q = 0
		List = []
		entry_items = int(label_entry_items/2)
		for i in range(entry_items):
			j += 2
			if winchild[j].get() == "":
				k += 1
			else:
				List.append(winchild[j].get())
				q += 1
		if k >= q :
			vw.View.field_err_msg()
		elif k == 0:
			if md.Model._insertDoc(col,db,List):
				return True
			elif md.Model._insertDoc(col,db,List) is False:
				vw.View.input_err_msg()"""
				
			#print(all_items)
			#print(winchild)

#for teacher insertDoc==============================================================================

	def _teacher_insertDoc(col,db,pwin):
		winchild = [] 
		for i in pwin.winfo_children():
			winchild.append(i)
		all_items = len(winchild)
		label_entry_items = all_items - 9

		List = [] 
		emptycounter = 0
		setcounter = 0
		for wiget in pwin.winfo_children()[:-4]:
			if hasattr(wiget,"get"):
				if wiget.get() == "":
					emptycounter += 1
				elif wiget.get() != "" and wiget.get() is not None:
					setcounter += 1
					List.append(wiget.get())
		print(emptycounter, " . This emptycounter ")
		print(setcounter, " . This is setcounter")
		#print(List[1:])
		if emptycounter != 0:
			vw.View.field_err_msg()
		elif emptycounter == 0:
			Listing = List[1:]
			if md.Model._insertDoc(col,db,Listing):
				return True
			elif md.Model._insertDoc(col,db,Listing) is False:
				vw.View.input_err_msg()

		"""
		j = 0
		k = 0
		q = 0
		List = []
		entry_items = int(label_entry_items/2)
		for i in range(entry_items):
			j += 2
			if winchild[j].get() == "":
				k += 1
			else:
				List.append(winchild[j].get())
				q += 1
		if k >= q or k > q or k == q:
			vw.View.field_err_msg()
		elif k == 0:
			if md.Model._insertDoc(col,db,List):
				return True
			elif md.Model._insertDoc(col,db,List) is False:
				vw.View.input_err_msg()"""
#for student insertDoc=============================================================================		 

	def _student_insertDoc(dbid,stuid,pwin):
		List = [] 
		emptycounter = 0
		setcounter = 0
		for wiget in pwin.winfo_children():
			if hasattr(wiget,"get"):
				if wiget.get() == "":
					emptycounter += 1
				elif wiget.get() != "" and wiget.get() is not None:
					setcounter += 1
					List.append(wiget.get())
		print(emptycounter, " . This emptycounter ")
		print(setcounter, " . This is setcounter")
		if emptycounter != 0:
			vw.View.in_out_err_msg()
		elif emptycounter == 0:
			if md.Model._student_insertDoc(dbid,stuid,List[1:]):
				return True
			elif md.Model._student_insertDoc(dbid,stuid,List[1:]) is False:
				vw.View.input_err_msg()




#for admin updateDoc=================================================================================

	def _updateDoc(col,db,pwin):
		counter = 0
		List = []
		for wiget in pwin.winfo_children():
			if hasattr(wiget,"get"):
				List.append(wiget.get())
				counter += 1
		counter -= 2
		md.Model._updateDoc(col,db,List,counter)
		print(List)
		return True
#for teacher updateDoc================================================================================

	def _teacher_updateDoc(col,db,pwin):
		counter = 0
		List = []
		for wiget in pwin.winfo_children():
			if hasattr(wiget,"get"):
				List.append(wiget.get())
				counter += 1
		counter -= 2
		md.Model._updateDoc(col,db,List,counter)
		print(List)
		return True
#for student updateDoc=================================================================================

	def _student_updateDoc(dbid,stuid,pwin):
		counter = 0
		List = []
		for wiget in pwin.winfo_children():
			if hasattr(wiget,"get"):
				List.append(wiget.get())
				counter += 1
		md.Model._student_updateDoc(dbid,stuid,List)
		#print(List)
		return True


#for admin deleDoc=====================================================================================		

	def _deleteDoc(col,db,pwin):
		counter = 0 
		List = []
		for wiget in pwin.winfo_children():
			if hasattr(wiget,"get"):
				List.append(wiget.get())
				counter += 1
		counter -= 2
		answer = vw.askyesno(title="do yo want to continue",message="are you sure?")
		if answer:
			md.Model._deleteDoc(col,db,List,counter)
			print(List)
			return True

#for teacher deleteDoc=================================================================================		
	
	def _teacher_deleteDoc(col,db,pwin):
		counter = 0 
		List = []
		for wiget in pwin.winfo_children():
			if hasattr(wiget,"get"):
				List.append(wiget.get())
				counter += 1
		counter -= 2
		answer = vw.askyesno(title="do yo want to continue",message="are you sure?")
		if answer:
			md.Model._deleteDoc(col,db,List,counter)
			#print(List)
			return True

#for student deleDoc===================================================================================

	def _student_deleteDoc(dbid,stuid,pwin):
		counter = 0
		List = []
		for wiget in pwin.winfo_children():
			if hasattr(wiget,"get"):
				List.append(wiget.get())
				counter += 1
		answer = vw.askyesno(title="do yo want to continue",message="are you sure?")
		if answer:
			md.Model._student_deleteDoc(dbid,stuid,List)
			#print(List)
			return True	

#for admin delcolumn====================================================================================
	
	def _delcolumn(col,db,doc):
		answer = vw.askyesno(title="do yo want to continue",message="are you sure?")
		if answer:
			if md.Model.connection_check():
				try:
					md.Model._delcolumn(col,db,doc)
					return True
				except Exception:
					vw.View.in_out_err_msg()
			else:
				vw.View.con_err_msg()

#for teacher delcolum===================================================================================
	
	def _teacher_delcolumn(col,db,doc):
		answer = vw.askyesno(title="do yo want to continue",message="are you sure?")
		if answer:
			if md.Model.connection_check():
				try:
					md.Model._delcolumn(col,db,doc)
					return True
				except Exception:
					vw.View.in_out_err_msg()
			else:
				vw.View.con_err_msg()

#for admin delcolumnCombox==============================================================================
	
	def _delcolumnCombobox(col,db,pwin):
		return md.Model._delcolumnCombobox(col,db,pwin)

#for teacher delcolumnCombox============================================================================
	
	def _teacher_delcolumnCombobox(col,db,pwin):
		return md.Model._teacher_delcolumnCombobox(col,db,pwin) 

#for admin addcolumn====================================================================================

	def _addcolumn(col,db,doc):
		if md.Model.connection_check():
			try:
				md.Model._addcolumn(col,db,doc)
				return True
			except Exception:
				vw.View.in_out_err_msg()
		else:
			vw.View.con_err_msg()

#for teacher addcolumn=================================================================================

	def _teacher_addcolumn(col,db,doc):
		if md.Model.connection_check():
			try:
				md.Model._addcolumn(col,db,doc)
				return True
			except Exception:
				vw.View.in_out_err_msg()
		else:
			vw.View.con_err_msg()

		

#for teacher showdb and usedb========================================================================

	def _teacher_showdb(u,p,l):
		if md.Model.connection_check():
			return md.Model._teacher_showdb(u,p,l)
		else:
			vw.View.con_err_msg()

	def _teacher_usedb(db):
		if md.Model._teacher_usedb(db) is False:
			vw.View.db_err_msg()
		elif md.Model._teacher_usedb(db) is not False:
			return md.Model._teacher_usedb(db)


#for student showcol=================================================================================

	def _student_showcol(u,p,l):
		if md.Model.connection_check():
			try:
				md.Model._student_showcol(u,p,l)
				return md.Model._student_showcol(u,p,l)
			except Exception:
				vw.View.db_err_msg()
		else:
			vw.View.con_err_msg()

#for student retrievedoc ===========================================================================


	def _student_retrievedoc(colid,stuid):
		if md.Model.connection_check():
			md.Model._student_retrievedoc(colid,stuid)
			return md.Model._student_retrievedoc(colid,stuid)
		else:
			vw.View.con_err_msg()

#for student retrieveDoc data ===========================================================================
		

	def _student_retrievedoc_data(colid,stuid):
		"""answer = vw.askyesno(title="do yo want to continue",message="are you sure?")
		if answer:
			print("work")"""
		if md.Model.connection_check():
			try:
				md.Model._student_retrievedoc_data(colid,stuid)
				return md.Model._student_retrievedoc_data(colid,stuid)
			except Exception:
				vw.View.in_out_err_msg()
		else:
			vw.View.con_err_msg()

	def _none_collection_err():
		return vw.View._none_collection_err()

#for student id==========================================================================================

	def _student_id(u,p,l):
		if md.Model.connection_check():
			try:
				return md.Model._student_id(u,p,l)
			except Exception:
				vw.View.in_out_err_msg()
		else:
			vw.View.con_err_msg()

		
#for student db==============================================================================================

	def _student_db(colid,stuid):
		if md.Model.connection_check():
			try:
				md.Model._student_db(colid,stuid)
				return md.Model._student_db(colid,stuid)
			except Exception:
				vw.View.db_err_msg()
		else:
			vw.View.con_err_msg()



			


		




