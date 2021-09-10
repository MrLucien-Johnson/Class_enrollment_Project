import unittest
from flask import url_for
from flask_testing import TestCase
from application import *
from application.models import *


# Create the base class
class TestBase(TestCase):
    def create_app(self):
        #Configurations for the app.
        #we can update the app's configuration for the tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///classEnroll.db",
                SECRET_KEY="abc654321",
                DEBUG=True,
                #Testing applications that use WTForms can cause issues with CSRF form validation
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

        c1 = Classes(classes_name = 'friday', classes_day = "monday")
        db.session.add(c1)
        db.session.commit()

        l1 = Linked(fk_classes_name = c1.id, fk_student_day = s1.id)
        db.session.add(l1)
        db.session.commit()

def tearDown(self):
        ##runs after every test removing records

        db.session.remove()
        db.drop_all()    

##
# views testing
##

class TestViewHome(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'HOME', response.data)  

class TestViewGetAddStudent(TestBase):
    def test_addstudent_get(self):
        response = self.client.get(url_for('addStudent'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Add Student', response.data)    

class TestViewGetAddClasses(TestBase):
    def test_addclasses_get(self):
        response = self.client.get(url_for('addClasses'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Add Classes', response.data) 

class TestAddClasses(TestBase):
    def test_add_Classes(self):
        response = self.client.post(
            url_for('addClasses'),
            data = dict(classes_name="friday", classes_day = "monday"),
            follow_redirects=True
        )
        self.assertIn(b'Add Classes',response.data)

class TestAddStudent(TestBase):
    def test_add_Student(self):
        response = self.client.post(
            url_for('addStudent'),
            data = dict(studnet_name="testadd",student_age=26 , student_city="London"),
            follow_redirects=True
        )
        self.assertIn(b'Add Student',response.data)

class TestUpdateStudent(TestBase):
    def test_update_student(self):
        response = self.client.post(
            url_for('updateStudent', qid=1),
            data = dict(studnet_name="testupdate",student_age=30 , student_city="Update"),
            follow_redirects=True
        )
        self.assertIn(b'Home',response.data)