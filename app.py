from flask import Flask,request,render_template,abort
import camera as db
app = Flask(__name__)
'''
AIOT RestfullApi
'''

PREFIX = '/api'
@app.route(PREFIX+'/cameras',methods=['POST','GET','PUT','DELETE'])
def cameras(data=False):
	if request.method == 'GET':
		# resp = make_response()
		# resp.headers["content-type"] = "application/json"
		return db.fetchall()
	elif request.method == 'POST':
		if request.get_json():
			camera = dict(request.get_json())
			camera["traffic"] = str(camera["traffic"])
			if "last_image" not in camera.keys():
				camera["last_image"] = ""
			db.create(tuple(camera.values()))
			return 'create a new record'
		else:
			return 'Can not create new record'
	elif request.method == 'PUT':
		if request.get_json():
			camera = dict(request.get_json())
			try:
				camera["traffic"] = sum(list(camera["traffic"].values()))/3
			except:
				pass
			db.updateAll(camera)
			return 'update a new record'
		else:
			return 'Can not update this record'
	elif request.method =='DELETE':
		return 'remove all records'
@app.route(PREFIX+'/cameras/<int:id>',methods=['GET','PUT','DELETE'])
def single_camera(id):
	if request.method == 'GET':
		return 'response with data of record: '+str(id)
	elif request.method == 'PUT':
		return 'update record: '+str(id)
	elif request.method =='DELETE':
		return 'remove record'+str(id)


if __name__ == '__main__':
        app.run(debug=True,host='0.0.0.0',port="9999")