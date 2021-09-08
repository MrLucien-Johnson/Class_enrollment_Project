import os
from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#Creates a local database will use env to hide in future
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///classEnroll.db"
##app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
#remove error while running
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False     

#Creates a secret key which is used by the forms needed to run will also use evn
app.config['SECRET_KEY'] = 'abc654321'

#Creates the database object
db = SQLAlchemy(app)        

from application import routes