from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///classEnroll.db"
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
