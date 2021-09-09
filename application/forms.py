from application import app                                             
from flask import *                       
from flask_wtf import FlaskForm    
from application import *                                   
from wtforms import StringField, IntegerField, SelectField, SubmitField              
from wtforms.validators import DataRequired, Length, ValidationError    


class  StudentForm(FlaskForm):
    student_name = StringField('Student Name', 
        validators=[DataRequired(), Length(min=1, max=50)])  
    
    student_age = StringField('Student age',
        validators=[DataRequired(), Length(min=1, max=12)])  
    
    student_city = StringField('City',
        validators=[DataRequired(), Length(min=1, max=40)]) 
    
    submit = SubmitField('Add Student')                          


class UpdateStudentForm(FlaskForm):
    student_name = SelectField('Select to update', choices=[], 
        validators=[DataRequired()])
        
    submit = SubmitField('Edit Student')

class DeleteStudentForm(FlaskForm):
    student_id = SelectField('Select Student to delete', choices=[],
        validators=[DataRequired()])

    submit = SubmitField('Delete Student')



class ClassesForm(FlaskForm):                          
    
    classes_name = StringField('Name of class',
        validators=[DataRequired(), Length(min=1, max=50)])    
    
    
    classes_day = StringField('Day in the week, Monday-Friday',
        validators=[DataRequired()])                            
        
    submit = SubmitField('Add class')                          


class UpdateClassesForm(FlaskForm):
    
    classes_name = StringField('Name of class',
        validators=[DataRequired(), Length(min=1, max=50)])    
    
    classes_day = StringField('Day in the week',
        validators=[DataRequired()])      

    submit = SubmitField('Edit class')

class DeleteClassesForm(FlaskForm):
    classes_id = SelectField('Select Student to delete', choices=[],
        validators=[DataRequired()])

    submit = SubmitField('Delete classes')