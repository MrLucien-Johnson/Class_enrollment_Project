import os
from app import db, Student

db.drop_all()
db.create_all()
# Add item to database 
teststudent1 = Student(first_name='abel',last_name='Lucien-Johnson') 
db.session.add(teststudent1)
db.session.commit()