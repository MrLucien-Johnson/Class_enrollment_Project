from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import *

# Create the base class
class TestBase(TestCase):
    def create_app(self):
        #Configurations for the app.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///classEnroll.db",
                SECRET_KEY='abc654321',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

def setUp(self):
        
        ##setup before each test creating records to work with
        
        # Create table
        db.create_all()

        
        s1 = Student(studnet_name="test",student_age=26 , student_city="London")

        
        db.session.add(s1)
        db.session.commit()

        c1 = Classes(classes_name = 'friday', classes_day = "monday", status = 'correct')
        db.session.add(c1)
        db.session.commit()

        l1 = Linked(fk_classes_name = c1.id, fk_student_day = s1.id)
        db.session.add(l1)
        db.session.commit()

def tearDown(self):
        ##runs after every test removing records

        db.session.remove()
        db.drop_all()        