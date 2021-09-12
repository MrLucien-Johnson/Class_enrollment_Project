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
The applicaiton i have chosen to build will be a student class enrollment system which allows users to create a user name (create functionality) view a range of classes (read functionality), select a number of classes to attend (update functionality) and remove the selected class from class list (delete functionality)

## CI Pipeline 
Due to the technical nature of this project and in order to ensure continuous integration and delivery, i found it important to utilise CI pipelining.
These in for of version controll, using git hub and working on brnaches. The project stored on an online git repo allowing the use in different environments especially that is is an aim to be able to run this application on an AWS ect instance while utilising jenkins. Project tracking in which i used a trello kanban board. This board included my user stories in which i worked out my story points utilising MoSCow (Must, Should,could have)

Jenkins will be used as a build server which specialises in automation and testing. For this project it was deemed neccessary that the project type would be that of a freestyle project which executes the test.sh script when it recieves a webhook from github any time a commit is made and pushed.

## Risk Assessment

## Testing


## The App


## Known Issues
Linked table had not been utilised 


## Future Work
There are a number of future improvements needed on this project.
Utilising the linked table to add a student and a class to create a booking. This would make the program usable in an enrollment environment. The database model has been successfully created and can be utilised however front end will need to be improved.

* UI UX - The look and feel of the application is very simplistic and could do with an overhaul on design
