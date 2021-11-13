from flask import Flask, request,jsonify
from flask_cors import CORS
from flask_classful import FlaskView,route
from flask_mysqldb import MySQL
import pymysql as my
from Detail import Details


app = Flask(__name__)

app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_USER'] ='root'
app.config['MYSQL_PASSWORD'] =''
app.config['MYSQL_DB'] ='flask_db'

mysql = MySQL(app)
CORS(app)

message ={"error":"","name":"","Delete":""}

class Website(FlaskView):

	def connection(self):
		return mysql.connection
	
	def cursor(self):
		return self.connection().cursor()

	def db_Connection(self):
		return Details(self.cursor(),self.connection())


	@route('/getDetails',methods =["GET"]) #retrieving user details(Admin Function)
	def getDetails(self):
		if request.method=="GET":
			try:
				return jsonify(self.db_Connection().insertDetails())
			except:
				return jsonify("Server Down")

	
	@route('/addUsers',methods=["POST","GET"]) #adding users to the system(Admin Function)
	def addUsers(self):
		if request.method=="POST":
			data = request.get_json()
			name =data['username']
			dob = data['dob']
			gender = data['gender']
			email =data['email']
			location = data['location']
			try:
				self.db_Connection().addPeople(name,dob,gender,email,location)
				message["error"]="Registration Successfull"
			except:
				message["error"] ="Server Down Registration Failed!"
			return(request.get_json())

	@route('/getMessage',methods =["GET"])
	def getMessage(self):
		if request.method=="GET":
			return jsonify([{"Message":message["error"]}])

	@route('/login',methods =["POST"])
	def login(self):
		if request.method=="POST":
			data = request.get_json()
			username = data["username"]
			is_member =self.db_Connection().login(username)
			if is_member==username:
				message['name']=username
			else:
				pass
		return data

	@route('/allow',methods =["POST"])
	def allowAuthentication(self):
		return jsonify([{"Name":message["name"]}])

	@route('/delete_user',methods=["POST"])
	def deleteUser(self):
		if request.method=="POST":
			data = request.get_json()
			message['Delete']=data
			return data
		if request.method=="GET":
			return jsonify([{"Name":message['Delete']}])

Website().register(app,route_base ="/")

if __name__=="__main__":
	app.run(debug=True)

