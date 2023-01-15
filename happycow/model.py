from controller import *
import controller as ctlr 

from pymongo import *
import pymongo as py  

import json
import os 

global connectionstring
#connectionstring = "mongodb+srv://<clustername>:<password>@cluster0.6irvlpn.mongodb.net/?retryWrites=true&w=majority"
connectionstring = "localhost:27017"

class Model:
	
	def __init__(self,*args,**kwargs):
		pass 
	def default_databases_creater():
		#print("default_databases_creater work!")
		cluster = py.MongoClient(connectionstring)
		defaultdbtlist = ["happycow","Authority","Task","Network_Lab","Security_Lab"]
		lendefaultdblist = len(defaultdbtlist)
		counter = 0
		clusterdblist = []
		for name in cluster.list_database_names():
			clusterdblist.append(name)
		for i in range(lendefaultdblist):
			if defaultdbtlist[i] in clusterdblist:
				print("{} has been ".format(defaultdbtlist[i]))
			else:
				print("{} has not been ".format(defaultdbtlist[i]))
				createdb = cluster[defaultdbtlist[i]]
				#print(createdb)
				if i == 0:
					userdoc = '[{"id":"S1","username":"root","password":"root","level":"supervisor"},{"id":"L1","username":"trk","password":"root","level":"leader"},{"id":"C1","username":"lwt","password":"root","level":"crew"}]'
					jsonuserdoc = json.loads(userdoc)
					createcol = createdb["user"]
					insertdoc = createcol.insert_many(jsonuserdoc)
					print(insertdoc.inserted_ids)
					leaderdoc = '[{"id":"L1","name":"Daw Thiri Kyaw"}]'
					jsonleaderdoc = json.loads(leaderdoc)
					createcol_two = createdb["leader"]
					insertdoc_two = createcol_two.insert_many(jsonleaderdoc)
					print(insertdoc_two.inserted_ids)
					crewdoc = '[{"id":"C1","name":"Mg La Win Tun"}]'
					jsoncrewdoc = json.loads(crewdoc)
					createcol_three = createdb["crew"]
					insertdoc_three = createcol_three.insert_many(jsoncrewdoc)
					print(insertdoc_three.inserted_ids)
				elif i == 1:
					l1doc = '[{"id":"A","database_name":"Security_Lab"},{"id":"B","database_name":"Network_Lab"}]'
					jsonl1doc = json.loads(l1doc)
					createcol_4 = createdb["L1"]
					insertdoc_4 = createcol_4.insert_many(jsonl1doc)
					print(insertdoc_4.inserted_ids)
				elif i == 2:
					c1doc = '[{"id":"Security_sb","database_name":"Security_Lab","collection_name":"systembox"},{"id":"Network_sb","database_name":"Network_Lab","collection_name":"systembox"}]'
					jsonc1doc = json.loads(c1doc)
					createcol_5 = createdb["C1"]
					insertdoc_5 = createcol_5.insert_many(jsonc1doc)
					print(insertdoc_5.inserted_ids)
				elif i == 3:
					netdoc = '[{"id":"SB1","performance":"good"},{"id":"SB2","performance":"bad"}]'
					jsonnetdoc = json.loads(netdoc)
					createcol_6 = createdb["systembox"]
					insertdoc_6 =  createcol_6.insert_many(jsonnetdoc)
					print(insertdoc_6.inserted_ids)
				elif i == 4:
					secdoc = '[{"id":"SB3","performance":"good"},{"id":"SB4","performance":"bad"}]'
					jsonsecdoc = json.loads(secdoc)
					createcol_7 = createdb["systembox"]
					insertdoc_7 =  createcol_7.insert_many(jsonsecdoc)
					print(insertdoc_7.inserted_ids)

				
		

	def _logincombobox():
		pass
#for teacher and student leadername=========================================================
	def leadername(u,p,l):
		cluster = py.MongoClient(connectionstring)
		db = cluster["happycow"]
		col = db["user"]
		x = col.find_one({"username":u,"password":p,"level":l})
		_id_ = x["id"]
		_level_ = x["level"]
		targetcol = db[_level_]
		y = targetcol.find_one({"id":_id_})
		name = y["name"]
		return name

	def field_check(username,password,level):
		if username == "" or password == "" :
			return False
		elif username != '' and password != '' and level != '':
			return True
	def connection_check():
		try:
			client = py.MongoClient(connectionstring)
			return True
		except py.errors.ConfigurationError:
			return False
	def user_check(username,password,level):
			client = py.MongoClient(connectionstring)
			db = client.happycow
			collection = db.user 
			valid_user = collection.find_one({"username":username,"password":password,"level":level})
			if valid_user is None:
				return False
			elif valid_user is not None:
				return True
	def _showdb():
		client = py.MongoClient(connectionstring)
		dbname = client.list_database_names()
		return dbname

	def _createdbfield_check(e1):
		if e1 == "":
			return False
		elif e1 != "":
			return True
	def _createdb(e1):
		myclient = py.MongoClient(connectionstring)
		db = myclient.get_database(e1)
		col = db.get_collection(e1)
		if e1 == "Task":
			default_doc = '[{"id":"A","database_name":"null","collection_name":"null"}]'
		elif e1 == "Authority":
			default_doc = '[{"id":"A","database_name":"null"}]'
		else:
			default_doc = '[{"id":"MA15","Type":"Light Machine Gun","original":"Germany","technology":"MG3 Clone"}]'
		json_default_doc = json.loads(default_doc)
		inserted = col.insert_many(json_default_doc)
		print(str(len(inserted.inserted_ids)))

	def _dropdb(e2):
		client = py.MongoClient(connectionstring)
		try:
			if e2 == "happycow" or e2 == "Authority" or e2 == "Task":
				return False
			elif e2 != "happycow" or e2 != "Authority" or e2 != "Task":
				client.get_database(e2)
				client.drop_database(e2)
		except Exception:
			print("ma ya buu kwar !")
			return False

	def _usedb(e2):
		cluster = py.MongoClient(connectionstring)
		try: 
			db = cluster[e2]
			collections = db.list_collection_names()
			return collections,True
		except Exception:
			print("ma ya buu kwar")
			return False 

	def _createcol_field_check(e1):
		if e1 == "":
			return False
		elif e1 != "":
			return True

#for teacher createcol field check=========================================================================================

	def _teacher_createcol_field_check(col):
		if col == "":
			return False
		else:
			return True

#for admin createcol=======================================================================================================

	def _createcol(e1,choose_db):
		cluster = py.MongoClient(connectionstring)
		db = cluster[choose_db]
		col = db[e1]
		if choose_db == "Task":
			default_doc = '[{"id":"A","database_name":"null","collection_name":"null"}]'
		elif choose_db == "Authority":
			default_doc = '[{"id":"A","database_name":"null"}]'
		else:
			default_doc = '[{"id":"MA15","Type":"Light Machine Gun","original":"Germany","technology":"MG3 Clone"}]'
		json_default_doc = json.loads(default_doc)
		inserted = col.insert_many(json_default_doc)
		print(str(len(inserted.inserted_ids)))

#for teacher_createcol =====================================================================================================

	def _teacher_createcol(col,db):
		cluster = py.MongoClient(connectionstring)
		database = cluster[db]
		collection = database[col]
		if db == "Task":
			default_doc = '[{"id":"A","database_name":"null","collection_name":"null"}]'
		elif db == "Authority":
			default_doc = '[{"id":"A","database_name":"null"}]'
		else:
			default_doc = '[{"id":"MA15","Type":"Light Machine Gun","original":"Germany","technology":"MG3 Clone"}]'
		json_default_doc = json.loads(default_doc)
		inserted = collection.insert_many(json_default_doc)
		if str(len(inserted.inserted_ids)) is not None or str(len(inserted.inserted_ids)) is not False:
			return True
		#print(str(len(inserted.inserted_ids)))


#for admin retrievedoc======================================================================================================
	def _retrievedoc(e2,choose_db):
		cluster = py.MongoClient(connectionstring)
		db = cluster[choose_db]
		col = db[e2]
		x = col.find_one()
		doc = col.find()
		List = []
		for key in x:
			if key != "_id":
				List.append(key)
		return List,doc

	def _retrievedoc_data(e2,choose_db):
		cluster = py.MongoClient(connectionstring)
		db =  cluster[choose_db]
		col = db[e2]
		doc = col.find()
		return doc 
#for teacher retrievedoc ===================================================================================================

	def _teacher_retrievedoc(col,db):
		cluster = py.MongoClient(connectionstring)
		database = cluster[db]
		collection = database[col]
		x = collection.find_one()
		List = []
		for key in x:
			if key != "_id":
				List.append(key)
		#print(x)
		return List


	def _teacher_retrievedoc_data(col,db):
		cluster = py.MongoClient(connectionstring)
		database = cluster[db]
		collection = database[col]
		doc = collection.find()
		return doc



#for admin deletecol =======================================================================================================

	def _deletecol(e2,choose_db):
		cluster = py.MongoClient(connectionstring)
		db = cluster[choose_db]
		col = db[e2]
		col.drop() 

#for teacher deletecol=======================================================================================================

	def _teacher_deletecol(e2,db):
		cluster = py.MongoClient(connectionstring)
		database = cluster[db]
		collection = database[e2]
		collection.drop()

#for admin and teacher insertDoc===============================================================================================================

	def _insertDoc(col,db,List):
		cluster = py.MongoClient(connectionstring)
		database = cluster[db]
		collection = database[col]
		targetcollection = database[col]
		header = collection.find_one()
		Listheader = []
		for i in header:
			if i != "_id":
				Listheader.append(i)
		lenListheader = len(Listheader) 
		dictionary = {}
		for i in range(lenListheader):
			#print(Listheader[i],List[i])
			dictionary[Listheader[i]] = List[i]
		x = targetcollection.find_one({"id":dictionary["id"]}) 
		if x is None:
			targetcollection.insert_one(dictionary)
			return True
		if x is not None:
			return False

#END admin and teacher insertDoc ===================================================================================
			
#for student insertDoc =============================================================================================

	def _student_insertDoc(dbid,stuid,List):
		cluster = py.MongoClient(connectionstring)
		database = cluster["Task"]
		authority = database[stuid]
		
		targetcol = authority.find_one({"id":dbid})#id in authority
		dbname = targetcol["database_name"]
		colname = targetcol["collection_name"]
		
		targetdatabase = cluster[dbname]
		targetcollection = targetdatabase[colname]
		
		#print(dbid)		
		#print(List)

		Listheader = []
		header = targetcollection.find_one()
		for i in header:
			if i != "_id":
				Listheader.append(i)
		lenListheader = len(Listheader)
		dictionary = {}
		for i in range(lenListheader):
			dictionary[Listheader[i]] = List[i]
		x = targetcollection.find_one({"id":dictionary["id"]})
		if x is None:
			targetcollection.insert_one(dictionary)
			return True 
		elif x is not None:
			return False

			
	"""def _alterDoc(*args):
		List = []
		for i in {*args}:
			List.append(i)
		db = List[1]
		col = List[0]
		print(db,col)
		
		cluster = py.MongoClient(connectionstring)
		database = cluster[str(db)]
		collection = database[str(col)]
		print(collection)"""

#for admin delcolumn ========================================================================================================

	def _delcolumn(col,db,doc):
		cluster = py.MongoClient(connectionstring)
		database = cluster[db]
		collection = database[col]
		header = collection.find_one()
		"""List = []
		for i in header:
			if i != "_id":
				List.append(i)
		List2 = [db,col,doc]"""
		collection.update_many({},{"$unset":{doc:""}})
		
#for admin delcolumnCombobox=====================================================================================

	def _delcolumnCombobox(col,db,pwin):
		cluster = py.MongoClient(connectionstring)
		database = cluster[db]
		collection = database[col]
		header = collection.find_one()
		List = []
		for i in header:
			if i != "_id":
				List.append(i)
		return List

#for teacher delcolumnCombobox==============================================================================================

	def _teacher_delcolumnCombobox(col,db,pwin):
		cluster = py.MongoClient(connectionstring)
		database = cluster[db]
		collection = database[col]
		header = collection.find_one()
		List = []
		for i in header:
			if i != "_id":
				List.append(i)
		return List

#for admin and teacher addcolumn========================================================================================================

	def _addcolumn(col,db,doc):
		cluster = py.MongoClient(connectionstring)
		database = cluster[db]
		collection = database[col]
		collection.update_many({},{"$set":{doc:"null"}})

#for student updateDoc ===================================================================================================
	def _student_updateDoc(dbid,stuid,Listing):
		cluster = py.MongoClient(connectionstring)
		db = cluster["Task"]
		col = db[stuid]
		List = Listing[1:]



		x = col.find_one({"id":dbid})
		dbname = x["database_name"]
		colname = x["collection_name"]
		
		cluster = py.MongoClient(connectionstring)
		targetdb = cluster[dbname]
		targetcol = targetdb[colname]

		x = targetcol.find_one()
		headerList = []
		for i in x:
			if i != "_id":
				headerList.append(i)
		dictionary = {}
		lenList = len(List)
		for i in range(lenList):
			dictionary[headerList[i]] = List[i]
		for k in dictionary.keys():
			if k == 'id':
				catch_id = dictionary[k]
		try:
			targetcol.replace_one({"id":str(catch_id)},dictionary)
			targetcol.replace_one({"id":catch_id},dictionary)
			return True
		except Exception:
			return False 

#for admin and teacher updatDoc============================================================================================

	def _updateDoc(col,db,Listing,counter):
		cluster = py.MongoClient(connectionstring)
		targetdb = cluster[db]
		targetcol = targetdb[col]
		List = Listing[1:-2] 
		#print("This is list ====  ",List)
		x = targetcol.find_one()
		headerList = []
		for i in x:
			if i != "_id":
				headerList.append(i)
		dictionary = {}
		lenList = len(List)
		for i in range(lenList):
			dictionary[headerList[i]] = List[i]
		for k in dictionary.keys():
			if k == 'id':
				catch_id = dictionary[k]
		try:
			targetcol.replace_one({"id":str(catch_id)},dictionary)
			targetcol.replace_one({"id":catch_id},dictionary)
			return True
		except Exception:
			return False 

		"""
		targetcollection = database[col]
		header = collection.find_one()
		headerList = []
		catch_id = None
		for i in header:
			headerList.append(i)
		dictionary = {}
		for i in range(counter):
			try:
				intOrstr = int(List[i])
			except Exception:
				intOrstr = str(List[i])
			dictionary[headerList[i+1]] = intOrstr
			
		for k in dictionary.keys():
			if k == 'id':
				catch_id = dictionary[k]  
		#print(dictionary)
		#print(catch_id)
		try:
			targetcollection.replace_one({"id":str(catch_id)},dictionary)
			targetcollection.replace_one({"id":catch_id},dictionary)
			return True
		except Exception:
			return False
			#collection.update({"id":catch_id},{"$set":dictionary})"""

#for admin and teacher deleteDoc===============================================================================================	

	def _deleteDoc(col,db,Listing,counter):
		cluster = py.MongoClient(connectionstring)
		database = cluster[db]
		targetcol = database[col]
		List = Listing[1:-2]
		#print("this is list ==== " , List)
		header = targetcol.find_one()
		headerList = []
		for i in header:
			headerList.append(i)

		dictionary = {}
		lenList = len(List)
		for i in range(lenList):
			dictionary[headerList[i+1]] = List[i]
		catch_id = dictionary["id"]
		targetcol.delete_one({"id":str(catch_id)})
		targetcol.delete_one({"id":catch_id})

		"""header = collection.find_one()
		catch_id = None 
		headerList = []
		for i in header:
			headerList.append(i)
		dictionary = {}
		for i in range(counter):
			try:
				intOrstr = int(List[i])
			except Exception:
				intOrstr = str(List[i])
			dictionary[headerList[i+1]] = intOrstr

		for k in dictionary.keys():
			if k == "id":
				catch_id = dictionary[k]
		collection.delete_one({"id":str(catch_id)})
		collection.delete_one({"id":catch_id})"""



	"""def _updateDocAction(catch_id,dictionary):
		collection.update({"id":catch_id},{"$set":dictionary})"""

#for student deleteDoc=========================================================================================================================
	def _student_deleteDoc(dbid,stuid,Listing):
		List = Listing[1:]
		cluster = py.MongoClient(connectionstring)
		db = cluster["Task"]
		col = db[stuid]

		x = col.find_one({"id":dbid})
		dbname = x["database_name"]
		colname = x["collection_name"]

		targetdb = cluster[dbname]
		targetcol = targetdb[colname]
		header = targetcol.find_one()
		headerList = []
		for i in header:
			headerList.append(i)

		dictionary = {}
		lenList = len(List)
		for i in range(lenList):
			dictionary[headerList[i+1]] = List[i]
		catch_id = dictionary["id"]
		targetcol.delete_one({"id":str(catch_id)})
		targetcol.delete_one({"id":catch_id})


#for teacher showdb=======================================================================================================
	def _teacher_showdb(u,p,l):
		cluster = py.MongoClient(connectionstring)
		database = cluster["happycow"]
		collection = database["user"]
		x = collection.find_one({"username":u,"password":p,"level":l})
		print(x["id"])
		
		teacher_id = x["id"]
		targetdatabase = cluster["Authority"]
		targetcollection = targetdatabase[teacher_id]
		y = targetcollection.find()
		List = []
		for i in y:
			for j in i:
				if j == 'database_name':
					List.append(i[j])
		return List

	def _teacher_usedb(db):
		cluster = py.MongoClient(connectionstring)
		if db in cluster.list_database_names():
			database = cluster[db]
			collection = database.list_collection_names()
			return collection
		elif db not in cluster.list_database_names():
			return False

#for student showcol======================================================================================================

	def _student_showcol(u,p,l):
		client = py.MongoClient(connectionstring)
		db = client["happycow"]
		col = db["user"]
		x = col.find_one({"username":u,"password":p,"level":l})
		_id_ = x["id"]
		targetdb = client["Task"]
		targetcol = targetdb[_id_]
		y = targetcol.find()
		return y

#for student retievedoc =================================================================================================

	def _student_retrievedoc(colid,stuid):
		cluster = py.MongoClient(connectionstring)
		db = cluster["Task"]
		col = db[stuid]		
		x = col.find_one({"id":colid})
				
		dbname = x["database_name"]
		colname = x["collection_name"]

		targetdb = cluster[dbname]
		targetcol = targetdb[colname]
		collection = targetcol.find_one()
		return collection
#for student retrievedoc data ==========================================================================================

	def _student_retrievedoc_data(colid,stuid):
		cluster = py.MongoClient(connectionstring)
		db = cluster["Task"]
		col = db[stuid]
		x = col.find_one({"id":colid})
		dbname = x["database_name"]
		colname = x["collection_name"]
		targetdb = cluster[dbname]
		targetcol = targetdb[colname]
		collection = targetcol.find()
		return collection

#for student db==========================================================================================================

	def _student_db(colid,stuid):
		cluster = py.MongoClient(connectionstring)
		db = cluster["Task"]
		col = db[stuid]
		x = col.find_one({"id":colid})
		dbname = x["database_name"]
		return dbname
	

#for student id ==========================================================================================================

	def _student_id(u,p,l):
		cluster = py.MongoClient(connectionstring)
		db = cluster["happycow"]
		col = db["user"]
		x = col.find_one({"username":u,"password":p,"level":l})
		_id_ = x["id"]
		return _id_



		




	

			


		

