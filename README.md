# Class_enrollment_Project
This repository contains many to many relation database supporting join tables, utilising html to create a web application

## Contents:
* [Project Aim](#Project-Aim)  
* [App Design](#App-Design)
* [CI Pipeline](#CI-Pipeline)  
* [Risk Assessment](#Risk-Assessment)
* [Testing](#Testing)
* [The App](#The-App)
* [Updates](#Updates)
* [Known Issues](#Known-Issues)
* [Future Work](#Future-Work)

## Project Aim 
The proposed aim of this project was to create a workking web application with a detailed report on work and findings.
This web application must have CRUD (create, read, update and delete) functionality, utilisation of the Flask micro-framework containing a relational database supporting join tables. 

## App Design
The applicaiton i have chosen to build will be a student class enrollment system which allows users to create a user name (create functionality) update their user information (update functionality), create a class (create functionality), remove a student from the list(delete functionality) update the list of classes information (update functionality) view a range of classes (read functionality), select a number of classes to attend (update functionality) and remove the selected class from class list (delete functionality)
An initial ERD sample design was instructed to gauge the relations between the database models:
![Initial ERD](https://github.com/MrLucien-Johnson/Class_enrollment_Project/blob/readme/images/early_erd.png)

Improvements were made to this initial ERD inorder to achive the current working ERD satisfying the join table requirements.

![Current ERD](https://github.com/MrLucien-Johnson/Class_enrollment_Project/blob/readme/images/currentERD.png)

## CI Pipeline 
Due to the technical nature of this project and in order to ensure continuous integration and delivery, i found it important to utilise CI pipelining.
Version controll was utilised, using github and working on branches. The project is stored on an online git repository allowing the use in different environments especially. The aim is to be able to run this application on an AWS ec2 instance while utilising jenkins. Project tracking in which i used a trello kanban board. This board included my user stories in which i worked out my story points utilising MoSCoW (Must, Should, could and wont haves)
![Trello](https://github.com/MrLucien-Johnson/Class_enrollment_Project/blob/readme/images/trello.png)

Jenkins has be used as a build server which specialises in automation and testing. For this project it was deemed neccessary that the project type would be that of a freestyle project which executes the test.sh script when it recieves a webhook from github, any time a commit is made and pushed. When building using jenkins the build will not complete as the flask application will show as a running process and therefore would not be able to complete and close the build.

![Jenkins](https://github.com/MrLucien-Johnson/Class_enrollment_Project/blob/readme/images/CI-with-Jenkins-Git.png)

The utilisation of systemD service, which is to run the flask application through jenkins onto the system that it is being accessed from. This would in turn allow the build to succeed by replacing program files which allow the running of the flask application as a process on the system. 

## Risk Assessment
In order to identify risks and propose measures to control these risks, a risk assessment was undertaken prior to building the app. Then in the flask app these identified measures could then be implemented. 
Risk assessment: 

![RiskAssesment](https://github.com/MrLucien-Johnson/Class_enrollment_Project/blob/readme/images/riskassesment.png)

* SQLAlchemy was used with Flask to prevent SQL commands being sent directly to the database.
* Credentials stored as secret texts on Jenkins VM and exported as environment variables to avoid accidentally publishing confidential details.
*  After the implementation of control measures, the likelihood and impact of each risk identified were estimated out of 5 to quantify the effect of implementing the measures.

## Testing
An essential part of the development process was testing the app :  
* To ensure that the CRUD (create, read, update and delete) functionality worked as intended, unit tests were written. Unit tests test the units of functionality within the app. ie. the functions of the app.
![TestsCoverage](https://github.com/MrLucien-Johnson/Class_enrollment_Project/blob/readme/images/TestsCoverage.png)
This image shows the tests being ran and the output of tests success, showing 81% coverage overall. 

Running tests thorugh jenkins would sujest that for a build to be successful all tests must pass, any single failed test marks the build overall as failed.


## The App
once tha application is navigated to, the home screen will be shown. Displaying the contents of the database and providing a navigation bar to add and delete students and classes.
![HomePage] (https://github.com/MrLucien-Johnson/Class_enrollment_Project/blob/readme/images/homepage.png)

To choose to populate the database and add a student once clicked on the href in the navigation bar you will be redirected to :
![AddStudent](https://github.com/MrLucien-Johnson/Class_enrollment_Project/blob/readme/images/addstudent.png)

To choose to populate the database and add classes once clicked on the href in the navigation bar you will be redirected to :
![AddClasses](https://github.com/MrLucien-Johnson/Class_enrollment_Project/blob/readme/images/addclasses.png)

To choose to remove Students from the database and add classes once clicked on the href in the navigation bar you will be redirected to :
![DeleteStudent](https://github.com/MrLucien-Johnson/Class_enrollment_Project/blob/readme/images/deletestudent.png)

To choose to remove Classes from the database and add classes once clicked on the href in the navigation bar you will be redirected to :
![DeleteClasses](https://github.com/MrLucien-Johnson/Class_enrollment_Project/blob/readme/images/deleteclasses.png)

To update a class or student an update button will be present for each record and will redirect you to the student/classes update pages respectively:
![UpdateStudent](https://github.com/MrLucien-Johnson/Class_enrollment_Project/blob/readme/images/updatestudent.png)
![UpdateClasses](https://github.com/MrLucien-Johnson/Class_enrollment_Project/blob/readme/images/updateclasses.png)

## Known Issues
* Linked table had not been utilised 
* Jenkins not setup with SystemD
* No external databse

## Future Work
There are a number of future improvements needed on this project.
Utilising the linked table to add a student and a class to create a booking. This would make the program usable in an enrollment environment. The database model has been successfully created and can be utilised however front end will need to be improved.

* UI UX - The look and feel of the application is very simplistic and could do with an overhaul on design
* Create and link external databse hiding secrets using env
