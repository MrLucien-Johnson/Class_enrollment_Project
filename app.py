from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@0.0.0.0:5000/classEnroll_db'

db = SQLAlchemy(app)
## drop all tables if any
##db.drop_all()
## create all tables based on 
##db.create_all()

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
