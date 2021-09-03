import os
from os import getenv
from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##use untill end of project and then connect to external database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///classEnroll.db"
## app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://username:password@databaseuri:port/<databse name>"
##bad practice as secrets are revealed
## app.config["SQLALCHEMY_DATABASE_URI"] = str(os.getenv('DATABASE_URI'))
##hiding it is app.config["SECRET_KEY"] = getenv('MY_SECRET_KEY')
## IN THE COMMAND LINE BEFORE RUNNING
##  EXPORT MY_SECRET_KEY 
##  EXPORT DATABSE_URI
##  EXPORT MY_SECRET_KEY = <my secret key>
##  EXPORT DATABSE_URI = <my_database_uri>

##app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:rootroot@app-database.ci6qrqchw1mv.us-west-2.rds.amazonaws.com:3306/classEnroll.db"

## get info from amazon ec2 rds
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

## setup database models
## setup student table
class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
## setup classes table 

## setup join table

## drop database if exists
db.drop_all()
## create database 
db.create_all()



@app.route('/')
def no_url():
    return  redirect('/home')

@app.route('/home')
def home_url():
    return  "Home for future students"

@app.route('/enroll')
def enroll_url():
    return  "Hello future students"



if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
