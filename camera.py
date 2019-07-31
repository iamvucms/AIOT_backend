import sqlite3 as db
import json
def fetchall():
	with db.connect('db.sqlite') as conn:
		try:
			cursor  = conn.cursor().execute("SELECT * FROM Cameras")
			data = cursor.fetchall()
			result = []
			for value in data:
				l = list(value)
				result.append({"id":l[0],"lat":l[1],"lon":l[2],"streetname":l[3],"vote":l[4],"traffic":dict(l[5]),"status":int(l[6]),last_image:str(l[7]),last_update:str(l[8])})
			return json.dumps(result)
		except db.Error as e: 
			print("Error "+str(e))
def create(data):
	with db.connect('db.sqlite') as conn:
		try:
			conn.cursor().execute("INSERT INTO Cameras (latitude,longtitude,streetname,status,traffic,vote,last_image,last_update) VALUES (?,?,?,?,?,?,?,strftime('%Y-%m-%d %H:%M:%f','now'))",data)
			conn.commit()
		except db.Error as e: 
			print("Error "+str(e))
def updateAll(data):
	with db.connect('db.sqlite') as conn:
		try:
			prepare = []
			query = "UPDATE Cameras SET "
			for key,val in data.items():
				if key == "streetname":
					query +=str(key)+"='"+str(val)+"',"
				else:
					query +=str(key)+"="+str(val)+","
			query = query.strip().strip(",")
			print(query)
			conn.cursor().execute(query)
			conn.commit()
		except db.Error as e: 
			print("Error "+str(e))