from application import db         

#Classes Table
class Classes(db.Model):
    id = db.Column(db.Integer, primary_key=True)                            
    classes_name = db.Column(db.String(50), unique=False, nullable=False)      
    classes_day = db.Column(db.String(10), nullable=False)   
    linkedclass = db.relationship('Linked', backref='classes')

#Students Table
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)                                        
    student_name = db.Column(db.String(100), nullable=False)                       
    student_age = db.Column(db.String(12), nullable=False)                        
    student_city = db.Column(db.String(40), nullable=False)                                  
    linkedstudent = db.relationship('Linked', backref='student')
#Linked Table
class Linked(db.Model):
    id = db.Column(db.Integer, primary_key=True)                                        
    fk_classes_id = db.Column(db.Integer, db.ForeignKey('classes.id'), nullable=False)      
    fk_student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)       
    #linked_day = db.Column(db.String(12), nullable=False)                        
    ##linked = db.relationship('Classes', backref='Linked')                                  