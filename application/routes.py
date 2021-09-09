from application import app, db                     
from application.models import *       
from flask import render_template, url_for, request, redirect, flash
from application.forms import * 



@app.route('/')
def home():
    # student1 = Student(student_name ="abel",student_age =26, student_city="london")
    # db.session.add(student1)     #stage
    # db.session.commit()             #commit
    allStudents = Student.query.all()         
    allClasses = Classes.query.all()  
    allLinked = Linked.query.all() 
    return render_template('home.html', allStudents=allStudents, allClasses=allClasses, allLinked=allLinked) 

@app.route('/addClasses', methods=['GET', 'POST'])
def addClasses():
    form = ClassesForm()              
    if form.validate_on_submit():
        newClasses = Classes(
        classes_name = form.classes_name.data,
        classes_day = form.classes_day.data,
        )
        db.session.add(newClasses)     #stage
        db.session.commit()             #commit
        message = f"you have added a class : {form.classes_name.data}"
        return render_template('addClasses.html', form=form, message=message)       
    else:
        return render_template('addClasses.html', form=form)

@app.route('/addStudent', methods=['GET', 'POST'])
def addStudent():
    form = StudentForm()
    if form.validate_on_submit():
        newStudent = Student(
            student_name = form.student_name.data,
            student_city = form.student_city.data,
            student_age = form.student_age.data
            )
        db.session.add(newStudent)
        db.session.commit()
        message = f"You have added the student: {form.student_name.data} {form.student_age.data} located in {form.student_city}"
        return render_template('addStudent.html', form=form, message=message)    
    else:
        return render_template('addStudent.html', form=form)


@app.route('/updateStudent', methods=['GET', 'POST'])
def updateStudent():
    form = StudentForm()         
    allStudents = Student.query.all()   
    #The drop down field will display student names
    for student in allStudents:
        form.student_name.choices.append(
            (student.student_name, f"{student.student_name}")      
        ) 
    if request.method == 'POST' and form.validate_on_submit():      
        chosenStudent = Student.query.filter_by(student_name=form.student_name.data).first()      
        chosenStudentName = chosenStudent.student_name
        return render_template('updateStudent.html', chosenStudentName=chosenStudentName, form=form)  
    return render_template('updateStudent.html', form=form)


@app.route('/updateStudentInfo/<int:id>', methods=['GET', 'POST'])
def updateStudentInfo(id):
    form = StudentForm()       
    chosenStudent = Student.query.filter_by(id=id).first() 
    chosenStudentName = Student.query.get(id)  
    if request.method == 'POST' and form.validate_on_submit():
        message = f"""Changes: 
            {chosenStudent.student_name} to {form.student_name.data}
            {chosenStudent.student_age} to {form.student_age.data}
            {chosenStudent.student_city} to {form.student_city.data}""" 
        chosenStudent.student_name = form.student_name.data
        chosenStudent.student_age = form.student_age.data 
        chosenStudent.student_city = form.student_city.data
        db.session.commit()

        flash(message)  
        return render_template('updateStudentInfo.html', chosenStudentName=chosenStudentName, form=form )
    
    return render_template('updateStudentInfo.html', form=form)

@app.route('/updateClassesInfo/<int:id>', methods=['GET', 'POST'])
def updateClassesInfo(id):
    form = ClassesForm()       
    chosenClasses = Classes.query.filter_by(id=id).first() 
    chosenClassesId = Classes.query.get(id)  
    if request.method == 'POST' and form.validate_on_submit():
        message = f"""Changes: 
            {chosenClasses.classes_name} to {form.classes_name.data}, 
            {chosenClasses.classes_day} to {form.classes_day.data}"""
        chosenClasses.classes_name = form.classes_name.data
        chosenClasses.classes_day = form.classes_day.data
        db.session.commit()
        flash(message)
        return render_template('updateClassesInfo.html', chosenClassesId=chosenClassesId, form=form )
    return render_template('updateClassesInfo.html', form=form)

@app.route('/updateClasses', methods=['GET', 'POST'])
def updateClasses():
    form = UpdateClassesForm()
    allClasses = Classes.query.all()
    for classes in allClasses:   
        form.classes_id.choices.append(
            (classes.id, f"{classes.Classes_name} {classes.Classes_day}")
        )
    if request.method == 'POST' and form.validate_on_submit():
        chosenClassesId = form.Classes_id.data
        return redirect(url_for('updateClassesInfo', chosenClassesId=chosenClassesId))
    return render_template('updateClasses.html', form=form)

@app.route('/deleteStudent', methods=['GET', 'POST'])
def deleteStudent():
    form = DeleteStudentForm()
    allStudents = Student.query.all()
    for student in allStudents:
        form.student_id.choices.append(
            (student.id, f"{student.student_name} {student.student_age}{student.student_city}")
        )
    if request.method == 'POST' and form.validate_on_submit():
        chosenStudentId = form.student_id.data
        studentfordeletion = Student.query.get(chosenStudentId)

        db.session.delete(studentfordeletion)
        db.session.commit()

        message = f"Student {studentfordeletion.student_name} {studentfordeletion.student_age} {studentfordeletion.student_city} has been deleted."
        flash(message)
        
        return redirect(url_for('deleteStudent'))
    return render_template('deleteStudent.html', form=form)

@app.route('/deleteClasses', methods=['GET', 'POST'])
def deleteClasses():
    form = DeleteClassesForm()
    allClasses = Classes.query.all()
    for classs in allClasses:
        form.classes_id.choices.append(
            (classs.id, f"{classs.classes_name} {classs.classes_day}")
        )
    if request.method == 'POST' and form.validate_on_submit():
        chosenclassId = form.classes_id.data
        classfordeletion = Classes.query.get(chosenclassId)

        db.session.delete(classfordeletion)
        db.session.commit()
        message = f"Class {classfordeletion.classes_name} {classfordeletion.classes_day}  has been deleted."
        flash(message)
        return redirect(url_for('deleteClasses'))
    return render_template('deleteClasses.html', form=form)



