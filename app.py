from flask import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@123.45.6.78:3306/class_enrollment_Project'

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
